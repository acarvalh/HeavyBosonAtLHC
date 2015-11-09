model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_WZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_oneSys.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noWZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root"
                                   ])

# 
rr = 10
print rr
rww =  rr/(1.+rr)
rwz =  1./(1+rr)

filename='results/ATLAS_WW_WZ_JJ_WZSel_Fudge_r'+str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]


fudgeWZ=[0.513282, 0.553725, 0.609789, 0.637297, 0.642589, 0.626628, 0.610983, 0.601232, 0.560182, 0.538367, 0.557967]

fudgeWW=[0.562062, 0.607006, 0.664361, 0.683049, 0.672502, 0.643021, 0.677244, 0.652601, 0.611615, 0.575068, 0.558068]


for j in range(0,11,1): 

  
  #for mass in range(1500,2500,100):
  #mass = 1800
  procnamewz = "WZ"+str(mass[j])
  procnameww = "BulkWW"+str(mass[j]) 
  #model.set_signal_processes(procnameww)

  # ATLAS syst
  Arww=fudgeWW[j]*rww*0.8382 
  Arwz=fudgeWZ[j]*rwz
                                                                        
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnameww,obsname='ATLAS_VV_JJ')
  #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnameww,obsname='ATLAS_VV_JJ')
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnamewz,obsname='ATLAS_VV_JJ')
  #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnamezz,obsname='ATLAS_VV_JJ')

  model.scale_predictions(Arwz,procname=procnamewz,obsname="ATLAS_VV_JJ")#The fudge factor  
  model.scale_predictions(Arww,procname=procnameww,obsname="ATLAS_VV_JJ")#The fudge factor 
        

  procname='VVBulk'+str(mass[j])
  #group = {procname : [procnameww, procnamezz]}
  # print group
 
  # add signal to group 
  if (j==0):
    group = {procname : [procnameww, procnamewz]}
  else:
    group[procname] = [procnameww, procnamewz]
print group


model.set_signal_process_groups( group )

#rangenorm=2.5
#for p in model.distribution.get_parameters():
#    d = model.distribution.get_distribution(p)
#    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
#        model.distribution.set_distribution_parameters(p, range = [-1*rangenorm, rangenorm])
#    
#    d = model.distribution.get_distribution(p)
#    print p, d

expected, observed = asymptotic_cls_limits(model)
clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
model_summary(model, True)
print expected, observed
print zlevel
print pvalue

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
with open(zfile, 'w') as fff:
    while current < len(zlevel)+1:
        masse = current*100+1400
        sig='VVBulk'+str(masse)
        zl = zlevel[sig]['Z'][0]
        pl = Z_to_p(zl)
        bf= pl_interval[sig][0][0]
        bf1u= pl_interval[sig][0.6826894921370859][0][0]
        bf1d= pl_interval[sig][0.6826894921370859][0][1]
        bf2u= pl_interval[sig][0.9544997361036416][0][0]
        bf2d= pl_interval[sig][0.9544997361036416][0][1]
        print str(masse) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl , " ", bf , " ", bf2d , " ", bf1d , " ", bf1u , " ", bf2u 
        fff.write( str(masse) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '  ' ) 
        fff.write( str(pl) )
        fff.write( '  ' ) 
        fff.write( str(bf) )
        fff.write( '  ' ) 
        fff.write( str(bf2d) )
        fff.write( '  ' ) 
        fff.write( str(bf1d) )
        fff.write( '  ' ) 
        fff.write( str(bf1u) )
        fff.write( '  ' ) 
        fff.write( str(bf2u) )
        fff.write( '\n' )
        current += 1
fff.close()
#report.write_html('htmlout')
print rr

# ../theta/utils2/theta-auto.py analysis_ATLAS_WW_WZ_JJ_SigComp_WZwindow_Fudge.py