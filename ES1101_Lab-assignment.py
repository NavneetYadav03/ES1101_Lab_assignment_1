#1.Write a Python program to find average of three numbers entered by the user.

a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
print("Average of three numbers is ",(a+b+c)/3)

""""
2.Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate
"""

GI=int(input("Enter Gross Income ",)) #GI is Gross Income
DP=int(input("Enter No. of Dependents ",))#DP is No. of Dependents
standard_deduction=10000
tax_rate=20#in percentage
TI=GI-standard_deduction-(DP*3000)#TI is Taxable Income
T=TI*(tax_rate)/100#T is Tax to be paid
print("Tax to be paid ",T)

"""
3.Write a python program to store different data type values into a list. (For an
example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5).
"""

Sid=int(input("Enter your SID ",))
Name=str(input("Enter your Name ", ))
GEN=str(input("Enter your gender enter M for male,enter F for female,enter U for other ",))
CN=str(input("Enter course Name ", ))
CGPA=float(input("Enter your CGPA ", ))
List2=["SID","NAME","GENDER","COURSE_NAME","CGPA"]
List=[Sid,Name,GEN,CN,CGPA]
print(List2)
print(List)

"""
4.Write a python program to enter marks of 5 students into a list and display
them in sorted manner.
"""

a=float(input("Enter marks of First student ",))
b=float(input("Enter marks of Second student ",))
c=float(input("Enter marks of Third student ",))
d=float(input("Enter marks of Fourth student ",))
e=float(input("Enter marks of Fivth student ",))
marks=[a,b,c,d,e]
marks.sort()
print(marks)

""""
5.List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a. Write a Python program to print a specified list after removing 4th element.
Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
Do that in one line code.
"""
#a part
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)
#b part
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3]="Purple"
color[4]="Purple"

print(color)









