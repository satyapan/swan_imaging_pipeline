#WRITE CROSS SPECTRA IN FORMAT SUPPORTED BY CASA

import numpy as np
from glob import glob
import sys


#input

tiles_src = int(sys.argv[1])
tiles_cal = int(sys.argv[2])
name_src = sys.argv[3]
name_cal = sys.argv[4]
nfft_src = int(sys.argv[5])
nfft_cal = int(sys.argv[6])

#FOR X POLARIZATION

#code for source
baselines_src_x = int(tiles_src*(tiles_src-1)/2)

file_src_x = sorted(glob(name_src + '/X*.npy'))
list_src_x = []

for i in range(baselines_src_x):
	list_src_x.append(np.load(file_src_x[i]))

length_src_x = min([np.shape(i)[1] for i in list_src_x])
casa_src_x = np.zeros((nfft_src,length_src_x*baselines_src_x),dtype='complex')

for i in range(length_src_x):
	for j in range(baselines_src_x):
		casa_src_x[:,i*baselines_src_x+j] = list_src_x[j][:,i]

np.save("casa_src_x.npy", casa_src_x)

#code for calib
baselines_cal_x = int(tiles_cal*(tiles_cal-1)/2)

file_cal_x = sorted(glob(name_cal + '/X*.npy'))
list_cal_x = []

for i in range(baselines_cal_x):
	list_cal_x.append(np.load(file_cal_x[i]))

length_cal_x = min([np.shape(i)[1] for i in list_cal_x])
casa_cal_x = np.zeros((nfft_cal,length_cal_x*baselines_cal_x),dtype='complex')

for i in range(length_cal_x):
	for j in range(baselines_cal_x):
		casa_cal_x[:,i*baselines_cal_x+j] = list_cal_x[j][:,i]

np.save("casa_cal_x.npy", casa_cal_x)

#REPEAT FOR Y POLARIZATION

#code for source
baselines_src_y = int(tiles_src*(tiles_src-1)/2)

file_src_y = sorted(glob(name_src + '/Y*.npy'))
list_src_y = []

for i in range(baselines_src_y):
	list_src_y.append(np.load(file_src_y[i]))

length_src_y = min([np.shape(i)[1] for i in list_src_y])
casa_src_y = np.zeros((nfft_src,length_src_y*baselines_src_y),dtype='complex')

for i in range(length_src_y):
	for j in range(baselines_src_y):
		casa_src_y[:,i*baselines_src_y+j] = list_src_y[j][:,i]

np.save("casa_src_y.npy", casa_src_y)

#code for calib
baselines_cal_y = int(tiles_cal*(tiles_cal-1)/2)

file_cal_y = sorted(glob(name_cal + '/Y*.npy'))
list_cal_y = []

for i in range(baselines_cal_y):
	list_cal_y.append(np.load(file_cal_y[i]))

length_cal_y = min([np.shape(i)[1] for i in list_cal_y])
casa_cal_y = np.zeros((nfft_cal,length_cal_y*baselines_cal_y),dtype='complex')

for i in range(length_cal_y):
	for j in range(baselines_cal_y):
		casa_cal_y[:,i*baselines_cal_y+j] = list_cal_y[j][:,i]

np.save("casa_cal_y.npy", casa_cal_y)

