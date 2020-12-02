
Maths_mark = (int(input("Enter your Maths mark: ")))
Chemistry_mark = (int(input("Enter your Chemistry mark: ")))
Physics_mark = (int(input("Enter your Physics mark: ")))

Total_marks = Maths_mark + Chemistry_mark + Physics_mark 

Percentage = (Total_marks/300) *100 

if Percentage >= 70:
    print ("A")
elif Percentage >= 60:
    print ("B")
elif Percentage >= 50:
    print ("C")
elif Percentage >= 40:
    print ("D")
else:
    print ("You failed")

