# Binomial Probability Mass Function

Probability and Statistics
Easy

Implement the Binomial distribution Probability Mass Function (PMF) and Cumulative Distribution Function (CDF). The Binomial distribution counts the number of successes in n independent Bernoulli trials with probability p.

Function Arguments
n: int - Number of trials
p: float - Success probability (0 ≤ p ≤ 1)
k: int - Number of successes (0 ≤ k ≤ n)

Examples
Input: n=5, p=0.5, k=2
Output: pmf=0.3125, cdf=0.5

Input: n=10, p=0.3, k=0
Output: pmf=0.0282, cdf=0.0282

Input: n=8, p=0.7, k=8
Output: pmf=0.0576, cdf=1.0

Requirements
Return tuple: (pmf, cdf)
Both pmf and cdf: scalar floats
Use stable computation (no factorial loops)
Handle edge cases: k=0, k=n, p=0, p=1

Constraints
0 ≤ k ≤ n ≤ 100
0 ≤ p ≤ 1
NumPy + SciPy allowed; time limit: 300ms
