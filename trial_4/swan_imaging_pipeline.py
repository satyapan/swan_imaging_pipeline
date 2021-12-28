#COMBINES ALL THE CODES FOR IMAGING

import os

#input
'''
name_src = 'SUN_20210414_121708'
name_cal = 'SUN_20210414_121708'
image_dim_src = 64
pixel_dim_src = "548.0arcsec"
image_dim_cal = 64
pixel_dim_cal = "548.0arcsec"
'''

import readline
readline.parse_and_bind("tab: complete")

#user input
name_src = raw_input('Folder containing source visibilities: ')
name_cal = raw_input('Folder containing calibrator visibilities: ')
image_dim_src = int(raw_input('Dimension of source image: '))
pixel_dim_src = raw_input('Source image pixel size in arcsec: ')
image_dim_cal = int(raw_input('Dimension of calibrator image: '))
pixel_dim_cal = raw_input('Calibrator image pixel size in arcsec: ')



#get metadata
file_src = open(name_src+'/info.cfg', 'r')
lines_src = file_src.readlines()
tiles_src = len(lines_src[3].split(','))
data_src = lines_src[5].split('\t')
file_cal = open(name_cal+'/info.cfg', 'r')
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
print("----------Calibration and Imaging----------\n")
os.system("casa -c imaging.py " + str(image_dim_src) + " " + pixel_dim_src + " " + str(image_dim_cal) + " " + pixel_dim_cal)
print("----------Calibration and Imaging completed successfully----------\n")
