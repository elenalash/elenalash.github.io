from datetime import date
today = date.today()
print(("\n------------------------------------------------------------"))
print(today.strftime("\nReport generated on: %d//%m/%Y\n\n"))
print(str("Packs distribution among the conference attendees:\n").upper())
fr = open("confPack.txt", "r")
packList = fr.read().splitlines()
fr.close()
packOne = packList[0]
packBoth = packList[1]
fr = open("employees.txt", "r")
empList = fr.read().splitlines()
fr.close()
attendList = []
for employee in empList:
    empCheckList = employee.split(sep = ",")
    if len(empCheckList) >= 3:
        attendList.append(employee)
for attendee in attendList:
    attendListCheck = attendee.split(sep = ",")
    surname = attendListCheck[0]
    name = attendListCheck[1]
    x = 0
    y = 0
    if attendListCheck[2] == "Y":
        x = 1
    if len(attendListCheck) > 3:
        if attendListCheck[3] == "Y":
            y = 1
    packOneDisp = packOne
    if x+y == 2:
        packBothDisp = ", "+ packBoth
    else:
        packBothDisp = " "
    print("Attendee: "+ surname + ", "+ name + " Pack/s: "+ packOneDisp + packBothDisp)
print(("\n------------------------------------------------------------"))
