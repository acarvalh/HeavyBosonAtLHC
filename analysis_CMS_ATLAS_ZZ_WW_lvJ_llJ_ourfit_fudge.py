model = build_model_from_rootfile([# CMS lvJ WW
                                   "CMS_VV_lnuJ/CMS_BulkWW_ELEHP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_ELELP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_MUHP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_MULP_1fb_NarrowSignal.root",
                                   # CMS lvJ bkg
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELEHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELELP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MUHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MULP_dijetLike.root",
                                   # ATLAS lvJ WW
                                   "ATLAS_VV_lnuJ/ATLAS_WVlvJ_MR_thetaNaming_uncorrSys.root",
                                   "ATLAS_VV_lnuJ/ATLAS_lnuJ_WW_MR_1fb_Signal.root",
                                   # CMS llJ ZZ
                                   "CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/signalsHP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsHP_MU_naming.root",
                                   "CMS_VV_llJ/signalsLP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsLP_MU_naming.root",
                                   # ATLAS llJ ZZ
                                   "ATLAS_VV_llJ/ATLAS_ZVllJ_thetaNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root"
                                   ])
# 
# print model

rr = 10
print rr
rww =  rr/(1.+rr)
rzz =  1./(1+rr)

#model.set_signal_processes("signalGbulk*")
rangenorm = 10
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWWlv=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291]
fudgeWZll=[0.959326, 0.924054, 0.843844, 0.854296, 0.834417, 0.8884, 0.844526, 0.811389, 0.838875, 0.767706, 0.759]
fudgeZZllCMS=[1.09879, 1.05341, 1.00664, 1.03848, 1.11259, 1.02073, 1.11013, 1.10722, 1.15051, 1.0962, 1.13582, 1.15223, 1.20053, 1.16918, 1.2755, 1.31541]
fudgeWZlvJATLAS = [0.795712, 0.929701, 0.936624, 0.980215, 1.03092, 1.04214, 1.07966, 1.04453, 1.0487, 1.00702, 0.959159, 0.880764, 0.787317, 0.729852, 0.674062, 0.645124]

filename='results/CMS_ATLAS_VV_lvJ_llJ_ZZ_WW_ourfit_Fudge_r' +str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

for j in range(0,16,1): 
    procnamezz = "BulkZZ"+str(mass[j])
    procnameww = "BulkWW"+str(mass[j])


    
    # ATLAS syst  lvJ WW 
    #
    model.scale_predictions(rww*fudgeWZlvJATLAS[j],procname=procnameww,obsname='ATLAS_WVlnJ_MR')
    model.add_lognormal_uncertainty("normalisation_WWlvJ_atlas",0.1,procname=procnameww,obsname='ATLAS_WVlnJ_MR')
    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnameww,obsname='ATLAS_WVlnJ_MR')

    #    # CMS syst lvJ WW
    model.scale_predictions(fudgeWWlv[j]*rww,procname=procnameww,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
    model.scale_predictions(fudgeWWlv[j]*rww,procname=procnameww,obsname='CMS_VV_lnuj_MULP')#The fudge factor    
    model.scale_predictions(fudgeWWlv[j]*rww,procname=procnameww,obsname='CMS_VV_lnuj_ELEHP')#The fudge factor    
    model.scale_predictions(fudgeWWlv[j]*rww,procname=procnameww,obsname='CMS_VV_lnuj_ELELP')#The fudge factor    
    # shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procnameww,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procnameww,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procnameww,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procnameww,obsname='CMS_VV_lnuj_ELELP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procnameww,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procnameww,obsname='CMS_VV_lnuj_ELEHP')
    # anti correlated
    model.add_lognormal_uncertainty("catMigration_CMS_WVnnuJ_LP",-0.24,procname=procnameww,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procnameww,obsname='CMS_VV_lnuj_ELELP')
    # lumi
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnameww,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnameww,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnameww,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnameww,obsname='CMS_VV_lnuj_ELELP')

    #    # CMS syst  llJ WZ
    # shape summed quadratically 
    model.scale_predictions(rzz*fudgeZZllCMS[j],procname=procnamezz,obsname='CMS_ZVmmJ_HP')#The fudge factor    
    model.scale_predictions(rzz*fudgeZZllCMS[j],procname=procnamezz,obsname='CMS_ZVmmJ_LP')#The fudge factor    
    model.scale_predictions(rzz*fudgeZZllCMS[j],procname=procnamezz,obsname='CMS_ZVeeJ_HP')#The fudge factor    
    model.scale_predictions(rzz*fudgeZZllCMS[j],procname=procnamezz,obsname='CMS_ZVeeJ_LP')#The fudge factor 
    #
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procnamezz,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procnamezz,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procnamezz,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procnamezz,obsname='CMS_ZVeeJ_LP')
    #    
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procnamezz,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procnamezz,obsname='CMS_ZVeeJ_HP')
    # anti correlated
    model.add_lognormal_uncertainty("catMigration_CMS_WVnnuJ_LP",-0.24,procname=procnamezz,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procnamezz,obsname='CMS_ZVeeJ_LP')
    # lumi
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnamezz,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnamezz,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnamezz,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procnamezz,obsname='CMS_ZVeeJ_LP')
    
    if j<11 :
        #    # ATLAS syst  llJ ZZ
        model.scale_predictions(fudgeWZll[j]*rzz,procname=procnamezz,obsname='ATLAS_ZVllJ_MR')#The fudge factor                 
        model.scale_predictions(fudgeWZll[j]*rzz,procname=procnamezz,obsname='ATLAS_ZVllJ_HR')#The fudge factor   
        model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procnamezz,obsname='ATLAS_ZVllJ_MR')
        model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procnamezz,obsname='ATLAS_ZVllJ_HR')
        model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnamezz,obsname='ATLAS_ZVllJ_MR')
        model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procnamezz,obsname='ATLAS_ZVllJ_MR')

    procnamet='WZsemi'+str(mass[j])
    if (j==0):
      group = {procnamet : [procnamezz, procnameww ]}
    else:
      group[procnamet] = [procnamezz, procnameww ]
#model.set_signal_process_groups( group )

print group
model.set_signal_process_groups( group )

rangenorm = 5.0
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
        model.distribution.set_distribution_parameters(p, range = [-1*rangenorm, rangenorm])
    
    d = model.distribution.get_distribution(p)
    print p, d

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
print expected
print observed
print zlevel



expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
with open(zfile, 'w') as fff:
    while current < len(zlevel):
        masse = mass[current]
        sig='WZsemi'+str(masse)
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
print rr
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_ZZ_WW_lvJ_llJ_ourfit_fudge.py