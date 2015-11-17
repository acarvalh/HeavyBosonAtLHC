model = build_model_from_rootfile(["CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkWW_1fb.root",
                                   "CMS_VV_JJ/CMS_VV_jj_WZ_1fb.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_correct_toSigComp_rescaled.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noWZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_sys_noJER_noWWname.root"
                                   ])

# 
rr = 0.1
print rr
rww =  rr/(1.+rr)
rzz =  1./(1+rr)

filename='results/CMS_ATLAS_WW_WZ_JJ_WWSel_r'+str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]


fudgeZZ=[0.531894, 0.555135, 0.566784, 0.601672, 0.630537, 0.618207, 0.596984, 0.616378, 0.519181, 0.520399, 0.495976]

fudgeWW=[0.534724, 0.580952, 0.63504, 0.654515, 0.650031, 0.626703, 0.607802, 0.598088, 0.559351, 0.541227, 0.528914]

fudgeWZ=[0.546842, 0.587651, 0.627857, 0.632878, 0.618277, 0.59454, 0.631304, 0.621285, 0.598796, 0.576514, 0.575571]

for j in range(0,11,1): 

  
  #for mass in range(1500,2500,100):
  #mass = 1800
  procnameww = "BulkWW"+str(mass[j])
  procnamezz = "WZ"+str(mass[j]) 
  #model.set_signal_processes(procnameww)

  # CMS syst
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.1326,procname=procnameww,obsname='CMS_JJ_HP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameww,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.1326,procname=procnameww,obsname='CMS_JJ_LP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameww,obsname='CMS_JJ_LP')

  # CMS syst
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.1326,procname=procnamezz,obsname='CMS_JJ_HP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnamezz,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.1326,procname=procnamezz,obsname='CMS_JJ_LP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnamezz,obsname='CMS_JJ_LP')
  
  # ATLAS syst
  Arzz=fudgeWZ[j]*rzz*0.6459 
  Arww=fudgeWW[j]*rww
                                                                        
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnameww,obsname='ATLAS_VV_JJ')
  #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnameww,obsname='ATLAS_VV_JJ')
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnamezz,obsname='ATLAS_VV_JJ')
  #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnamezz,obsname='ATLAS_VV_JJ')

  model.scale_predictions(Arzz,procname=procnamezz,obsname="ATLAS_VV_JJ")#The fudge factor  
  model.scale_predictions(Arww,procname=procnameww,obsname="ATLAS_VV_JJ")#The fudge factor 
        
  model.scale_predictions(rww,procname=procnameww,obsname="CMS_JJ_HP")#The fudge factor                                                    
  model.scale_predictions(rzz,procname=procnamezz,obsname="CMS_JJ_HP")#The fudge factor  
  model.scale_predictions(rww,procname=procnameww,obsname="CMS_JJ_LP")#The fudge factor                                                    
  model.scale_predictions(rzz,procname=procnamezz,obsname="CMS_JJ_LP")#The fudge factor 

  procname='VVBulk'+str(mass[j])
  #group = {procname : [procnameww, procnamezz]}
  # print group
 
  # add signal to group 
  if (j==0):
    group = {procname : [procnameww, procnamezz]}
  else:
    group[procname] = [procnameww, procnamezz]
print group


model.set_signal_process_groups( group )

# less r  2.5 ; midle r 3.5
#rangenorm=5.5
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

model_summary(model, True)
print expected, observed
print zlevel
print pvalue

expected.write_txt(expfile)
observed.write_txt(obsfile)

#  clevel = pl_interval(model, "data", 1)
#  zlevel = zvalue_approx(model, "data", 1)
#  model_summary(model, True)
#  print expected, observed
#print zlevel
#  print pvalue
current = 1
with open(zfile, 'w') as fff:
    while current < len(zlevel)+1:
        masse = current*100+1400
        sig='VVBulk'+str(masse)
        # print sig
        zl = zlevel[sig]['Z'][0]
        pl = Z_to_p(zl)
        print str(masse) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl 
        fff.write( str(masse) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '  ' ) 
        fff.write( str(pl) )
        fff.write( '\n' )
        current += 1
fff.close()
print rr
report.write_html('htmlout')

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WW_WZ_JJ_SigComp_WWwindow.py