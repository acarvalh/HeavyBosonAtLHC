model = build_model_from_rootfile([
                                   "ATLAS_VV_JJ/ATLAS_WW_correct_toSigComp_rescaled.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_oneSys.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root"])
# 
rr = 0.1
print rr
rww =  rr/(1.+rr)
rzz =  1./(1+rr)

filename='results/ATLAS_WW_ZZ_JJ_WWSel_r'+str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeZZ=[0.531894, 0.555135, 0.566784, 0.601672, 0.630537, 0.618207, 0.596984, 0.616378, 0.519181, 0.520399, 0.495976]

fudgeWW=[0.516994, 0.557296, 0.607179, 0.630566, 0.636335, 0.622595, 0.610246, 0.605146, 0.568741, 0.551866, 0.577838]


for j in range(0,11,1): 
  procnameww = "BulkWW"+str(mass[j])
  procnamezz = "BulkZZ"+str(mass[j])
  
  totWW= rww
  totZZ= rzz*0.4172

  model.scale_predictions(totWW,procname=procnameww,obsname='ATLAS_VV_JJ')#The fudge factor                                                                 
  model.scale_predictions(totZZ,procname=procnamezz,obsname='ATLAS_VV_JJ')#The fudge factor                                  
    
  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnameww,obsname='ATLAS_VV_JJ')
  model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnameww,obsname='ATLAS_VV_JJ')

  model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnamezz,obsname='ATLAS_VV_JJ') 
  model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnamezz,obsname='ATLAS_VV_JJ')

  procname='VVBulk'+str(mass[j])
  #group = {procname : [procnameww, procnamezz]}
  # print group
 
  # add signal to group 
  if (j==0):
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

report.write_html('htmlout')
print rr
# ../theta/utils2/theta-auto.py analysis_ATLAS_WW_ZZ_JJ_SigComp_WWsel.py