import re 

minDiff = float('inf')

with open('w_data.dat') as file:
    for line in file.readlines()[6:36]: # read only lines 7-36
        cols = line.strip().split()
        currMaxTemp = ''.join(re.findall(r'[\d.]+', cols[1])) # use regex to filter out * char
        currMinTemp = ''.join(re.findall(r'[\d.]+', cols[2]))
        currDiff = float(currMaxTemp) - float(currMinTemp)

        if (currDiff < minDiff):
            minDiff = currDiff
            minDayNum = cols[0]
        
        # print(cols[0], currMaxTemp, currMinTemp, currDiff)

print(minDayNum)
