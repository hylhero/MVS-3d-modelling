#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Frame4

modules ={'Frame4': [1, 'Main frame of Application', u'Frame4.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame4.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
