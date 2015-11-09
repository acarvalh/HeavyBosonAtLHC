model = build_model_from_rootfile([# cms lv
                                   "CMS_VV_lnuJ/CMS_WVlnuJ_thetaNaming_HIGHPURITY_ELE.root",
                                   "CMS_VV_lnuJ/CMS_WVlnuJ_thetaNaming_HIGHPURITY_MU.root",
                                   "CMS_VV_lnuJ/CMS_WVlnuJ_thetaNaming_LOWPURITY_ELE.root",
                                   "CMS_VV_lnuJ/CMS_WVlnuJ_thetaNaming_LOWPURITY_MU.root",
                                   "CMS_VV_lnuJ/signalsHP_ELE.root",
                                   "CMS_VV_lnuJ/signalsHP_MU.root",
                                   "CMS_VV_lnuJ/signalsLP_ELE.root",
                                   "CMS_VV_lnuJ/signalsLP_MU.root",
                                   # atlas bulk ww lv
                                   "ATLAS_VV_lnuJ/ATLAS_WVlvJ_MR_thetaNaming_uncorrSys.root",
                                   #"ATLAS_VV_lnuJ/ATLAS_WVlnuJ_dijetfit_correct_MR.root",
                                   "ATLAS_VV_lnuJ/ATLAS_lnuJ_WW_MR_1fb_Signal.root",
                                   #"ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root"
                                   # CMS bulk VV JJ
                                   "CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkWW_1fb.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root",
                                   # atlas bulk vv JJ
                                   "ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   #"ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_sys_noJER_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   #"ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_sys_noJER_noWWname.root",
                                   # atlas bulk zz ll
                                   "ATLAS_VV_llJ/ATLAS_ZVllJ_thetaNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_MR_1fb_Signal.root",
                                   "ATLAS_VV_llJ/ATLAS_WZ_HR_1fb_Signal.root",
                                   # cms bulk ZZ ll
                                   "CMS_VV_llJ/CMS_ZVeeJ_HP_dijetLike.root",
                                   "CMS_VV_llJ/CMS_ZVeeJ_LP_dijetLike.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_HP_dijetLike.root",
                                   "CMS_VV_llJ/CMS_ZVmmJ_LP_dijetLike.root",
                                   "CMS_VV_llJ/CMS_ZZ_HP_ELE_1fb_Signal.root",
                                   "CMS_VV_llJ/CMS_ZZ_HP_MU_1fb_Signal.root",
                                   "CMS_VV_llJ/CMS_ZZ_LP_ELE_1fb_Signal.root",
                                   "CMS_VV_llJ/CMS_ZZ_LP_MU_1fb_Signal.root",
                                   
                                   ])
# 

rr = 0.1
print rr
rww =  rr/(1.+rr)
rzz =  1./(1+rr)

filename='results/CMS_ATLAS_WW_ZZ_JJ_lvJ_llJ_ZZSel_r'+str(rr)
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

#model.set_signal_processes("signalGbulk*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWWl=[1.15845, 1.17291, 1.19139, 1.17989, 1.17139, 1.1563, 1.14428, 1.1503, 1.10711, 1.14094, 1.1075, 1.09258, 1.11947, 1.13576, 1.16994, 1.19509]

fudgeWW=[1.0, 1.0,1.0, 1.0, 1.0, 0.534724, 0.580952, 0.63504, 0.654515, 0.650031, 0.626703, 0.607802, 0.598088, 0.559351, 0.541227, 0.528914]

fudgeZZ=[1.0, 1.0,1.0, 1.0, 1.0, 0.534724, 0.580952, 0.63504, 0.654515, 0.650031, 0.626703, 0.607802, 0.598088, 0.559351, 0.541227, 0.528914]#tofix

