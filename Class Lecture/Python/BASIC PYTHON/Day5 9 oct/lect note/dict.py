# students = {
# 101 :{ "Name":'aditi', "scores": [10,20,25]},
# 102 :{ "Name": 'ravi', "scores": [30,50,25]},
# 103 :{ "Name": 'kisha', "scores": [50,28,25]},
# }

# for sid ,details in students.items():
#     avg = sum (details["scores"])/ len(details["scores"])
#     details["average"] = avg
#     details["Passed"] =  avg >= 30 

#     print("")
#     for sid, details in students.items():
#         if details["Passed"]:
#             print(details["name"])

            
students = {
101: {"Name": "aditi", "scores": [10,20,25]},
102: {"Name": "ravi", "scores": [30,50,25]},
103: {"Name": "kisha", "scores": [50,28,25]}
}

for sid, details in students.items():
    avg = sum(details["scores"]) / len(details["scores"])
    details["average"] = avg
    details["Passed"] = avg >= 30

print("Passed students:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])
