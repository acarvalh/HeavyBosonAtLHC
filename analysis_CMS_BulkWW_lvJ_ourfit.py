model = build_model_from_rootfile([#"CMS_VV_lnuJ/CMS_BulkWW_ELEHP_1fb_NarrowSignal.root",
                                   #"CMS_VV_lnuJ/CMS_BulkWW_ELELP_1fb_NarrowSignal.root",
                                   #"CMS_VV_lnuJ/CMS_BulkWW_MUHP_1fb_NarrowSignal.root",
                                   #"CMS_VV_lnuJ/CMS_BulkWW_MULP_1fb_NarrowSignal.root",
                                   #
                                   "CMS_VV_lnuJ/CMS_BulkWW_ELEHP_1fb_ZpToWW_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_ELELP_1fb_ZpToWW_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_MUHP_1fb_ZpToWW_NarrowSignal.root",
                                   "CMS_VV_lnuJ/CMS_BulkWW_MULP_1fb_ZpToWW_NarrowSignal.root",
                                   #
                                   #"CMS_VV_lnuJ/CMS_BulkWW_ELEHP_1fb_ZpToWW_WideSignal.root",
                                   #"CMS_VV_lnuJ/CMS_BulkWW_ELELP_1fb_ZpToWW_WideSignal.root",
                                   #"CMS_VV_lnuJ/CMS_BulkWW_MUHP_1fb_ZpToWW_WideSignal.root",
                                   #"CMS_VV_lnuJ/CMS_BulkWW_MULP_1fb_ZpToWW_WideSignal.root",
                                   #
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELEHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_ELELP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MUHP_dijetLike.root",
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MULP_dijetLike.root"
                                   ])
# 
# print model

model.set_signal_processes("BulkWW*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWW=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291]

rangenorm = 3.0

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

#filename='results/CMS_VV_lvJ_BulkWW_ourfit'
#filename='results/CMS_VV_lvJ_ZpWW_ourfit_wide'
filename='results/CMS_VV_lvJ_ZpWW_ourfit'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

for j in range(0,16,1): 
    procname = "BulkWW"+str(mass[j])
#    # CMS syst
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
#    model.scale_predictions(fudgeWW[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
#    model.scale_predictions(fudgeWW[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    

#    model.scale_predictions(fudgeWW[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
#    model.scale_predictions(fudgeWW[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    


zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
print expected
print observed
#print zlevel

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
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

#report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_CMS_BulkWW_lvJ_ourfit.py