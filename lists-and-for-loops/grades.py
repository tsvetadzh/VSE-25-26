grades = [5, 12, 18, 21, 33, 42, 50, 77, 90]
excellent = []
good = []
passTest = []
fail = []
for grade in grades:
    if grade >= 90:
        excellent.append(grade)
    elif grade >= 70:
        good.append(grade)
    elif grade >= 50:
        passTest.append(grade)
    elif grade < 50:
        fail.append(grade)
print("excellent:", excellent)
print("good:", good)
print("pass:", passTest)
print("summer school:", fail)


