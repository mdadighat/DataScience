############################################################################################
# download_VSX.py
##
# This script downloads all entries from AAVSO's VSX database, with the option to include
# suspected variables.
##
# All entries are saved to a .csv file that contains the desired attributes from VSX
############################################################################################

import urllib.request
import re
import csv
from xml.dom import minidom
from xml.etree import ElementTree
from xml.parsers import expat
import sys

################################################################
# getDataFromNodes
# param: list of fields to be used to check the tag contents
# returns: the list of data ordered in the same order as the
# 		   original fields
################################################################


def getDataFromNodes(fieldList):
    # Change this to reflect any removed fields
    data = [None] * 15
    # Comment out any unneeded fields
    # The encode/decode is done as a way to sanitize the xml and ignore bad characters
    if node.getElementsByTagName("TD")[fieldList["name"]].firstChild:
        data[fieldList["name"]] = node.getElementsByTagName("TD")[fieldList["name"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["auid"]].firstChild:
        data[fieldList["auid"]] = node.getElementsByTagName("TD")[fieldList["auid"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["const"]].firstChild:
        data[fieldList["const"]] = node.getElementsByTagName("TD")[fieldList["const"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["radec2000"]].firstChild:
        data[fieldList["radec2000"]] = node.getElementsByTagName("TD")[fieldList["radec2000"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["varType"]].firstChild:
        data[fieldList["varType"]] = node.getElementsByTagName("TD")[fieldList["varType"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["maxMag"]].firstChild:
        data[fieldList["maxMag"]] = node.getElementsByTagName("TD")[fieldList["maxMag"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["maxPass"]].firstChild:
        data[fieldList["maxPass"]] = node.getElementsByTagName("TD")[fieldList["maxPass"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["minMag"]].firstChild:
        data[fieldList["minMag"]] = node.getElementsByTagName("TD")[fieldList["minMag"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["minPass"]].firstChild:
        data[fieldList["minPass"]] = node.getElementsByTagName("TD")[fieldList["minPass"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["epoch"]].firstChild:
        data[fieldList["epoch"]] = node.getElementsByTagName("TD")[fieldList["epoch"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["novaYr"]].firstChild:
        data[fieldList["novaYr"]] = node.getElementsByTagName("TD")[fieldList["novaYr"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["period"]].firstChild:
        data[fieldList["period"]] = node.getElementsByTagName("TD")[fieldList["period"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["riseDur"]].firstChild:
        data[fieldList["riseDur"]] = node.getElementsByTagName("TD")[fieldList["riseDur"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["specType"]].firstChild:
        data[fieldList["specType"]] = node.getElementsByTagName("TD")[fieldList["specType"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    if node.getElementsByTagName("TD")[fieldList["disc"]].firstChild:
        data[fieldList["disc"]] = node.getElementsByTagName("TD")[fieldList["disc"]].firstChild.data.encode(
            sys.stdout.encoding, "ignore").decode(sys.stdout.encoding)

    return data

# Pull results by constellation - the VSX server can't handle a request for all entries


# First, create a hash of all the available fields
fields = {}

# Andromeda and field setup
response = urllib.request.urlopen(
    "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=-30&maxlo=16.49999&constid=01")
secondResponse = urllib.request.urlopen(
    "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=16.5&maxlo=1000&constid=01")

RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                 u'|' + \
                 u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
    (chr(0xd800), chr(0xdbff), chr(0xdc00), chr(0xdfff),
     chr(0xd800), chr(0xdbff), chr(0xdc00), chr(0xdfff),
     chr(0xd800), chr(0xdbff), chr(0xdc00), chr(0xdfff))

_illegal_xml_chars_RE = re.compile(
    u'[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]')
data = re.sub(_illegal_xml_chars_RE, "?", response.read().decode(
    "iso-8859-1", "ignore")).encode("utf-8")
pr = expat.ParserCreate("utf-8")
pr.Parse(data)
xmldoc = minidom.parseString(data.decode('utf-8'))

print("Now loading constellation 01")
# Only need to populate the fields list once, so we'll just do it as part of the first constellation pulled
inc = 0
for fieldnode in xmldoc.getElementsByTagName("FIELD"):
    field = fieldnode.getAttribute("id")
    fields[field] = inc
    inc += 1

# create variables for all fields and initialize to empty strings for safety
fieldNames = ["auid", "name", "const", "ra", "dec", "varType",  "maxMag", "maxPass",
              "minMag", "minPass", "epoch", "novaYr", "period", "riseDur", "specType", "disc"]

# open connection to CSV file and add headers
vsx_file = open("vsx_data.csv", "w", newline='')
csvwriter = csv.DictWriter(vsx_file, fieldnames=fieldNames)
csvwriter.writeheader()

count = 0

# Pull star data from all nodes - one star per row
for node in xmldoc.getElementsByTagName("TR"):
    starData = getDataFromNodes(fields)

    # split RA/DEC
    ra_dec = str(starData[fields["radec2000"]]).split(",")

    # add to csv
    csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                        "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                        "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                        "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                        "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

    count += 1

print("Records added: " + str(count))

data = re.sub(_illegal_xml_chars_RE, "?", secondResponse.read().decode(
    "iso-8859-1", "ignore")).encode("utf-8")
pr = expat.ParserCreate("utf-8")
pr.Parse(data)
xmldoc = minidom.parseString(data.decode('utf-8'))

print("Now loading constellation 01")
count = 0
# Pull star data from all nodes - one star per row
for node in xmldoc.getElementsByTagName("TR"):
    starData = getDataFromNodes(fields)

    # split RA/DEC
    ra_dec = str(starData[fields["radec2000"]]).split(",")

    # add to csv
    csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                        "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                        "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                        "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                        "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

    count += 1
print("Records added: " + str(count))

# Do the rest of the constellations
for x in range(2, 89):
    constId = x
    if x < 10:
        constId = "0" + str(x)

    response0 = ""
    response = ""
    secondResponse = ""
    thirdResponse = ""
    fourthResponse = ""
    fifthResponse = ""
    sixthResponse = ""
    seventhResponse = ""
    eighthResponse = ""

    large_constellations = [1, 5, 6, 8, 18, 19, 20,
                            34, 38, 40, 42, 45, 50, 52, 55, 57, 60, 63, 68, 71]
    extra_large_constellations = [17, 31, 59, 72, 73]
    # split search into two chunks if there will be more then 9999 results since VSX can't handle that
    # the check is arbitrary - use whether or not the star has an epoch entered in VSX to break up the list
   # if x in large_constellations:
    # print("Special case")
    #   response = urllib.request.urlopen(
    #       "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=-30&maxlo=13.99999&constid=" + str(constId))
    #   secondResponse = urllib.request.urlopen(
    #     "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=14&maxlo=1000&constid=" + str(constId))

   # elif x in extra_large_constellations:
    # there are a ton of results for these so the query has to be broken down further
    response0 = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=-30&maxlo=8.49999&constid=" + str(constId))
    response = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=8.5&maxlo=12.49999&constid=" + str(constId))
    secondResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=12.5&maxlo=13.49999&constid=" + str(constId))
    thirdResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=13.5&maxlo=14.49999&constid=" + str(constId))
    fourthResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=14.5&maxlo=14.99999&constid=" + str(constId))
    fifthResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=15&maxlo=15.99999&constid=" + str(constId))
    sixthResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=16&maxlo=16.99999&constid=" + str(constId))
    seventhResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=17&maxlo=17.99999&constid=" + str(constId))
    eighthResponse = urllib.request.urlopen(
        "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=18&maxlo=1000&constid=" + str(constId))

    # else:
    #   response = urllib.request.urlopen(
    #      "http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&constid=" + str(constId))
    data = re.sub(_illegal_xml_chars_RE, "?", response0.read().decode(
        "iso-8859-1", "ignore")).encode("utf-8")
    pr = expat.ParserCreate("utf-8")
    pr.Parse(data)
    xmldoc = minidom.parseString(data.decode('utf-8'))

    print("Now loading constellation ", str(constId))
    count = 0
    # Pull star data from all nodes - one star per row
    for node in xmldoc.getElementsByTagName("TR"):
        starData = getDataFromNodes(fields)

        # split RA/DEC
        ra_dec = str(starData[fields["radec2000"]]).split(",")

        # add to csv
        csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                            "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                            "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                            "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                            "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

        count += 1
    print("Records added: " + str(count))

    if response:
        data = re.sub(_illegal_xml_chars_RE, "?", response.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if secondResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", secondResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if thirdResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", thirdResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if fourthResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", fourthResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if fifthResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", fifthResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if sixthResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", sixthResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if seventhResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", seventhResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

    if eighthResponse:
        data = re.sub(_illegal_xml_chars_RE, "?", eighthResponse.read().decode(
            "iso-8859-1", "ignore")).encode("utf-8")
        pr = expat.ParserCreate("utf-8")
        pr.Parse(data)
        xmldoc = minidom.parseString(data.decode('utf-8'))

        print("Now loading constellation ", str(constId))
        count = 0
        # Pull star data from all nodes - one star per row
        for node in xmldoc.getElementsByTagName("TR"):
            starData = getDataFromNodes(fields)

            # split RA/DEC
            ra_dec = str(starData[fields["radec2000"]]).split(",")

            # add to csv
            csvwriter.writerow({"auid": starData[fields["auid"]], "name": starData[fields["name"]], "const": starData[fields["const"]],
                                "ra": ra_dec[0], "dec": ra_dec[1], "varType": starData[fields["varType"]], "maxMag": starData[fields["maxMag"]],
                                "maxPass": starData[fields["maxPass"]], "minMag":  starData[fields["minMag"]], "minPass": starData[fields["minPass"]],
                                "epoch": starData[fields["epoch"]], "novaYr": starData[fields["novaYr"]], "period": starData[fields["period"]],
                                "riseDur": starData[fields["riseDur"]], "specType": starData[fields["specType"]], "disc": starData[fields["disc"]]})

            count += 1
        print("Records added: " + str(count))

vsx_file.close()
