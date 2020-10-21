#IMPORT THE MODIFIED FITS FILES FOR BOTH SOURCE AND CALIBRATOR INTO A SINGLE MS TABLE

importuvfits(fitsfile='mod_src.fits',vis='mod_src.ms')
importuvfits(fitsfile='mod_cal.fits',vis='mod_cal.ms')

concat(vis=['mod_src.ms','mod_cal.ms'],concatvis='mod_final.ms')
