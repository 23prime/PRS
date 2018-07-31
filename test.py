from sympy import *
from prs import *

######################
# Define Polynomials #
######################
u = x ** 8 + x ** 6 - 3 * x ** 4 - 3 * x ** 3 + 6 * x ** 2 + 4 * x - 3
v = 3 * x ** 6 + 5 * x ** 4 - 4 * x ** 2 + 7 * x + 5

########
# Test #
########
# Calculate PRSes
prs0 = prs_prem(u, v)
prs1 = prs_red_prem(u, v)
prs2 = prs_subresultant(u, v)

# Last coefficients of PRSes
last_coeff0 = prs0[-1]
last_coeff1 = prs1[-1]
last_coeff2 = prs2[-1]

# Length of above coefficients
len0 = len(str(abs(last_coeff0)))
len1 = len(str(abs(last_coeff1)))
len2 = len(str(abs(last_coeff2)))


# Output result
with open('result.txt', mode='w') as file:
    file.write('------------------------------------------------\n')
    file.write('- Calculate each PRS by polynomials u(x), v(x) -\n')
    file.write('------------------------------------------------\n')

    # Above PRSes
    file.write('\n- By Pseudo division\n')
    file.write(str(prs0))

    file.write('\n\n- Reduced PRS\n')
    file.write(str(prs1))

    file.write('\n\n- Subresultant PRS\n')
    file.write(str(prs2))

    # Above lengthes
    file.write('\n\n\n----------------------------------------------\n')
    file.write('- Length of last coefficients of above PRSes -\n')
    file.write('----------------------------------------------\n')

    file.write('\n- By Pseudo division\n')
    file.write(str(len0))

    file.write('\n\n- Reduced PRS\n')
    file.write(str(len1))

    file.write('\n\n- Subresultant PRS\n')
    file.write(str(len2))