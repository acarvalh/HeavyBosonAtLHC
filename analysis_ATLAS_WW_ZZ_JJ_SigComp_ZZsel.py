model = build_model_from_rootfile([
                                   "ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_oneSys.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root"])
# 
rr = 10
print rr
rww =  rr/(1.+rr)
rzz =  1./(1+rr)

filename='results/ATLAS_WW_ZZ_JJ_ZZSel_r'+str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

for j in range(0,11,1): 
  procnameww = "BulkWW"+str(mass[j])
  procnamezz = "BulkZZ"+str(mass[j])
  
  totWW= rww*0.7027
  totZZ= rzz

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
pl_interval = pl_interval(model, "data", 1)
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
# ../theta/utils2/theta-auto.py analysis_ATLAS_WW_ZZ_JJ_SigComp_ZZsel.py