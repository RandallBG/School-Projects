from datetime import date,time,datetime
import csv

today = date.today()
startTime = datetime.now()

lines, males, females = 0,0,0

try:
    with open("MOCK_DATA.csv", 'r') as fp:
        reader = csv.reader(fp)
        for line in reader:
            if lines>0:
                id = line[0]
                first_name= line[1]
                last_name= line[2]
                gender = line[4]
                if gender=="Male":
                    males += 1
                else:
                    females += 1
                print(f"{lines} {first_name} {last_name}")
            lines +=1
    
    print(f"{datetime.now()}")
    print(f"{males}")
    print(f"{females}")

    with open("MOCK_CSV.txt", "a") as fp2:
        # writer = csv.writer(fp2)
        fp2.write(f"{today} time \n")
        fp2.write(f"{males} males\n")
        fp2.write(f"{females} females\n")

except:
    print("problem")
    