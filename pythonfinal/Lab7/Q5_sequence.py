# Sequence: -10, -8, 6, 40, 102, ...
# Differences: 2, 14, 34, 62; difference pattern = 4, 20, 28 ...
# Simple assumed rule: n^3 - 10, for n=0,1,2... gives -10,-9,-2,17,...
# Use the quadratic sequence from the listed terms: n^3? not consistent.
# Here generate the first given terms and continue using a cubic fit.
terms = [-10, -8, 6, 40, 102]
# Difference table reveals the pattern isn't uniquely defined; extend by repeating
# the 4th-order difference as 0 (polynomial fit through these 5 terms).
diffs = terms[:]
levels = [diffs]
while len(diffs) > 1:
    diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
    levels.append(diffs)
levels[-1].append(0)
for i in range(len(levels)-2, -1, -1):
    levels[i].append(levels[i][-1] + levels[i+1][-1])
print(levels[0])
