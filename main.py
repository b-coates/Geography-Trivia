print('Welcome to the great geography quiz! Question will get harder as you get further into the game. ')
answer = input('Are you ready to play? (yes/no) :')
score = 0
total_questions = 5
 
if answer.lower()=='yes':
    answer = input('Question 1: What continent is Spain located on?')
    if answer.lower()=='europe':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
 
 
    answer = input('Question 2: What is the smallest country in the world? ')
    if answer.lower()=='vatican city':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer = input('Question 3: What is the capital of Chile? ')
    if answer.lower()=='santiago':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
    
    answer = input('Question 4: What African nation has Portuguese as its official language?')
    if answer.lower()=='mozambique':
        score += 1
        print('correct!')
    else:
        print('Wrong Answer  :( ')
    answer = input('Question 5: What is the largest island in Canada?')
    if answer.lower()=='baffin island':
        score += 1
        print('correct!')
    else:
        print('Wrong Answer :( ')
    answer = input('Question 6: Where is the Hunua range located?')
    if answer.lower()=='new zealand':
        score += 1
        print('correct!')
    else:
        print('Wrong Answer :( ' )
    answer = input('Question 7: In what country would you find Lake Tiberias, or the Sea of Galilee? ')
    if answer.lower()=='israel':
        score += 1
        print('correct!')
    else:
        print('Wrong Answer :(')



    

print('Thank you for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Total Points:',mark)
print('Bye!')