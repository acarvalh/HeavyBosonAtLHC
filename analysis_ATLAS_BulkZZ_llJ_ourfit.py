model = build_model_from_rootfile(["ATLAS_VV_llJ/ATLAS_ZVllJ_newNaming.root",
                                   "ATLAS_VV_llJ/ATLAS_ZZ_MR_1fb_Signal.root"
                                   #"ATLAS_VV_llJ/ATLAS_ZZ_HR_1fb_Signal.root"
                                   ])
# 
# print model

model.set_signal_processes("BulkZZ*")
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000,1100,1200,1300,1400,1500, 1600, 1700, 1800, 1900, 2000]
fudgeZZllJATLAS=[1.2004, 1.1734, 1.03546, 1.04473, 1.06224, 0.939548, 1.0411, 1.02485, 1.00821, 1.01614, 0.915197]


lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

fudge=0
filename='results/ATLAS_VV_llJ_BulkZZ_ourfit' 
fudgeLabel = '_Fudge'
if fudge :
    expfile = filename+fudgeLabel+'_expected.txt'
    obsfile = filename+fudgeLabel+'_observed.txt'
    zfile = filename+fudgeLabel+'_zlevel.txt'
else : 
    expfile = filename+'_expected.txt'
    obsfile = filename+'_observed.txt'
    zfile = filename+'_zlevel.txt'

for j in range(0,11,1): 
    procname = "BulkZZ"+str(mass[j])
    if fudge :
       model.scale_predictions(fudgeZZllJATLAS[j],procname=procname,obsname='ATLAS_ZVllJ_MR')#The fudge factor         
       #model.scale_predictions(fudgeZZll[j],procname=procname,obsname='ATLAS_ZVllJ_HR')#The fudge factor         
    model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_MR')
    #model.add_lognormal_uncertainty("normalisation_VVJJ_atlas",0.1,procname=procname,obsname='ATLAS_ZVllJ_HR')
    model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_ZVllJ_MR')
    #model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_ZVllJ_MR')

zlevel = zvalue_approx(model, "data", 1)
expected, observed = asymptotic_cls_limits(model)
pl_interval = pl_interval(model, "data", 1)
print expected
print observed
print zlevel

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
with open(zfile, 'w') as fff:
    while current < 11:
        masse = mass[current]
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

print zfile
# ../theta/utils2/theta-auto.py analysis_ATLAS_BulkZZ_llJ_ourfit.py