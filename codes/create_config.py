#CREATE THE INPUT CONFIGURATION FILE FOR CASA
import os
import sys

config_data = ["6051714.67719166 1490265.3574421208 -5028499.072829625   4.0  T001",
"6051691.088789608 1490305.789631197 -5028438.251664513   4.0  T002",
"6051690.460534494 1490331.4898462987 -5028464.004054427  4.0  T003",
"6051697.730783643 1490362.2440451474 -5028530.7927353345 4.0  T004",
"6051703.562190832 1490294.0686041447 -5028481.150569755  4.0  T005",
"6051698.870807559 1490321.8119440177 -5028490.956010129  4.0  T006",
"6051695.1444783   1490290.41250288   -5028439.342895502  4.0  T007",
"6051707.987910144 1490317.6181852415 -5028527.174760653  4.0  T008"]

#input
tiles_used_src = []
tiles_used_cal = []

for i in range(int(sys.argv[1])):
	elem = raw_input("Enter tile id for source: ")
	tiles_used_src.append(int(elem))

for i in range(int(sys.argv[2])):
	elem = raw_input("Enter tile id for calibrator: ")
	tiles_used_cal.append(int(elem))

#code for source
outfile_src = open("gbd_src.cfg", "w")
outfile_src.write("# observatory=GBD\n# coordsys=LOC (local tangent plane)\n# x y z diam pad#\n# Created by user\n# June 14 2018\n")

for i in tiles_used_src:
	outfile_src.write(config_data[i-1]+"\n")

outfile_src.close()

#code for calibrator
outfile_cal = open("gbd_cal.cfg", "w")
outfile_cal.write("# observatory=GBD\n# coordsys=LOC (local tangent plane)\n# x y z diam pad#\n# Created by user\n# June 14 2018\n")

for i in tiles_used_cal:
	outfile_cal.write(config_data[i-1]+"\n")

outfile_cal.close()
