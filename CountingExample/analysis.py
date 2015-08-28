#model = build_model_from_rootfile(["ATLAS_VV_JJ_WW_correct.root","ATLAS_WW_JJ_1fb_Signal_sys.root","ATLAS_WW_JJ_1fb_SignalWPrime.root"])
#model = build_model_from_rootfile(["ATLAS_VV_JJ_WW_corr.root","ATLAS_WW_JJ_signal_sys.root","ATLAS_WW_JJ_signal.root"])
model = build_model_from_rootfile(["ATLAS_VV_JJ_WW_reescaled_correct.root","ATLAS_WW_JJ_signal_sys.root","ATLAS_WW_JJ_signal.root"])

model.set_signal_processes("WW*") 
# ATLAS VV JJ

i=0
for mass in range (1500,2500,100):
    procname = "WW"+str(mass)
    # model.add_lognormal_uncertainty("trackmult",math.log(1.20),procname,"ATLAS_VV_JJ_WZ")
    # i=(i+1)

    model.add_lognormal_uncertainty("trackmult",math.log(1.20),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("jms",math.log(1.05),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("jmr",math.log(1.055),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("ptbals",math.log(1.035),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("ptbalr",math.log(1.02),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("psm",math.log(1.05),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("pdf",math.log(1.035),procname,"ATLAS_VV_JJ_WW")
    model.add_lognormal_uncertainty("lumi",math.log(1.028),procname,"ATLAS_VV_JJ_WW")
    i=(i+1)

expected, observed = asymptotic_cls_limits(model)

clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)

model_summary(model, True)
print expected, observed
print zlevel
print pvalue
expected.write_txt('ATLAS_VV_JJ__WW_expected.txt')
observed.write_txt('ATLAS_VV_JJ__WW_observed.txt')
report.write_html('htmlout')

# ../../theta-auto.py analysis.py 
# model.set_signal_processes("signalRSqq*") 
# dijet
