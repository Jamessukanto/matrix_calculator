from math import pi, sqrt, ceil
from statistics import mean, mode, variance

import numpy as np
from scipy.stats import binom, nbinom, expon
from scipy.stats import poisson as pois
from scipy.integrate import quad


def sample_info(operands):
    nums = sorted(operands[0])
    n = len(nums)
    s_mean, s_var = mean(nums), variance(nums)
    s_mode, s_std = mode(nums), sqrt(s_var)

    # quantiles
    qts = []
    for tile in [t*(n+1)-1 for t in [.25, .5, .75]]:
        n1, n2 = nums[int(tile)], nums[ceil(tile)]
        frac = tile-int(tile) if tile != int(tile) else 0
        dis = n2-n1 if tile != int(tile) else 0
        qts.append(n1 + (frac * dis))
    
    # boxplot
    iqr = qts[2] - qts[0]
    # whisks = [qts[0] - iqr*1.5, qts[2] + iqr*1.5]
    whisks = [max(nums[0], qts[0] - 1.5*iqr), min(nums[-1], qts[2] + 1.5*iqr)]

    # skewness
    sum_ = 0
    for num in nums:
        sum_ += ((num-s_mean) / s_std)**3
    scalar = n / ((n-1)*(n-2))
    s_skew = scalar * sum_
    
    print("SAMPLE INFO: ")
    print()
    print(nums)
    print()
    print("mean     %.3f" % (s_mean))
    print("mode     %.6f" % (s_mode))
    print("range    %.3f" % (nums[-1]-nums[0]))
    print()
    print("s_var    %.3f" % (s_var))
    print("s_std    %.3f" % (s_std))
    print("coef_v = p_std / p_mean")
    print()
    print("Q1 = (0.25 * (n+1))th data, idx frm 1")
    print("QTS %.2f %.2f %.2f  IQR %.3f" % (qts[0], qts[1], qts[2], iqr))
    print()
    print("boxplot: lav Q1 Q2 Q3 uav")
    print("lower whisk/fence: Q1–1.5(IQR) = %.4f" % (whisks[0]))
    print("upper whisk/fence: Q3+1.5(IQR) = %.4f" % (whisks[1]))
    print()
    print("lav: smallest observd >= l_fence")
    print("uav: largest observd <= u_fence")
    print("check outliers")
    print()
    print("skew = (n / (n-1)(n-2)) * sumtion_1_to_n ((xi - s_mean) / s)^3")
    print("skew %.2f" % (s_skew), "neg_vals==left_skewed")

def print_dist(title, p_mean, p_var, fx, Fx):
    print(title)
    print()
    print("p_mean %.6f  p_var %.6f" % (p_mean, p_var))
    print(f"fx    {fx:.6f}\nFx    {Fx:.6f}")

def binomial(operands):
    k, n, p = operands
    p_mean, p_var = binom.stats(n, p)
    fx, Fx = binom.pmf(k, n, p), binom.cdf(k, n, p)

    print_dist("BINOMIAL: ", p_mean, p_var, fx, Fx)
    print()
    print("b(k; n, p) = (nCk) * p^k * q^(n-k)")
    print("E(X) = np")
    print("Var(X) = npq")
    print()
    print("only 1 outcome/trial; consistent prob across trials; ind trials")

def negbinomial(operands):
    k, r, p = operands
    p_mean, p_var = nbinom.stats(r, p)
    fx, Fx = nbinom.pmf(k, r, p), nbinom.cdf(k, r, p)

    print_dist("NEG BINOMIAL: ", p_mean, p_var, fx, Fx)
    print()
    print("NEG BINOMIAL: ")
    print("f(k_fails): ((r+k-1)Ck) * p^r * q^k")
    print()
    print("GEO: ")
    print("f(k_fails; r=1, p) = (q^k) * p")
    print("F(k_fails; r=1, p) = 1 - q^(k+1)")
    print("E(X) = q/p")
    print("Var(X) = q/(p^2)")
    print()
    print("f(v=k+1_draws; p) = q^(v-1) * p")
    print("F(v=k+1_draws; p) = 1 - q^v")
    print("E(X) = 1/p")
    print("Var(X) = q/(p^2)")
    print()
    print("consistent prob across trials; ind trials")

