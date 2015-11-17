model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_WZ_correct_toSigComp_rescaled.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_sys_noJER_noWWname.root"])

filename='results/ATLAS_VV_JJ_WW_rescaled_Fudge_WZSel'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)
model.set_signal_processes("BulkWW*")

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]


fudgeWW=[0.516994, 0.557296, 0.607179, 0.630566, 0.636335, 0.622595, 0.610246, 0.605146, 0.568741, 0.551866, 0.577838]

for j in range(0,11,1): 
  procname = "BulkWW"+str(mass[j])
  # ATLAS syst
  ArZZ=fudgeWW[j]*0.8382

  model.scale_predictions(ArZZ,procname=procname,obsname="ATLAS_VV_JJ")#The fudge factor 
                                                                        
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
  model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ')
  
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
        sig='BulkWW'+str(masse)
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

# ../theta/utils2/theta-auto.py analysis_ATLAS_WW_JJ_WZwindow.py