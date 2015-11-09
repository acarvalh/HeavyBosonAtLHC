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
                                   "ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root",
                                   #
                                   "ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root",
                                   #
                                   #"CMS_VV_JJ/CMS_VV_jj_data.root",
                                   #"CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root"
                                   ])
# 
# print model

model.set_signal_processes("BulkZZ*")
#rangenorm = 2.5
model.fill_histogram_zerobins(epsilon=0.001)

mass=[1000,1100,1200,1300,1400,1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
fudgeWZll=[0.959326, 0.924054, 0.843844, 0.854296, 0.834417, 0.8884, 0.844526, 0.811389, 0.838875, 0.767706, 0.759]

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

filename='results/CMS_ATLAS_VV_llJ_JJ_BulkZZ_ourfit'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'
z17 = filename+'_Lik1700.txt'
z18 = filename+'_Lik1800.txt'
z19 = filename+'_Lik1900.txt'
z20 = filename+'_Lik2000.txt'
z21 = filename+'_Lik2100.txt'
z22 = filename+'_Lik2200.txt'

for j in range(0,16,1): 
    procname = "BulkZZ"+str(mass[j])

    #
    # semilep
    #
    #    # CMS syst
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
        #model.scale_predictions(fudgeWZll[j],procname=procname,obsname='ATLAS_ZVllJ_MR')#The fudge factor                 
        #model.scale_predictions(fudgeWZll[j],procname=procname,obsname='ATLAS_ZVllJ_HR')#The fudge factor   
      model.add_lognormal_uncertainty("normalisation_VVllJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
      model.add_lognormal_uncertainty("normalisation_VVllJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
      model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')
      model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_ZVllJ_MR')

    if j>4 :
      #model.scale_predictions(fudgeZZ[j],procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor                            
      model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
      model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ')
      # CMS syst
      #model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
      #model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_HP')
      #model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
      #model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_LP')

rangenorm=5.0
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 :
        model.distribution.set_distribution_parameters(p, range = [-1*rangenorm, rangenorm])    
    d = model.distribution.get_distribution(p)
    print p, d

expected, observed = asymptotic_cls_limits(model)
print expected
print observed
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
nll = nll_scan(model, "data", 1, range=[0.0, 25.0])
print zlevel

#expected.write_txt('results/CMS_ATLAS_VV_llJ_JJ_BulkZZ_ourfit_expected.txt')
#observed.write_txt('results/CMS_ATLAS_VV_llJ_JJ_BulkZZ_ourfit_observed.txt')

current = 0
with open(zfile, 'w') as fff:
    while current < len(zlevel):
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

#print nll

with open(z17, 'w') as fff:
        masse = 1700
        sig='BulkZZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z18, 'w') as fff:
        masse = 1800
        sig='BulkZZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z19, 'w') as fff:
        masse = 1900
        sig='BulkZZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z20, 'w') as fff:
        masse = 2000
        sig='BulkZZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z21, 'w') as fff:
        masse = 2100
        sig='BulkZZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z22, 'w') as fff:
        masse = 2200
        sig='BulkZZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkZZ_llJ_JJ_ourfit.py