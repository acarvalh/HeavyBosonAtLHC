model = build_model_from_rootfile([
                                   "ATLAS_VV_lnuJ/ATLAS_WVlvJ_MR_thetaNaming_uncorrSys.root",
                                   #"ATLAS_VV_lnuJ/ATLAS_WVlvJ_HR_thetaNaming.root",
                                   "ATLAS_VV_lnuJ/ATLAS_lnuJ_WZ_MR_1fb_Signal.root"#,
                                   #"ATLAS_VV_lnuJ/ATLAS_lnuJ_WZ_HR_1fb_Signal.root"
                                   ])
# 
# print model

model.set_signal_processes("WZ*")
rangenorm = 5
model.fill_histogram_zerobins(epsilon=0.001)
mass=[1000, 1100,1200,1300,1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

fudgeWZlvJATLAS = [0.795712, 0.929701, 0.936624, 0.980215, 1.03092, 1.04214, 1.07966, 1.04453, 1.0487, 1.00702, 0.959159, 0.880764, 0.787317, 0.729852, 0.674062, 0.645124] 
fudgeWWlvJATLAS = [1.34167, 1.21314, 1.08996, 1.08625, 1.11429, 1.14418, 1.1409,  1.06639, 1.08099, 1.06824, 1.01071, 0.963582, 0.904669, 0.831587, 0.787872, 0.746516]

lumiSystNameATLAS = "lumiSystATLAS"
lumiSystValueATLAS = 0.028

fudge=1
filename='results/ATLAS_VV_lvJ_WZ_ourfit'
fudgeLabel = '_Fudge'
if fudge :
    expfile = filename+fudgeLabel+'_expected.txt'
    obsfile = filename+fudgeLabel+'_observed.txt'
    zfile = filename+fudgeLabel+'_zlevel.txt'
else : 
    expfile = filename+'_expected.txt'
    obsfile = filename+'_observed.txt'
    zfile = filename+'_zlevel.txt'

for j in range(0,16,1): 
    procname = "WZ"+str(mass[j])
    if fudge : model.scale_predictions(fudgeWZlvJATLAS[j],procname=procname,obsname='ATLAS_WVlnJ_MR')#The fudge factor                 
    model.add_lognormal_uncertainty("normalisation_VVlvJ_atlas",0.1,procname=procname,obsname='ATLAS_WVlnJ_MR')
    model.add_lognormal_uncertainty(lumiSystNameATLAS,lumiSystValueATLAS,procname=procname,obsname='ATLAS_WVlnJ_MR')



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
print zlevel

expected.write_txt(expfile)
observed.write_txt(obsfile)

current = 1
with open(zfile, 'w') as fff:
    while current < 11:
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


# ../theta/utils2/theta-auto.py analysis_ATLAS_WZ_lvJ_ourfit.py