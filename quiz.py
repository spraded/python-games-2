print("Welcome to the present perfect English quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play! Fill in the blanks below with the correct answer in the present perfect.")
score = 0

answer = input("I _____ never ______ (be) to space. ")
if answer.lower() == "have been":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("_____ you ever ______ (fall) in love? ")
if answer.lower() == "have fallen":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("She _____ _______ (not quit) a job before. ")
if answer.lower() == "hasn't quit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many movies _______ he _________ (see) today? ")
if answer.lower() == "has seen":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got", score, "questions correct!")
print("You got", (score / 4) * 100, "%.")