execfile("common.py")
# RUN: ../../theta-auto.py analysis_top.py 

# 1.a.
# def ex1a():
    # b = 5.2
    #    b = 0.4
    # print "p-values for a counting experiment with b=", b
    # for nobs in [1,2,3]: #[5,6,7,8,10,15,20]:
    #    p = poisson_p_ge(nobs, b)
    #    Z = p_to_Z(p)
    
# print "for nobs=%d: p=%.3g; Z=%.2f" % (nobs, p, Z)
# Z_a = (nobs - b)/sqrt(b)
# print "for nobs=%d: p=%.3g; Z=%.2f; Z_a=%.2f" % (nobs, p, Z, Z_a)

# calculate the approximate Z-value based on Wilks' Theorem for a counting experiment
# with known b (for 1.a. iii.)
# def calc_Z_w(n, b):
#    s_hat = max([0.0, n - b])
#    return sqrt(2 * ( n * log((s_hat + b) / b) - s_hat))
#
# ex1a()


# 1.b.
#def generate_poisson(mu0, ntoy, par):
#    mu=mu0 * (1 + par)
#    return poisson.rvs(mu, size = ntoy)
# II. plot the distribution of generated Poisson data; "poisson5.pdf" will be created
#    in the current working directory you call theta-auto from.
# data = generate_poisson(5.0, 1000, 0)
# plot_histogram(data, 'poisson5.pdf')

###################################################################
################## Will not use but is cool easy result
def generate_poisson(mu0, ntoy):
    par = 0
    mu=mu0 * (1 + par)
    return poisson.rvs(mu, size = ntoy)
# I. print some generated Poisson numbers:
#data = generate_poisson(5.0, 10)
#print data
# II. plot the distribution of generated Poisson data; "poisson5.pdf" will be created
#    in the current working directory you call theta-auto from.
data = generate_poisson(5.0, 1000)
plot_histogram(data, 'poisson5.pdf')

###################################################################
#### Bayesian (exercice 3)
# returns x,y data (= s values, posterior density values)
# for the posterior density for s for a counting
# experiment with known background b and a flat prior for s for
# nobs observed events by scanning s from smin to smax, using nscan points.
#
# For the normalization, it is assumed that the posterior is negligible outside the
# range [smin, smax]
def counting_posterior(nobs, b, smin, smax, nscan=1000):
    delta_s = (smax - smin) / nscan
    x, y = [], []
    for i in range(nscan):
        s = smin + delta_s * i
        x.append(s)
        # the posterior at this point is the poisson probability; note
        # that at this point, we don't care about normalization:
        y.append(poisson_p_eq(nobs, s + b))
    # now, scale the y values such that we have actually a density:
    factor = 1.0 / (sum(y) * delta_s)
    y = [factor * y0 for y0 in y]
    return x, y
########### do the 95% CL
def get95up(xpost, ypost):
    ytotal = sum(ypost)
    # print "normalization = %.3g" % ytotal
    y = 0.0
    for i in range(len(xpost)):
        y += ypost[i]
        # print "posterior = %.2g nexp = %.3g ratio = %.4g" % (y,xpost[i],y/ytotal)
        if y/ytotal > 0.95: return xpost[i]
########## print result
x, y = counting_posterior(10, 5.2, 0.0, 30.0)
plot_xy(x, y, 'counting_posterior.pdf') 
l = get95up(x, y)
print "counting experiment b=5.2; nobs=6"
print "Bayesian limit for s: %.3g" % l
###################################################################
#### Frequentist (exercice 2)
###################################################################
################## Cutting the Poisson
# return the maximum value for nmin such that the probability
# to observe n>=nmin for a Poisson
# with mean mu is >= pmin.
#def find_nmin_poisson(pmin, mu):
    # note: this is a very inefficient implementation, but at least it should
    # be very transparent how it works (scipy.stats.poisson.ppf provides a more efficient
    # implementation).
    # it is discrete!!!!
