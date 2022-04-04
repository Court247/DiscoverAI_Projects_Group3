import io
import csv

e = open('C:\\Users\\chica\\Documents\\AI4ALL\\COVIDCount.csv')
lines = e.readlines()
l = []

count = 0

for line in lines:
    tokens = line.split(",")
    if tokens[3] == 'Female':
        tokens[3] = 1
    if tokens[3] == 'Male':
        tokens[3] = 0
    if tokens[6] != "COVID-19 Deaths" and int(tokens[6]) > 900:
        tokens[7] = True;
    if tokens[6] != "COVID-19 Deaths" and int(tokens[6]) < 900:
        tokens[7] = False;
    l.append(tokens)




f = open('C:\\Users\\chica\\Documents\\AI4ALL\\COVIDCount2.csv', 'w', newline="")
writer = csv.writer(f)

writer.writerow(l[0])

for i in range(1,len(l)):
    writer.writerow(l[i])
    
