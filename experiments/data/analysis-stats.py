# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import scipy.stats

# The Kruskal-Wallis H-test tests the null hypothesis that the population
# median of all of the groups are equal. It is a non-parametric version of
# ANOVA. The test works on 2 or more independent samples, which may have
# different sizes. Note that rejecting the null hypothesis does not indicate
# which of the groups differs. Post-hoc comparisons between groups are required
# to determine which groups are different.


def test(group1, group2):
    H, p = scipy.stats.kruskal(group1, group2)
    if p < 0.0005:
        return "***", H, p
    elif p < 0.005:
        return " **", H, p
    elif p < 0.05:
        return "  *", H, p
    else:
        return "  -", H, p


print("Kruskal-Wallis H-test with the null hypothesis that the\n"
      "population median of all of the conditions are equal")
print("(*: p < 0.05     **: p < 0.005     ***: p< 0.0005)\n")

Z = np.loadtxt("./theoretical-raw-data.txt")
C0 = Z[np.where(Z[:, 2] == 0)][:, 0]
C2 = Z[np.where(Z[:, 2] == 2)][:, 0]
C3 = Z[np.where(Z[:, 2] == 3)][:, 0]
C4 = Z[np.where(Z[:, 2] == 4)][:, 0]

print("Theoretical results")
print("-------------------")
print("C4 / C0 : %s (H = %g, p = %g)" % test(C4, C0))
print("C4 / C2 : %s (H = %g, p = %g)" % test(C4, C2))
print("C4 / C2 : %s (H = %g, p = %g)" % test(C4, C3))
print()

Z = np.loadtxt("./experimental-raw-data.txt")
C0 = Z[np.where(Z[:, 2] == 0)][:, 0]
C2 = Z[np.where(Z[:, 2] == 2)][:, 0]
C3 = Z[np.where(Z[:, 2] == 3)][:, 0]
C4 = Z[np.where(Z[:, 2] == 4)][:, 0]

print("Experimental results")
print("--------------------")
print("C4 / C0 : %s (H = %g, p = %g)" % test(C4, C0))
print("C4 / C2 : %s (H = %g, p = %g)" % test(C4, C2))
print("C4 / C2 : %s (H = %g, p = %g)" % test(C4, C3))
print()
