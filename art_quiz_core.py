# ART QUIZ


def processDatabase():
    dbd = {}    #create empty dictionary
    print("Open database file")
    db = open('database.txt', 'r') #open file to read
    #file format: int \t str \t str
    #paint no, painter name, paint name
    for line in db:
        ll = line.split("\t") #split string with Tab
        paintID = int(ll[0])
        painterName = ll[1]
        paintName = ll[2][:-1]  #omit \n at the end
        dbd[ paintID ] = (painterName, paintName)
        
    #ToDo: Check duplicate (painter,paint) entries
    
    return dbd
        

#main program
db=processDatabase()
#print(db)


#constants
MAX_NUM = len(db)   #length of database
NUM_OF_CHOICE = 4   #number of choices in questions
GAME_TYPE = 1       #0: Painter Name, 1: Paint Name
LETTER = ['A) ', 'B) ', 'C) ', 'D) ', 'E) ', 'F) ', 'G) ', 'H) ']


#select paint number and get correct answer
paint_no = int(random()*MAX_NUM) +1 #database starts from 1
corr_ans = db[paint_no][GAME_TYPE]
print("Paint No = %d, Correct Answer = %s" %(paint_no, corr_ans) )

#pick wrong answers
choice_array = []   #empty list
num_picked_choices = 0
while 1:
    temp = int(random()*MAX_NUM)+1
    candidate = db[temp][GAME_TYPE]
    if(candidate == corr_ans):  #cannot pick correct answer
        continue
    if(choice_array.count(candidate) == 0):   #if candidate is not in list
        choice_array.append(candidate)   #append at the end
        num_picked_choices = num_picked_choices +1; #new choice is picked
    if(num_picked_choices == NUM_OF_CHOICE-1):
        break
#insert correct answer into a random position
corr_choice = int(random()*NUM_OF_CHOICE)
choice_array.insert(corr_choice, corr_ans)


print("Who painted %d ?" %paint_no)
temp=0
for s in choice_array:
    print(LETTER[temp]+s)
    temp = temp+1




























