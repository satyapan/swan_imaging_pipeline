#SIMULATE A MOCK OBSERVATION IN CASA WITH SAME PARAMETERS AS ACTUAL OBSERVATION

import numpy as np
import sys

#input
int_time = float(sys.argv[3])

ra_src = sys.argv[4]
dec_src = sys.argv[5]
freq_centre_src = float(sys.argv[6])
image_dim_src = int(sys.argv[7])
pixel_dim_src = sys.argv[8]
date_src = sys.argv[9]
tiles_src = int(sys.argv[10])

ra_cal = sys.argv[11]
dec_cal = sys.argv[12]
freq_centre_cal = float(sys.argv[13])
image_dim_cal = int(sys.argv[14])
pixel_dim_cal = sys.argv[15]
date_cal = sys.argv[16]
tiles_cal = int(sys.argv[17])

lst_src = 19.06
lst_cal = 15.41

#code for source
direction = "J2000 " + ra_src + " " + dec_src
cl.done()
cl.addcomponent(dir=direction, flux=1.0, fluxunit='Jy', freq=str(freq_centre_src-8)+"MHz", shape="Gaussian", 
                majoraxis="30arcmin", minoraxis='30arcmin', positionangle='45.0deg')
ia.fromshape("Gaussian_src.im",[image_dim_src,image_dim_src,1,256],overwrite=True)
cs=ia.coordsys()
cs.setunits(['rad','rad','','Hz'])
cell_rad=qa.convert(qa.quantity(pixel_dim_src),"rad")['value']
cs.setincrement([-cell_rad,cell_rad],'direction')
cs.setreferencevalue([qa.convert(ra_src,'rad')['value'],qa.convert(dec_src,'rad')['value']],type="direction")
cs.setreferencevalue(str(freq_centre_src-8)+"MHz",'spectral')
cs.setincrement('0.0625MHz','spectral')
ia.setcoordsys(cs.torecord())
ia.setbrightnessunit("Jy/pixel")
ia.modify(cl.torecord(),subtract=False)
exportfits(imagename='Gaussian_src.im',fitsimage='Gaussian_src.fits',overwrite=True)

baselines_src = int(tiles_src*(tiles_src-1)/2)
length_src = int(np.shape(np.loadtxt("casa_real_src_x.txt", float))[0]/baselines_src)
hr_angle_src = lst_src - (float(ra_src.split("h")[0])+(float(ra_src.split("h")[1].split("m")[0])/60)+(float(ra_src.split("h")[1].split("m")[1][:-1])/3600))


simobserve(project="src",
skymodel="Gaussian_src.fits",
incell=pixel_dim_src,
indirection = "J2000 " + ra_src + " " + dec_src,
incenter = str(freq_centre_src)+"MHz",
inwidth = '0.0625MHz',
inbright = '0.06mJy/pixel',
integration = str(int_time)+"s",
refdate = date_src,
hourangle = str(round(hr_angle_src,2))+"h",
totaltime = str(int_time*length_src)+"s",
obsmode = 'int',
antennalist = 'gbd_src.cfg',
thermalnoise = '')


#code for calibrator
direction = "J2000 " + ra_cal + " " + dec_cal
cl.done()
cl.addcomponent(dir=direction, flux=1.0, fluxunit='Jy', freq=str(freq_centre_cal-8)+"MHz", shape="Gaussian", 
                majoraxis="30arcmin", minoraxis='30arcmin', positionangle='45.0deg')
ia.fromshape("Gaussian_cal.im",[image_dim_cal,image_dim_cal,1,256],overwrite=True)
cs=ia.coordsys()
cs.setunits(['rad','rad','','Hz'])
cell_rad=qa.convert(qa.quantity(pixel_dim_cal),"rad")['value']
cs.setincrement([-cell_rad,cell_rad],'direction')
cs.setreferencevalue([qa.convert(ra_cal,'rad')['value'],qa.convert(dec_cal,'rad')['value']],type="direction")
cs.setreferencevalue(str(freq_centre_cal-8)+"MHz",'spectral')
cs.setincrement('0.0625MHz','spectral')
ia.setcoordsys(cs.torecord())
ia.setbrightnessunit("Jy/pixel")
ia.modify(cl.torecord(),subtract=False)
exportfits(imagename='Gaussian_cal.im',fitsimage='Gaussian_cal.fits',overwrite=True)

baselines_cal = int(tiles_cal*(tiles_cal-1)/2)
length_cal = int(np.shape(np.loadtxt("casa_real_cal_x.txt", float))[0]/baselines_cal)
hr_angle_cal = lst_cal - (float(ra_cal.split("h")[0])+(float(ra_cal.split("h")[1].split("m")[0])/60)+(float(ra_cal.split("h")[1].split("m")[1][:-1])/3600))

simobserve(project="cal",
skymodel="Gaussian_cal.fits",
incell=pixel_dim_cal,
indirection = "J2000 " + ra_cal + " " + dec_cal,
incenter = str(freq_centre_cal)+"MHz",
inwidth = '0.0625MHz',
inbright = '0.06mJy/pixel',
integration = str(int_time)+"s",
refdate = date_cal,
hourangle = str(round(hr_angle_cal,2))+"h",
totaltime = str(int_time*length_cal)+"s",
obsmode = 'int',
antennalist = 'gbd_cal.cfg',
thermalnoise = '')

#EXPORT BOTH SOURCE AND CALIBRATOR TABLE TO FITS FORMAT
exportuvfits(vis='src/src.gbd_src.ms',fitsfile='src.fits')
exportuvfits(vis='cal/cal.gbd_cal.ms',fitsfile='cal.fits')

