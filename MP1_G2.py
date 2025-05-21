i = 0
normal = 0
elevated = 0
high = 0

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
summary = []
while i < 7:
    print (f"Day: {days[i]}")
    category = ""
    try:
        systolic = int(input ("Enter your systolic blood pressure: "))
        diastolic = int(input ("Enter your diastolic blood pressure: "))
        
        if systolic < 0 or diastolic < 0:
                print(f"Error message for {days[i]}: Blood pressure readings cannot be negative.")
                category = "Invalid"
        else:
            if  systolic < 120 and diastolic < 80:
                print ("Normal")
                normal += 1
                category = "Normal"
            if 120 <= systolic < 130 and diastolic < 80:
                print ("Elevated")
                elevated +=1
                category = "Elevated"
            elif systolic >= 130 or diastolic >= 80:
                print ("High")
                high +=1
                category = "High"
    except ValueError:
        print(f"Invalid input on {days[i]}: Please enter a valid number for blood pressure readings")
        category = "Invalid"

    summary.append({
        "day": days[i],
        "category": category
    })

    i += 1
if normal == 7:
    print ("Classification for each day: Normal" )
elif elevated == 7:
    print ("Classification for each day: Elevated" )
elif high == 7:
    print ("Classification for each day: High" )
else:
    print ("Classification for each day: ")
    for entry in summary:
        print(f"{entry['day']}: {entry['category']}")

print ("Summary Report:")
print ("Normal: ", normal, "days")
print ("Elevated: ", elevated, "days")
print ("High: ", high, "days")

if high > 3:
    print("Warning: More than 3 days are classified as High. Please consult a doctor.")
elif high <= 3:
    print("No warning message")