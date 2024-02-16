# find numbers which are devisible by 7 and multiple of 5 between a rangef
# 1500 and 2700 (both included)
nl = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        nl.append(str(i))
print(','.join(nl))

