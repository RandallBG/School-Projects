import csv
from datetime import date, time, datetime
from os import write

lines = 0
startTime = datetime.now()
endTime = datetime.now()
totalPayout = 0
try:
    with open("timesheet.csv","r") as ts:
        with open("payroll.csv", "a", newline='') as pr:
            startTIme = datetime.now()
            writer = csv.writer(pr)
            reader = csv.reader(ts)
            for line in reader:
                if lines > 0:
                    id = line[0]
                    firstName = line[1]
                    lastName = line[2]
                    hours = line[3]
                    pay = line[4]
                    totalPay = round((float(hours) * float(pay)), 3)
                    totalPayout += totalPay
                    writer.writerow([id, firstName, lastName, hours, pay, '{:.2f}'.format(totalPay)])
                lines += 1
            endTime = datetime.now()
    with open("payrollSummary.txt", "a") as ps:
        writer = csv.writer(ps)
        ps.write(f"Payroll Date: {datetime.today().strftime('%x')}\n")
        ps.write(f"Start Time: {startTime.strftime('%X')}\n")
        ps.write(f"End Time: {endTime.strftime('%X')}\n")
        ps.write(f"Records Processed: {lines}\n")
        ps.write(f"Total Payout: {'{:.2f}'.format(round(totalPayout, 3))}\n")

except:
    print("error accessing csv file")