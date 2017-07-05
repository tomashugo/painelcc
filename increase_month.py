from datetime import datetime


a = datetime.strptime("01/01/2016","%d/%m/%Y")

now = datetime.now()

meses = []

while a.month != now.month or a.year != now.year:
    meses.append(a)
    if a.month != 12:
       a  = a.replace(month=a.month + 1)
    else:
       a  = a.replace(month=1,year=a.year +1)


for mes in meses:
   print mes
