#REPLACE DATA COLUMN IN SIMULATED TABLES BY ACTUAL VISIBILITIES

import numpy as np

#code for source
cx_src = np.load("casa_src_x.npy")
cy_src = np.load("casa_src_y.npy")
msfile = 'gbd_src.ms'
tb.open(msfile, nomodify = False)
data_src = tb.getcol("DATA")
data_src[0,:,0:np.shape(cx_src)[1]] = cx_src
data_src[1,:,0:np.shape(cy_src)[1]] = cy_src
tb.putcol("DATA", data_src)
tb.putcol("CORRECTED_DATA", data_src)
tb.done()

#code for calib
cx_cal = np.load("casa_cal_x.npy")
cy_cal = np.load("casa_cal_y.npy")
msfile = 'gbd_cal.ms'
tb.open(msfile, nomodify = False)
data_cal = tb.getcol("DATA")
data_cal[0,:,0:np.shape(cx_cal)[1]] = cx_cal
data_cal[1,:,0:np.shape(cy_cal)[1]] = cy_cal
tb.putcol("DATA", data_cal)
tb.putcol("CORRECTED_DATA", data_cal)
tb.done()
