from sympy import *

x = Symbol('x')


###########
# Get PRS #
###########
# PRS by pseudo division
def prs_prem(f, g):
    prs = []
    while degree(f) > 1:
        p = prem(f, g)
        prs.append(p)

        f = g
        g = p
    return prs


# Get leading coefficient
def lcoeff(f):
    return f.coeff(x ** degree(f))

# Pseudo division for Reduced PRS
def prem2(f, g):
    if degree(f) < degree(g):
        prem2(g, f)
    else:
        a = lcoeff(g) ** (degree(f) - degree(g) + 1)
        p = div(a * f, g, domain='Z')[1]
        return (p, a)

# Reduced PRS
def prs_red_prem(f, g):
    prs = []
    a0 = 1
    while degree(f) > 1:
        (p, a) = prem2(f, g)
        p      = p / a0
        prs.append(p)

        a0 = a
        f  = g
        g  = p
    return prs


# Subresultant PRS
def prs_subresultant(f, g):
    prs = subresultants(f, g)
    del prs[0:2]
    return prs