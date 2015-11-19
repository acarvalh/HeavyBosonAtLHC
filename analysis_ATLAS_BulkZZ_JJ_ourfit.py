model = build_model_from_rootfile([
                                   "ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp.root",
                                   #"ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp_rescaled.root",
                                   #"ATLAS_VV_JJ/ATLAS_ZZ_correct_toSigComp_rescaled_sideband.root",
                                   #"ATLAS_VV_JJ/ATLAS_ZZJJ__DATA_noZZname_publicBackground.root",
                                   #
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_SignalRS_noZZname.root",
                                   "ATLAS_VV_JJ/ATLAS_ZZ_JJ_1fb_Signal_oneSys.root"])
# 
# print model
# 

fudge = 0
alternativeBKG = 0
#alterLabel = '_rescaled'
#alterLabel = '_rescaled_sideband'
alterLabel = '_public'

model.set_signal_processes("BulkZZ*")
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
fudgeZZJJATLAS=[0.55619, 0.565121, 0.561593, 0.569191, 0.564982, 0.528031, 0.488941,0.488903, 0.40283, 0.401571, 0.387373]

lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

filename='results/ATLAS_VV_JJ_BulkZZ_ourfit'

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
elif alternativeBKG :
    expfile = filename+alterLabel+'_expected.txt'
    obsfile = filename+alterLabel+'_observed.txt'
    zfile = filename+alterLabel+'_zlevel.txt'
    z17 = filename+alterLabel+'_Lik1700.txt'
    z18 = filename+alterLabel+'_Lik1800.txt'
    z19 = filename+alterLabel+'_Lik1900.txt'
    z20 = filename+alterLabel+'_Lik2000.txt'
    z21 = filename+alterLabel+'_Lik2100.txt'
    z22 = filename+alterLabel+'_Lik2200.txt'
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

#####################################################################
for j in range(0,11,1): 
    procname = "BulkZZ"+str(mass[j])
    if fudge :
       model.scale_predictions(fudgeZZJJATLAS[j],procname=procname,obsname='ATLAS_VV_JJ') 
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.226,procname=procname,obsname='ATLAS_VV_JJ')
    model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_VV_JJ')
######################################################################

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
nll = nll_scan(model, "data", 1, range=[0.0, 25.0])

print expected
print observed

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
with open(zfile, 'w') as fff:
    while current < len(zlevel)+1:
        mass = current*100+1400
        sig='BulkZZ'+str(mass)
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

#print nll

with open(z17, 'w') as fff:
        mass = 1700
        print str(mass)
        sig='BulkZZ'+str(mass)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z18, 'w') as fff:
        mass = 1800
        print str(mass)
        sig='BulkZZ'+str(mass)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z19, 'w') as fff:
        mass = 1900
        print str(mass)
        sig='BulkZZ'+str(mass)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z20, 'w') as fff:
        mass = 2000
        print str(mass)
        sig='BulkZZ'+str(mass)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z21, 'w') as fff:
        mass = 2100
        print str(mass)
        sig='BulkZZ'+str(mass)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

with open(z22, 'w') as fff:
        mass = 2200
        print str(mass)
        sig='BulkZZ'+str(mass)
        nllLik = nll[sig][0]
        #print str(mass) , " DLik ", nllLik
        fff.write( str(nllLik) )
fff.close()

print zfile
# ../theta/utils2/theta-auto.py analysis_ATLAS_BulkZZ_JJ_ourfit.py