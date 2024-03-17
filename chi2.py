from scipy.stats import chi2_contingency
import numpy as np

# Updated data from the table, excluding the totals
observed = np.array([
    [0, 16, 6, 3],
    [1, 12, 0, 2],
    [2, 2, 1, 5]
])

# Perform the Chi-Square Test on the updated data
chi2, p, dof, expected = chi2_contingency(observed)
print(chi2, p)