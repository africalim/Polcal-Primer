# Polcal Primer using CASA
A primer for polarization calibration using CASA

The goal of this walkthrough is to familiarize yourself with the primary calibration steps involved in calibrating a linear feed system using CASA.
We will not attempt to address all the nuances with reducing wideband data, including flagging, SNR considerations and a reversal in phasing on,
in particular, the MeerKAT S-band system, but we hope this will give you enough of a footing to work from on larger datasets. We also leave writing this recipe
as a Stimela v2 recipe up to the reader as an exercise.

We used CASA 5.6 throughout, but theoretically this recipe should execute in 4.7 and above -- no guarrantees are made for this though!

About this data
--------------------
The dataset is a 100MHz UHF dataset only containing the core antennas for the MeerKAT array to conserve space. We have substantially averaged down the raw data to reflect the lack of long spacings in this dataset. You will have the opportunity to reduce a large wide-band L-band dataset performing the calibration steps we will discuss here through Kubernetes. This can be found in the [data](https://github.com/africalim/Polcal-Primer/tree/master/data) subfolder.

The limb of the Moon (and other rocky planatory/planatoid bodies) is radially linearly polarized due to the refraction of the inertial thermal radiation at the boundary of the dielectic surface regolith and (approximately) free space above. We expect to see near perfect radially polarized light
to the limb which makes these bodies an excellent source of absolutely known polarization angle calibrators (with which we can calibrate other sources, e.g. 3C286). A full physical description can be found in e.g. [Perley and Butler 2013](https://iopscience.iop.org/article/10.1088/0067-0049/206/2/16/meta).

For linear feeds the calibration, mainly, removes the elliptical response induced by the impedance phase between the vertical and horizontal feeds. We will run through the core steps needed to perform transfer calibration here, excluding technicalities such as RFI excision, SNR constraints at the low part of UHF band, and the inverted phase seen on MeerKAT S-Band receivers (which inverts the handedness of the polarization vector, and has to be corrected). See [EVLA memo 219](https://library.nrao.edu/public/memos/evla/EVLAM_219.pdf) for a full discussion. These steps should be enough to get you started on calibrating larger wider bandwidth data for MeerKAT. Below we show the expected result after successful calibration of the Moon. The radial emission of the Moon is an excellent way to debug both the handedness of the data, as well as the phasing. According to IAU righthanded convention, these vectors should rotate north (towards increasing declination) through east (towards increasing right ascension), see [Hamaker and Bregman (1996)](https://doi.org/10.1051/aas:1996147).
![IQUV Moon](https://raw.githubusercontent.com/africalim/Polcal-Primer/master/resultsIQUV.png)

*The calibrated Moon at 858 MHz. Top image shows I Q U V stokes decomposition of the polarized Moon with +Q pointing north and -Q pointing east. The thermal emission from the limb is near-perfectly polarized by refraction. One of the primary effects is to calibrate the impedance which
makes the Stokes V response to the moon noiselike. This is shown in the bottom right panel. Here Q, U and V are locked to the same minima and maxima. Save for a relatively quiescent ionosphere this data is corrected for phase and amplitude gains, bandpass, leakages, crosshand phase and (geometric) parallactic angle rotation of the vectors.*

![Lunar polarization vectors](https://raw.githubusercontent.com/africalim/Polcal-Primer/master/final_pol_vectors.png)

*We overplot the polarization angle over total linear polarization (shown in colour). Thermal radio light is near perfectly radially polarized at the limb of the Moon by refraction through the dielectric surface regolith by Snell's Law in which the radial component dominates over the azimuthal component, giving rise to increasingly polarized light (up to 30+%) at the limb of the Moon.*


Data fair use notice
---------------------
This data is wholely owned by SARAO and distributed with intent of teaching purposes. The data is subject to the MeerKAT [data policy](https://www.sarao.ac.za/wp-content/uploads/2019/12/MeerKAT-Telescope-and-Data-Access-Guidelines.pdf) clause 4.2.2.2. 
The full data is available, on request to the observatory, under proposal code EXT-20220902-BH-01.
