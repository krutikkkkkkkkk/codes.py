import random
import time
print("Stone Paper Scissors: Reboot13")
time.sleep(1.0)
print('You have 10 Chances')
time.sleep(1.0)
print('Start')
time.sleep(2.0)


level = 11
onLevel = 0
score = 0
opponentScore = 0

while level >= 1:
    level = level - 1
    onLevel = onLevel + 1
    if level == 0 and score == opponentScore:
        print("Result: Tie")
    elif level == 0 and score > opponentScore:
        print("Result: You win")
    elif level == 0 and score < opponentScore:
        print("Result: You loose")
    else:
        randChoice = ["STONE", "PAPER", "SCISSOR"]
        opponentChoice = random.choice(randChoice)
        print("Level: " + str(onLevel))
        yourChoice = input('Choose STONE  PAPER or SCISSOR: ')
        yourChoice = yourChoice.upper()
        if yourChoice == opponentChoice:
            print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
            print("Your Score: " + str(score) + " || Opponent Score: " + str(opponentScore) + "\n")
        elif yourChoice == "STONE" and opponentChoice == "SCISSOR":
            score += 1
            print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
            print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))
        elif yourChoice == "PAPER" and opponentChoice == "STONE":
            score += 1
            print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
            print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))
        elif yourChoice == "SCISSOR" and opponentChoice == "PAPER":
            score += 1
            print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
            print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))
        elif yourChoice not in randChoice:
            print("Invalid input")
        else:
            opponentScore += 1
            print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
            print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))
