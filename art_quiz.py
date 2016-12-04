import wx
class TopGUI(wx.Frame):
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
        editques = wx.ComboBox(self, size=(60, -1), choices=sampleList, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        ver_grid.Add(editques, pos=(2,1))
        editques.Bind(wx.EVT_COMBOBOX, self.EvtComboBox)
        editques.Bind(wx.EVT_TEXT, self.EvtText)
        
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
        self.buttonA = wx.ToggleButton(self, label="A- ")
        choice_grid.Add(self.buttonA, pos=(0,0))
        self.buttonA.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonB = wx.ToggleButton(self, label="B- ")
        choice_grid.Add(self.buttonB, pos=(0,1))
        self.buttonB.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonC = wx.ToggleButton(self, label="C- ")
        choice_grid.Add(self.buttonC, pos=(1,0))
        self.buttonC.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonD = wx.ToggleButton(self, label="D- ")
        choice_grid.Add(self.buttonD, pos=(1,1))
        self.buttonD.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonE = wx.ToggleButton(self, label="E- ")
        choice_grid.Add(self.buttonE, pos=(2,0))
        self.buttonE.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonF = wx.ToggleButton(self, label="F- ")
        choice_grid.Add(self.buttonF, pos=(2,1))
        self.buttonF.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonG = wx.ToggleButton(self, label="G- ")
        choice_grid.Add(self.buttonG, pos=(3,0))
        self.buttonG.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        self.buttonH = wx.ToggleButton(self, label="H- ")
        choice_grid.Add(self.buttonH, pos=(3,1))
        self.buttonH.Bind(wx.EVT_TOGGLEBUTTON, self.OnChoice)
        
        
        #main sizer
        mainSizer.Add(ver_grid, pos=(0,0), span=(2,1),
                      flag=wx.ALIGN_RIGHT|wx.ALL, border=10)
        mainSizer.Add(choice_grid, pos=(1,1),
                      flag=wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizerAndFit(mainSizer)
        
        #panel to close the application with ESC key
              
        #pnl.SetFocus()
        self.Bind(wx.EVT_KEY_DOWN, self.OnCloseWindow)
        
        self.SetSize((400, 600))
        self.Show(True)

    #call events
    def EvtRadioBox1(self, event):
        self.logger.AppendText('EvtRadioBox1: %d\n' % event.GetInt())
    def EvtRadioBox2(self, event):
        self.logger.AppendText('EvtRadioBox2: %d\n' % event.GetInt())
        if(event.GetInt() == 0):    #4 choices
            print('4 choices')
            self.quotename.SetLabel('4 choi')
            self.buttonE.Hide()
            self.buttonF.Hide()
            self.buttonG.Hide()
            self.buttonH.Hide()
            #self.quotename.SetLabel('4 choi')
        elif(event.GetInt() == 1):    #6 choices
            print('6 choices')
            self.buttonE.Show()
            self.buttonF.Show()
            self.buttonG.Hide()
            self.buttonH.Hide()
        elif(event.GetInt() == 2):    #8 choices
            print('8 choices')
            self.buttonE.Show()
            self.buttonF.Show()
            self.buttonG.Show()
            self.buttonH.Show()
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def OnChoice(self,event):
        obj = event.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            self.logger.AppendText("Pressed, Id %d\n" %event.GetId())
        else:
            self.logger.AppendText("De-Pressed, Id %d\n" %event.GetId())
        
        dummyfunc(event.GetId())
    def OnCloseWindow(self,event):
        key = event.GetKeyCode() 
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Are you sure to quit?', 'Question', 
                                       wx.YES_NO | wx.NO_DEFAULT, self)
            if ret == wx.YES:
                print('Escape char!')
                self.Close()
                

def dummyfunc(x):
    ss = "Dummy func " + str(x)
    print ss

def main():
    app = wx.App(False)
    TopGUI(None, wx.ID_ANY, "Painting Quiz") #wx.Frame(Parent, Id, Title)     
    app.MainLoop()
    del(app)

if __name__ == '__main__':
    main()  