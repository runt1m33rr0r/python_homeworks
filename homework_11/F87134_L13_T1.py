from urllib import urlopen
import wx
import wx.html


page = urlopen('http://rss.slashdot.org/slashdot/slashdot')

titles = []
descriptions = []


def parse_tag(line, tag, closing_tag):
    if tag in line:
        left = line.find(tag) + len(tag)
        right = line.find(closing_tag)
        res = line[left + 1:right]

        return res

    return


in_item = False
for line in page:
    if '<item' in line and '<items' not in line:
        in_item = True
    if '</item>' in line and '</items>' not in line:
        in_item = False

    if in_item:
        title = parse_tag(line, '<title', '</title>')
        if title:
            titles.append(title)

        description = parse_tag(line, '<description', '</description>')
        if description:
            descriptions.append(description)


class Interface(object):
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None, title='RSS', size=(600, 540), style=wx.CLOSE_BOX | wx.SYSTEM_MENU)
        self.panel = wx.Panel(self.frame)
        self.listbox = wx.ListBox(self.panel, choices=titles)
        self.listbox.Bind(wx.EVT_LISTBOX, self.on_listbox_click)

        self.html_window = wx.html.HtmlWindow(self.panel, size=(600, 200))
        self.set_description(0)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.listbox, flag=wx.ALIGN_CENTER)
        self.sizer.AddSpacer(50)
        self.sizer.Add(self.html_window, flag=wx.ALIGN_CENTER)

        self.panel.SetSizer(self.sizer)
        self.panel.Layout()
        self.frame.Show()
        self.app.MainLoop()

    def set_description(self, idx):
        self.html_window.SetPage('<html><body>{}</body></html>'.format(descriptions[idx]))

    def on_listbox_click(self, ev):
        selected = self.listbox.GetSelection()

        if selected != wx.NOT_FOUND:
            self.set_description(selected)


interface = Interface()