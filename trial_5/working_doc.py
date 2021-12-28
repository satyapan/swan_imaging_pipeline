import numpy as np
import glob

file_list = sorted(glob.glob('*.npy'))
xx_file_list = []
yy_file_list = []
N = len(file_list)/2
for i in range(N):
	xx_file_list.append(file_list[i])
	yy_file_list.append(file_list[N+i])

'''
For Cygnus
for i in range(N):
    xx_list.append(np.load(xx_file_list[i])[1,:,:])
    yy_list.append(np.load(yy_file_list[i])[1,:,:])
xx_arr = np.hstack(xx_list)
yy_arr = np.hstack(yy_list)

np.save('X1X2.npy',xx_arr)
np.save('Y1Y2.npy',yy_arr)
'''

def get_sec(x):
	h = int(x[0:2])
	m = int(x[2:4])
	s = int(x[4:6])
	return s+60*m+3600*h


xx_list = []
yy_list = []

n_ext=5
time = get_sec(xx_file_list[0][-22:-16])
file_count = 0
for i in range(N/n_ext):
	file_name_xx = xx_file_list[i*n_ext]
	file_name_yy = yy_file_list[i*n_ext]
	offset = get_sec(file_name_xx[-22:-16]) - time
	if offset != 0:
		blank_arr = np.zeros((256,offset),dtype='complex')
		xx_list.append(blank_arr)
		yy_list.append(blank_arr)
	time = get_sec(file_name_xx[-22:-16])
	for j in range(n_ext):
		file_name_xx = xx_file_list[i*n_ext+j]
		file_name_yy = yy_file_list[i*n_ext+j]
		xx = np.load(file_name_xx)[1,:,:]
		yy = np.load(file_name_yy)[1,:,:]
		xx_list.append(xx)
		yy_list.append(yy)
		time = time + xx.shape[1]


xx_arr = np.hstack(xx_list)
yy_arr = np.hstack(yy_list)

np.save('X3X7.npy',xx_arr)
np.save('Y3Y7.npy',yy_arr)
