import random


countries_namelist=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo ", "Croatia", "Cuba", "Cyprus", "Czechia ", "Denmark", "Djibouti", "Dominica",  "Ecuador", "Egypt", "Eritrea", "Estonia", "Eswatini ", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar ", "Namibia", "Nauru", "Nepal", "Netherlands",  "Nicaragua", "Niger", "Nigeria", "Korea", "Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Samoa", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia",  "Somalia",  "Spain", "SriLanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand",  "Togo", "Tonga",  "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",  "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"



]

        
def get_word():
    word = random.choice(countries_namelist)
    return word.upper()



def game(word):
    word_blanks = "_" * len(word)
    letters = []
    words = []
    guesses = 8
    guessed= False
    print("Let's start playing!")
    
    print(word_blanks)
    print("\n")
    while not guessed and  guesses > 0:
        guess = input("Enter a letter or a country's name: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters:
                print("You have already guessed this letter", guess + ".", "Guess a different one!")
            elif guess not in word:
                print(guess, "is not in the word.")
                guesses -= 1
                letters.append(guess)
                print(display_hangman(guesses))
            else:
                print("Great!", guess, "is in the word!")
                letters.append(guess)
                new_list = list(word_blanks)
                position = [i for i, j in enumerate(word) if j == guess]
                for loc in position:
                    new_list[loc] = guess
                word_blanks = "".join(new_list)
                if "_" not in word_blanks:
                    guessed = True
                
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words:
                print("You already guessed this word", guess + ".", "Try your luck again!")
            elif guess != word:
                print(guess, "is not the word.")
                guesses -= 1
                words.append(guess)
                print(display_hangman(guesses))
            else:
                guessed = True
                word_blanks = word
        else:
            print("This is not a valid guess.")
        
        print(word_blanks)

        print("\n")
    if guessed:
        print("YAYYYYYY, you correctly guessed the word! You win!")
    else:
        print("Sorry, you ran out of guesses. The word was", word +"." ,"Maybe next time!")

import turtle
win=turtle.Screen()
stick=turtle.Turtle()
win.bgcolor('pink')
stick.pensize(2)
stick.pencolor("white")
stick.penup()
stick.goto(-100,100)
stick.pendown()
stick.right(90)
stick.forward(250)
stick.penup()
stick.goto(-100,100)
stick.pendown()
stick.left(90)
stick.forward(100)
stick.right(90)
stick.forward(50)
stick.penup()
stick.goto(-30,20)
stick.pendown()



def display_hangman(guesses):
   


    if guesses==8:
        pass
    if guesses==7 :
        stick.circle(30)
        stick.penup()
        stick.goto(0,-10)
        stick.pendown()
    if guesses==6:
        stick.forward(40)
    if guesses==5 :
        stick.left(50)
        stick.forward(50)
        stick.penup()
        stick.goto(0,-50)
        stick.pendown()
    if guesses==4 :
        stick.right(100)
        stick.forward(50)
        stick.penup()
        stick.goto(0,-50)
        stick.pendown()
    if guesses==3 :
        stick.left(50)
        stick.forward(60)
    if guesses==2 :
        stick.left(50)
        stick.forward(50)
        stick.penup()
        stick.goto(0,-110)
        stick.pendown()
    if guesses==1 :
        stick.right(100)
        stick.forward(50)
        stick.penup()
        stick.goto(0,-110)
        stick.pendown()
        stick.left(50)
        

def main():
    
    word = get_word()
    game(word)
    

        
       
if __name__ == "__main__":
    main()

    

    



