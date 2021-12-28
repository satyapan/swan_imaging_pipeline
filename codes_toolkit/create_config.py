#CREATE THE INPUT CONFIGURATION FILE FOR CASA
import os
import sys
import numpy as np

config_data = ["1349783.1183164874	6052369.188149821	1490432.8161248143	4.0	T001",
"1349849.4922549364	6052345.6053048  	1490476.7343282872	4.0	T002",
"1349818.3704501214	6052346.271209999	1490497.792848539	4.0	T003",
"1349749.0157884855	6052351.018719776	1490528.2749782056	4.0	T004",
"1349803.4351994954	6052353.884256003	1490463.5134460311	4.0	T005",
"1349794.3460679834	6052350.917344763	1490492.1603514191	4.0	T006",
"1349839.1331877327	6052350.865902079	1490460.5826145809	4.0	T007"]

#input
tiles_used_src = []
tiles_used_cal = []

for i in range(int(sys.argv[1])):
	elem = raw_input("Enter tile id for source: ")
	tiles_used_src.append(int(elem))

for i in range(int(sys.argv[2])):
	elem = raw_input("Enter tile id for calibrator: ")
	tiles_used_cal.append(int(elem))

np.savetxt('tiles_used_src.cfg', np.array(tiles_used_src), fmt='%i')
np.savetxt('tiles_used_cal.cfg', np.array(tiles_used_cal), fmt='%i')

#code for source
outfile_src = open("gbd_src.cfg", "w")
outfile_src.write("# observatory=GBD\n# coordsys=XYZ\n# x y z diam pad#\n# Created by user\n# June 14 2018\n")

for i in tiles_used_src:
	outfile_src.write(config_data[i-1]+"\n")

outfile_src.close()

#code for calibrator
outfile_cal = open("gbd_cal.cfg", "w")
outfile_cal.write("# observatory=GBD\n# coordsys=XYZ\n# x y z diam pad#\n# Created by user\n# June 14 2018\n")

for i in tiles_used_cal:
	outfile_cal.write(config_data[i-1]+"\n")

outfile_cal.close()
