print("Welocome to my quiz!")

playing = input("Are you ready? ")

if playing.lower() != "Hell yeah":
    quit()

print("Let's go!")
score = 0

answer = input("Question 1")
if answer.lower() == "Answer 1":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Question 2")
if answer.lower() == "Answer 2":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Question 3")
if answer.lower() == "Answer 3":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")