def poisson(operands):
    k, p_mean = operands
    p_mean, p_var = pois.stats(p_mean)
    fx, Fx = pois.pmf(k, p_mean), pois.cdf(k, p_mean)

    print_dist("POISSON: ", p_mean, p_var, fx, Fx)
    print()
    print("p(k; lamb*t) = (lamb*t)^k / (e^(lamb*t) * k!)")
    print("E(X) = lamb")
    print("Var(X) = lamb")
    print()
    print("events rate constant tru time; events cannot occur simultaneously; ind events")

def hypergeometric(operands):
    print("HYPERGEOMETRIC: ")
    print()
    print("h(x) = rCk * n-rCh-k / nCh")
    print("E(X) = h * (r/n)")
    print("Var(X) = (h * (r/n)) * (1-(r/n)) * ((n-h)/n-1)")
    print()
    print("if h/n is small, <0.1, binom approximates n=h, p=r/n")
    
def uniform(operands):                                                      
    print("UNIFORM DISC: ")
    print()
    print("f(x) = 1/n")
    print("E(X) = (n+1) / 2")
    print("Var(X) = (n^2 - 1) / 12")
    print()
    print("UNIFORM CONT: ")
    print()
    print("f(x) = 1/(b-a)")
    print("E(X) = (a+b) / 2")
    print("Var(X) = (b-a)^2 / 12")

def exponential(operands):
    k, lamb = operands
    p_mean, p_var = expon.stats(scale=1/lamb)
    fx, Fx = expon.pdf(x=k, scale=1/lamb), expon.cdf(x=k, scale=1/lamb)

    print_dist("EXPONENTIAL: ", p_mean, p_var, fx, Fx)
    print()
    print("lamb = avg num events eg fails / unit time")
    print("f(t) = lamb / e^(lamb*t) for t>=0")
    print("F(t) = 1 - (1 / e^(lamb*t))")
    print("E(X) = 1 / lamb")
    print("Var(X) = 1 / (lamb^2)")
    print()
    print("pois approx of binom: n >= 50, p <= 0.05")
    print()
    print("Let x = curr age of a component => X>t")
    print("cond prob it won't fail for k+ units:")
    print("P(X>x+k | X>x) = P(X>x+k) / P(X>x) = e^(-lamb*(x+k)) / e^(-lamb*k) = e^(-lamb*k)")
    print("cond prob depends only on new duration, not past info, ind of current age")
    print()
    print("lives are ind and expon-distributed")

def normal(operands):
    if len(operands)==3:
        k1_in, k2_in, p_mean, p_std = None, *operands
    elif len(operands)==4:
        k1_in, k2_in, p_mean, p_std = operands
    
    k1, k2 = k1_in if k1_in else 0, k2_in if k2_in else 0
    z1 = round((k1-p_mean) / p_std, 2)
    z2 = round((k2-p_mean) / p_std, 2)

    integrand = lambda z: 1 / (sqrt(2*pi) * np.exp(z**2 / 2))
    Fx_0_a, _ = quad(integrand, 0, z1)
    Fx_0_b, _ = quad(integrand, 0, z2)

    Fx_abs_b = 2 * Fx_0_b
    Fx_ni_b = 0.5 + Fx_0_b
    Fx_b_pi = 1 - Fx_ni_b
    Fx_a_b = Fx_0_b - Fx_0_a

    print("NORMAL: ")
    print()
    print("z1 %.2f   z2 %.2f" % (z1, z2))
    print("Fx_abs_b  %.6f" % (Fx_abs_b))
    print("Fx_ni_b   %.6f" % (Fx_ni_b))
    print("Fx_b_pi   %.6f" % (Fx_b_pi))
    print("Fx_a_b    %.6f" % (Fx_a_b))

    print()
    print("f(x) = (1 / std * sqrt(2*pi)) * e^(-0.5 * ((x-p_mean)/std)^2)")
    print()
    print("within 1 std: 0.68;  2 std: 0.95;  3 std: 0.997")
    print()
    print("chebyshev's rule: Let k>1. At least (1-(1/k^2)) of data is within 2 std's of mean, regardless dist")
    print()
    print("lognorm:")
    print("Let X be norm dist; X = ln(Y) <=> Y = expo(X)")
