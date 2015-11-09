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
                                   "CMS_VV_lnuJ/CMS_VV_lnuj_MULP_dijetLike.root"
                                   ])
# 
# print model

model.set_signal_processes("WZ*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWZ=[1.41025, 1.35686, 1.31496, 1.25667, 1.22709, 1.20154, 1.18648, 1.19411, 1.15167, 1.18859, 1.15312, 1.13278, 1.1486, 1.14364, 1.14226, 1.11291]

rangenorm = 3.0

lumiSystName = "lumiSystCMS"
lumiSystValue = 0.026

for j in range(0,16,1): 
    procname = "WZ"+str(mass[j])
    # CMS syst
    model.scale_predictions(fudgeWZ[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
    model.scale_predictions(fudgeWZ[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    

    model.scale_predictions(fudgeWZ[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
    model.scale_predictions(fudgeWZ[j],procname=procname,obsname='CMS_VV_lnuj_MUHP')#The fudge factor    
    # lumi
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_MUHP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_ELEHP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_MULP')
    model.add_lognormal_uncertainty(lumiSystName,lumiSystValue,procname=procname,obsname='CMS_VV_lnuj_ELELP')

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
print expected
print observed
print zlevel

expected.write_txt('results/CMS_VV_lvJ_WZ_ourfit_Fudge_expected.txt')
observed.write_txt('results/CMS_VV_lvJ_WZ_ourfit_Fudge_observed.txt')
#zlevel.write_txt('CMS_ATLAS_VV_JJ_WZ_ourfit_noFudge_zlevel.txt')


current = 1
with open('results/CMS_VV_lvJ_WZ_ourfit_Fudge_zlevel.txt', 'w') as fff:
    while current < 17:
        masse = current*100+900
        sig='WZ'+str(masse)
        zl = zlevel[sig]['Z'][0]
        pl = Z_to_p(zl)
        print str(masse) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl 
        fff.write( str(masse) )
        fff.write( '  ' ) 
        fff.write( str(zlevel[sig]['Z'][0]) )
        fff.write( '  ' ) 
        fff.write( str(pl) )
        fff.write( '\n' )
        current += 1
fff.close()

report.write_html('htmlout')
# ../theta/utils2/theta-auto.py analysis_CMS_WZ_lvJ_ourfit_fudge.py