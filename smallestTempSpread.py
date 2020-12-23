numeric = '0123456789.'
minDiff = float('inf')

with open('w_data.dat') as file:
    for line in file.readlines()[6:36]: # read only lines 7-36
        cols = line.strip().split()

        currMaxTemp = ''.join([x for x in cols[1] if x in numeric]) 
        currMinTemp = ''.join([x for x in cols[2] if x in numeric])
        currDiff = float(currMaxTemp) - float(currMinTemp)

        if (currDiff < minDiff):
            minDiff = currDiff
            minDayNum = cols[0]
        
        # print(cols[0], currMaxTemp, currMinTemp, currDiff)

print(minDayNum)
