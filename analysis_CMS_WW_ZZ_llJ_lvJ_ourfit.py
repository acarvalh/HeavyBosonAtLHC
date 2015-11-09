model = build_model_from_rootfile(["CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/signalsHP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsHP_MU_naming.root",
                                   "CMS_VV_llJ/signalsLP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsLP_MU_naming.root"
                                   ])
# 
# print model

model.set_signal_processes("BulkZZ*")
#rangenorm = 2.5
model.fill_histogram_zerobins(epsilon=0.001)
#mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

#for j in range(0,6,1): 
#    procname = "BulkZZ"+str(mass[j])
#    # model.scale_predictions(0.5,procname=procname,obsname='ATLAS_VV_JJ_ZZ')#The fudge factor                                                                 
#    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
#    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
#    # model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ_WZ')

#for p in model.distribution.get_parameters():
#    d = model.distribution.get_distribution(p)
#    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='vtagcms' :
#        model.distribution.set_distribution_parameters(p, range = [-1*rangenorm, rangenorm])
#    
#    d = model.distribution.get_distribution(p)
#    print p, d


expected, observed = asymptotic_cls_limits(model)
print expected
print observed
zlevel = zvalue_approx(model, "data", 1)
print zlevel

expected.write_txt('results/CMS_VV_llJ_BulkZZ_ourfit_expected.txt')
observed.write_txt('results/CMS_VV_llJ_BulkZZ_ourfit_observed.txt')
#zlevel.write_txt('CMS_ATLAS_VV_JJ_WZ_ourfit_noFudge_zlevel.txt')

current = 1
with open('results/CMS_VV_llJ_BulkZZ_ourfit_zlevel.txt', 'w') as fff:
    while current < 16:
        mass = current*100+900
        sig='BulkZZ'+str(mass)
        zl = zlevel[sig]['Z'][0]
        pl= Z_to_p(zl)
        print str(mass) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl 
        fff.write( str(mass) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '  ' ) 
        fff.write( str(pl))
        fff.write( '\n' )
        current += 1
fff.close()

report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_CMS_BulkZZ_llJ_ourfit.py