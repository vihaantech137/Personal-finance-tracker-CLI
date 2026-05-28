print("Welcome to Personal Finance Tracker CLI")
while True:
    main=input("""Please choose any of the following options:
    1.Profit and Loss calcculator
    2.Debt coverage analyser
    3.Quit
    Enter your answer here as 1,2 or 3:""")
    if main=='1' or main=='1.':
        try:
            Income=float(input("Please enter your Monthly Salary:"))
            Expenses=float(input("Please enter an estimated value of your expenses:"))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
        if Income > Expenses:
            print("Congratulations! you make a profit of", round(Income - Expenses,2), 'every month')
        elif Income == Expenses:
            print("you are neither in profit nor in loss")
        else:
            print("You are in", round(Expenses - Income,2), "of loss every month")
    elif main=='2' or main=='2.':
        try:
            debt=float(input("Enter the amount of debt you are in:"))
            salary=float(input("Enter your monthly salary"))
            mexp=float(input("Please enter an estimated value of your expenses"))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
        if salary-mexp<=0:
            print("Your monthly expenses are higher or equal than your monthly salary you cannot pay off your debts yet")
        else:
            extramoney=salary-mexp
            print("it will take",round(debt/extramoney,1),"months for you to cover your debts")
    elif main == '3' or main == '3.':
        print("Hope you have a wonderful day ahead Goodbye!")
        break
    else:
        print("You have entered a wrong value please choose from one of the options")
