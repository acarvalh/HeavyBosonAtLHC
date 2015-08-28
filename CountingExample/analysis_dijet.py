#model = build_model_from_rootfile(["CMS_DiJet_correct.root","CMS_DiJet_Signal_RSqq.root"])
model = build_model_from_rootfile(["ATLAS_DiJet_correct.root","ATLAS_DiJet_Signal_RSqq_correct.root"])

model.set_signal_processes("signalRSqq*") 
# ATLAS VV JJ

expected, observed = asymptotic_cls_limits(model)

clevel = pl_interval(model, "data", 1)
zlevel = zvalue_approx(model, "data", 1)

model_summary(model, True)
print expected, observed
print zlevel
print pvalue
expected.write_txt('ATLAS_Dijet_expected.txt')
observed.write_txt('ATLAS_Dijet_observed.txt')
report.write_html('htmlout')

# ../../theta-auto.py analysis.py 
# 
# dijet
# model.set_signal_processes("signalRSqq*") 
