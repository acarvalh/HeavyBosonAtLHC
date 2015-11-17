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

fudgeWZ=[0.513282, 0.553725, 0.609789, 0.637297, 0.642589, 0.626628, 0.610983, 0.601232, 0.560182, 0.538367, 0.557967]

fudgeWW=[0.562062, 0.607006, 0.664361, 0.683049, 0.672502, 0.643021, 0.677244, 0.652601, 0.611615, 0.575068, 0.558068]

filename='results/CMS_ATLAS_VV_JJ_WZ_ourfit_Fudge'
expfile = filename+'_expected.txt'
obsfile = filename+'_observed.txt'
zfile = filename+'_zlevel.txt'
z17 = filename+'_Lik1700.txt'
z18 = filename+'_Lik1800.txt'
z19 = filename+'_Lik1900.txt'
z20 = filename+'_Lik2000.txt'
z21 = filename+'_Lik2100.txt'
z22 = filename+'_Lik2200.txt'

model.fill_histogram_zerobins(epsilon=0.001)
for j in range(0,11,1): 
    procname = "WZ"+str(mass[j])
    model.scale_predictions(fudgeWZ[j]*1.1,procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor          
    #model.scale_predictions(1.1,procname=procname,obsname='ATLAS_VV_JJ')#The fudge factor                    
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    # model.add_lognormal_uncertainty("lumi_atlas",0.028,procname=procname,obsname='ATLAS_VV_JJ_WZ')
    # CMS syst
    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_HP')
    #model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_HP')
    model.add_lognormal_uncertainty("normalisation_VVJJ",0.13,procname=procname,obsname='CMS_JJ_LP')
    #model.add_lognormal_uncertainty("lumicms",0.026,procname=procname,obsname='CMS_JJ_LP')

for p in model.distribution.get_parameters():
    d = model.distribution.get_distribution(p)
    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas'):
        model.distribution.set_distribution_parameters(p, range = [-5.5, 5.5])
    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
        model.distribution.set_distribution_parameters(p, range = [-5.5, 5.5])

    d = model.distribution.get_distribution(p)
    print p, d

expected, observed = asymptotic_cls_limits(model)
clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)
pl_interval = pl_interval(model, "data", 1)
nll = nll_scan(model, "data", 1, range=[0.0, 35.0])
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

#print nll

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

# ../theta/utils2/theta-auto.py analysis_CMS_ATLAS_WZ_JJ_ourfit_fudge.py 