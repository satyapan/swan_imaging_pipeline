#input
image_dim_src = 64
pixel_dim_src = "548.0arcsec"


tclean(vis = 'gbd_src.ms', imagename = 'dirty', imsize = image_dim_src, deconvolver = 'hogbom', specmode = 'cubedata', weighting = 'natural', niter = 0, cell = pixel_dim_src)



tclean(vis='mod_final.ms',
       imagename='source_init',
       field='1',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       nterms=1,
       gridder='standard',
       imsize=[64,64],
       cell=['548.0arcsec'],
       weighting='natural',
       threshold='0mJy',
       niter=5000,
       interactive=True,
       savemodel='modelcolumn')
imview('source_init.image')
gaincal(vis="mod_final.ms",
        caltable="phase.cal",
        field="0",
        solint="30s",
        calmode="p",
        refant="1",
        minblperant=1,
        minsnr=2.0,
        gaintype="G")
plotms(vis="phase.cal", 
       xaxis="time", 
       yaxis="phase", 
       gridrows=3, 
       gridcols=3, 
       iteraxis="antenna", 
       plotrange=[0,0,-30,30], 
       titlefont=7, 
       xaxisfont=7, 
       yaxisfont=7, 
       plotfile="mod_image_cal_phase_scan.png", 
       showgui = True)
applycal(vis="mod_final.ms",
         field="1",
         gaintable=["phase.cal"],
         interp="linear")
split(vis="mod_final.ms",
      outputvis="mod_final_cal.ms",
      datacolumn="corrected")


tclean(vis='mod_final_cal.ms',
       imagename='source_cal',
       field='1',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       nterms=1,
       gridder='standard',
       imsize=[64,64],
       cell=['548.0arcsec'],
       weighting='natural',
       threshold='0mJy',
       niter=5000,
       interactive=True,
       savemodel='modelcolumn')
imview('source_cal.image')

