#SIMULATE A MOCK OBSERVATION IN CASA WITH SAME PARAMETERS AS ACTUAL OBSERVATION

import numpy as np
import sys
from simutil import simutil

#input

ra_src = sys.argv[3]
dec_src = sys.argv[4]
freq_centre_src = float(sys.argv[5])
image_dim_src = int(sys.argv[6])
pixel_dim_src = sys.argv[7]
date_src = sys.argv[8]
tiles_src = int(sys.argv[9])
nfft_src = int(sys.argv[10])
int_time_src = float(sys.argv[11])
lst_src = float(sys.argv[12])
lst_src_end = float(sys.argv[13])
name_src = sys.argv[14]

ra_cal = sys.argv[15]
dec_cal = sys.argv[16]
freq_centre_cal = float(sys.argv[17])
image_dim_cal = int(sys.argv[18])
pixel_dim_cal = sys.argv[19]
date_cal = sys.argv[20]
tiles_cal = int(sys.argv[21])
nfft_cal = int(sys.argv[22])
int_time_cal = float(sys.argv[23])
lst_cal = float(sys.argv[24])
lst_cal_end = float(sys.argv[25])
name_cal = sys.argv[26]


#code for source
direction = "J2000 " + ra_src + " " + dec_src
cl.done()
cl.addcomponent(dir=direction, flux=1.0, fluxunit='Jy', freq=str(freq_centre_src-8)+"MHz", shape="Gaussian", 
                majoraxis="3arcmin", minoraxis='3arcmin', positionangle='45.0deg')
ia.fromshape("Gaussian_src.image",[image_dim_src,image_dim_src,1,256],overwrite=True)
cs=ia.coordsys()
cs.setunits(['rad','rad','','Hz'])
cell_rad=qa.convert(qa.quantity(pixel_dim_src),"rad")['value']
cs.setincrement([-cell_rad,cell_rad],'direction')
cs.setreferencevalue([qa.convert(ra_src,'rad')['value'],qa.convert(dec_src,'rad')['value']],type="direction")
cs.setreferencevalue(str(freq_centre_src-8)+"MHz",'spectral')
cs.setincrement(str(16.0/nfft_src) + 'MHz','spectral')
ia.setcoordsys(cs.torecord())
ia.setbrightnessunit("Jy/pixel")
ia.modify(cl.torecord(),subtract=False)
ia.close()

baselines_src = int(tiles_src*(tiles_src-1)/2)
length_src = int(np.shape(np.load("casa_src_x.npy"))[1]/baselines_src)
hr_angle_src = lst_src - (float(ra_src.split("h")[0])+(float(ra_src.split("h")[1].split("m")[0])/60)+(float(ra_src.split("h")[1].split("m")[1][:-1])/3600))
hr_angle_src_end = lst_src_end - (float(ra_src.split("h")[0])+(float(ra_src.split("h")[1].split("m")[0])/60)+(float(ra_src.split("h")[1].split("m")[1][:-1])/3600))
start_time = str(round(hr_angle_src,2))+"h"
stop_time = str(round(hr_angle_src_end,2))+"h"

freq_min = str(qa.convert(str(freq_centre_src)+'MHz','MHz')['value']-(float(nfft_src)/2)*qa.convert(str(16.0/nfft_src)+'MHz','MHz')['value'])+'MHz'
conf_file = 'gbd_src.cfg'
u = simutil()
xx,yy,zz,diam,padnames,telescope,posobs = u.readantenna(conf_file)
ms_name = 'gbd_src.ms'
sm.open(ms_name)
pos_gmrt = me.observatory('GMRT')
sm.setconfig(telescopename = telescope, x = xx, y = yy, z = zz, dishdiameter = diam.tolist(), mount = 'alt-az', antname = padnames, padname = padnames, coordsystem = 'global', referencelocation = pos_gmrt)
sm.setspwindow(spwname = 'Band', freq = freq_min, deltafreq = str(16.0/nfft_src)+'MHz', freqresolution = str(16.0/nfft_src)+'MHz', nchannels = nfft_src, stokes = 'XX YY')
sm.setfeed('perfect X Y', pol=[''])
sm.setauto(0.0)
sm.settimes(integrationtime = int_time_src, usehourangle = True, referencetime = me.epoch('utc', date_src))
sm.setfield(sourcename = 'Gaussian_source', sourcedirection = me.direction('J2000',ra_src,dec_src), calcode='OBJ', distance='0m')
sm.observe('Gaussian_source', 'Band', starttime = start_time, stoptime = stop_time)
sm.predict(imagename = 'Gaussian_src.image')
sm.done()

