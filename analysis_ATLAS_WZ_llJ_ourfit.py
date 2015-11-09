model = build_model_from_rootfile(["ATLAS_VV_llJ/ATLAS_ZVllJ_newNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_HR_1fb_Signal.root"])

# 
# print model

model.set_signal_processes("WZ*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000,1100,1200,1300,1400,1500, 1600, 1700, 1800, 1900, 2000]

for j in range(0,11,1): 
    procname = "WZ"+str(mass[j])
    # model.scale_predictions(0.5,procname=procname,obsname='ATLAS_VV_JJ_ZZ')#The fudge factor                                                                 
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')
    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_HR')
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

expected.write_txt('results/ATLAS_VV_llJ_WZ_ourfit_expected.txt')
observed.write_txt('results/ATLAS_VV_llJ_WZ_ourfit_observed.txt')
#zlevel.write_txt('CMS_ATLAS_VV_JJ_WZ_ourfit_noFudge_zlevel.txt')


current = 1
with open('results/ATLAS_VV_llJ_WZ_ourfit_zlevel.txt', 'w') as fff:
    while current < 11:
        masse = mass[current]
        sig='WZ'+str(masse)
        zl = zlevel[sig]['Z'][0]
        pl= Z_to_p(zl)
        print str(masse) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl 
        fff.write( str(masse) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '  ' ) 
        fff.write( str(pl))
        fff.write( '\n' )
        current += 1
fff.close()

report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_ATLAS_WZ_llJ_ourfit.py