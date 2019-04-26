import wx


class Program:
    def __init__(self):      
        self.app = wx.App()
        self.frame = wx.Frame(None, title='BMI', size=(400, 400), style=wx.CLOSE_BOX | wx.SYSTEM_MENU)
        self.panel = wx.Panel(self.frame)

        self.heading = wx.StaticText(self.panel, label='Body Mass Index')
        self.weight_text = wx.StaticText(self.panel, label='weight:')
        self.weight_ctrl = wx.SpinCtrl(self.panel, min=0, max=1000)
        self.height_text = wx.StaticText(self.panel, label='height:')
        self.height_ctrl = wx.SpinCtrl(self.panel, min=0, max=1000)
        self.result_text = wx.StaticText(self.panel, label='result:')
        self.result = wx.StaticText(self.panel, label='0')

        self.compute_button = wx.Button(self.panel, label='Compute')
        self.close_button = wx.Button(self.panel, label='Close')

        self.close_button.Bind(wx.EVT_BUTTON, self.on_close_press)
        self.compute_button.Bind(wx.EVT_BUTTON, self.on_compute_press)

        self.grid_sizer = wx.GridSizer(rows=4, cols=2, hgap=10, vgap=30)
        self.grid_sizer.Add(self.weight_text)
        self.grid_sizer.Add(self.weight_ctrl)
        self.grid_sizer.Add(self.height_text)
        self.grid_sizer.Add(self.height_ctrl)
        self.grid_sizer.Add(self.result_text)
        self.grid_sizer.Add(self.result)
        self.grid_sizer.Add(self.compute_button, flag=wx.ALIGN_CENTER)
        self.grid_sizer.Add(self.close_button, flag=wx.ALIGN_CENTER)

        self.edge_spacing = 30
        self.content_spacing = 50

        self.content = wx.BoxSizer(wx.VERTICAL)
        self.content.AddSpacer(self.edge_spacing)
        self.content.Add(self.heading, flag=wx.ALIGN_LEFT)
        self.content.AddSpacer(self.content_spacing)
        self.content.Add(self.grid_sizer, flag=wx.ALIGN_LEFT)

        self.main = wx.BoxSizer(wx.HORIZONTAL)
        self.main.AddSpacer(self.edge_spacing)
        self.main.Add(self.content)

        self.panel.SetSizer(self.main)
        self.panel.Layout()

        self.frame.Show()
        self.app.MainLoop()


    def on_close_press(self, ev):
        self.frame.Close()


    def on_compute_press(self, ev):
        weight = float(self.weight_ctrl.GetValue())
        height = float(self.height_ctrl.GetValue())
        height_meters = height / 100.0

        if height_meters > 0:
            self.result.SetLabel(str(weight / (height_meters * height_meters)))


program = Program()