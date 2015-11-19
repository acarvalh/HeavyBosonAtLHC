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
                                   #"ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root",
                                   #
                                   "ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root",
                                   #
                                   "CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root"
                                   ])
# 
# print model



mass=[1000,1100,1200,1300,1400,1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]


fudge = 1

fudgeWWlvCMS=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291] 
fudgeWZlvJATLAS = [0.795712, 0.929701, 0.936624, 0.980215, 1.03092, 1.04214, 1.07966, 1.04453, 1.0487, 1.00702, 0.959159, 0.880764, 0.787317, 0.729852, 0.674062, 0.645124] 
fudgeWWlvJATLAS = [1.34167, 1.21314, 1.08996, 1.08625, 1.11429, 1.14418, 1.1409,  1.06639, 1.08099, 1.06824, 1.01071, 0.963582, 0.904669, 0.831587, 0.787872, 0.746516]

fudgeZZllCMS=[1.09879, 1.05341, 1.00664, 1.03848, 1.11259, 1.02073, 1.11013, 1.10722, 1.15051, 1.0962, 1.13582, 1.15223, 1.20053, 1.16918, 1.2755, 1.31541]
fudgeZZllJATLAS=[1.2004, 1.1734, 1.03546, 1.04473, 1.06224, 0.939548, 1.0411, 1.02485, 1.00821, 1.01614, 0.915197]
fudgeWZllJATLAS = [1.04091, 0.959243, 0.86275, 0.869074, 0.844375, 0.8973, 0.852316, 0.817111, 0.843688, 0.777118, 0.768438]

fudgeZZJJATLAS=[1,1,1,1,1,0.55619, 0.565121, 0.561593, 0.569191, 0.564982, 0.528031, 0.488941,0.488903, 0.40283, 0.401571, 0.387373]
fudgeWWJJATLAS=[1,1,1,1,1,0.513282, 0.553725, 0.609789, 0.637297, 0.642589, 0.626628, 0.610983, 0.601232, 0.560182, 0.538367, 0.557967]
fudgeWZJJATLAS=[1,1,1,1,1,0.562062, 0.607006, 0.664361, 0.683049, 0.672502, 0.643021, 0.677244,0.652601, 0.611615, 0.575068, 0.558068]

lumiSystNameCMS = "lumiSystCMS"
lumiSystValueCMS = 0.026
lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

narrow=1.1

filename='results/CMS_ATLAS_VV_llJ_JJ_BulkZZ_ourfit'
fudgeLabel = '_Fudge'
if fudge :
   expfile = filename+fudgeLabel+'_expected.txt'
   obsfile = filename+fudgeLabel+'_observed.txt'
   zfile = filename+fudgeLabel+'_zlevel.txt'
   z17 = filename+fudgeLabel+'_Lik1700.txt'
   z18 = filename+fudgeLabel+'_Lik1800.txt'
   z19 = filename+fudgeLabel+'_Lik1900.txt'
   z20 = filename+fudgeLabel+'_Lik2000.txt'
   z21 = filename+fudgeLabel+'_Lik2100.txt'
   z22 = filename+fudgeLabel+'_Lik2200.txt'
else :
    expfile = filename+'_expected.txt'
    obsfile = filename+'_observed.txt'
    zfile = filename+'_zlevel.txt'
    z17 = filename+'_Lik1700.txt'
    z18 = filename+'_Lik1800.txt'
    z19 = filename+'_Lik1900.txt'
    z20 = filename+'_Lik2000.txt'
    z21 = filename+'_Lik2100.txt'
    z22 = filename+'_Lik2200.txt'


model.set_signal_processes("BulkZZ*")
model.fill_histogram_zerobins(epsilon=0.001)

for j in range(0,16,1): 
    procname = "BulkZZ"+str(mass[j])
    #####################################################################################################
    # Fudge
    if fudge :
       # CMS llJ
       model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVmmJ_HP')
       model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVeeJ_HP')
       model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVmmJ_LP')
       model.scale_predictions(fudgeZZllCMS[j],procname=procname,obsname='CMS_ZVeeJ_LP')
       # ATLAS llJ
       if j<11 :
          model.scale_predictions(fudgeZZllJATLAS[j],procname=procname,obsname='ATLAS_ZVllJ_MR')#The fudge factor                 
          #model.scale_predictions(fudgeWZllJATLAS[j],procname=procname,obsname='ATLAS_ZVllJ_HR')#The fudge factor      
       if j>4 :
          model.scale_predictions(fudgeZZJJATLAS[j]*narrow,procname=procname,obsname='ATLAS_VV_JJ') 
    elif j>4 :
       model.scale_predictions(narrow,procname=procname,obsname='ATLAS_VV_JJ') 
    ######################################################################################################
    # systematics
    # CMSllJ
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVeeJ_LP')
    # shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_MUHP",0.03,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_ELEHP",0.037,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_MULP",0.03,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_ELELP",0.037,procname=procname,obsname='CMS_ZVeeJ_LP')
    # migration
    model.add_lognormal_uncertainty("catMigration_CMS_VV_llj_MUHP",0.09,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_llj_ELEHP",0.09,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_WVllJ_LP",-0.24,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_llj_ELELP",-0.24,procname=procname,obsname='CMS_ZVeeJ_LP')
    # ATLAS llJ
    if j<11 :
      model.add_lognormal_uncertainty("normalisation_VVllJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
      #model.add_lognormal_uncertainty("normalisation_VVllJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
      model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_ZVllJ_MR')
      #model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_ZVllJ_HR')
    # VV JJ
    if j>4 :
      # ATLAS
      model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
      model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_VV_JJ')
      # CMS syst
      model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
      model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_JJ_HP')
      model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
      model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_JJ_LP')

expected, observed = asymptotic_cls_limits(model)
print expected
print observed
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
nll = nll_scan(model, "data", 1, range=[0.0, 25.0])
print zlevel

expected.write_txt(expfile)
observed.write_txt(obsfile)

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

print zfile
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkZZ_llJ_JJ_ourfit.py