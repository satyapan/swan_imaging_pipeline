#COMBINES ALL THE CODES FOR IMAGING

import os


#input
name_src = 'CYGOBSTEST_20170306_124648'
name_cal = 'CASOBSTEST_20170306_124648'
image_dim_src = 64
pixel_dim_src = "548.0arcsec"
image_dim_cal = 64
pixel_dim_cal = "548.0arcsec"

file_src = open(name_src+'/info.txt', 'r')
lines_src = file_src.readlines()
tiles_src = len(lines_src[3].split(','))
data_src = lines_src[5].split('\t')
file_cal = open(name_cal+'/info.txt', 'r')
lines_cal = file_cal.readlines()
tiles_cal = len(lines_cal[3].split(','))
data_cal = lines_cal[5].split('\t')

int_time_src = float(data_src[5])
ra_src = data_src[2]
dec_src = data_src[3]
freq_centre_src = float(data_src[1])
date_src = name_src.split('_')[1][0:4]+'/'+name_src.split('_')[1][4:6]+'/'+name_src.split('_')[1][6:8]
lst_src = float(data_src[6])
lst_src_end = float(data_src[7])
nfft_src = int(data_src[4])

int_time_cal = float(data_cal[5])
ra_cal = data_cal[2]
dec_cal = data_cal[3]
freq_centre_cal = float(data_cal[1])
date_cal = name_cal.split('_')[1][0:4]+'/'+name_cal.split('_')[1][4:6]+'/'+name_cal.split('_')[1][6:8]
lst_cal = float(data_cal[6])
lst_cal_end = float(data_cal[7])
nfft_cal = int(data_cal[4])

'''
#user input
tiles_src = int(raw_input("Enter number of tiles in source observation: "))
tiles_cal = int(raw_input("Enter number of tiles in calibrator observation: "))
int_time = float(raw_input("Enter the integration time used (in sec): "))
ra_src = raw_input("Enter source RA (eg. 10h10m10s): ")
dec_src = raw_input("Enter source Dec (eg. +10d10m10s): ")
freq_centre_src = float(raw_input("Enter central frequency of source observation (in MHz): "))
image_dim_src = int(raw_input("Enter dimension of source image: "))
pixel_dim_src = raw_input("Enter pixel dimension for source image (eg. 10arcsec): ")
date_src = raw_input("Enter date of source observation (eg. YYYY/MM/DD): ")
ra_cal = raw_input("Enter calibrator RA (eg. 10h10m10s): ")
dec_cal = raw_input("Enter calibrator Dec (eg. +10d10m10s): ")
freq_centre_cal = float(raw_input("Enter central frequency of calibrator observation (in MHz): "))
image_dim_cal = int(raw_input("Enter dimension of calibrator image: "))
pixel_dim_cal = raw_input("Enter pixel dimension for calibrator image (eg. 10arcsec): ")
date_cal = raw_input("Enter date of calibrator observation (eg. YYYY/MM/DD): ")
lst_src = float(raw_input("Enter lst at start of source observation (in hour): "))
lst_cal = float(raw_input("Enter lst at start of calibrator observation (in hour): "))
'''

#run scripts
print("----------Creating tables compatible with casa----------\n")
os.system("python write_vis.py " + str(tiles_src) + " " + str(tiles_cal) + " " + str(name_src) + " " + str(name_cal) + " " + str(nfft_src) + " " + str(nfft_cal))
print("----------Tables created successfully----------\n")
print("----------Creating config file----------\n")
os.system("python create_config.py " + str(tiles_src) + " " + str(tiles_cal))
print("----------Config file created successfully----------\n")
print("----------Starting mock simulation in casa----------\n")
os.system("casa -c casa_sim.py " + ra_src + " " + dec_src + " " + str(freq_centre_src) + " " + str(image_dim_src) + " " + pixel_dim_src + " " + date_src + " " + str(tiles_src) + " " + str(nfft_src) + " " + str(int_time_src) + " " + str(lst_src) + " " + str(lst_src_end) + " " + name_src + " " + ra_cal + " " + dec_cal + " " + str(freq_centre_cal) + " " + str(image_dim_cal) + " " + pixel_dim_cal + " " + date_cal + " " + str(tiles_cal) + " " + str(nfft_cal) + " " + str(int_time_cal) + " " + str(lst_cal) + " " + str(lst_cal_end) + " " + name_cal)
print("----------Simulation completed successfully----------\n")
print("----------Writing visibilities into casa table----------\n")
os.system("casa -c edit_ms.py")
print("----------Casa table created successfully----------\n")
