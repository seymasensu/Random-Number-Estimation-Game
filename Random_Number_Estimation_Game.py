import easygui
from random import randrange

# Game of guessing the number that the computer generates randomly.

inputfile = open("file.txt", "w")  # open our input file for writing
inputfile.write("") # clear our input file
inputfile.close() # close input file
i = True  # Boolean value is assigned to i for using it in the while loop
easygui.msgbox("**** welcome to number estimation game ****")  # Welcome message printed on the screen
choices = ["New Game", "Exit Game"]
choice = easygui.buttonbox("Choose your action", "", choices)  # options of the game asked to the user
while i == True:  # User can play this game infinity times
    if choice == "New Game":  # If user choose to play the estimation game
        number = randrange(11)  # Computer will generate numbers 0 to 10 and keep one of them as an estimated number

        est_num = 1  # This variable will keep the tries of estimation
        while choice == "New Game":  # While loop: user can play it until he/she finds the estimated number

            estimate = easygui.enterbox("Estimation between 0 & 10")  # Estimation value will be taken as an input
            try:     # try to convert input value to int
                estimate = int(estimate)   # convertion
            except TypeError:     # if type error occurs
                i = False         # assign i to False for ending the game
                break             # break our while loop
            if estimate > 10 or estimate < 0:  # If the estimated value is bigger than 10 or smaller than 0
                easygui.msgbox("Invalid Value \n please estimate a number between 0 and 10")
            else:  # If valid value is entered
                if estimate < number:  # If estimated value is smaller than our random number
                    print("increase your estimation")  # Increasing the estimated value will be informed to the user
                    est_num = est_num + 1  # Estimation number incremented
                elif estimate > number:  # If estimated value is bigger than our random number
                    print("decrease your estimation")  # Decreasing the estimated value will be informed to the user
                    est_num = est_num + 1  # Estimation number incremented
                else:  # The condition that user finds the random number
                    Wins = []    # create a list that stores scores
                    with open('file.txt') as f:    # open our file.txt file to read string in it
                        for line in f:        # loop on file line by line
                            line = line.strip()    # trailing characters removed from our line string
                            Wins.append(line[37])    # store 37. char in line which is score in wins list
                    Winned = '\n'.join(Wins)          # adding a new line
                    inputfile.close()                 # close our input file
                    easygui.msgbox("this time, you found it in your" + " " + str(est_num) + ".try" + '\n' + "Previous scores : " + "\n" + str(Winned), "You Win")  # result message is send via messagebox
                    inputfile = open("file.txt", 'a')  # open our input file in appending mode
                    inputfile.write("congratulations you found it in your" + " " + str(est_num) + ".try \n")  # append result messages to store the previous scores to file
                    inputfile.close() # close our input file
                    # Message box will be diplayed when user finds the random number and number of estimatons will be shown
                    break  # while loop breaks after finding the random number
    elif (choice == "Exit Game"):  # If user enters 2 for exiting the game
        i = False  # Exits game
    else:  # The condition that user enters a value that is not 1 or 2
        print("please give a valid input")