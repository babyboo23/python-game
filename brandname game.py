
import random


score = 0
lives = 3
words = ['dior','chanel','gucci','prada','ysl','celine']
 

def update_clue(guess, secret_word, clue):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i] = guess

    win = ''.join(clue) == secret_word
    return win

while (len(words) > 0) and (lives > 0):
    secret_word = words.pop()
    clue = list('_'*len(secret_word))

    while True:
        print(clue)
        print('your life is: ' + str(lives))
        guess = input('try a guess: ')

        if guess in secret_word:
            win = update_clue(guess, secret_word, clue)
            if win:
                print('correct this words is: ' + secret_word)
                score = score + 1
                print('score: ' + str(score)) 
                break

        else:
            print('wrong')
            lives = lives - 1
            if lives == 0:
                print('wrong this words is: ' + secret_word)     
                break

print('final score: ' + str(score))
print('game over')
                    
