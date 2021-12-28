import os

#inputs
image_dim_src = int(sys.argv[3])
pixel_dim_src = sys.argv[4]
image_dim_cal = int(sys.argv[5])
pixel_dim_cal = sys.argv[6]
n_iterations = int(raw_input('Maximum number of iterations for CLEAN: '))

os.system('mkdir cal_image')

#dirty
tclean(vis = 'gbd_src.ms', datacolumn='data', imagename = 'cal_image/dirty_src', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_src)

tclean(vis = 'gbd_cal.ms', datacolumn='data', imagename = 'cal_image/dirty_cal', imsize = image_dim_cal, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_cal)

'''
#bandpass calibration
setjy(vis='gbd_cal.ms', fluxdensity = [5000,0,0,0], standard='manual')

bandpass(vis='gbd_cal.ms', caltable='bandpass.cal', bandtype='BPOLY', minblperant=1, fillgaps=True)

plotms(vis='bandpass.bcal', xaxis='frequency', yaxis='amplitude', gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="bandpass_cal.png", showgui = True)
'''

#primary calibration
os.system('cp -r gbd_cal.ms gbd_cal_pri.ms')

setjy(vis='gbd_cal_pri.ms', fluxdensity = [10000,0,0,0], standard='manual', usescratch=True)
gaincal(vis="gbd_cal_pri.ms", caltable="primary.cal", solint="10s", calmode="p", minblperant=1, gaintype="G", minsnr = 1)

#plotms(vis="primary.cal", xaxis="time", yaxis="amplitude", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="primary_cal_amp.png", showgui = True)
plotms(vis="primary.cal", xaxis="time", yaxis="phase", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="primary_cal_phase.png", showgui = True)

applycal(vis="gbd_cal_pri.ms", gaintable=["primary.cal"], interp="linear")

tclean(vis = 'gbd_cal_pri.ms', datacolumn='corrected', imagename = 'cal_image/dirty_cal_pri', imsize = image_dim_cal, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_cal)

os.system('cp -r gbd_src.ms gbd_src_pri.ms')
applycal(vis="gbd_src_pri.ms", gaintable=["primary.cal"], interp="nearest")

tclean(vis = 'gbd_src_pri.ms', datacolumn='corrected', imagename = 'cal_image/dirty_src_pri', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_src)


#self calibration
tclean(vis = 'gbd_src_pri.ms', imagename = 'image_src_init', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = n_iterations, cell = pixel_dim_src, savemodel='modelcolumn', threshold='0.0Jy')

gaincal(vis="gbd_src_pri.ms", caltable="self.cal", solint="10s", calmode="p", refant="1", minblperant=1, minsnr=1, gaintype="G")

plotms(vis="self.cal", xaxis="time", yaxis="phase", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="self_src_phase.png", showgui = True)

os.system('cp -r gbd_src.ms gbd_src_self.ms')

applycal(vis="gbd_src_self.ms", gaintable=["self.cal"], interp="nearest")

tclean(vis = 'gbd_src_self.ms', imagename = 'image_src_self', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = n_iterations, cell = pixel_dim_src)

imview('source_final.image')




'''
#inputs
image_dim_src = int(sys.argv[3])
pixel_dim_src = sys.argv[4]
image_dim_cal = int(sys.argv[5])
pixel_dim_cal = sys.argv[6]
n_iterations = int(raw_input('Maximum number of iterations for CLEAN: '))

#dirty
tclean(vis = 'gbd_src.ms', datacolumn='DATA', imagename = 'dirty_src', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_src)

tclean(vis = 'gbd_cal.ms', datacolumn='DATA', imagename = 'dirty_cal', imsize = image_dim_cal, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_cal)


#bandpass calibration
#setjy(vis='gbd_cal.ms', fluxdensity = [5000,0,0,0], standard='manual')

#bandpass(vis='gbd_cal.ms', caltable='bandpass.cal', bandtype='BPOLY', minblperant=1, fillgaps=True)

#plotms(vis='bandpass.bcal', xaxis='frequency', yaxis='amplitude', gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, #yaxisfont=7, plotfile="bandpass_cal.png", showgui = True)


#primary calibration
setjy(vis='gbd_cal.ms', fluxdensity = [11000,0,0,0], standard='manual')

gaincal(vis="gbd_cal.ms", caltable="primary.cal", solint="10s", calmode="ap", minblperant=1, gaintype="G", minsnr = 0.001)

plotms(vis="primary.cal", xaxis="time", yaxis="phase", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="primary_cal_phase.png", showgui = True)
plotms(vis="primary.cal", xaxis="time", yaxis="amplitude", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="primary_cal_amp.png", showgui = True)

os.system('cp -r gbd_cal.ms gbd_cal_pri.ms')
applycal(vis="gbd_cal_pri.ms", gaintable=["primary.cal"], interp="linear")

tclean(vis = 'gbd_cal_pri.ms', datacolumn='corrected', imagename = 'dirty_cal_pri', imsize = image_dim_cal, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_cal)

os.system('cp -r gbd_src.ms gbd_src_pri.ms')
applycal(vis="gbd_src_pri.ms", gaintable=["primary.cal"], interp="linear")

tclean(vis = 'gbd_src_pri.ms', datacolumn='corrected', imagename = 'dirty_src_pri', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = 0, cell = pixel_dim_src)


#self calibration
tclean(vis = 'gbd_src_pri.ms', imagename = 'image_src_init', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = n_iterations, cell = pixel_dim_src, savemodel='modelcolumn', threshold='0.0Jy')

gaincal(vis="gbd_cal.ms", caltable="self.cal", solint="30s", calmode="ap", refant="1", minblperant=1, minsnr=0.001, gaintype="G")

plotms(vis="self.cal", xaxis="time", yaxis="phase", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="self_cal_phase.png", showgui = True)
plotms(vis="self.cal", xaxis="time", yaxis="amplitude", gridrows=3, gridcols=3, iteraxis="antenna", titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="self_cal_amp.png", showgui = True)

os.system('cp -r gbd_src.ms gbd_src_self.ms')

applycal(vis="gbd_src_self.ms", gaintable=["self.cal"], interp="linear")

tclean(vis = 'gbd_src_self.ms', imagename = 'image_src_self', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'mfs', weighting = 'natural', niter = n_iterations, cell = pixel_dim_src)

imview('source_final.image')

'''
