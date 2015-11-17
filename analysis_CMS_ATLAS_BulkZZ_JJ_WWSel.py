model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_WW_correct_toSigComp_rescaled.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root",
                                   "CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root"]) #,"CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root"

# print model

model.set_signal_processes("BulkZZ*")

fudgeWW=[0.534724, 0.580952, 0.63504, 0.654515, 0.650031, 0.626703, 0.607802, 0.598088, 0.559351, 0.541227, 0.528914]
fudgeWZ=[0.530061, 0.569708, 0.61412, 0.615966, 0.595161, 0.567389, 0.598222, 0.587551, 0.564537, 0.542425, 0.50572]
fudgeZZ=[0.531894, 0.555135, 0.566784, 0.601672, 0.630537, 0.618207, 0.596984, 0.616378, 0.519181, 0.520399, 0.495976]

#fudge=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

model.fill_histogram_zerobins(epsilon=0.001)
for j in range(0,11,1): 
    procname = "BulkZZ"+str(mass[j])
    model.scale_predictions(fudgeZZ[j]*0.4172,procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor          
    #model.scale_predictions(1.1,procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor                    
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    # model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ_WZ')
    # CMS syst
    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
    #model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_HP')
    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
    #model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_LP')

# with fudge 3.5
# no fudge: 2.5

for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-3.5, 3.5])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
        model.distribution.set_distribution_parameters(p, range = [-3.0, 3.0])

    d = model.distribution.get_distribution(p)
    print p, d

expected, observed = asymptotic_cls_limits(model)
clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
model_summary(model, True)
print expected, observed
print zlevel
print pvalue

expected.write_txt('results/CMS_ATLAS_VV_JJ_BulkZZ_WWSel_rescaled_Fudge_expected.txt')
observed.write_txt('results/CMS_ATLAS_VV_JJ_BulkZZ_WWSel_rescaled_Fudge_observed.txt')
#zlevel.write_txt('CMS_ATLAS_VV_JJ_ZZ_ourfit_noFudge_zlevel.txt')
  

current = 1
with open('results/CMS_ATLAS_VV_JJ_BulkZZ_WWSel_rescaled_Fudge_zlevel.txt', 'w') as fff:
    while current < len(zlevel)+1:
        masse = current*100+1400
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

report.write_html('htmlout')

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_BulkZZ_JJ_WWSel.py 