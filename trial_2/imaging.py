#inputs
image_dim_src = int(sys.argv[3])
pixel_dim_src = sys.argv[4]
image_dim_cal = int(sys.argv[5])
pixel_dim_cal = sys.argv[6]
n_iterations = int(raw_input('Maximum number of iterations for CLEAN: '))

#dirty
tclean(vis = 'gbd_src.ms', imagename = 'dirty_src', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'cubedata', weighting = 'natural', niter = 0, cell = pixel_dim_src)

tclean(vis = 'gbd_cal.ms', imagename = 'dirty_cal', imsize = image_dim_cal, deconvolver = 'hogbom', specmode = 'cubedata', weighting = 'natural', niter = 0, cell = pixel_dim_cal)

#calibration
tclean(vis = 'gbd_src.ms', imagename = 'source_init', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'cubedata', weighting = 'natural', niter = n_iterations, cell = pixel_dim_src, savemodel='modelcolumn')

tclean(vis = 'gbd_cal.ms', imagename = 'calib_init', imsize = image_dim_cal, deconvolver = 'hogbom', specmode = 'cubedata', weighting = 'natural', niter = n_iterations, cell = pixel_dim_cal, savemodel='modelcolumn')

gaincal(vis="gbd_cal.ms", caltable="phase.cal", solint="30s", calmode="p", refant="1", minblperant=1, minsnr=2.0, gaintype="G")

plotms(vis="phase.cal", xaxis="time", yaxis="phase", gridrows=3, gridcols=3, iteraxis="antenna", plotrange=[0,0,-30,30], titlefont=7, xaxisfont=7, yaxisfont=7, plotfile="gbd_image_cal_phase_scan.png", showgui = True)

os.system('cp -r gbd_src.ms gbd_src_calib.ms')

applycal(vis="gbd_src_calib.ms", gaintable=["phase.cal"], interp="linear")

tclean(vis = 'gbd_src_calib.ms', imagename = 'source_final', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'cubedata', weighting = 'natural', niter = n_iterations, cell = pixel_dim_src)

imview('source_final.image')
