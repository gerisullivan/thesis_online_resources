from collections import Counter
with open("all.sbpsv2.map.out.2c") as f:
    #next(f)  # do this to skip the first row of the file
    c = Counter(tuple(row.split()) for row in f if not row.isspace())

sites = sorted(set(x[0] for x in c))
genes = sorted(set(x[1] for x in c))

print 'genes\t', '\t'.join(sites)
for gen in genes:
    print gen,'\t', '\t'.join(str(c[site, gen]) for site in sites
)
