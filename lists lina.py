math = ["charlie", "kevin","alise", "bob", "leo"]
physics = ["jack", "paolo", "alex", "bob", "charlie"]
math.insert(input("inter the name of the student you want in math: "))
print(math)
physics.insert(2, input("inter the name of the student you want in physics: "))
print(physics)
math.sort()
print("the display of sorted list of math alphabetically: ", math)
physics.sort()
print("the display of sorted list of physics alphabetically: ", physics)
inputName = input("Enter a student name to remove from physics list:  ")


if inputName in physics:
    physics.remove(inputName)
    print("the Removed student from physics:" ,inputName)
else:
    print("Student not found in physics list.")

print("the final list of math students is: ",math)
print("the final list of physics students is:", physics)
