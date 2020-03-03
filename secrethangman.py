import random
randomWords = ["ducks" , "jumbo" ,"lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
#print secret 
def initialize(): 
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print "Enter a letter"
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord: 
        print "you win"
    else:
        getLetter()
def main():
    initialize ()
    getLetter()
    ifWon()
main()
val=0
def test():
    global val
    secret = "BALOON"
    updatedword = ['_','_','_','_','_','_','_']
    for i in range (0, len(Secret)):
        print (updatedWord[1]
    Letter = str(input("What is your guess: "))
    val = Secret.find (Letter)
    del updatedWord[val]
    updatedWord.insert(val, Letter)
    for i in range (0, len(Secret)):
            print(updatedWord[i], end =" ")
    if Secret.find(Letter) ==-1
        return "Wrong Letter"            
#def tester():
    #global updateWord
    #updateWord = raw_input()
    #if updateWord== secret:
     #   print "yay"
    #else: 
     #   print "no"
  
    
    
    