#code for calib
direction = "J2000 " + ra_cal + " " + dec_cal
cl.done()
cl.addcomponent(dir=direction, flux=1.0, fluxunit='Jy', freq=str(freq_centre_cal-8)+"MHz", shape="Gaussian", 
                majoraxis="3arcmin", minoraxis='3arcmin', positionangle='45.0deg')
ia.fromshape("Gaussian_cal.image",[image_dim_cal,image_dim_cal,1,256],overwrite=True)
cs=ia.coordsys()
cs.setunits(['rad','rad','','Hz'])
cell_rad=qa.convert(qa.quantity(pixel_dim_cal),"rad")['value']
cs.setincrement([-cell_rad,cell_rad],'direction')
cs.setreferencevalue([qa.convert(ra_cal,'rad')['value'],qa.convert(dec_cal,'rad')['value']],type="direction")
cs.setreferencevalue(str(freq_centre_cal-8)+"MHz",'spectral')
cs.setincrement(str(16.0/nfft_cal) + 'MHz','spectral')
ia.setcoordsys(cs.torecord())
ia.setbrightnessunit("Jy/pixel")
ia.modify(cl.torecord(),subtract=False)
ia.close()

baselines_cal = int(tiles_cal*(tiles_cal-1)/2)
length_cal = int(np.shape(np.load("casa_cal_x.npy"))[1]/baselines_cal)
hr_angle_cal = lst_cal - (float(ra_cal.split("h")[0])+(float(ra_cal.split("h")[1].split("m")[0])/60)+(float(ra_cal.split("h")[1].split("m")[1][:-1])/3600))
hr_angle_cal_end = lst_cal_end - (float(ra_cal.split("h")[0])+(float(ra_cal.split("h")[1].split("m")[0])/60)+(float(ra_cal.split("h")[1].split("m")[1][:-1])/3600))
start_time = str(round(hr_angle_cal,2))+"h"
stop_time = str(round(hr_angle_cal_end,2))+"h"

freq_min = str(qa.convert(str(freq_centre_cal)+'MHz','MHz')['value']-(float(nfft_cal)/2)*qa.convert(str(16.0/nfft_cal)+'MHz','MHz')['value'])+'MHz'
conf_file = 'gbd_cal.cfg'
u = simutil()
xx,yy,zz,diam,padnames,telescope,posobs = u.readantenna(conf_file)
ms_name = 'gbd_cal.ms'
sm.open(ms_name)
pos_gmrt = me.observatory('GMRT')
sm.setconfig(telescopename = telescope, x = xx, y = yy, z = zz, dishdiameter = diam.tolist(), mount = 'alt-az', antname = padnames, padname = padnames, coordsystem = 'global', referencelocation = pos_gmrt)
sm.setspwindow(spwname = 'Band', freq = freq_min, deltafreq = str(16.0/nfft_cal)+'MHz', freqresolution = str(16.0/nfft_cal)+'MHz', nchannels = nfft_cal, stokes = 'XX YY')
sm.setfeed('perfect X Y', pol=[''])
sm.setauto(0.0)
sm.settimes(integrationtime = int_time_cal, usehourangle = True, referencetime = me.epoch('utc', date_cal))
sm.setfield(sourcename = 'Gaussian_source', sourcedirection = me.direction('J2000',ra_cal,dec_cal), calcode='OBJ', distance='0m')
sm.observe('Gaussian_source', 'Band', starttime = start_time, stoptime = stop_time)
sm.predict(imagename = 'Gaussian_cal.image')
sm.done()


