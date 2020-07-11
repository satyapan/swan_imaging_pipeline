#COMBINES ALL THE CODES FOR IMAGING

import os


#input
tiles_src = 4
tiles_cal = 4
int_time = 9.216
ra_src = "21h10m15s"
dec_src = "-16d18m10s"
freq_centre_src = 195
image_dim_src = 64
pixel_dim_src = "548.0arcsec"
date_src = "2017/02/03"
ra_cal = "19h59m28s"
dec_cal = "+40d44m2s"
freq_centre_cal = 191
image_dim_cal = 64
pixel_dim_cal = "548.0arcsec"
date_cal = "2016/12/15"
lst_src = 19.06
lst_cal = 15.41

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
os.system("python write_vis.py " + str(tiles_src) + " " + str(tiles_cal))
print("----------Tables created successfully----------\n")
print("----------Creating config file----------\n")
os.system("python create_config.py " + str(tiles_src) + " " + str(tiles_cal))
print("----------Config file created successfully----------\n")
print("----------Starting mock simulation in casa----------\n")
os.system("casa -c casa_sim.py " + str(int_time) + " " + ra_src + " " + dec_src + " " + str(freq_centre_src) + " " + str(image_dim_src) + " " + pixel_dim_src + " " + date_src + " " + str(tiles_src) + " " + ra_cal + " " + dec_cal + " " + str(freq_centre_cal) + " " + str(image_dim_cal) + " " + pixel_dim_cal + " " + date_cal + " " + str(tiles_cal) + " " + str(lst_src) + " " + str(lst_cal))
print("----------Simulation completed successfully----------\n")
print("----------Writing visibilities into casa table----------\n")
os.system("python edit_ms.py")
os.system("casa -c import_join.py")
print("----------Casa table created successfully----------\n")
