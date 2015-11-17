model = build_model_from_rootfile(["CMS_VV_lnuJ/CMS_WZ_ELEHP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_WZ_ELELP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_WZ_MUHP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_WZ_MULP_1fb_NarrowSignal.root",
                                   #
                                   #"CMS_VV_lnuJ/CMS_WZ_ELEHP_1fb_WideSignal.root",
                                   #"CMS_VV_lnuJ/CMS_WZ_ELELP_1fb_WideSignal.root",
                                   #"CMS_VV_lnuJ/CMS_WZ_MUHP_1fb_WideSignal.root",
                                   #"CMS_VV_lnuJ/CMS_WZ_MULP_1fb_WideSignal.root",
                                   #
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELEHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELELP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MUHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MULP_dijetLike.root",
                                   #
                                   #
                                   "ATLAS_VV_lnuJ/ATLAS_WVlvJ_MR_thetaNaming_uncorrSys.root",
                                   "ATLAS_VV_lnuJ/ATLAS_lnuJ_WZ_MR_1fb_Signal.root",
                                   # fix to WZ llJ
                                   #"CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike_uncorrSys.root",
                                   #"CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike_uncorrSys.root",
                                   #"CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike_uncorrSys.root",
                                   #"CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike_uncorrSys.root",
                                   #"CMS_VV_llJ/signalsHP_ELE_naming.root",
                                   #"CMS_VV_llJ/signalsHP_MU_naming.root",
                                   #"CMS_VV_llJ/signalsLP_ELE_naming.root",
                                   #"CMS_VV_llJ/signalsLP_MU_naming.root",
                                   #
                                   #"ATLAS_VV_llJ/ATLAS_ZVllJ_newNaming.root",
                                   #"ATLAS_VV_llJ/ATLAS_WZ_MR_1fb_Signal.root",
                                   #"ATLAS_VV_llJ/ATLAS_WZ_HR_1fb_Signal.root",
                                   #
                                   "ATLAS_VV_JJ/ATLAS_WZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noJER_noWZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root",
                                   #
                                   "CMS_VV_JJ/CMS_VV_jj_data_propernaming.root",
                                   "CMS_VV_JJ/CMS_VV_jj_WZ_1fb.root" 
                                   ])
# 
# print model

#model.set_signal_processes("signalGbulk*")

model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWWl=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291]
model.fill_histogram_zerobins(epsilon=0.01)


model.set_signal_processes("WZ*")

filename='results/CMS_ATLAS_VV_lvJ_JJ_WZ_ourfit'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

for j in range(0,16,1): 
    procname = "WZ"+str(mass[j])
    print j , " ", mass[j]
#    model.scale_predictions(fudgeWWl[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
#    model.scale_predictions(fudgeWWl[j],procname=procname,obsname='CMS_VV_lnuj_MULP')#The fudge factor    
#    model.scale_predictions(fudgeWWl[j],procname=procname,obsname='CMS_VV_lnuj_ELEHP')#The fudge factor    
#    model.scale_predictions(fudgeWWl[j],procname=procname,obsname='CMS_VV_lnuj_ELELP')#The fudge factor    
    
    #    procnameA = "BulkWW"+str(mass[j])
    # ATLAS syst                                                               
    #model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_WVlnJ_MR')
    #model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_WVlnJ_MR')
    
    #    # CMS syst
    # shape summed quadratically 
    #model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    #model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    #model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procname,obsname='CMS_VV_lnuj_MULP')
    #model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procname,obsname='CMS_VV_lnuj_ELELP')
    #model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    #model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    # anti correlated
    #model.add_lognormal_uncertainty("catMigration_CMS_WVnnuJ_LP",-0.24,procname=procname,obsname='CMS_VV_lnuj_MULP')
    #model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procname,obsname='CMS_VV_lnuj_ELELP')
    # lumi
    #model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    #model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    #model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_MULP')
    #model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_ELELP')
                                   
    #if (j>4) :
    #    print j , " also hadronic ", mass[j]
    #    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    #    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ')
    #    # CMS syst
    #    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
    #    model.add_lognormal_uncertainty(lumiSystName,0.026,procname=procname,obsname='CMS_JJ_HP')
    #    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
    #    model.add_lognormal_uncertainty(lumiSystName,0.026,procname=procname,obsname='CMS_JJ_LP')

#model.set_signal_process_groups( group )

rangenorm = 4.5
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jescms' or p == 'migrationcms') :
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 :
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    d = model.distribution.get_distribution(p)
    print p, d

print model

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
print expected
print observed
print zlevel



expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 0
with open(zfile, 'w') as fff:
    while current < len(zlevel):
        masse = mass[current]
        sig='WZ'+str(masse)
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
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WZ_lvJ_JJ_ourfit.py