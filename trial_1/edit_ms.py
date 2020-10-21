#REPLACE DATA COLUMN IN SIMULATED TABLES BY ACTUAL VISIBILITIES

from astropy.io import fits
import numpy as np

#code for source
hdu_list = fits.open('src.fits', memmap=True)
c1 = np.loadtxt("casa_real_src_x.txt", float)
c2 = np.loadtxt("casa_imag_src_x.txt", float)
c3 = np.loadtxt("casa_real_src_y.txt", float)
c4 = np.loadtxt("casa_imag_src_y.txt", float)
d1 = np.array(c1, dtype='float32')
d2 = np.array(c2, dtype='float32')
d3 = np.array(c3, dtype='float32')
d4 = np.array(c4, dtype='float32')
length_src = np.shape(c1)[0]
hdu_list[0].data.field("DATA")[0:length_src,0,0,0,:,0,0] = d1
hdu_list[0].data.field("DATA")[0:length_src,0,0,0,:,0,1] = d2
hdu_list[0].data.field("DATA")[0:length_src,0,0,0,:,1,0] = d3
hdu_list[0].data.field("DATA")[0:length_src,0,0,0,:,1,1] = d4
hdu_list.writeto("mod_src.fits")

#code for calibrator
hdu_list = fits.open('cal.fits', memmap=True)
c1 = np.loadtxt("casa_real_cal_x.txt", float)
c2 = np.loadtxt("casa_imag_cal_x.txt", float)
c3 = np.loadtxt("casa_real_cal_y.txt", float)
c4 = np.loadtxt("casa_imag_cal_y.txt", float)
d1 = np.array(c1, dtype='float32')
d2 = np.array(c2, dtype='float32')
d3 = np.array(c3, dtype='float32')
d4 = np.array(c4, dtype='float32')
length_cal = np.shape(c1)[0]
hdu_list[0].data.field("DATA")[0:length_cal,0,0,0,:,0,0] = d1
hdu_list[0].data.field("DATA")[0:length_cal,0,0,0,:,0,1] = d2
hdu_list[0].data.field("DATA")[0:length_cal,0,0,0,:,1,0] = d3
hdu_list[0].data.field("DATA")[0:length_cal,0,0,0,:,1,1] = d4
hdu_list.writeto("mod_cal.fits")
