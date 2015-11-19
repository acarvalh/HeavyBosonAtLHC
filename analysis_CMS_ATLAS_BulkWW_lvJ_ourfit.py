model = build_model_from_rootfile(["CMS_VV_lnuJ/CMS_BulkWW_ELEHP_1fb_Signal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_ELELP_1fb_Signal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_MUHP_1fb_Signal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_MULP_1fb_Signal.root",
                                   #
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELEHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELELP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MUHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MULP_dijetLike.root",
                                   #
                                   "ATLAS_VV_lnuJ/ATLAS_WVlvJ_MR_thetaNaming_uncorrSys.root",
                                   #"ATLAS_VV_lnuJ/ATLAS_WVlnuJ_dijetfit_correct_MR.root",
                                   "ATLAS_VV_lnuJ/ATLAS_lnuJ_WW_MR_1fb_Signal.root"#,
                                   #"ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root"
                                   ])
# 
# print model

fudge = 0

model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWWlvCMS=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291] 
fudgeWZlvJATLAS = [0.795712, 0.929701, 0.936624, 0.980215, 1.03092, 1.04214, 1.07966, 1.04453, 1.0487, 1.00702, 0.959159, 0.880764, 0.787317, 0.729852, 0.674062, 0.645124] 
fudgeWWlvJATLAS = [1.34167, 1.21314, 1.08996, 1.08625, 1.11429, 1.14418, 1.1409,  1.06639, 1.08099, 1.06824, 1.01071, 0.963582, 0.904669, 0.831587, 0.787872, 0.746516]

lumiSystNameCMS = "lumiSystCMS"
lumiSystValueCMS = 0.026
lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

model.set_signal_processes("BulkWW*")

filename='results/CMS_ATLAS_VV_lvJ_BulkWW_ourfit'
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


for j in range(0,16,1): 
    procname = "BulkWW"+str(mass[j])
    #####################################################################################################
    # Fudge
    if fudge :
        # CMS lvJ
        model.scale_predictions(fudgeWWlvCMS[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')
        model.scale_predictions(fudgeWWlvCMS[j],procname=procname,obsname='CMS_VV_lnuj_ELEHP')
        model.scale_predictions(fudgeWWlvCMS[j],procname=procname,obsname='CMS_VV_lnuj_MULP')
        model.scale_predictions(fudgeWWlvCMS[j],procname=procname,obsname='CMS_VV_lnuj_ELELP')
        # ATLAS lvJ
        model.scale_predictions(fudgeWWlvJATLAS[j],procname=procname,obsname='ATLAS_WVlnJ_MR')#The fudge factor
    ######################################################################################################  
    # ATLAS syst                        
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_WVlnJ_MR')
    model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_WVlnJ_MR')    
    #  CMS syst
    # shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_MUHP",0.03,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELEHP",0.037,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty("normalisation_CMS_WVnnuJ_LP",0.03,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_lnuj_ELELP",0.037,procname=procname,obsname='CMS_VV_lnuj_ELELP')
    # migration
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_MUHP",0.09,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELEHP",0.09,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty("catMigration_CMS_WV_lnuJ_MULP",-0.24,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_lnuj_ELELP",-0.24,procname=procname,obsname='CMS_VV_lnuj_ELELP')
    # lumi
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_VV_lnuj_ELELP')

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
nll = nll_scan(model, "data", 1, range=[0.0, 25.0])
print expected
print observed
print zlevel

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 0
with open(zfile, 'w') as fff:
    while current < len(zlevel):
        masse = mass[current]
        sig='BulkWW'+str(masse)
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
        sig='BulkWW'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z18, 'w') as fff:
        masse = 1800
        print str(masse)
        sig='BulkWW'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z19, 'w') as fff:
        masse = 1900
        print str(masse)
        sig='BulkWW'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z20, 'w') as fff:
        masse = 2000
        print str(masse)
        sig='BulkWW'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z21, 'w') as fff:
        masse = 2100
        print str(masse)
        sig='BulkWW'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z22, 'w') as fff:
        masse = 2200
        print str(masse)
        sig='BulkWW'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

print zfile
#report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkWW_lvJ_ourfit_fudge.py