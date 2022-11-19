"""
Word Guesser Game
Code by: Simran Naryani
"""

#Import required libraries
import time #To include waiting time

print("Time to play Word Guesser!!!")
mode=int(input("Select the mode: 1. Easy  2. Medium 3. Hard "))
time.sleep(2)

#Defining modes
if (mode==1):
 print("Hint: One of the 4 suites of cards")
 time.sleep(1)
 print("Start guessing, you have got 5 turns...")
 time.sleep(0.5)
 word = "spade"
 guesses = ''
 turns = 5

 while turns > 0:         
    failed = 0              
    for char in word:      
        if char in guesses:       
          print(char)
        else:
            print("_")   
            failed += 1    
    if failed == 0:        
        print("You won!!!!")
        break              
    print
    guess= input("Guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("Wrong")
        print("You have", + turns, "more guesses")
        if turns == 0:               
            print("You Lose")  
            
if mode==2:
 print("Hint: One of the coding languages")
 time.sleep(1)
 print("Start guessing, you have got 5 turns...")
 time.sleep(0.5)
 word1 = "cobol"
 guesses1 = ''
 turns1 = 5

 while turns1 > 0:         
    failed1 = 0              
    for char in word1:      
        if char in guesses1:       
          print(char)
        else:
            print("_")   
            failed1 += 1    
    if failed1 == 0:        
        print("You won!!!!")
        break              
    print
    guess1= input("Guess a character:") 
    guesses1 += guess1                    
    if guess1 not in word1:  
        turns1 -= 1        
        print("Wrong")
        print("You have", + turns1, "more guesses")
        if turns1 == 0:               
            print("You Lose") 
            
if mode==3:
 print("Hint: Field of study after HSC")
 time.sleep(1)
 print("Start guessing, you have got 5 turns...")
 time.sleep(0.5)
 word2 = "biotechnology"
 guesses2 = ''
 turns2 = 5

 while turns2 > 0:         
    failed2 = 0              
    for char in word2:      
        if char in guesses2:       
          print(char)
        else:
            print("_")   
            failed2 += 1    
    if failed2 == 0:        
        print("You won!!!!")
        break              
    print
    guess2= input("Guess a character:") 
    guesses2 += guess2
    
    if guess2 not in word2:  
        turns2 -= 1        
        print("Wrong")
        print("You have", + turns2, "more guesses")
        if turns2 == 0:               
            print("You Lose")
            
if(mode!= 1 and mode != 2 and mode != 3):
 print("Wrong data entered!!!")
