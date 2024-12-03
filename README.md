# Polcal Primer using CASA
A primer for polarization calibration using CASA

The goal of this walkthrough is to familiarize yourself with the primary calibration steps involved in calibrating a linear feed system using CASA.
We will not attempt to address all the nuances with reducing wideband data, including flagging, SNR considerations and a reversal in phasing on,
in particular, the MeerKAT S-band system, but we hope this will give you enough of a footing to work from on larger datasets. We also leave writing this recipe
as a Stimela v2 recipe up to the reader as an exercise.

We used CASA 5.6 throughout, but theoretically this recipe should execute in 4.7 and above -- no guarrantees are made for this though!

The dataset is a 100MHz UHF dataset only containing the core antennas for the MeerKAT array to conserve space. This can be found in the [data](https://github.com/africalim/Polcal-Primer/data) subfolder.

Data fair use notice
---------------------
This data is wholely owned by SARAO and distributed with intent of teaching purposes. The data is subject to the MeerKAT [data policy](https://www.sarao.ac.za/wp-content/uploads/2019/12/MeerKAT-Telescope-and-Data-Access-Guidelines.pdf) clause 4.2.2.2. 
The full data is available, on request to the observatory, under proposal code EXT-20220902-BH-01.