#    n = 1
#    while poisson_p_ge(n, mu) > pmin: n+= 1
#    n -= 1
#    return n
################## cl is the confidence level (=1-alpha)
#def construct_belt(b, s0min, s0max, nscan, cl = 0.95):
#    delta_s = (s0max - s0min) / nscan
#    nmins, svals = [], []
#    for i in range(nscan):
#        s0 = s0min + i*delta_s
#        # for given s0, the poisson mean is mu = b+s0, and we want
#        # to choose nmin such that the probability for n>=nmin is the confidence level cl:
#        nmin = find_nmin_poisson(cl, s0 + b)
            #        if i == 6:
            #print "nmin for s0=%.2f: %.3g" % (s0, nmin)
#        svals.append(s0)
#        nmins.append(nmin)
#    plot_xy(svals, nmins, 'neyman_belt.pdf', ymin = 0, xlabel = 's', ylabel = 'n')
#construct_belt(5.2, 0.0, 10.0, 100, 0.95)
############################
#nmin = find_nmin_poisson(0.95, 6)
#print "nmin for s0=6.5 : %.2f" % (nmin)
###################################################################
################# exact value
# def get_pvalue(s0, b, nobs):
#    # here, the p-value is the probability to observe <= n events
    # in a Poisson distribution with mean s0 + b:
#    return poisson_p_le(nobs, s0+b)
# p = get_pvalue(6, 5.2, 6)
# print "p for s0=6: %.2f" % (p)
##################################################
# def scan_s0_pvalue(b, nobs, s0min, s0max, nscan):
#    delta_s = (s0max - s0min) / nscan
#    pvals, svals = [], []
#    for i in range(nscan): # i=0...nscan-1
#        s0 = s0min + i*delta_s
#        p = get_pvalue(s0, b, nobs)
#        print "p for s0=%.2f: %.3g" % (s0, p)
#        svals.append(s0)
#        pvals.append(p)
#    plot_xy(svals, pvals, 'p-vs-s.pdf')
# scan_s0_pvalue(5.2, 6, 5.0, 10.0, 100)
###################################################################
################## Towards to insert a model and get sensibility


###################################################################

# this is only the poisson with observed = mu0
# how to I take the value of the poisson in mue ?



# return the number of elements in the list l which are >= x
# def count_ge(l, x):
#    n=0
#    for x0 in l:
#        if x0 >= x: n+=1
#    return n
# equivalent implementation: return sum([1 for x0 in l if x0 >= x])


def get_pvalue(b, nobs, ntoy = 1000):
    # generate an ensemble of values of n for background only:
    bonly_ns = generate_poisson(b, ntoy)
    # count the number of toys for which n >= nobs:
    ntoy_ge_nobs = count_ge(bonly_ns, nobs)
    # the estimated p-value is the fraction of toys with n >= nobs:
    return ntoy_ge_nobs * 1.0 / ntoy

# III. get the p-value for b=5.2 and nobs = 8:
#p = get_pvalue(5.2, 8)
#print "p=%.3f; Z=%.3f" % (p, p_to_Z(p))




# 1.c.

# def generate_poisson_unc(mu0, delta_mu, ntoy):
#   result = []
#    for i in range(ntoy):
#        # generate Poisson mean mu according to a normal distribution with mean mu0 and width delta_mu
#        mu = norm.rvs(mu0, delta_mu)
#        # generate a Poisson random number around mean mu and append it to the result list:
#        result.append(poisson.rvs(mu))
#    return result

# Using get_pvalue as starting point, write a method called "get_pvalue_syst" for calculating the p-value with a
# background uncertainty.


# 1.d.
def ex1d():
    # In theta, the statistical model is an instance of the class "Model",
    # which contains all information for other routines -- including the observed data.
    # This is the shape model introduced in the lecture:
    model = build_shape_model(signal_mass = 500.)
    # get the test statistic values for background-only:
    ntoy = 5000
    t_bkg = get_bkg_t(model, ntoy)
    tobs = get_data_t(model)
    # note: you can use plot_histogram as in 1.b. to visualize the test statistic distribution
    # count the number of toys for which t >= tobs:
    n = count_ge(t_bkg, tobs)
    p = n * 1.0 / ntoy
    Z = p_to_Z(p)
    print "p = %.3g; Z = %.3g" % (p, Z)


#ex1d()
    
