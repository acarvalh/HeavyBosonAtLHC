model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_WZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_SignalWPrime_noJER_noWZname.root",
                                   "ATLAS_VV_JJ/ATLAS_WZ_JJ_1fb_Signal_oneSys.root",
                                   "CMS_VV_JJ/CMS_VV_jj_data.root",
                                   "CMS_VV_JJ/CMS_VV_jj_WZ_1fb.root"
                                   ]) #,"CMS_VV_JJ/CMS_VV_jj_BulkZZ_1fb.root"

# 
# print model

model.set_signal_processes("WZ*")

mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
model.fill_histogram_zerobins(epsilon=0.001)
filename='results/CMS_ATLAS_VV_JJ_WZ_ourfit'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'

model.fill_histogram_zerobins(epsilon=0.001)
for j in range(0,11,1): 
    procname = "WZ"+str(mass[j])
    #model.scale_predictions(fudge[j],procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor          
    #model.scale_predictions(1.1,procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor                    
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ')
    # CMS syst
    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
    model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_HP')
    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
    model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_LP')

rangenorm = 3.5
for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jescms' or p == 'migrationcms') :
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 :
        model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])
    d = model.distribution.get_distribution(p)
    print p, d

expected, observed = asymptotic_cls_limits(model)
clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
print model
model_summary(model, True)
print expected, observed
print zlevel
print pvalue

expected.write_txt(expfile)
observed.write_txt(obsfile)

print expfile
#  clevel = pl_interval(model, "data", 1)
#  zlevel = zvalue_approx(model, "data", 1)
#  model_summary(model, True)
#  print expected, observed
#print zlevel
#  print pvalue



current = 1
with open(zfile, 'w') as fff:
    while current < len(zlevel)+1:
        masse = current*100+1400
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

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WZ_JJ_ourfit.py 