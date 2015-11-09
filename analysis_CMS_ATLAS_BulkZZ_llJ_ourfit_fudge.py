model = build_model_from_rootfile(["CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/signalsHP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsHP_MU_naming.root",
                                   "CMS_VV_llJ/signalsLP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsLP_MU_naming.root",
                                   #
                                   "ATLAS_VV_llJ/ATLAS_ZVllJ_thetaNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root"
                                   ])
# 
# print model

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

mass=[1000,1100,1200,1300,1400,1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
fudgeWZll=[0.959326, 0.924054, 0.843844, 0.854296, 0.834417, 0.8884, 0.844526, 0.811389, 0.838875, 0.767706, 0.759,1,1,1,1,1]
fudgeZZllCMS=[1.09879, 1.05341, 1.00664, 1.03848, 1.11259, 1.02073, 1.11013, 1.10722, 1.15051, 1.0962, 1.13582, 1.15223, 1.20053, 1.16918, 1.2755, 1.31541]

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

model.set_signal_processes("BulkZZ*")
#rangenorm = 2.5
model.fill_histogram_zerobins(epsilon=0.001)
#mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

for j in range(0,16,1): 
    #    # model.scale_predictions(0.5,procname=procname,obsname='ATLAS_VV_JJ_ZZ')#The fudge factor    
    procname = "BulkZZ"+str(mass[j])
    #    # CMS syst
    model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVmmJ_HP')
    model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVeeJ_HP')
    model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVmmJ_LP')
    model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVeeJ_LP')
    # shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procname,obsname='CMS_ZVeeJ_LP')
    
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procname,obsname='CMS_ZVeeJ_HP')
    # anti correlated
    model.add_lognormal_uncertainty("catMigration_CMS_WVnnuJ_LP",-0.24,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procname,obsname='CMS_ZVeeJ_LP')
    # lumi
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_ZVeeJ_LP')

    if j<11 :
       model.scale_predictions(fudgeWZll[j],procname=procname,obsname='ATLAS_ZVllJ_MR')#The fudge factor                 
       model.scale_predictions(fudgeWZll[j],procname=procname,obsname='ATLAS_ZVllJ_HR')#The fudge factor   
       model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
       model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
       model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')
       model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')

expected, observed = asymptotic_cls_limits(model)
print expected
print observed
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
print zlevel

expected.write_txt('results/CMS_ATLAS_VV_llJ_BulkZZ_ourfit_Fudge_expected.txt')
observed.write_txt('results/CMS_ATLAS_VV_llJ_BulkZZ_ourfit_Fudge_observed.txt')
#zlevel.write_txt('CMS_ATLAS_VV_JJ_WZ_ourfit_noFudge_zlevel.txt')

current = 1
with open('results/CMS_ATLAS_VV_llJ_BulkZZ_ourfit_Fudge_zlevel.txt', 'w') as fff:
    while current < 16:
        masse = mass[current]
        sig='BulkZZ'+str(masse)
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

report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkZZ_llJ_ourfit_fudge.py