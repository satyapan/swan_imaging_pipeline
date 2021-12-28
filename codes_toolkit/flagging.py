import numpy as np
import sys

name_src = sys.argv[3]
name_cal = sys.argv[4]


#CALIBRATOR
tiles_used_cal = np.loadtxt('tiles_used_cal.cfg', dtype=int)
msfile = 'gbd_cal.ms'
tb.open(msfile, nomodify = False)
flag_cal = tb.getcol("FLAG")
ant1_cal = tb.getcol("ANTENNA1")
ant2_cal = tb.getcol("ANTENNA2")

n_time = np.shape(ant1_cal)[0]

for j in tiles_used_cal:
	for i in range(n_time):
		ant1 = ant1_cal[i]
		ant2 = ant2_cal[i]
		if j==ant1 or j==ant2:
			flag_mask_x =abs(np.loadtxt(name_cal+'/RFI/'+'X'+str(j)+'.rfi')-1)
			flag_mask_y =abs(np.loadtxt(name_cal+'/RFI/'+'Y'+str(j)+'.rfi')-1)
			flag_cal[0,:,i] = flag_mask_x
			flag_cal[1,:,i] = flag_mask_y

tb.putcol("FLAG", flag_cal)
tb.done()

#SOURCE
tiles_used_src = np.loadtxt('tiles_used_src.cfg', dtype=int)
msfile = 'gbd_src.ms'
tb.open(msfile, nomodify = False)
flag_src = tb.getcol("FLAG")
ant1_src = tb.getcol("ANTENNA1")
ant2_src = tb.getcol("ANTENNA2")

n_time = np.shape(ant1_src)[0]

for j in tiles_used_src:
	for i in range(n_time):
		ant1 = ant1_src[i]
		ant2 = ant2_src[i]
		if j==ant1 or j==ant2:
			flag_mask_x =abs(np.loadtxt(name_src+'/RFI/'+'X'+str(j)+'.rfi')-1)
			flag_mask_y =abs(np.loadtxt(name_src+'/RFI/'+'Y'+str(j)+'.rfi')-1)
			flag_src[0,:,i] = flag_mask_x
			flag_src[1,:,i] = flag_mask_y

tb.putcol("FLAG", flag_src)
tb.done()
