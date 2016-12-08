# Supernova Temperatures
Use the data from the ASCII files on https://www.cfa.harvard.edu/supernova/SNarchive.html.

Anything before 1995 needs to have its flux scaled up by 10^20. Also, initial guesses for fit parameters may need to be adjusted depending on which supernovae you are looking at. (Adjust p0 on line

The program fits spectra from the website mentioned above with Planck's Law to determine the surface temperature of the supernova each day that it was observed. You may need to adjust the inital guess on the curve fit for a few of the data sets. 

To take into account redshift use the table on page 93 of Optical Spectroscopy of Type Ia Supernovae 1 by T. Matheson and friends. 

If you have any questions, email lmrailing@gmail.com. 
