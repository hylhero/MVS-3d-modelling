#Boa:Dialog:Dialog1

import wx
import wx.lib.filebrowsebutton

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1DIRBROWSEBUTTON1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(506, 302), size=wx.Size(400, 250),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(384, 212))

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_DIALOG1DIRBROWSEBUTTON1,
              labelText='Select a directory:', newDirectory=False, parent=self,
              pos=wx.Point(96, 72), size=wx.Size(296, 48),
              startDirectory=u'C:\\3d-Model\\bin', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetValue(u'C:\\')
        self.dirBrowseButton1.SetLabel(u'Select a directory:')

    def __init__(self, parent):
        self._init_ctrls(parent)
