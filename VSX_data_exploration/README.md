# VSX Data Exploration

**What is the VSX?**
The VSX is the International Variable Star Index, hosted and maintained by the American Association of Variable Star Observers (AAVSO). When it was first compiled, it contained records from the General Catalog of Variable Stars (GCVS), the 3rd release of the All Sky Automated Survey (ASAS-3), Optical Gravitational Lensing Experiment (OGLE), and more. The catalog is updated regular by both amateurs and professionals discovering new variable stars, as well as suspected and new variables from survey results. All changes are reviewed for accuracy before updates are made.


## Data access
VSX data can be access through web-based API queries, such as this one:

`http://www.aavso.org/vsx/index.php?view=query.votable&filter=0&maxhi=8.5&maxlo=12.49999&constid=01`

This returns all stars with a maximum magnitude between 8.5 and 12.49999 from the constellation Andromeda, which has an id of 01 as the constellations are in alphabetical order.

There is currently no mechanism to download the entire catalog, and queries are limited to 9999 entries, so I wrote a script to download in sections based on constellation and magnitude range. Originally I tried to do it on a per constellation basis, but many constellations have more than 9999 records. Data is returned in the *votable* format, which is created and maintained by the International Virtual Observatory Alliance. More information on this format can be found here: https://www.ivoa.net/documents/VOTable/20191021/REC-VOTable-1.4-20191021.html

## Goals
The primary goal of this analysis is to see exactly what types of records are in the VSX - only a percentage of them have AUIDs assigned, and an AUID is necessary to get a finder chart or photometry of comparison stars in order to do differential photometry. Other records might be fainter stars from surveys that might be of limited use to the typical amateur observer, but getting a better picture of the type of data in the catalog might provide some insights on potential areas where observers could follow up on newer or poorly classified stars. 

## Data Acknowledgments and Copyright Info
All data is Copyright ©2005-2011 The American Association of Variable Star Observers. All Rights Reserved.

Acknowledgments about contributors here:
https://www.aavso.org/vsx/index.php?view=about.acknowledgments