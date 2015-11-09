model = build_model_from_rootfile(["CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_WZ_1fb.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noJER_noWZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root"])

# 
rr = 1
print rr
rWW =  rr/(1.+rr)
rWZ =  1./(1+rr)

filename='results/CMS_ATLAS_VV_JJ_WZ_ourfit_WWSel'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)
model.set_signal_processes("WZ*")

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]


fudgeWZ=[0.516994, 0.557296, 0.607179, 0.630566, 0.636335, 0.622595, 0.610246, 0.605146, 0.568741, 0.551866, 0.577838]

for j in range(0,11,1): 

  
  #for mass in range(1500,2500,100):
  #mass = 1800
  procnameWZ = "WZ"+str(mass[j])
  #  model.scale_predictions(rWZ,procname=procnameZZ,obsname="CMS_JJ_HP")#The fudge factor                                                    

#  model.scale_predictions(rWZ,procname=procnameZZ,obsname="CMS_JJ_LP")#The fudge factor                                                    
  #model.set_signal_processes(procnameZZ)

  # CMS syst
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameWZ,obsname='CMS_JJ_HP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameZZ,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameWZ,obsname='CMS_JJ_LP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameZZ,obsname='CMS_JJ_LP')
  
  # ATLAS syst
  ArWZ=0.6459

  model.scale_predictions(ArWZ,procname=procnameWZ,obsname="ATLAS_VV_JJ")#The fudge factor 
                                                                        
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnameWZ,obsname='ATLAS_VV_JJ')
  #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnameZZ,obsname='ATLAS_VV_JJ')
  
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-4.5, 4.5])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
        model.distribution.set_distribution_parameters(p, range = [-4.5, 4.5])
    
    d = model.distribution.get_distribution(p)
    print p, d

expected, observed = asymptotic_cls_limits(model)
clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
print model
model_summary(model, True)
print expected, observed
print zlevel
print pvalue

expected.write_txt(expfile)
observed.write_txt(obsfile)

print expfile
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
        sig='WZ'+str(masse)
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

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WZ_JJ_WWwindow.py