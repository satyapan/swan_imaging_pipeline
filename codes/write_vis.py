#WRITE CROSS SPECTRA IN FORMAT SUPPORTED BY CASA

import numpy as np
from glob import glob
import sys


#input

tiles_src = int(sys.argv[1])
tiles_cal = int(sys.argv[2])


#code for source
baselines_src_x = int(tiles_src*(tiles_src-1)/2)

file_real_src_x = sorted(glob("source_real*_x.txt"))
file_imag_src_x = sorted(glob("source_imag*_x.txt"))
list_real_src_x = []
list_imag_src_x = []

for i in range(baselines_src_x):
	list_real_src_x.append(np.loadtxt(file_real_src_x[i], float))
	list_imag_src_x.append(np.loadtxt(file_imag_src_x[i], float))

length_src_x = min([np.shape(i)[1] for i in list_real_src_x])
casa_real_src_x = np.zeros((256,length_src_x*baselines_src_x))
casa_imag_src_x = np.zeros((256,length_src_x*baselines_src_x))

for i in range(length_src_x):
	for j in range(baselines_src_x):
		casa_real_src_x[:,i*baselines_src_x+j] = list_real_src_x[j][:,i]
		casa_imag_src_x[:,i*baselines_src_x+j] = list_imag_src_x[j][:,i]

casa_real_src_x = np.transpose(casa_real_src_x)
casa_imag_src_x = np.transpose(casa_imag_src_x)

np.savetxt("casa_real_src_x.txt", casa_real_src_x)
np.savetxt("casa_imag_src_x.txt", casa_imag_src_x)


#code for calibrator
baselines_cal_x = int(tiles_cal*(tiles_cal-1)/2)

file_real_cal_x = sorted(glob("calib_real*_x.txt"))
file_imag_cal_x = sorted(glob("calib_imag*_x.txt"))
list_real_cal_x = []
list_imag_cal_x = []

for i in range(baselines_cal_x):
	list_real_cal_x.append(np.loadtxt(file_real_cal_x[i], float))
	list_imag_cal_x.append(np.loadtxt(file_imag_cal_x[i], float))

length_cal_x = min([np.shape(i)[1] for i in list_real_cal_x])
casa_real_cal_x = np.zeros((256,length_cal_x*baselines_cal_x))
casa_imag_cal_x = np.zeros((256,length_cal_x*baselines_cal_x))

for i in range(length_cal_x):
	for j in range(baselines_cal_x):
		casa_real_cal_x[:,i*baselines_cal_x+j] = list_real_cal_x[j][:,i]
		casa_imag_cal_x[:,i*baselines_cal_x+j] = list_imag_cal_x[j][:,i]

casa_real_cal_x = np.transpose(casa_real_cal_x)
casa_imag_cal_x = np.transpose(casa_imag_cal_x)

np.savetxt("casa_real_cal_x.txt", casa_real_cal_x)
np.savetxt("casa_imag_cal_x.txt", casa_imag_cal_x)

#repeat for y polarization
#code for source
baselines_src_y = int(tiles_src*(tiles_src-1)/2)

file_real_src_y = sorted(glob("source_real*_y.txt"))
file_imag_src_y = sorted(glob("source_imag*_y.txt"))
list_real_src_y = []
list_imag_src_y = []

for i in range(baselines_src_y):
	list_real_src_y.append(np.loadtxt(file_real_src_y[i], float))
	list_imag_src_y.append(np.loadtxt(file_imag_src_y[i], float))

length_src_y = min([np.shape(i)[1] for i in list_real_src_y])
casa_real_src_y = np.zeros((256,length_src_y*baselines_src_y))
casa_imag_src_y = np.zeros((256,length_src_y*baselines_src_y))

for i in range(length_src_y):
	for j in range(baselines_src_y):
		casa_real_src_y[:,i*baselines_src_y+j] = list_real_src_y[j][:,i]
		casa_imag_src_y[:,i*baselines_src_y+j] = list_imag_src_y[j][:,i]

casa_real_src_y = np.transpose(casa_real_src_y)
casa_imag_src_y = np.transpose(casa_imag_src_y)

np.savetxt("casa_real_src_y.txt", casa_real_src_y)
np.savetxt("casa_imag_src_y.txt", casa_imag_src_y)


#code for calibrator
baselines_cal_y = int(tiles_cal*(tiles_cal-1)/2)

file_real_cal_y = sorted(glob("calib_real*_y.txt"))
file_imag_cal_y = sorted(glob("calib_imag*_y.txt"))
list_real_cal_y = []
list_imag_cal_y = []

for i in range(baselines_cal_y):
	list_real_cal_y.append(np.loadtxt(file_real_cal_y[i], float))
	list_imag_cal_y.append(np.loadtxt(file_imag_cal_y[i], float))

length_cal_y = min([np.shape(i)[1] for i in list_real_cal_y])
casa_real_cal_y = np.zeros((256,length_cal_y*baselines_cal_y))
casa_imag_cal_y = np.zeros((256,length_cal_y*baselines_cal_y))

for i in range(length_cal_y):
	for j in range(baselines_cal_y):
		casa_real_cal_y[:,i*baselines_cal_y+j] = list_real_cal_y[j][:,i]
		casa_imag_cal_y[:,i*baselines_cal_y+j] = list_imag_cal_y[j][:,i]

casa_real_cal_y = np.transpose(casa_real_cal_y)
casa_imag_cal_y = np.transpose(casa_imag_cal_y)

np.savetxt("casa_real_cal_y.txt", casa_real_cal_y)
np.savetxt("casa_imag_cal_y.txt", casa_imag_cal_y)




