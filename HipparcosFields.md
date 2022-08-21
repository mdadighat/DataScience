Copied from the Hipparcos Catalog:
https://heasarc.gsfc.nasa.gov/W3Browse/all/hipparcos.html

**Vmag**
The magnitude in Johnson V band, given to a precision of 0.01 magnitudes in the original Hipparcos Catalog.

**Var_Flag**
A coarse variability flag which indicates if the entry (or one of the components in the case of a multiple system) is variable in its Hipparcos magnitude Hip_mag at the level of:

       1: < 0.06mag ; 2: 0.06-0.6mag ; 3: >0.6mag
  

**Vmag_Source**
The source of the V magnitude:

       G:  ground-based multicolor photometry, either directly in or
           reduced to the Johnson UBV system
       H:  Hipparcos magnitude Hip_mag, combined with information on the
           color index (either V-I or BT_mag-VT_mag), in combination with
           the luminosoty class
       T:  Tycho photometry, i.e., VT_mag and BT_mag-VT_mag
        :  no data available
  
**Astrom_Ref_Dbl**
Reference flag for astrometric parameters of double and multiple systems. This flag indicates that the astrometric parameters refer to:

    A, B etc: the letter indicates the specified component of a double
              or multiple system
           *: the photocentre of a double or multiple system included in
              Part C of the Double and Multiple Systems Annex
           +: the centre of mass: for such an entry, an orbit is given in
              Part O of the Double and Multiple Systems Annex
  

**Parallax**
The trigonometric parallax pi in units of milliarcseconds: thus to calculate the distance D in parsecs, D = 1000/pi. The estimated parallax is given for every star, even if it appears to be insignificant or negative.

**PM_RA**
The proper motion component in the RA direction expressed in milliarcseconds per Julian year (mas/yr), and given with respect to the ICRS reference system: mu_RA* = mu_RA x cos (declination).

**PM_Dec**
The proper motion component in the declination direction expressed in milliarcseconds per Julian year (mas/yr), and given with respect to the ICRS reference system.

**RA_Error**
The standard error in the Right Ascension given at the catalog epoch, J1991.25, and expressed in milliarcseconds: sigma_RA* = sigma_RA x cos (declination).

**Dec_Error**
The standard error in the declination given at the catalog epoch, J1991.25, and expressed in milliarcseconds.

**Parallax_Error**
The standard error in the parallax given in milliarcseconds.

**PM_RA_Error**
The standard error in the proper motion component in the RA direction expressed in milliarcseconds per Julian year (mas/yr): sigma_mu_RA* = sigma_mu_RA x cos (declination).

**PM_Dec_Error**
The standard error in the proper motion component in the declination direction expressed in milliarcseconds per Julian year (mas/yr), sigma_mu_declination.

**Reject_Percent**
The percentage of data that had to be rejected in order to obtain an acceptable solution.

*This will be useful for eliminating potential outliers or bad data*

**Quality_Fit**
The goodness-of-fit statistic: this number indicates the goodness of fit of the astrometric solution to the accepted data (i.e., excluding the rejected data). For good fits, this should approximately follow a normal distribution with zero mean value and unit standard deviation. Values exceeding, say +3, thus indicate a bad fit to the data.

*This will be useful for eliminating potential outliers or bad data*

**BT_Mag (and error)**
The mean magnitude in the Tycho photometric system, B_T.

**VT_Mag (and error)**
The mean magnitude in the Tycho photometric system, V_T.

**BT_Mag_Ref_Dbl**
a reference flag for BT_mag and VT_mag which indicates, for non-single stars, the component measured in Tycho photometry, or indicates that several components have been directly measured together by Tycho, or have had their Tycho data combined. The flag takes the following values:

   A, B, etc. : the Tycho photometry refers to the designated Hipparcos
                Catalog component
            * : the Tycho photometry refers to all components of the
                relevant Hipparcos entry
            - : the Tycho photometry refers to a single-pointing triple or
                quadruple system, for which only a close pair has been
                observed by Tycho, the other components being too faint
                to be detected by Tycho
  

**BV_Color**
The (B-V) color index in, or reduced to, the Johnson UBV system.

**BV_Color_Error**
The standard error of the (B-V) color index, BV_Color.

**BV_Mag_Source**
The source of the (B-V) color index, BV_Color:

            G: indicates that it was taken from ground-based observations
            T: indicates that it was determined from the transformed Tycho
               (B_T-V_T) data
             : indicates that no data are available
  

**VI_Color**
the (V-I) color index in Cousins' photometric system; it represents the best available (V-I) value at the time of the Hipparcos Catalog publication.

**VI_Color_Error**
The standard error in the (V-I) color index, VI_Color.

**VI_Color_Source**
The Source of the (V-I) color index, VI_Color (see Section 1.3, Appendix 5 of the published Hipparcos Catalog for full details):

       'A'        :for an observation of V-I in Cousins' system;
       'B' to 'K' :when V-I derived from measurements in other
                   bands/photoelectric systems
       'L' to 'P' :when V-I derived from Hipparcos and Star Mapper
                   photometry
       'Q'        :for long-period variables
       'R' to 'T' :when colours are unknown
  

