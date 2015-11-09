model = build_model_from_rootfile(["CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkWW_1fb.root",
                                   "CMS_VV_JJ/CMS_VV_jj_WZ_1fb.root"])

# 
rr = 2
print rr
rww =  rr/(1.+rr)
rzz =  1./(1+rr)

filename='results/CMS_WW_WZ_JJ_r'+str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)

for mass in range(1500,2600,100):
    #for rr in range(1, 11,2): # r

  
  #for mass in range(1500,2500,100):
  #mass = 1800
  procnameww = "BulkWW"+str(mass)
  procnamezz = "WZ"+str(mass)
  model.scale_predictions(rww,procname=procnameww,obsname="CMS_JJ_HP")#The fudge factor                                                    
  model.scale_predictions(rzz,procname=procnamezz,obsname="CMS_JJ_HP")#The fudge factor  
  model.scale_predictions(rww,procname=procnameww,obsname="CMS_JJ_LP")#The fudge factor                                                    
  model.scale_predictions(rzz,procname=procnamezz,obsname="CMS_JJ_LP")#The fudge factor  
  #model.set_signal_processes(procnameww)

  # CMS syst
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameww,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameww,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameww,obsname='CMS_JJ_LP')
  model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameww,obsname='CMS_JJ_LP')

  # CMS syst
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnamezz,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("lumicms",0.026,procname=procnamezz,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnamezz,obsname='CMS_JJ_LP')
  model.add_lognormal_uncertainty("lumicms",0.026,procname=procnamezz,obsname='CMS_JJ_LP')

  procname='VVBulk'+str(mass)
  #group = {procname : [procnameww, procnamezz]}
  # print group
 
  # add signal to group 
  if (mass==1500):
    group = {procname : [procnameww, procnamezz]}
  else:
    group[procname] = [procnameww, procnamezz]

model.set_signal_process_groups( group )
#      else:
#group[procname] = [procname1, procname1]
#  model.set_signal_process_groups( "VVBulk*" )
 
  
#model.set_signal_processes("VVBulk*")

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
        mass = current*100+1400
        sig='VVBulk'+str(mass)
        # print sig
        zl = zlevel[sig]['Z'][0]
        pl = Z_to_p(zl)
        print str(mass) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl 
        fff.write( str(mass) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '  ' ) 
        fff.write( str(pl) )
        fff.write( '\n' )
        current += 1
fff.close()
print rr
report.write_html('htmlout')

# ../theta/utils2/theta-auto.py analysis_CMS_WW_WZ_JJ_SigComp.py