model = build_model_from_rootfile(["ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_SignalRS_noWWname.root",
                                   "ATLAS_VV_JJ/ATLAS_WW_JJ_1fb_Signal_oneSys.root"])

fudge = 0
alternativeBKG = 0
#alterLabel = '_rescaled'
#alterLabel = '_rescaled_sideband'
alterLabel = '_public'

narrow = 0.7027

filename='results/ATLAS_VV_JJ_BulkWW_ourfit'
fudgeLabel = '_Fudge'
selection='_ZZSel'
if fudge :
    expfile = filename+fudgeLabel+selection+'_expected.txt'
    obsfile = filename+fudgeLabel+selection+'_observed.txt'
    zfile = filename+fudgeLabel+selection+'_zlevel.txt'
    z17 = filename+fudgeLabel+selection+'_Lik1700.txt'
    z18 = filename+fudgeLabel+selection+'_Lik1800.txt'
    z19 = filename+fudgeLabel+selection+'_Lik1900.txt'
    z20 = filename+fudgeLabel+selection+'_Lik2000.txt'
    z21 = filename+fudgeLabel+selection+'_Lik2100.txt'
    z22 = filename+fudgeLabel+selection+'_Lik2200.txt'
elif alternativeBKG :
    expfile = filename+alterLabel+selection+'_expected.txt'
    obsfile = filename+alterLabel+selection+'_observed.txt'
    zfile = filename+alterLabel+selection+'_zlevel.txt'
    z17 = filename+alterLabel+selection+'_Lik1700.txt'
    z18 = filename+alterLabel+selection+'_Lik1800.txt'
    z19 = filename+alterLabel+selection+'_Lik1900.txt'
    z20 = filename+alterLabel+selection+'_Lik2000.txt'
    z21 = filename+alterLabel+selection+'_Lik2100.txt'
    z22 = filename+alterLabel+selection+'_Lik2200.txt'
else :
    expfile = filename+selection+'_expected.txt'
    obsfile = filename+selection+'_observed.txt'
    zfile = filename+selection+'_zlevel.txt'
    z17 = filename+selection+'_Lik1700.txt'
    z18 = filename+selection+'_Lik1800.txt'
    z19 = filename+selection+'_Lik1900.txt'
    z20 = filename+selection+'_Lik2000.txt'
    z21 = filename+selection+'_Lik2100.txt'
    z22 = filename+selection+'_Lik2200.txt'

model.set_signal_processes("BulkWW*")
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
fudgeWWJJATLAS=[0.513282, 0.553725, 0.609789, 0.637297, 0.642589, 0.626628, 0.610983, 0.601232, 0.560182, 0.538367, 0.557967]

lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

for j in range(0,11,1): 
    procname = "BulkWW"+str(mass[j])
    if fudge :
        model.scale_predictions(fudgeWWJJATLAS[j]*narrow,procname=procname,obsname='ATLAS_VV_JJ') 
    else :
        model.scale_predictions(narrow,procname=procname,obsname='ATLAS_VV_JJ') 
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_VV_JJ')

#for p in model.distribution.get_parameters():
#    d = model.distribution.get_distribution(p)
#    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
#        model.distribution.set_distribution_parameters(p, range = [-1*rangenorm, rangenorm])
#    
#    d = model.distribution.get_distribution(p)
#    print p, d

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)

print expected
print observed

expected.write_txt(expfile)
observed.write_txt(obsfile)


current = 1
with open(zfile, 'w') as fff:
    while current < len(zlevel)+1:
        mass = current*100+1400
        sig='BulkWW'+str(mass)
        zl = zlevel[sig]['Z'][0]
        pl = Z_to_p(zl)
        bf= pl_interval[sig][0][0]
        bf1u= pl_interval[sig][0.6826894921370859][0][0]
        bf1d= pl_interval[sig][0.6826894921370859][0][1]
        bf2u= pl_interval[sig][0.9544997361036416][0][0]
        bf2d= pl_interval[sig][0.9544997361036416][0][1]
        print str(mass) , " Zlevel ",zlevel[sig]['Z'][0] , " ", pl , " ", bf , " ", bf2d , " ", bf1d , " ", bf1u , " ", bf2u 
        fff.write( str(mass) )
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

# ../theta/utils2/theta-auto.py analysis_ATLAS_BulkWW_JJ_ourfit_ZZSel.py