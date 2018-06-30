#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import Dialog
import Frame

modules ={u'Dialog': [0, '', u'Dialog.py'],
 u'Frame': [1, 'Main frame of Application', u'Frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
