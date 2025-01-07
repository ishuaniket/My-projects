    total = 1000
    deduction = 500
    print("Welcome to The KBC Game.")
    print()
    print("Rules:")
    print()
    print("1. You will be asked 5 questions from general knowledge.")
    print("2. You have to select your answer from the 4 options provided.")
    print("3. For every correct answer you will be awarded with 1000 Rs.")
    print("4. In case of wrong answer, you will be penalized by 500 Rs.")
    print()
    a = input("Do you want to play : ").lower()
    print()
    if a == 'yes':
        print("Thankyou for entering the game")
    else:
        print("Bye bye")
    print()

    print("So the first question is: ")
    print("1. The language of Lakshadweep. a Union Territory of India, is")
    c = "A.Tamil"
    d = "B.Hindi"
    e = "C.Malayalam"
    f = "D.Telugu"
    print(c)
    print(d)
    print(e)
    print(f)
    b = input("Answer : ").title()
    if b == 'C':
        print("Ohh great your answer is correct, you have won 1000 Rs. ")
    else:
        print("Incorrect answer, you will be penalized by 500 Rs. ")
    print("Now you have moved to the next level")
    print()
    print("The second question is : ")
    print()
    print("2.'Good Friday' is observed to commemorate the event of")
    print("A.birth of Jesus Christ")
    print("B.certification 'of Jesus Christ")
    print("C.birth of' St. Peter")
    print("D.rebirth of Jesus Christ")

    b = input("Answer : ").title()
    if b == 'B':
        print(f"Ohh great your answer is correct, you have won 1000 Rs. and now your total winning amount is {total + 1000} Rs. ")
    else:
        print(f"Incorrect answer, again you will be penalized by 500 Rs. and now your total penalty is {deduction+500} ")
    print()
    print("Great you answer the 2 question correctly and Now you have moved to the level 3.")
    print("The Third question is : ")
    print()
    print("3.Pongal is a popular festival of which state?")
    print("A.Karnataka")
    print("B.Kerala")
    print("C.Andhra Pradesh")
    print("D.Tamil Nadu")
    b = input("Answer : ").title()
    if b == 'D':
        print(f"Ohh great your answer is correct, you have won 1000 Rs. and now your total winning amount is {total + 2000} Rs. ")
    else:
        print(f"Incorrect answer, again you will be penalized by 500 Rs. and now your total penalty is {deduction+1000} ")
    print()
    print()
    print("Great you entered in the lavel 4.")
    print("The Fourth question is : ")
    print()
    print("4.Rath Yatra is famous festival at")
    print("A.Ayodhya")
    print("B.Mathura")
    print("C.Dwaraka")
    print("D.Puri")
    b = input("Answer : ").title()
    if b == 'D':
        print(f"Ohh great your answer is correct, you have won 1000 Rs. and now your total winning amount is {total + 3000} Rs. ")
    else:
        print(f"Incorrect answer, again you will be penalized by 500 Rs. and now your total penalty is {deduction+1500} ")
    print()
    print()
    print("Great you entered in the Last lavel 5.")
    print("The Fifth question is : ")
    print()
    print("5.White Flag is the symbol of")
    print("A.Peace")
    print("B.War")
    print("C.Truth")
    print("D.Friendship")
    b = input("Answer : ").title()
    if b == 'A':
        print(f"Ohh great your answer is correct, you have won 1000 Rs. and now your total winning amount is {total + 4000} Rs. ")
        print("Congratulations you won the 5000 Rs. amount")
    else:
        print(f"Incorrect answer, again you will be penalized by 500 Rs. and now your total penalty is {deduction+2000} ")

