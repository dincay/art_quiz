#art quiz top (core+GUI)

PAINTER = 0
PAINT = 1

#GUI globals
MAX_NUM = 10   #length of database
MAX_QUES = 10
ACTIVE_QUES = 0
CORRECT_AT_1ST_ATTEMPT = 0
SCORE = 0
GAME_TYPE = PAINTER
NUM_OF_CHOICES = 4
dbd = {}    #database dictionary
LETTER = ['A) ', 'B) ', 'C) ', 'D) ', 'E) ', 'F) ', 'G) ', 'H) ']
IMAGE_HEIGHT = 480
IMAGE_WIDTH = 640

import time

import wx
class TopGUI(wx.Frame):
    
    #button colors
    defaultColor = wx.Colour()
    defaultColor.SetRGB(0xE0E0E0)    
    wrongColor = wx.Colour()
    wrongColor.SetRGB(0xA0A0FF)
    correctColor = wx.Colour()
    correctColor.SetRGB(0xA0FFA0)
    
    
    
    
    def __init__(self, *args, **kwargs):
        super(TopGUI, self).__init__(*args, **kwargs)
        self.InitGUI()
        
    def InitGUI(self):     
        
        #create master panel        
        pnl = wx.Panel(self)          
        
        # sizers
        mainSizer = wx.GridBagSizer(hgap=20, vgap=20) #main sizer
        ver_grid = wx.GridBagSizer(hgap=20, vgap=20) #vertical left-menu sizer
        choice_grid = wx.GridBagSizer(hgap=2, vgap=4) #choice sizer

        # game title
        titlefont = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        titlefont.SetPointSize(15)
        self.quotename = wx.StaticText(self, label="Dincay Akcoren")
        self.quotename.SetFont(titlefont)
        ver_grid.Add(self.quotename, pos=(0,0),span=(1,2),flag=wx.ALIGN_CENTER)
        self.quotetitle = wx.StaticText(self, label="ART TEST")
        ver_grid.Add(self.quotetitle, pos=(1,0),span=(1,2),flag=wx.ALIGN_CENTER)
        self.quotetitle.SetFont(titlefont)
        
        # number of questions
        lblques = wx.StaticText(self, label="# of question: ")
        ver_grid.Add(lblques, pos=(2,0))
        sampleList = ['10', '20', '30']
        editques = wx.ComboBox(self, size=(60, -1), choices=sampleList, value='10',
                               style=wx.CB_DROPDOWN|wx.CB_READONLY)
        ver_grid.Add(editques, pos=(2,1))
        editques.Bind(wx.EVT_COMBOBOX, self.EvtNumOfQuestions)
        
        # game type
        radioList1 = ['Guess the Painter', 'Guess the Painting']
        gametype = wx.RadioBox(self, label="Game Type", choices=radioList1, 
                               majorDimension=1, style=wx.RA_SPECIFY_COLS)
        ver_grid.Add(gametype, pos=(3,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtGameType, gametype)
        
        # number of choices
        radioList2 = ['4', '6', '8']
        numcho = wx.RadioBox(self, label="Number of Choices", choices=radioList2, 
                             majorDimension=3, style=wx.RA_SPECIFY_COLS)
        ver_grid.Add(numcho, pos=(4,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtNumOfChoices, numcho)
        
        # start button
        self.startbutton =wx.Button(self, label="START", size=(150, 60))
        ver_grid.Add(self.startbutton, pos=(5,0), span=(1,2), flag=wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.OnStart,self.startbutton)
        
        # logger
        self.logger = wx.TextCtrl(self, size=(180,200), 
                                  style=wx.TE_MULTILINE | wx.TE_READONLY)
        ver_grid.Add(self.logger, pos=(6,0), span=(1,2))
           
        #choice buttons
        butDefSize = (250,30) #tuple width,heigth
        self.buttonA = wx.ToggleButton(self, label="A) ", name="0", size=butDefSize)
        choice_grid.Add(self.buttonA, pos=(0,0))
        self.buttonB = wx.ToggleButton(self, label="B) ", name="1", size=butDefSize)
        choice_grid.Add(self.buttonB, pos=(0,1))
        self.buttonC = wx.ToggleButton(self, label="C) ", name="2", size=butDefSize)
        choice_grid.Add(self.buttonC, pos=(1,0))
        self.buttonD = wx.ToggleButton(self, label="D) ", name="3", size=butDefSize)
        choice_grid.Add(self.buttonD, pos=(1,1))
        self.buttonE = wx.ToggleButton(self, label="E) ", name="4", size=butDefSize)
        choice_grid.Add(self.buttonE, pos=(2,0))  
        self.buttonF = wx.ToggleButton(self, label="F) ", name="5", size=butDefSize)
        choice_grid.Add(self.buttonF, pos=(2,1))
        self.buttonG = wx.ToggleButton(self, label="G) ", name="6", size=butDefSize)
        choice_grid.Add(self.buttonG, pos=(3,0))
        self.buttonH = wx.ToggleButton(self, label="H) ", name="7", size=butDefSize)
        choice_grid.Add(self.buttonH, pos=(3,1))
        self.allButtonsDisable()
              
        #display picture        
        image = wx.Image('image/0000.jpg', wx.BITMAP_TYPE_ANY)
        #imageSize = image.GetSize()
        image.Rescale(IMAGE_WIDTH, IMAGE_HEIGHT)
        self.imageBitmap = wx.StaticBitmap(self, -1, wx.BitmapFromImage(image))
        
        #main sizer
        mainSizer.Add(ver_grid, pos=(0,0), span=(2,1),
                      flag=wx.ALIGN_RIGHT|wx.ALL, border=10)
        mainSizer.Add(choice_grid, pos=(1,1),
                      flag=wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL)
        mainSizer.Add(self.imageBitmap, pos=(0,1))
        self.SetSizerAndFit(mainSizer)
        
        
        #panel to close the application with ESC key

              
        #pnl.SetFocus()
        self.Bind(wx.EVT_KEY_DOWN, self.OnCloseWindow)
        
        self.SetSize((400, 600))
        self.Show(True)
        
        self.buttonE.Hide() #default is 4 choices
        self.buttonF.Hide() #default is 4 choices
        self.buttonG.Hide() #default is 4 choices
        self.buttonH.Hide() #default is 4 choices



    #helper functions - These are used to increase code readability
    def allButtonsSetValue(self,val):
        self.buttonA.SetValue(val)
        self.buttonB.SetValue(val)
        self.buttonC.SetValue(val)
        self.buttonD.SetValue(val)
        self.buttonE.SetValue(val)
        self.buttonF.SetValue(val)
        self.buttonG.SetValue(val)
        self.buttonH.SetValue(val)
    def allButtonsEnable(self):
        self.buttonA.Enable()
        self.buttonB.Enable()
        self.buttonC.Enable()
        self.buttonD.Enable()
        self.buttonE.Enable()
        self.buttonF.Enable()
        self.buttonG.Enable()
        self.buttonH.Enable()
    def allButtonsDisable(self):    
        self.buttonA.Disable()
        self.buttonB.Disable()
        self.buttonC.Disable()
        self.buttonD.Disable()
        self.buttonE.Disable()
        self.buttonF.Disable()
        self.buttonG.Disable()
        self.buttonH.Disable()
    def allButtonsUnbind(self):
        self.buttonA.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonB.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonC.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonD.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonE.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonF.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonG.Unbind(wx.EVT_TOGGLEBUTTON)
        self.buttonH.Unbind(wx.EVT_TOGGLEBUTTON)
    def allButtonsSetBackgroundColour(self, color):
        self.buttonA.SetBackgroundColour(color)
        self.buttonB.SetBackgroundColour(color)
        self.buttonC.SetBackgroundColour(color)
        self.buttonD.SetBackgroundColour(color)
        self.buttonE.SetBackgroundColour(color)
        self.buttonF.SetBackgroundColour(color)
        self.buttonG.SetBackgroundColour(color)
        self.buttonH.SetBackgroundColour(color)
    def allButtonsDeInitLabel(self):
        self.buttonA.SetLabel(LETTER[0])
        self.buttonB.SetLabel(LETTER[1])
        self.buttonC.SetLabel(LETTER[2])
        self.buttonD.SetLabel(LETTER[3])
        self.buttonE.SetLabel(LETTER[4])
        self.buttonF.SetLabel(LETTER[5])
        self.buttonG.SetLabel(LETTER[6])
        self.buttonH.SetLabel(LETTER[7])


    #call events that change quiz parameters
    def EvtGameType(self, event):
        global GAME_TYPE
        if event.GetInt() == 0:
            gametypestr = 'Painter'
        else:
            gametypestr = 'Painting'
        self.logger.AppendText('Game Type: %s\n' %gametypestr)
        GAME_TYPE = event.GetInt()
    def EvtNumOfChoices(self, event):
        global NUM_OF_CHOICES
        obj = event.GetEventObject()
        NUM_OF_CHOICES = int(obj.GetString(obj.GetSelection()) )
        self.logger.AppendText('Num of Choices: %d\n' % NUM_OF_CHOICES)
        if(event.GetInt() == 0):    #4 choices
            self.buttonE.Hide()
            self.buttonF.Hide()
            self.buttonG.Hide()
            self.buttonH.Hide()
        elif(event.GetInt() == 1):    #6 choices
            self.buttonE.Show()
            self.buttonF.Show()
            self.buttonG.Hide()
            self.buttonH.Hide()
        elif(event.GetInt() == 2):    #8 choices
            self.buttonE.Show()
            self.buttonF.Show()
            self.buttonG.Show()
            self.buttonH.Show()   
    def EvtNumOfQuestions(self, event):
        global MAX_QUES
        MAX_QUES = int(event.GetString())
        self.logger.AppendText('Num Of Questions: %d\n' %MAX_QUES)



    #This function should be called before any question
    #It picks a paint and generates choices, updates button labels and
    #assign appropiate bindings to buttons
    def initializeQuestion(self):
        global CORRECT_AT_1ST_ATTEMPT
        #initially mark question as corect at first attempt
        CORRECT_AT_1ST_ATTEMPT = 1
        #print("---Starting initializeQuestion()")
        self.logger.AppendText('Q%d ' %ACTIVE_QUES)
        #select paint number and get correct answer
        paint_no = int(random()*MAX_NUM) +1 #database starts from 1
        corr_ans = dbd[paint_no][GAME_TYPE]
        #print("---corr_ans=%s, paint_no=%d, GAME_TYPE=%d" %(corr_ans,paint_no,GAME_TYPE))
        #pick wrong answers
        choice_array = []   #empty list
        num_picked_choices = 0
        #print("---NUM_OF_CHOICES=%d" %NUM_OF_CHOICES)
        while 1:
            temp = int(random()*MAX_NUM)+1
            candidate = dbd[temp][GAME_TYPE]
            #print("------candidate = %s" %candidate)
            if candidate == corr_ans :  #cannot pick correct answer
                continue
            if choice_array.count(candidate) == 0 :   #if candidate is not in list
                choice_array.append(candidate)   #append at the end
                num_picked_choices = num_picked_choices +1; #new choice is picked
            if num_picked_choices == NUM_OF_CHOICES-1 : #if all choices are picked,exit loop
                break
        #insert correct answer into a random position
        corr_choice = int(random()*NUM_OF_CHOICES)
        choice_array.insert(corr_choice, corr_ans)
        #print("---Correct choice is at position %d" %corr_choice)
        #print("---All choices are %s" %str(choice_array))        
        #draw the painting
        self.imageBitmap.SetBitmap( draw_image(paint_no) )
        #choices are generated, update labels in buttons
        #print("---Update Labels") 
        self.buttonA.SetLabel(LETTER[0]+choice_array[0])
        self.buttonB.SetLabel(LETTER[1]+choice_array[1]) 
        self.buttonC.SetLabel(LETTER[2]+choice_array[2]) 
        self.buttonD.SetLabel(LETTER[3]+choice_array[3])
        if NUM_OF_CHOICES > 4:
            self.buttonE.SetLabel(LETTER[4]+choice_array[4])
            self.buttonF.SetLabel(LETTER[5]+choice_array[5])
        if NUM_OF_CHOICES > 6:
            self.buttonG.SetLabel(LETTER[6]+choice_array[6])
            self.buttonH.SetLabel(LETTER[7]+choice_array[7])        
        #update buttons   
        self.allButtonsEnable()
        self.allButtonsUnbind()
        #assign correct bindings
        if corr_choice==0:
            self.buttonA.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonA.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==1:
            self.buttonB.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonB.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==2:
            self.buttonC.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonC.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==3:
            self.buttonD.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonD.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==4:
            self.buttonE.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonE.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==5:
            self.buttonF.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonF.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==6:
            self.buttonG.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonG.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        if corr_choice==7:
            self.buttonH.Bind(wx.EVT_TOGGLEBUTTON, self.CorrectChoice)
        else:
            self.buttonH.Bind(wx.EVT_TOGGLEBUTTON, self.WrongChoice)
        #print("---Exiting initializeQuestion()")
        return 

    #event binded to correct choice button
    #it updates the score and perform end-of-quiz processes
    def CorrectChoice(self,event):
        global ACTIVE_QUES
        global SCORE
        global MAX_QUES
        global CORRECT_AT_1ST_ATTEMPT
        #print("Correct Choice")
        if CORRECT_AT_1ST_ATTEMPT == 1:
            SCORE = SCORE + 1
            #self.logger.AppendText("Correct in 1st try!\n")
        self.logger.AppendText("Score= %d/%d\n" %(SCORE,ACTIVE_QUES))
        time.sleep(1)   #wait 1 secound to let user digest correct answer
        #unselect and uncolor all buttons
        self.allButtonsSetValue(False)
        self.allButtonsSetBackgroundColour(self.defaultColor)
        if ACTIVE_QUES == MAX_QUES: #if quiz ended
            #print("Quiz Ended!!!")
            self.logger.AppendText("Quiz Ended!!!\n")
            self.logger.AppendText("Final Score= %d/%d\n" %(SCORE,MAX_QUES))
            ACTIVE_QUES = 0
            SCORE = 0
            #enable left menu items
            self.startbutton.Enable()
            #self.editques.Enable()
            #self.gametype.Enable()
            #self.numcho.Enable()
            #deinit buttons
            self.allButtonsSetValue(False)
            self.allButtonsDisable()
            self.allButtonsDeInitLabel()            
        else: #if quiz not ended but only a question is answered    
            ACTIVE_QUES = ACTIVE_QUES+1 #increment active question
            self.initializeQuestion()   #init a new question


    #event binded to wrong choice buttons
    #it updates the wrong button (red background and disable)
    def WrongChoice(self,event):
        #print("Wrong Choice")
        global CORRECT_AT_1ST_ATTEMPT
        #mark this question won't be counted as correct at 1st attempt
        #since a wrong answer is given.
        CORRECT_AT_1ST_ATTEMPT = 0 
        #change the background of selected wrong choice to red and disable
        #it to prevent reselection
        obj = event.GetEventObject()
        buttonName = obj.GetName()
        if buttonName == '0':
            self.buttonA.SetBackgroundColour(self.wrongColor)
            self.buttonA.Disable()
        elif buttonName == '1':
            self.buttonB.SetBackgroundColour(self.wrongColor)
            self.buttonB.Disable()
        elif buttonName == '2':
            self.buttonC.SetBackgroundColour(self.wrongColor)
            self.buttonC.Disable()
        elif buttonName == '3':
            self.buttonD.SetBackgroundColour(self.wrongColor)
            self.buttonD.Disable()
        elif buttonName == '4':
            self.buttonE.SetBackgroundColour(self.wrongColor)
            self.buttonE.Disable()
        elif buttonName == '5':
            self.buttonF.SetBackgroundColour(self.wrongColor)
            self.buttonF.Disable()
        elif buttonName == '6':
            self.buttonG.SetBackgroundColour(self.wrongColor)
            self.buttonG.Disable()
        elif buttonName == '7':
            self.buttonH.SetBackgroundColour(self.wrongColor)
            self.buttonH.Disable()
        else:
            print("Button Name not Defined! UNEXPECTED ERROR!!!")

        
    #event binded to start button
    def OnStart(self,event):
        global ACTIVE_QUES
        global SCORE
        #reset globals
        SCORE = 0
        ACTIVE_QUES = 1
        #disable left menu items
        self.startbutton.Disable()
        #self.editques.Disable()
        #self.gametype.Disable()
        #self.numcho.Disable()
        #enable all buttons
        self.allButtonsEnable()
        self.logger.AppendText("Quiz is starting!!!\n")
        #process database 
        self.logger.AppendText("Processing database\n")
        processDatabase()
        self.logger.AppendText("Database processed\n")
        #print quiz parameters
        self.logger.AppendText("Quiz is started with %d questions\n" %MAX_QUES)
        if GAME_TYPE == 0:
            gametypestr = 'Painter'
        else:
            gametypestr = 'Painting'
        self.logger.AppendText("Quiz type is 'Find the %s'\n" %gametypestr)
        #initialize first question
        self.initializeQuestion()
       
            
    #not working yet    
    def OnCloseWindow(self,event):
        key = event.GetKeyCode() 
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Are you sure to quit?', 'Question', 
                                       wx.YES_NO | wx.NO_DEFAULT, self)
            if ret == wx.YES:
                print('Escape char!')
                self.Close()

    
#function to process the question database as the beginngin of the program.
#returns a dictionary 
def processDatabase():
    #dbdd = {}    #create empty dictionary
    global MAX_NUM
    #print("Opening database file")
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
    MAX_NUM = len(dbd)   #length of database
    return dbd

#function to draw an image from paint_no
def draw_image(paint_no):
    long_file_name = '0000'+str(paint_no)
    file_location = 'image/' + long_file_name[-4:] + '.jpg'
    image = wx.Image(file_location, wx.BITMAP_TYPE_ANY)
    [width, heigth] = image_rescale(image)
    image.Rescale(width, heigth)
    return wx.BitmapFromImage(image)
    
#function to determine the width and height of image. Image width and height
#should be maximum to fit in rectangle IMAGE_WIDTH x IMAGE_HEIGHT
def image_rescale(image):
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    img_width = image.GetWidth()
    img_height = image.GetHeight()
    aspect_ratio = (1.0*img_width)/img_height
    if aspect_ratio > (1.0*IMAGE_WIDTH)/IMAGE_HEIGHT:
        #image is wide
        width = IMAGE_WIDTH
        heigth = int((1.0*IMAGE_WIDTH)/aspect_ratio)
    else:   #image is long
        heigth = IMAGE_HEIGHT
        width =  int(1.0*IMAGE_HEIGHT*aspect_ratio)
    #print("---Original size= %d x %d, scaled size= %d x %d" 
    #                        %(img_width, img_height, width, heigth))
    return [width, heigth]
    
       

def main():
    app = wx.App(False)
    TopGUI(None, wx.ID_ANY, "Painting Quiz") #wx.Frame(Parent, Id, Title)     
    app.MainLoop()
    del(app)

if __name__ == '__main__':
    main()  