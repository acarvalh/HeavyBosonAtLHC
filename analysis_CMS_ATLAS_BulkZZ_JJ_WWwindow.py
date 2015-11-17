model = build_model_from_rootfile(["CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_correct_toSigComp_rescaled.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_sys_noJER_noZZname.root"])

# 
rr = 1
print rr
rWW =  rr/(1.+rr)
rWZ =  1./(1+rr)

filename='results/CMS_ATLAS_VV_JJ_ZZ_rescaled_Fudge_WWSel'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)
model.set_signal_processes("BulkZZ*")

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]


fudgeZZ=[0.531894, 0.555135, 0.566784, 0.601672, 0.630537, 0.618207, 0.596984, 0.616378, 0.519181, 0.520399, 0.495976]

for j in range(0,11,1): 

  
  #for mass in range(1500,2500,100):
  #mass = 1800
  procnameWW = "BulkZZ"+str(mass[j])
  #  model.scale_predictions(rWZ,procname=procnameZZ,obsname="CMS_JJ_HP")#The fudge factor                                                    

#  model.scale_predictions(rWZ,procname=procnameZZ,obsname="CMS_JJ_LP")#The fudge factor                                                    
  #model.set_signal_processes(procnameZZ)

  # CMS syst
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameWW,obsname='CMS_JJ_HP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameZZ,obsname='CMS_JJ_HP')
  model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameWW,obsname='CMS_JJ_LP')
  #model.add_lognormal_uncertainty("lumicms",0.026,procname=procnameZZ,obsname='CMS_JJ_LP')
  
  # ATLAS syst
  ArZZ=fudgeZZ[j]*0.4172

  model.scale_predictions(ArZZ,procname=procnameWW,obsname="ATLAS_VV_JJ")#The fudge factor 
                                                                        
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnameWW,obsname='ATLAS_VV_JJ')
  #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnameZZ,obsname='ATLAS_VV_JJ')
  
#procname='VVBulk'+str(mass[j])
  #group = {procname : [procnameZZ, procnamezz]}
  # print group
 
  # add signal to group 
  #  if (j==0):
  #  group = {procname : [procnameZZ, procnamezz]}
  #else:
#  group[procname] = [procnameZZ, procnamezz]
#print group

#model.set_signal_process_groups( group )
#      else:
#group[procname] = [procname1, procname1]
#  model.set_signal_process_groups( "VVBulk*" )
 
  
#model.set_signal_processes("VVBulk*")

expected, observed = asymptotic_cls_limits(model)
clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)

print model
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
        sig='BulkZZ'+str(masse)
        #print sig
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

report.write_html('htmlout')

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkZZ_JJ_WWwindow.py