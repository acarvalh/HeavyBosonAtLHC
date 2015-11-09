#model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_VV_JJ_WZ_corrected.root","ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalRS.root","ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_sys_noJER.root"])

model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_WZJJ__DATA_noWZname_publicBackground.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noWZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root"])

# print model

model.set_signal_processes("WZ*")
model.fill_histogram_zerobins(epsilon=0.001)

for mass in range(1500,2500,100):
    procname = "WZ"+str(mass)
    # model.scale_predictions(0.5,procname=procname,obsname='ATLAS_VV_JJ_WZ')#The fudge factor                                                                 
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ')

#rangenorm = 5.5
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

expected.write_txt('results/ATLAS_VV_JJ_WZ_public_expected.txt')
observed.write_txt('results/ATLAS_VV_JJ_WZ_public_observed.txt')

current = 1
with open('results/ATLAS_VV_JJ_WZ_public_zlevel.txt', 'w') as fff:
    while current < len(zlevel):
        masse = current*100+1400
        sig='WZ'+str(masse)
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

# ../theta/utils2/theta-auto.py analysis_ATLAS_WZ_JJ_public.py