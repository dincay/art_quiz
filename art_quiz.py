import wx
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # sizers
        #main sizer
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        #vertical sizer
        ver_grid = wx.GridBagSizer(hgap=1, vgap=6)

        # game title
        self.quotename = wx.StaticText(self, label="Dincay Akcoren")
        ver_grid.Add(self.quotename, pos=(0,0))
        self.quotetitle = wx.StaticText(self, label="ART TEST")
        ver_grid.Add(self.quotetitle, pos=(1,0))
        
        # number of questions
        self.lblques = wx.StaticText(self, label="# of question: ")
        ver_grid.Add(self.lblques, pos=(2,0))
        self.sampleList = ['10', '20', '30']
        self.editques = wx.ComboBox(self, size=(60, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        ver_grid.Add(self.editques, pos=(2,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editques)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.editques)
        
        # game type
        radioList = ['Guess the Painter', 'Guess the Painting']
        gametype = wx.RadioBox(self, label="Game Type", choices=radioList, majorDimension=1, style=wx.RA_SPECIFY_COLS)
        ver_grid.Add(gametype, pos=(3,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, gametype)
        
        # start button
        self.startbutton =wx.Button(self, label="START")
        ver_grid.Add(self.startbutton, pos=(4,0), span=(1,2))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.startbutton)

        # logger
        self.logger = wx.TextCtrl(self, size=(160,200), style=wx.TE_MULTILINE | wx.TE_READONLY)
        ver_grid.Add(self.logger, pos=(5,0), span=(1,2))
        
        #main sizer
        mainSizer.Add(ver_grid, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        

    #call events
    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()


app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
del(app)