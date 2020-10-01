def displayIntro():
  #put an Introduction message to the users
    print("Hi. Welcome to our donation page. Here you can choose non-profits and donate money to them.")

def displayNonProfits():
  #print all the non-profits to the screen numerically. For Example:
#    1. World Central Kitchen
#    2. Crisis Text Line
#    3. Heart to Heart International
    donate = input("Would you like to donate to a non-profit?(Y/N)")
    
def main():
    displayIntro()
    displayNonProfits()
    choice1 = 0;
    choice2 = 0;
    choice3 = 0;
    donate = "Y"
    if donate == "Y":
        while donate == "Y":
            print("1.World Central Kitchen")
            print("2.Crisis Text Line")
            print("3.Heart to Heart International")
            choice = int(input("Enter the number of the non-profit you would like to donate to: "))
            amount = int(input("Enter the amount of money you would like to donate: "))
            if choice == 1:
                choice1 += amount
                print(f"The World Central Kitchen has received {amount} and now has a total of {choice1}")
            elif choice == 2:
                choice2 += amount
                print(f"The Crisis Text Line has received {amount} and now has a total of {choice2}")
            else:
                choice3 += amount
                print(f"The Heart to Heart International has received {amount} and now has a total of {choice3}")
            donate = input("Would you like to donate to another non-profit?(Y/N)")
            if donate == "Y":
                displayNonProfits()
            elif donate == "N":
                print("Have a nice day.")
            else:
                print("I don't understand.")
    elif donate == "N":
          print("Have a nice day.")
    else:
          print("I don't understand.")

main()
    
    
    
	#steps: 
	#1. welcome the user using a unique Intro Message (use a function for this)
	#2. create a variable for each nonprofit/charity that keeps track of how much total money has been donated
	#3. display all the non-profits to the user and ask which one they would like to donate to 
	#4. then ask the user how much money they would like to donate to that specific charity chosen in step 3
	#5. update the variable created in step 2 with whatever amount the user wanted to donated
			#for example: missionbit = 0 -> user wants to donate 100 so you would add 100 to missionbit. missionbit is now 100
	#6. now display all the nonprofits with their new total amounts donated
	#7. repeat this process until the user wants to stop donating (only do this if you cover while loops)
	#push to github after every single step
          
        