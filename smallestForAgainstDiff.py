minDiff = float('inf')

with open('soccer.dat') as file:
    for line in file.readlines()[3:24]: # read only lines 3-24
        cols = line.strip().split()
        if len(cols) == 1:  # skip ------ line
            continue

        currFor = cols[6]
        currAgainst = cols[8]
        currDiff = abs(int(currFor) - int(currAgainst))

        if (currDiff < minDiff):
            minDiff = currDiff
            minTeam = cols[1]
        
        # print(cols[0], currFor, currAgainst, currDiff)

print(minTeam)
