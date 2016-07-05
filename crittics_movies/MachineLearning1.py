import sys
import urllib2
import numpy as np

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)

xList = []
labels = []
for line in data:
    row = line.strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

col = 3
colData =[]


for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = \t" + str(colMean) + "\t\tStandard Deviation \t " + str(colsd))


ntiles = 4
percentBdry = []

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))


sys.stdout.write("\nBoundaries")#page33

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1

    colCounts.append(type)
    type = [0]*3

sys.stdout.write("col# \t" + " Number " + "\t" + "Strings \t" + "Other \n")

iCol = 0
for types in colCounts:
    sys.stdout.write(str(iCol) + "\t\t" + str(types[0]) + " \t\t" + str(types[1]) + "\t\t" + str(types[2]) + "\n")
    iCol += 1



#sys.stdout.write("Number of rows: " + str(len(xList)) + "\n")
#sys.stdout.write("Number of cols: " + str(len(xList[1])))

