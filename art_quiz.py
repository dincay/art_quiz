import wx
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

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
        self.lblques = wx.StaticText(self, label="# of question: ")
        ver_grid.Add(self.lblques, pos=(2,0))
        self.sampleList = ['10', '20', '30']
        self.editques = wx.ComboBox(self, size=(60, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        ver_grid.Add(self.editques, pos=(2,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editques)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.editques)
        
        # game type
        radioList1 = ['Guess the Painter', 'Guess the Painting']
        gametype = wx.RadioBox(self, label="Game Type", choices=radioList1, majorDimension=1, style=wx.RA_SPECIFY_COLS)
        ver_grid.Add(gametype, pos=(3,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox1, gametype)
        
        # number of choices
        radioList2 = ['4', '6', '8']
        numcho = wx.RadioBox(self, label="Number of Choices", choices=radioList2, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        ver_grid.Add(numcho, pos=(4,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox2, numcho)
        
        # start button
        self.startbutton =wx.Button(self, label="START", size=(150, 60))
        ver_grid.Add(self.startbutton, pos=(5,0), span=(1,2), flag=wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.startbutton)
        
        # logger
        self.logger = wx.TextCtrl(self, size=(160,200), style=wx.TE_MULTILINE | wx.TE_READONLY)
        ver_grid.Add(self.logger, pos=(6,0), span=(1,2))
        
        
        #choice buttons
        self.buttonA =wx.Button(self, label="A- ")
        choice_grid.Add(self.buttonA, pos=(0,0))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonA)
        
        self.buttonB =wx.Button(self, label="B- ")
        choice_grid.Add(self.buttonB, pos=(0,1))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonB)
        
        self.buttonC =wx.Button(self, label="C- ")
        choice_grid.Add(self.buttonC, pos=(1,0))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonC)
        
        self.buttonD =wx.Button(self, label="D- ")
        choice_grid.Add(self.buttonD, pos=(1,1))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonD)
        
        self.buttonE =wx.Button(self, label="E- ")
        choice_grid.Add(self.buttonE, pos=(2,0))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonE)
        
        self.buttonF =wx.Button(self, label="F- ")
        choice_grid.Add(self.buttonF, pos=(2,1))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonF)
        
        self.buttonG =wx.Button(self, label="G- ")
        choice_grid.Add(self.buttonG, pos=(3,0))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonG)
        
        self.buttonH =wx.Button(self, label="H- ")
        choice_grid.Add(self.buttonH, pos=(3,1))
        self.Bind(wx.EVT_BUTTON, self.OnChoice,self.buttonH)
        
        
        #main sizer
        mainSizer.Add(ver_grid, pos=(0,0), span=(2,1),
                      flag=wx.ALIGN_RIGHT|wx.ALL, border=10)
        mainSizer.Add(choice_grid, pos=(1,1),
                      flag=wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizerAndFit(mainSizer)
        
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        

    #call events
    def EvtRadioBox1(self, event):
        self.logger.AppendText('EvtRadioBox1: %d\n' % event.GetInt())
    def EvtRadioBox2(self, event):
        self.logger.AppendText('EvtRadioBox2: %d\n' % event.GetInt())
        if(event.GetInt() == 0):    #4 choices
            print('4 choices')
            #self.buttonE.Show(False)
            #self.ButtonF.Show(False)
            #self.ButtonG.Show(False)
            #self.ButtonH.Show(False)
            self.quotename.SetLabel('4 choi')
        elif(event.GetInt() == 1):    #6 choices
            print('6 choices')
            self.ButtonE.Show()
            self.ButtonF.Show()
            self.ButtonG.Hide()
            self.ButtonH.Hide()
        elif(event.GetInt() == 2):    #8 choices
            print('8 choices')
            self.ButtonE.Show()
            self.ButtonF.Show()
            self.ButtonG.Show()
            self.ButtonH.Show()
            
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def OnChoice(self,event):
        self.logger.AppendText(" Choice Id %d\n" %event.GetId())
        dummyfunc(event.GetId())
    def OnCloseWindow(self,event):
        print('Exiting')
        self.Destroy()

def dummyfunc(x):
    ss = "Dummy func " + str(x)
    print ss

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Painting Quiz", size=(400, 600)) #wx.Frame(Parent, Id, Title)
panel = ExamplePanel(frame)
frame.Show(True) 
app.MainLoop()
del(app)