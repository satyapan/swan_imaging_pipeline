from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.coordinates import FK5
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.time import Time
import scipy.fftpack

RA = "1h30m56s"
Dec = "9d30m37s"
date = '2021-04-14'
hour = '12'
minute = '17'
second = '8'


#ECEF TO ENU
import pymap3d as pm
tilecoordsx = []
tilecoordsy = []
coordslist = np.loadtxt('ECEF_SWAN.txt')
lat = 13.6183
long = 77.5146
h = 691.09
zeropoint = pm.ecef2enu(coordslist[0,0],coordslist[0,1],coordslist[0,2],lat,long,h,ell=None,deg=True)
for i in range(np.shape(coordslist)[0]):
	converted = pm.ecef2enu(coordslist[i,0],coordslist[i,1],coordslist[i,2],lat,long,h,ell=None,deg=True)
	tilecoordsx.append(converted[0]-zeropoint[0])
	tilecoordsy.append(converted[1]-zeropoint[1])

tilecoordsx = np.array(tilecoordsx)
tilecoordsy = np.array(tilecoordsy)

#tilecoordsx = np.array([0,-69.8,-39.4,28,-23.6,-16.2,-59.2])
#tilecoordsy = np.array([0,44.6,69.6,99.4,33.6,63.3,27.5])

tilecoords = np.zeros((7,2))
tilecoords[:,0] = tilecoordsx
tilecoords[:,1] = tilecoordsy

tileh = 4
tilev = 1
duration_pc = 30
cen_freq = 200e6

#EXPECTED
def currdelay(a,b,h,m,s):
    c = SkyCoord(RA, Dec, frame='icrs', equinox = 'J2000')    
    gbd = EarthLocation(lat=13.6112*u.deg, lon=77.5170*u.deg, height=694*u.m)          
    utcoffset = 5.5*u.hour                                                             
    arg = date + ' ' + str(h) +':' + str(m) + ':' + str(s)
    time = Time(arg) - utcoffset
    altaz = c.transform_to(AltAz(obstime=time,location=gbd))
    alt = "{0.alt}".format(altaz)
    az = "{0.az}".format(altaz)
    import re
    alt = float((re.findall("\d+\.\d+", alt))[0])
    az = float((re.findall("\d+\.\d+", az))[0])
    alt = alt*np.pi/180
    az = az*np.pi/180
    x = np.sin(az)*np.cos(alt)
    y = np.cos(az)*np.cos(alt)
    z = np.sin(alt)
    sourcevec = np.array([x,y,z])
    baselinex = np.zeros((7,7))
    baseliney = np.zeros((7,7))
    baselinez = np.zeros((7,7))
    for i in range(7):
        for j in range(7):
            baselinex[i,j] = tilecoords[j,0]-tilecoords[i,0]
            baseliney[i,j] = tilecoords[j,1]-tilecoords[i,1]
    vector = np.array([baselinex[a,b],baseliney[a,b],0])
    c = 3e8
    z = np.dot(vector,sourcevec)/c
    return z


tile1 = int(tileh)-1
tile2 = int(tilev)-1
start_time = (int(hour)*3600)+(int(minute)*60)+(int(second))                     
def conv(t):
    l = []
    h = t//3600
    m = (t-h*3600)//60
    s = (t-h*3600-m*60)
    l.append(h)
    l.append(m)
    l.append(s)
    return l


expdelay = []
exptime = []
for i in range(duration_pc):                           
    currt = start_time + i*0.92
    currt = int(currt)
    temp = currdelay(tile2,tile1,int(conv(currt)[0]),int(conv(currt)[1]),conv(currt)[2])
    expdelay.append(temp)
    exptime.append(float(i)/0.92)


#OBSERVED
phase = []
obsdel = []
data = np.load('Correlation_Y4Y1_ch04_SUN_20210414_121708_000.mbr_ch01_SUN_20210414_121708_000.mbr.txt.npy')
for j in range(np.shape(data)[1]):
	c = data[:,j]
	a = [i.real for i in c]
	b = [i.imag for i in c]
	z = []
	for i in range(256):
		z.append(complex(a[i],b[i]))
	for i in range(256*9):
		z.append(0)  
	corr = scipy.fftpack.ifft(z)
	corr = [corr[i]/np.sqrt(len(corr)) for i in range(len(corr))]
	corr1 = [i.real for i in corr]
	corr2 = [i.imag for i in corr]
	ampcorr = [np.sqrt(corr1[i]**2 + corr2[i]**2) for i in range(2560)]
	phase.append(np.angle(complex(corr1[np.argmax(ampcorr)],corr2[np.argmax(ampcorr)]))*180/np.pi)
	
phasefinal = np.array(phase)
i = 0
while i < len(phase)-1:
    if (phase[i+1] - phase[i]) > 180:
        phase[i+1] = phase[i+1] - 360
    elif (phase[i+1] - phase[i]) < -180:
        phase[i+1] = phase[i+1] + 360
    else:
        i = i + 1


phase = np.array(phase)
phase = phase - min(phase)
obsdelay = phase/(360*cen_freq)


plt.plot(phasefinal)
plt.show()
plt.plot(exptime,expdelay-min(expdelay), label='Expected')
plt.plot(obsdelay, label='Observed')
plt.legend()
plt.show()
