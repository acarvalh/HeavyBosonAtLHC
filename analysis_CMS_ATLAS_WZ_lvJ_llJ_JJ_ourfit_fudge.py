model = build_model_from_rootfile(["CMS_VV_lnuJ/CMS_WZ_ELEHP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_WZ_ELELP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_WZ_MUHP_1fb_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_WZ_MULP_1fb_NarrowSignal.root",
                                   #
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELEHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELELP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MUHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MULP_dijetLike.root",
                                   #
                                   "ATLAS_VV_lnuJ/ATLAS_WVlvJ_MR_thetaNaming_uncorrSys.root",
                                   "ATLAS_VV_lnuJ/ATLAS_lnuJ_WZ_MR_1fb_Signal.root",
                                   #
                                   "CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/signalsHP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsHP_MU_naming.root",
                                   "CMS_VV_llJ/signalsLP_ELE_naming.root",
                                   "CMS_VV_llJ/signalsLP_MU_naming.root",
                                   #
                                   "ATLAS_VV_llJ/ATLAS_ZVllJ_thetaNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_HR_1fb_Signal.root",
                                   #
                                   "ATLAS_VV_JJ/ATLAS_WZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noWZname.root",
                                   #"ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root",
                                   #
                                   #"CMS_VV_JJ/CMS_VV_jj_data.root",
                                   #"CMS_VV_JJ/CMS_VV_jj_WZ_1fb.root"
                                   ])
# 
# print model

#model.set_signal_processes("signalGbulk*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWWlv=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291]
fudgeWZll=[0.959326, 0.924054, 0.843844, 0.854296, 0.834417, 0.8884, 0.844526, 0.811389, 0.838875, 0.767706, 0.759]
fudgeZZllCMS=[1.09879, 1.05341, 1.00664, 1.03848, 1.11259, 1.02073, 1.11013, 1.10722, 1.15051, 1.0962, 1.13582, 1.15223, 1.20053, 1.16918, 1.2755, 1.31541]
fudgeWZlvJATLAS = [0.795712, 0.929701, 0.936624, 0.980215, 1.03092, 1.04214, 1.07966, 1.04453, 1.0487, 1.00702, 0.959159, 0.880764, 0.787317, 0.729852, 0.674062, 0.645124]

fudgeWZJJ=[1,1,1,1,1,0.513282, 0.553725, 0.609789, 0.637297, 0.642589, 0.626628, 0.610983, 0.601232, 0.560182, 0.538367, 0.557967]

rangenorm = 3.0

model.set_signal_processes("WZ*")

filename='results/CMS_ATLAS_VV_lvJ_llJ_JJ_WZ_ourfit_Fudge'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'
z17 = filename+'_Lik1700.txt'
z18 = filename+'_Lik1800.txt'
z19 = filename+'_Lik1900.txt'
z20 = filename+'_Lik2000.txt'
z21 = filename+'_Lik2100.txt'
z22 = filename+'_Lik2200.txt'

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

for j in range(0,16,1): 
    procname = "WZ"+str(mass[j])
    procname2 = "BulkZZ"+str(mass[j])

    model.scale_predictions(fudgeWWlv[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
    model.scale_predictions(fudgeWWlv[j],procname=procname,obsname='CMS_VV_lnuj_MULP')#The fudge factor    
    model.scale_predictions(fudgeWWlv[j],procname=procname,obsname='CMS_VV_lnuj_ELEHP')#The fudge factor    
    model.scale_predictions(fudgeWWlv[j],procname=procname,obsname='CMS_VV_lnuj_ELELP')#The fudge factor    
    
    #    procnameA = "WZsemi"+str(mass[j])
    # ATLAS syst                                                               
    model.scale_predictions(fudgeWZlvJATLAS[j],procname=procname,obsname='ATLAS_WVlnJ_MR')
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_WVlnJ_MR')
    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_WVlnJ_MR')
    
    #    # CMS syst lvJ
    # shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procname,obsname='CMS_VV_lnuj_ELELP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    # anti correlated
    model.add_lognormal_uncertainty("catMigration_CMS_WVnnuJ_LP",-0.24,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procname,obsname='CMS_VV_lnuj_ELELP')
    # lumi
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_ELELP')

    #    # CMS syst  llJ -- fix to WZ
    model.scale_predictions(fudgeZZllCMS[j],procname=procname2,obsname='CMS_ZVmmJ_HP')
    model.scale_predictions(fudgeZZllCMS[j],procname=procname2,obsname='CMS_ZVeeJ_HP')
    model.scale_predictions(fudgeZZllCMS[j],procname=procname2,obsname='CMS_ZVmmJ_LP')
    model.scale_predictions(fudgeZZllCMS[j],procname=procname2,obsname='CMS_ZVeeJ_LP')
    # shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procname2,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procname2,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procname2,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procname2,obsname='CMS_ZVeeJ_LP')
    
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procname2,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procname2,obsname='CMS_ZVeeJ_HP')
    # anti correlated
    model.add_lognormal_uncertainty("catMigration_CMS_WVnnuJ_LP",-0.24,procname=procname2,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procname2,obsname='CMS_ZVeeJ_LP')
    # lumi
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname2,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname2,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname2,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname2,obsname='CMS_ZVeeJ_LP')
    
    if j<11 :
        model.scale_predictions(fudgeWZll[j],procname=procname,obsname='ATLAS_ZVllJ_MR')#The fudge factor                 
        model.scale_predictions(fudgeWZll[j],procname=procname,obsname='ATLAS_ZVllJ_HR')#The fudge factor   
        model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
        model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
        model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')
        model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')

    if j>4 :
        model.scale_predictions(fudgeWZJJ[j],procname=procname,obsname='ATLAS_VV_JJ') 
        model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
        model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ')
        # CMS syst
#model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
#model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_HP')
#model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
#model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_LP')

    procnamet='WZsemi'+str(mass[j])
    if (j==0):
      group = {procnamet : [procname, procname2]}
    else:
      group[procnamet] = [procname, procname2]
#model.set_signal_process_groups( group )

print group
model.set_signal_process_groups( group )

#####################################
# with fudge 3.5
# no fudge: 2.5
rangenorm = 3.0
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    
    d = model.distribution.get_distribution(p)
    print p, d
#####################################

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
nll = nll_scan(model, "data", 1, range=[0.0, 25.0])
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

with open(z17, 'w') as fff:
        masse = 1700
        print str(masse)
        sig='WZsemi'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z18, 'w') as fff:
        masse = 1800
        print str(masse)
        sig='WZsemi'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z19, 'w') as fff:
        masse = 1900
        print str(masse)
        sig='WZsemi'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z20, 'w') as fff:
        masse = 2000
        print str(masse)
        sig='WZsemi'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z21, 'w') as fff:
        masse = 2100
        print str(masse)
        sig='WZsemi'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z22, 'w') as fff:
        masse = 2200
        print str(masse)
        sig='WZsemi'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WZ_lvJ_llJ_JJ_ourfit_fudge.py