for j in range(0,16,1): 
    # CMS lv
    procnameC = "signalGbulk"+str(mass[j])
    Czz= fudgeWWl[j]*0.7027*rww
    model.scale_predictions(Czz,procname=procnameC,obsname='CMS_WVenuJ_HP')#The fudge factor    
    model.scale_predictions(Czz,procname=procnameC,obsname='CMS_WVenuJ_LP')#The fudge factor    

    model.scale_predictions(Czz,procname=procnameC,obsname='CMS_WVmnuJ_HP')#The fudge factor    
    model.scale_predictions(Czz,procname=procnameC,obsname='CMS_WVmnuJ_LP')#The fudge factor    

    procnameAww = "BulkWW"+str(mass[j])                                                                
    procnameAzz = "BulkZZ"+str(mass[j])                    
    #model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procnameA,obsname='ATLAS_WVlnJ_MR')
    #model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procnameA,obsname='ATLAS_WVlnJ_MR')
  
    # cms ll 
    
    model.scale_predictions(rzz,procname=procnameAzz,obsname='CMS_ZVeeJ_HP')#The fudge factor    
    model.scale_predictions(rzz,procname=procnameAzz,obsname='CMS_ZVeeJ_LP')#The fudge factor    
    model.scale_predictions(rzz,procname=procnameAzz,obsname='CMS_ZVmmJ_HP')#The fudge factor    
    model.scale_predictions(rzz,procname=procnameAzz,obsname='CMS_ZVmmJ_LP')#The fudge factor 

    #atlas lv
    model.scale_predictions(rww,procname=procnameAww,obsname='ATLAS_WVlnJ_MR')
    
    # atlas ll
    if(j<11):
        model.scale_predictions(rzz,procname=procnameAzz,obsname='ATLAS_ZVllJ_MR')
        model.scale_predictions(rzz,procname=procnameAzz,obsname='ATLAS_ZVllJ_HR')


    if (j>5):
        #model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procnameA,obsname='ATLAS_VV_JJ')
        #model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameA,obsname='CMS_JJ_HP')
        #model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procnameA,obsname='CMS_JJ_LP')
        # atlas VV JJ
        model.scale_predictions(fudgeWW[j]*0.7027*rww,procname=procnameAww,obsname='ATLAS_VV_JJ')#The fudge factor  
        model.scale_predictions(fudgeZZ[j]*rzz,procname=procnameAzz,obsname='ATLAS_VV_JJ')#The fudge factor  
        # cms VV JJ
        model.scale_predictions(rww,procname=procnameAww,obsname="CMS_JJ_HP")#The fudge factor                                                    
        model.scale_predictions(rzz,procname=procnameAzz,obsname="CMS_JJ_HP")#The fudge factor  
        model.scale_predictions(rww,procname=procnameAww,obsname="CMS_JJ_LP")#The fudge factor                                                    
        model.scale_predictions(rzz,procname=procnameAzz,obsname="CMS_JJ_LP")#The fudge factor 

        

    print str(mass[j])
    procname='VVBulk'+str(mass[j])
    if (j==0):
        group = {procname : [procnameAww,procnameAzz,procnameC]}
    elif (j<5):
        group[procname] = [procnameAww,procnameAzz,procnameC]
    elif (j>5):
        group[procname] = [procnameAww,procnameAzz, procnameC]
    else:
       group[procname] = [procnameAww,procnameAzz, procnameC]

print group

model.set_signal_process_groups( group )

#####################################
# with fudge 3.5
# no fudge: 2.5
rangenorm = 3.0
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-2.5, 2.5])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
        model.distribution.set_distribution_parameters(p, range = [-2.0, 2.0])
    
    d = model.distribution.get_distribution(p)
    print p, d
#####################################


zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
print expected
print observed
print zlevel

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
with open(zfile, 'w') as fff:
    while current < 17:
        masse = current*100+900
        sig='VVBulk'+str(masse)
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
# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkWW_lvJ_JJ_ourfit_fudge_SigComp_ZZwindow.py