**Mag_Ref_Dbl**
A reference flag for the (B-V) and (V-I) color indices and the V magnitude Vmag (and all their standard errors) which is set to '*' when they refer to the combined light of double or multiple systems which are otherwise resolved by the main mission astrometry and photometry.

**HIP_Mag**
The median magnitude H_P in the Hipparcos photometric system, and defined on the basis of the accepted observations (or field transits) for a given star. Note that the Hipparcos magnitude could not be determined for 14 stars.

**HIP_Mag_Error**
The standard error of the median magnitude H_P.

**Scat_HIP_Mag**
The scatter of the H_P observations.

**N_Obs_HIP_Mag**
The number of H_P observations: this is the number of photometric observations (or field transits) used for the construction of the median, standard error, and scatter in H_P.

**HIP_Mag_Ref_Dbl**
A reference flag for the Hipparcos photometric parameters. For a double or multiple entry, this flag indicates that the photometry refers to:

   A, B, etc. : the specified component of a double or multiple system
            * : combined photometry of a double system, corrected for
                attenuation by the detector's instantaneous field of view
                profile response
            - : combined photometry of a double system, NOT corrected for
                attenuation by the detector's instantaneous field of view
                profile response
  

**HIP_Mag_Max**
The observed magnitude at maximum luminosity. This is defined as the 5th percentile of the epoch photometry.

**HIP_Mag_Min**
The observed magnitude at minimum luminosity. This is defined as the 95th percentile of the epoch photometry.

**Var_Period**
The variability period, or a provisional estimate of such a period, derived on the basis of the Hipparcos data (possibly in combination with ground-based observations) and expressed in days, with a precision of 0.01 days.

**HIP_Var_Type**
The variability type: the sources of scatter in the photometric data are various, and this flag indicates the origin of the extra scatter, which may be astrophysical, or, in some cases, instrumental. See Section 1.3, Appendix 2 of the published Hipparcos Catalog for a more detailed description. Amongst astrophysical sources of variability, this parameter only distinguishes between 'M' (micro-variables), 'P' (periodic variables), and 'U' (unsolved variables). Further variability details for the periodic or unsolved variables are included in the Variability Annex. The flag takes the following values:

       C : no variability detected ("constant")
       D : duplicity-induced variability
       M : possibly micro-variable, with amplitude < 0.03 mag (stars
           classified with high confidence as micro-variable are flagged U)
       P : periodic variable
       R : the V-I colour index was revised during the variability analysis
       U : unsolved variable which does not fall in the other categories;
           this class also includes irregular or semi-regular variables,
           and possibly varaibles with amplitude > or ~ 0.03 mag
         : a blank indicates that the entry could not be classified as
           variable or constant with any degree of certainty

**Var_Data_Annex**
A Variability Annex flag indicating the existence of additional tabular data in the Variability Annex, where '1' means that additional data are provided in a table of periodic variables, and '2' means that additional data are provided in a table of 'unsolved' variables.

**Astrom_Mult_Source**
A flag for the source of the absolute astrometry. This parameter qualifies the source of the astrometric parameters for some of the entries with a value of 'C' for the parameter Dbl_Mult_Annex. The values are as follows:

       P : primary target of a 2- or 3-pointing system
       F : secondary or tertiary of a 2- or 3-pointing 'fixed' system
           (common parallax and proper motions)
       I : secondary or tertiary of a 2- or 3-pointing 'independent'
           system (no constraints on parallax or proper motions)
       L : secondary or tertiary of a 2- or 3-pointing 'linear' system
           (common parallax)
       S : astrometric parameters from 'single-star merging' process.
  
**Dbl_Soln_Qual**
A solution quality flag which indicates the reliability of the double or multiple star solution, and is set for all entries in Part C of the Double and Multiple Systems Annex. The flags can be understood as follows:

       A: 'good', or reliable solution
       B: 'fair', or moderately reliable solution
       C: 'poor', or less reliable solution
       D: uncertain solution
       S: suspected non-single, i.e., possible double or multiple,
          although no significant or convincing non-single star solution
          was found
  

**Dbl_Ref_ID**
Component designation for the double star parameters, Dbl_theta, dbl_rho, etc. The first letter gives the 'reference' component, and the second letter gives the subsidiary component. In the case of the Hipparcos observations, the reference component is always defined to be the brighter component (in median H_P) such that the magnitude difference between the components (Diff_Hip_Mag) is always positive.

**Dbl_Theta**
The rounded value for the position angle between the components specified in the Dbl_Ref_id field, expressed in degrees (in the usual sense measured counterclockwise from North).

**Dbl_Rho**
The rounded value for the angular separation between the components specified in the Dbl_Ref_id field, expressed in arcseconds.

**Diff_HIP_Mag**
The Hipparcos magnitude difference of the components specified in the Dbl_Ref_id field, expressed in magnitudes.

**VI_Color_Reduct**
The (V-I) color index used for the photometric processing (not necessarily the same as the `final' value given in the parameter VI_mag).

**Spect_Type**
The MK or HD spectral type acquired from ground-based compilations and primarily taken from the Hipparcos Input Catalog, with some updates, especially for variable stars.