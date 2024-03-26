def main(dwarfs):
    totalWeight = sum(dwarfs)

    for i in range(9):
        for j in range(i+1, 9):
            fakeDwarfWeight1, fakeDwarfWeight2 = dwarfs[i], dwarfs[j]
            if (totalWeight - (fakeDwarfWeight1 + fakeDwarfWeight2)) == 100:
                dwarfs.remove(fakeDwarfWeight1)
                dwarfs.remove(fakeDwarfWeight2)
                return dwarfs


dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()
RealDwarfs = main(dwarfs)
for i in range(7):
    print(RealDwarfs[i])
