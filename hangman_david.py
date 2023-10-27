hangman={}
hangman['open_word'] = (input("Insert word "))
hangman['shadow_word'] = (["-"] * len(hangman['open_word']))
hangman['attempt']= int(input(("How may attempts? ")))
hangman['mistakes']=[]
hangman['result'] = False

games = []

def oc_char (st,char):
    
    # base case;
    if (len(st) == 0):
        return 0
    count = 0
    if (st[0] == char):
        count += 1
    count += oc_char(char, st[1:])
 
    return count
     
str = "geeksforgeeks"
c = 'e'
print(oc_char(c, str))

import os
os.system('cls')

while True if (input(('Are you ready to play? '))) == "yes" else False:
  
    attempts=0

    while attempts < hangman['attempt']:
        j2_att= (input(("Insert letter ")))

        if j2_att in (hangman['open_word']):
            hangman['shadow_word'][hangman['open_word'].find(j2_att)] = j2_att
        #oc_char(j2_att) in len(hangman[open_word])
        else:
            hangman['mistakes'].append(j2_att)
            attempts +=1

        print ('Letters that are not in the word', *hangman["mistakes"], sep = ", ")
        print (hangman['shadow_word'])   
        
        if hangman['open_word'] == "".join(hangman['shadow_word']):
            hangman['result'] = True
            attempts = hangman['attempt']

    if (hangman['result']):
        print("Congratulations you won!")
    else:
        print('Game over, maxed attempts')
    games.append(hangman)

else:
    print('Goodbye')

# Print the names of the columns.
print("{:<10} {:<10} {:<10} {:<10}".format('WORD', 'MISTAKES', 'ATTEMPS', 'RESULT'))
 
# print each data item.
for game in games:
    print("{:<10} {:<10} {:<10} {:<10}".format(game['open_word'], game['mistakes'], game['attempt'], "WIN" if game['result'] else "LOOSE"))



   
