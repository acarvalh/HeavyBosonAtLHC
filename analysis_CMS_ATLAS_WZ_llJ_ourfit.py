model = build_model_from_rootfile(["CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike_uncorrSys.root",
                                   "CMS_VV_llJ/CMS_WZ_ELEHP_1fb_WpToZlepWhad_NarrowSignal.root",
                                   "CMS_VV_llJ/CMS_WZ_ELELP_1fb_WpToZlepWhad_NarrowSignal.root",
                                   "CMS_VV_llJ/CMS_WZ_MUHP_1fb_WpToZlepWhad_NarrowSignal.root",
                                   "CMS_VV_llJ/CMS_WZ_MULP_1fb_WpToZlepWhad_NarrowSignal.root",
                                   #
                                   "ATLAS_VV_llJ/ATLAS_ZVllJ_newNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_MR_1fb_Signal.root"
                                   ])
# 
# print model

fudge = 1

mass=[1000,1100,1200,1300,1400,1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeZZllCMS=[1.09879, 1.05341, 1.00664, 1.03848, 1.11259, 1.02073, 1.11013, 1.10722, 1.15051, 1.0962, 1.13582, 1.15223, 1.20053, 1.16918, 1.2755, 1.31541]
fudgeZZllJATLAS=[1.2004, 1.1734, 1.03546, 1.04473, 1.06224, 0.939548, 1.0411, 1.02485, 1.00821, 1.01614, 0.915197]
fudgeWZllJATLAS = [1.04091, 0.959243, 0.86275, 0.869074, 0.844375, 0.8973, 0.852316, 0.817111, 0.843688, 0.777118, 0.768438]

lumiSystNameCMS = "lumiSystCMS"
lumiSystValueCMS = 0.026
lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

filename='results/CMS_ATLAS_VV_llJ_WZ_ourfit'
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

model.set_signal_processes("WZ*")
#rangenorm = 2.5
model.fill_histogram_zerobins(epsilon=0.001)
#mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

for j in range(0,16,1):    
    procname = "WZ"+str(mass[j])
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
    ###################################################################################################### 
    # CMSllJ
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty(lumiSystNameCMS,lumiSystValueCMS,procname=procname,obsname='CMS_ZVeeJ_LP')
    ## shape summed quadratically 
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_MUHP",0.03,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_ELEHP",0.037,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_MULP",0.03,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("normalisation_CMS_VV_llj_ELELP",0.037,procname=procname,obsname='CMS_ZVeeJ_LP')
    ## migration
    model.add_lognormal_uncertainty("catMigration_CMS_VV_llj_MUHP",0.09,procname=procname,obsname='CMS_ZVmmJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_llj_ELEHP",0.09,procname=procname,obsname='CMS_ZVeeJ_HP')
    model.add_lognormal_uncertainty("catMigration_CMS_WV_llJ_MULP",-0.24,procname=procname,obsname='CMS_ZVmmJ_LP')
    model.add_lognormal_uncertainty("catMigration_CMS_VV_llj_ELELP",-0.24,procname=procname,obsname='CMS_ZVeeJ_LP')
    # ATLAS ZZ llJ
    if j<11 :
       model.add_lognormal_uncertainty("normalisation_VVllJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
       model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_ZVllJ_MR')

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

with open(z17, 'w') as fff:
        masse = 1700
        print str(masse)
        sig='WZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z18, 'w') as fff:
        masse = 1800
        print str(masse)
        sig='WZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z19, 'w') as fff:
        masse = 1900
        print str(masse)
        sig='WZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z20, 'w') as fff:
        masse = 2000
        print str(masse)
        sig='WZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z21, 'w') as fff:
        masse = 2100
        print str(masse)
        sig='WZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z22, 'w') as fff:
        masse = 2200
        print str(masse)
        sig='WZ'+str(masse)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

print zfile
#report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WZ_llJ_ourfit.py