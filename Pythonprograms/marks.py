marks=int(input("Enter the marks:"))
if marks>90 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<=80:
    print("Grade B")
elif marks>60 and marks<70:
    print("Grade C")
else:
    print("Fail")