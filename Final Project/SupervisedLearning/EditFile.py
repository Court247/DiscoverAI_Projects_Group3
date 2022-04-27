import io
import csv

e = open('C:\\Users\\chica\\Documents\\AI4ALL\\COVIDCount.csv')
lines = e.readlines()
l = []

count = 0

for line in lines:
    tokens = line.split(",")

    if tokens[3] != "COVID-19 Deaths" and int(tokens[3]) > 900:
        tokens[4] = "T"
    if tokens[3] != "COVID-19 Deaths" and int(tokens[3]) < 900:
        tokens[4] = "F"
    l.append(tokens)




f = open('C:\\Users\\chica\\Documents\\AI4ALL\\COVIDCount2.csv', 'w', newline="")
writer = csv.writer(f)

writer.writerow(l[0])

for i in range(1,len(l)):
    writer.writerow(l[i])
    
