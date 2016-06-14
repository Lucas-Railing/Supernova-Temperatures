import matplotlib.pyplot as plt
from numpy import e, asarray, diag
from datetime import datetime
from scipy.optimize import curve_fit
from os import listdir
from math import sqrt

#Enter recession velocity here:
v = 0.0
beta = v/300000000.0
shift = sqrt((1.0 - beta)/(1.0 + beta))
print shift

files = listdir('.')

Flist = sorted([x for x in files if x.split('.')[-1]== 'flm'])
DateList = [x.split('-')[1] for x in Flist]

YearList = []
for x in DateList:
    YearList.append(float(x[0:4]))

maglists = []
lenlists = []
Fit      = []
for x in Flist:
    maglists.append([])
    lenlists.append([])
    Fit.append([])
Dlist = []
for x in Flist:
    Dlist.append(open(x))

x = 0
while x < len(Flist):
    row = Dlist[x].readline().strip()
    while len(row) > 1:
        rlist = row.split()
        lenlists[x].append(shift*float(rlist[0]))
        maglists[x].append(float(rlist[1]))
        row = Dlist[x].readline().strip()
    Dlist[x].close()
    x = x + 1

def bb(l, p, k):
    y = p*(l**(-5))/(e**(k/l) - 1)
    return y
i = 0
T    = []
aday = []
f = 1
m = 0
while i < len(Flist):
    x = asarray(lenlists[i])
    y = asarray(maglists[i])
    popt, pcov = curve_fit(bb, x, y, p0 = [10**(19), 10*10])
    for x in lenlists[i]:
        Fit[i].append(bb(x, popt[0], popt[1]))
    dt = datetime(int(DateList[i][0:4]), int(DateList[i][4:6]), int(DateList[i][6:8]), 0, 0)
    tt = dt.timetuple()
    aday.append(tt.tm_yday + 365*(YearList[i] - min(YearList)))
    T.append(144043478.3/popt[1])
    i += 1

i = 1
fig = plt.figure(figsize = (25,9))
fig.canvas.set_window_title('Plank Law Curve Fit')
while i <= len(Flist):
    plt.subplot(int(round(sqrt(len(Flist)))),int(round(sqrt(len(Flist)))) + 1,int(i))
    try:
        plt.title(Flist[i-1].split('-')[1]+Flist[i-1].split('-')[2].split('.')[0])
    except IndexError:
        plt.title(Flist[i-1].split('-')[1])
    plt.xlabel("Wavelength (Angstroms)")
    plt.ylabel("Flux (erg/s/cm^2/A)*10^15")
    L1 = plt.scatter(lenlists[i-1], maglists[i-1], color = 'r')
    L2 = plt.plot(lenlists[i-1], Fit[i-1], color = 'b')
    i = i + 1
plt.show()  
fig = plt.figure(figsize = (15,15))
fig.canvas.set_window_title('Temperatures from Curve Fit')
plt.title('Temperature vs. Time')
plt.xlabel('Day')
plt.ylabel('Temperature (K)')
try:
    plt.scatter(aday, T, color = 'b', label = 'fast')
except ValueError:
    plt.scatter(aday, T, color = 'b')
plt.show()
