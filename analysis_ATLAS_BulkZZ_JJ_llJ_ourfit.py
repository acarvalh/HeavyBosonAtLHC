model = build_model_from_rootfile([
                                   "ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp_rescaled.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root",
                                   "ATLAS_VV_llJ/ATLAS_ZVllJ_newNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root"])
# 
# print model

model.set_signal_processes("BulkZZ*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

for j in range(0,6,1): 
    procname = "BulkZZ"+str(mass[j])
    # model.scale_predictions(0.5,procname=procname,obsname='ATLAS_VV_JJ_ZZ')#The fudge factor                                                                 
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    # model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ_WZ')

    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')

#for p in model.distribution.get_parameters():
#    d = model.distribution.get_distribution(p)
#    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
#        model.distribution.set_distribution_parameters(p, range = [-1*rangenorm, rangenorm])
#    
#    d = model.distribution.get_distribution(p)
#    print p, d

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
print expected
print observed
print zlevel

expected.write_txt('results/ATLAS_VV_JJ_llJ_BulkZZ_rescaled_expected.txt')
observed.write_txt('results/ATLAS_VV_JJ_llJ_BulkZZ_rescaled_observed.txt')
#zlevel.write_txt('CMS_ATLAS_VV_JJ_WZ_ourfit_noFudge_zlevel.txt')


current = 1
with open('results/ATLAS_VV_JJ_llJ_BulkZZ_rescaled_zlevel.txt', 'w') as fff:
    while current < 12:
        mass = current*100+1400
        sig='BulkZZ'+str(mass)
        zl = zlevel[sig]['Z'][0]
        print str(mass) , " Zlevel ",zlevel[sig]['Z'][0] 
        fff.write( str(mass) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '\n' )
        current += 1
fff.close()

report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_ATLAS_BulkZZ_JJ_llJ_ourfit.py