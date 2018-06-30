#Boa:Frame:homeFrame

import wx
import time
import wx.richtext
import wx.lib.filebrowsebutton
import os
import zipfile
import time
import Dialog
import loadproject
import subprocess
from PIL import Image
import sys
import getopt
from glob import glob
wrk_drr=os.getcwd()
draw_flag=0
flagbrowse=True
flagshow=True
path = ""
projName2 = ""
proceed_flag=0
calib_flag=0
gauge_value=0

def create(parent):
    return homeFrame(parent)

[wxID_HOMEFRAME, wxID_HOMEFRAMEABORT, wxID_HOMEFRAMEALLTOGETHER, 
 wxID_HOMEFRAMEBITMAPBUTTON1, wxID_HOMEFRAMEBITMAPBUTTON2, 
 wxID_HOMEFRAMEBITMAPBUTTON3, wxID_HOMEFRAMEBITMAPBUTTON4, 
 wxID_HOMEFRAMEBITMAPBUTTON5, wxID_HOMEFRAMEBROWSEFILES, 
 wxID_HOMEFRAMEBROWSE_CALIB, wxID_HOMEFRAMEBUTTON1, wxID_HOMEFRAMEBUTTON3, 
 wxID_HOMEFRAMEBUTTON4, wxID_HOMEFRAMEBUTTON5, wxID_HOMEFRAMECALIBRATION, 
 wxID_HOMEFRAMECALIB_GAUGE, wxID_HOMEFRAMECANNY, wxID_HOMEFRAMECHANGE, 
 wxID_HOMEFRAMECOMBO_BOX_SENSE, wxID_HOMEFRAMECONTOUR, wxID_HOMEFRAMECROP, 
 wxID_HOMEFRAMEDIRBROWSEBUTTON1, wxID_HOMEFRAMEDIRBROWSEBUTTON2, 
 wxID_HOMEFRAMEDIRBROWSEBUTTON3, wxID_HOMEFRAMEDIRBROWSEBUTTON4, 
 wxID_HOMEFRAMEDRAWBUILD, wxID_HOMEFRAMEFILEBROWSEBUTTON1, 
 wxID_HOMEFRAMEFINISH, wxID_HOMEFRAMEFOOTPRINTEX, wxID_HOMEFRAMEFOOTPROCESS, 
 wxID_HOMEFRAMEFOOTPROCESSGAUGE, wxID_HOMEFRAMEHEIGHT, 
 wxID_HOMEFRAMEMASKINGTEXT, wxID_HOMEFRAMEMASK_BUTTON, wxID_HOMEFRAMEMM, 
 wxID_HOMEFRAMENEWBUILDING, wxID_HOMEFRAMENOTEBOOK1, wxID_HOMEFRAMENOT_FOUND, 
 wxID_HOMEFRAMEONEBYONE, wxID_HOMEFRAMEOPENPOINTCLOUD, wxID_HOMEFRAMEPANEL1, 
 wxID_HOMEFRAMEPANEL2, wxID_HOMEFRAMEPANEL3, wxID_HOMEFRAMEPANEL4, 
 wxID_HOMEFRAMEPANEL5, wxID_HOMEFRAMEPLACEMARK, wxID_HOMEFRAMEPROCEED, 
 wxID_HOMEFRAMERESULT, wxID_HOMEFRAMERICHTEXTCTRL1, 
 wxID_HOMEFRAMERICHTEXTCTRL2, wxID_HOMEFRAMESEGMENT, 
 wxID_HOMEFRAMESEGMENTATION, wxID_HOMEFRAMESENSE, wxID_HOMEFRAMESENSORBUTTON, 
 wxID_HOMEFRAMESHOW, wxID_HOMEFRAMESTATUSBAR, wxID_HOMEFRAMETEXTCTRL1, wxID_HOMEFRAMEHELPABOUT, 
 wxID_HOMEFRAMEVISUALISEGAUGE, wxID_HOMEFRAMEVISUALISEGE, 
] = [wx.NewId() for _init_ctrls in range(60)]

[wxID_HOMEFRAMEABOUT, wxID_HOMEFRAMEHELPHELP, 
] = [wx.NewId() for _init_coll_Help_Items in range(2)]

[wxID_HOMEFRAMEFILEEXIT, wxID_HOMEFRAMEFILELOADPROJ, wxID_HOMEFRAMEFILENEW, 
] = [wx.NewId() for _init_coll_File_Items in range(3)]

[wxID_HOMEFRAMETIMER] = [wx.NewId() for _init_utils in range(1)]

class homeFrame(wx.Frame):
    def _init_coll_MenuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.File, title=u'File')
        parent.Append(menu=self.Help, title=u'Help')

    def _init_coll_File_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Make New Project', id=wxID_HOMEFRAMEFILENEW,
              kind=wx.ITEM_NORMAL, text=u'New Project')
        parent.Append(help='', id=wxID_HOMEFRAMEFILELOADPROJ,
              kind=wx.ITEM_NORMAL, text=u'Load Project')
        parent.Append(help=u'Exit Application', id=wxID_HOMEFRAMEFILEEXIT,
              kind=wx.ITEM_NORMAL, text=u'Exit')
        self.Bind(wx.EVT_MENU, self.OnFileNewMenu, id=wxID_HOMEFRAMEFILENEW)
        self.Bind(wx.EVT_MENU, self.OnFileExitMenu, id=wxID_HOMEFRAMEFILEEXIT)
        self.Bind(wx.EVT_MENU, self.OnFileLoadprojMenu,
              id=wxID_HOMEFRAMEFILELOADPROJ)

    def _init_coll_Help_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'App Help', id=wxID_HOMEFRAMEHELPHELP,
              kind=wx.ITEM_NORMAL, text=u'Help')
        parent.Append(help=u'About App', id=wxID_HOMEFRAMEHELPABOUT,
              kind=wx.ITEM_NORMAL, text=u'About')
        self.Bind(wx.EVT_MENU, self.OnHelpHelpMenu, id=wxID_HOMEFRAMEHELPHELP)
        self.Bind(wx.EVT_MENU, self.OnHelpAboutMenu, id=wxID_HOMEFRAMEHELPABOUT)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text=u'CameraCalibration')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'PointCloudGeneration')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text=u'Segmentation and Masking')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text=u'Height Extraction')
        parent.AddPage(imageId=-1, page=self.panel5, select=True,
              text=u'3dModelGeneration')

    def _init_coll_StatusBar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'Status')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.File = wx.Menu(title=u'')

        self.Help = wx.Menu(title=u'')

        self.MenuBar = wx.MenuBar()
        self.MenuBar.SetClientSize(wx.Size(196353888, 503523728))

        self.timer = wx.Timer(id=wxID_HOMEFRAMETIMER, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimerTimer, id=wxID_HOMEFRAMETIMER)

        self._init_coll_File_Items(self.File)
        self._init_coll_Help_Items(self.Help)
        self._init_coll_MenuBar_Menus(self.MenuBar)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_HOMEFRAME, name=u'homeFrame',
              parent=prnt, pos=wx.Point(238, 252), size=wx.Size(936, 639),
              style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX,
              title=u'Welcome to 3-D Street View v1.0(alpha)')
        self._init_utils()
        self.SetClientSize(wx.Size(920, 601))
        self.SetMenuBar(self.MenuBar)
        self.Center(wx.BOTH)

        self.StatusBar = wx.StatusBar(id=wxID_HOMEFRAMESTATUSBAR,
              name=u'StatusBar', parent=self, style=0)
        self.StatusBar.SetToolTipString(u'StatusBar')
        self._init_coll_StatusBar_Fields(self.StatusBar)
        self.SetStatusBar(self.StatusBar)

        self.notebook1 = wx.Notebook(id=wxID_HOMEFRAMENOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(920, 558), style=0)

        self.panel1 = wx.Panel(id=wxID_HOMEFRAMEPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Enable(True)
        self.panel1.SetToolTipString(u'panel1')

        self.panel2 = wx.Panel(id=wxID_HOMEFRAMEPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_HOMEFRAMEPANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wx.Panel(id=wxID_HOMEFRAMEPANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.panel5 = wx.Panel(id=wxID_HOMEFRAMEPANEL5, name='panel5',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.newBuilding = wx.Button(id=wxID_HOMEFRAMENEWBUILDING,
              label=u'Add New Building', name=u'newBuilding',
              parent=self.panel5, pos=wx.Point(32, 32), size=wx.Size(168, 48),
              style=0)
        self.newBuilding.Bind(wx.EVT_BUTTON, self.OnNewBuildingButton,
              id=wxID_HOMEFRAMENEWBUILDING)

        self.FootprintEx = wx.Button(id=wxID_HOMEFRAMEFOOTPRINTEX,
              label=u'Footprint Extraction', name=u'FootprintEx',
              parent=self.panel5, pos=wx.Point(288, 80), size=wx.Size(160, 48),
              style=0)
        self.FootprintEx.Enable(False)
        self.FootprintEx.Bind(wx.EVT_BUTTON, self.OnFootprintExButton,
              id=wxID_HOMEFRAMEFOOTPRINTEX)

        self.footprocess = wx.Button(id=wxID_HOMEFRAMEFOOTPROCESS,
              label=u'Footprint Processing', name=u'footprocess',
              parent=self.panel5, pos=wx.Point(296, 320), size=wx.Size(160, 48),
              style=0)
        self.footprocess.Enable(False)
        self.footprocess.Bind(wx.EVT_BUTTON, self.OnFootprocessButton,
              id=wxID_HOMEFRAMEFOOTPROCESS)

        self.drawbuild = wx.Button(id=wxID_HOMEFRAMEDRAWBUILD,
              label=u'Construct Building(s)', name=u'drawbuild',
              parent=self.panel5, pos=wx.Point(296, 400), size=wx.Size(160, 48),
              style=0)
        self.drawbuild.Enable(False)
        self.drawbuild.Bind(wx.EVT_BUTTON, self.OnDrawbuildButton,
              id=wxID_HOMEFRAMEDRAWBUILD)

        self.visualiseGE = wx.Button(id=wxID_HOMEFRAMEVISUALISEGE,
              label=u'Visualise on Geo Portal', name=u'visualiseGE',
              parent=self.panel5, pos=wx.Point(296, 480), size=wx.Size(160, 50),
              style=0)
        self.visualiseGE.Enable(True)
        self.visualiseGE.Bind(wx.EVT_BUTTON, self.OnVisualiseGEButton,
              id=wxID_HOMEFRAMEVISUALISEGE)

        self.oneBYone = wx.RadioButton(id=wxID_HOMEFRAMEONEBYONE,
              label=u': Draw Buildings One by One', name=u'oneBYone',
              parent=self.panel5, pos=wx.Point(288, 160), size=wx.Size(224, 13),
              style=0)
        self.oneBYone.SetValue(False)
        self.oneBYone.Enable(False)
        self.oneBYone.Bind(wx.EVT_RADIOBUTTON, self.OnOneBYoneRadiobutton,
              id=wxID_HOMEFRAMEONEBYONE)

        self.allTogether = wx.RadioButton(id=wxID_HOMEFRAMEALLTOGETHER,
              label=u': Draw All Buildings Together', name=u'allTogether',
              parent=self.panel5, pos=wx.Point(288, 192), size=wx.Size(224, 13),
              style=0)
        self.allTogether.SetValue(False)
        self.allTogether.Enable(False)
        self.allTogether.Bind(wx.EVT_RADIOBUTTON, self.OnAllTogetherRadiobutton,
              id=wxID_HOMEFRAMEALLTOGETHER)

        self.footprocessgauge = wx.Gauge(id=wxID_HOMEFRAMEFOOTPROCESSGAUGE,
              name=u'footprocessgauge', parent=self.panel5, pos=wx.Point(480,
              328), range=100, size=wx.Size(256, 28), style=wx.GA_HORIZONTAL)
        self.footprocessgauge.Enable(False)

        self.visualisegauge = wx.Gauge(id=wxID_HOMEFRAMEVISUALISEGAUGE,
              name=u'visualisegauge', parent=self.panel5, pos=wx.Point(480,
              488), range=100, size=wx.Size(264, 28), style=wx.GA_HORIZONTAL)
        self.visualisegauge.Enable(False)

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON1,
              labelText='Select a directory:', newDirectory=False,
              parent=self.panel5, pos=wx.Point(288, 232), size=wx.Size(440, 48),
              startDirectory=u'C:\\3d-Model\\projects',
              toolTip='Type directory name or browse to select')
        
        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_HOMEFRAMERICHTEXTCTRL1,
              parent=self.panel5, pos=wx.Point(24, 152), size=wx.Size(184, 384),
              style=wx.richtext.RE_MULTILINE, value=u'Progress Updates....')
        self.richTextCtrl1.SetEditable(False)
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetInsertionPoint(0)

        self.Segmentation = wx.Button(id=wxID_HOMEFRAMESEGMENTATION,
              label=u'Select Image', name=u'Segmentation', parent=self.panel3,
              pos=wx.Point(59, 12), size=wx.Size(272, 40), style=10)
        self.Segmentation.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Segmentation.Bind(wx.EVT_BUTTON, self.OnSegmentationButton,
              id=wxID_HOMEFRAMESEGMENTATION)

        self.browsefiles = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_HOMEFRAMEBROWSEFILES, initialValue='',
              labelText=u'Select Picture', parent=self.panel3, pos=wx.Point(44,
              69), size=wx.Size(296, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.browsefiles.Enable(False)
        self.browsefiles.SetName(u'browsefiles')
        self.browsefiles.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.show = wx.Button(id=wxID_HOMEFRAMESHOW, label=u'Show Image----->',
              name=u'show', parent=self.panel3, pos=wx.Point(59, 135),
              size=wx.Size(270, 40), style=0)
        self.show.Enable(False)
        self.show.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.show.Bind(wx.EVT_BUTTON, self.OnShowButton, id=wxID_HOMEFRAMESHOW)

        self.change = wx.Button(id=wxID_HOMEFRAMECHANGE, label=u'Change Image',
              name=u'change', parent=self.panel3, pos=wx.Point(32, 286),
              size=wx.Size(128, 31), style=0)
        self.change.Enable(False)
        self.change.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.change.Bind(wx.EVT_BUTTON, self.OnChangeButton,
              id=wxID_HOMEFRAMECHANGE)

        self.proceed = wx.Button(id=wxID_HOMEFRAMEPROCEED,
              label=u'Proceed---->', name=u'proceed', parent=self.panel3,
              pos=wx.Point(277, 286), size=wx.Size(128, 31), style=0)
        self.proceed.Enable(False)
        self.proceed.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.proceed.Bind(wx.EVT_BUTTON, self.OnProceedButton,
              id=wxID_HOMEFRAMEPROCEED)

        self.abort = wx.Button(id=wxID_HOMEFRAMEABORT, label=u'Abort',
              name=u'abort', parent=self.panel3, pos=wx.Point(568, 488),
              size=wx.Size(128, 31), style=0)
        self.abort.Enable(False)
        self.abort.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.abort.Bind(wx.EVT_BUTTON, self.OnAbortButton,
              id=wxID_HOMEFRAMEABORT)

        self.finish = wx.Button(id=wxID_HOMEFRAMEFINISH, label=u'Finish!',
              name=u'finish', parent=self.panel3, pos=wx.Point(750, 488),
              size=wx.Size(128, 31), style=0)
        self.finish.Enable(False)
        self.finish.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.finish.Bind(wx.EVT_BUTTON, self.OnFinishButton,
              id=wxID_HOMEFRAMEFINISH)

        self.canny = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\Cannyedge_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMECANNY,
              name=u'canny', parent=self.panel3, pos=wx.Point(6, 344),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.contour = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\contour_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMECONTOUR,
              name=u'contour', parent=self.panel3, pos=wx.Point(231, 344),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.segment = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\segment_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMESEGMENT,
              name=u'segment', parent=self.panel3, pos=wx.Point(463, 343),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.crop = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\image_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMECROP,
              name=u'crop', parent=self.panel3, pos=wx.Point(685, 344),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.mask_button = wx.Button(id=wxID_HOMEFRAMEMASK_BUTTON,
              label=u'Masking', name=u'mask_button', parent=self.panel3,
              pos=wx.Point(136, 224), size=wx.Size(120, 32), style=0)
        self.mask_button.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.mask_button.Enable(False)
        self.mask_button.Bind(wx.EVT_BUTTON, self.OnMask_buttonButton,
              id=wxID_HOMEFRAMEMASK_BUTTON)

        self.maskingText = wx.StaticText(id=wxID_HOMEFRAMEMASKINGTEXT,
              label=u'Click the button if you want to mask this photo',
              name=u'maskingText', parent=self.panel3, pos=wx.Point(91, 200),
              size=wx.Size(224, 13), style=0)

        self.dirBrowseButton2 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON2,
              labelText=u'Select directory for photos', newDirectory=False,
              parent=self.panel2, pos=wx.Point(112, 72), size=wx.Size(560, 48),
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')

        self.textCtrl1 = wx.TextCtrl(id=wxID_HOMEFRAMETEXTCTRL1,
              name='textCtrl1', parent=self.panel2, pos=wx.Point(128, 33),
              size=wx.Size(528, 40), style=0, value=u'enterBundleOutputPath')
        self.textCtrl1.Show(False)

        self.dirBrowseButton3 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON3,
              labelText=u'Select directory for saving point_clouds:',
              newDirectory=False, parent=self.panel2, pos=wx.Point(112, 144),
              size=wx.Size(560, 48), startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton3.Show(False)

        self.button1 = wx.Button(id=wxID_HOMEFRAMEBUTTON1,
              label=u'Georeference your point_cloud', name='button1',
              parent=self.panel2, pos=wx.Point(192, 144), size=wx.Size(384,
              128), style=0)
        self.button1.Show(False)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_HOMEFRAMEBUTTON1)

        self.button3 = wx.Button(id=wxID_HOMEFRAMEBUTTON3,
              label=u'Start Bundler', name='button3', parent=self.panel2,
              pos=wx.Point(336, 208), size=wx.Size(168, 56), style=0)
        self.button3.Show(True)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_HOMEFRAMEBUTTON3)

        self.button4 = wx.Button(id=wxID_HOMEFRAMEBUTTON4, label=u'Start PMVS',
              name='button4', parent=self.panel2, pos=wx.Point(360, 304),
              size=wx.Size(168, 56), style=0)
        self.button4.Show(False)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_HOMEFRAMEBUTTON4)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON1, name='bitmapButton1',
              parent=self.panel2, pos=wx.Point(80, 384), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton1.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/runbundler_r.png',
              wx.BITMAP_TYPE_PNG))

        self.bitmapButton2 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON2, name='bitmapButton2',
              parent=self.panel2, pos=wx.Point(328, 387), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton2.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/runpmvs_r.png',
              wx.BITMAP_TYPE_PNG))

        self.bitmapButton3 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON3, name='bitmapButton3',
              parent=self.panel2, pos=wx.Point(584, 382), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton3.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/georef_r.png',
              wx.BITMAP_TYPE_PNG))

        self.button5 = wx.Button(id=wxID_HOMEFRAMEBUTTON5,
              label=u'Proceed to georef', name=u'button5', parent=self.panel2,
              pos=wx.Point(384, 504), size=wx.Size(112, 23), style=0)
        self.button5.Show(True)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_HOMEFRAMEBUTTON5)

        self.fileBrowseButton1 = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_HOMEFRAMEFILEBROWSEBUTTON1, initialValue='',
              labelText=u'Select Point Cloud File', parent=self.panel4,
              pos=wx.Point(232, 72), size=wx.Size(432, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')

        self.dirBrowseButton4 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON4,
              labelText=u'Select Directory for Coordinates:',
              newDirectory=False, parent=self.panel4, pos=wx.Point(232, 168),
              size=wx.Size(432, 48), startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton4.Show(False)

        self.OpenPointCloud = wx.Button(id=wxID_HOMEFRAMEOPENPOINTCLOUD,
              label=u'Open Point Cloud', name=u'OpenPointCloud',
              parent=self.panel4, pos=wx.Point(392, 248), size=wx.Size(128, 48),
              style=0)
        self.OpenPointCloud.Bind(wx.EVT_BUTTON, self.OnOpenPointCloudButton,
              id=wxID_HOMEFRAMEOPENPOINTCLOUD)

        self.Height = wx.Button(id=wxID_HOMEFRAMEHEIGHT,
              label=u'Extract Height', name=u'Height', parent=self.panel4,
              pos=wx.Point(400, 312), size=wx.Size(120, 40), style=0)
        self.Height.Show(False)
        self.Height.Bind(wx.EVT_BUTTON, self.OnHeightButton,
              id=wxID_HOMEFRAMEHEIGHT)

        self.bitmapButton4 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON4, name='bitmapButton4',
              parent=self.panel4, pos=wx.Point(152, 368), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton4.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/pickpoints_r.png',
              wx.BITMAP_TYPE_PNG))

        self.bitmapButton5 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON5, name='bitmapButton5',
              parent=self.panel4, pos=wx.Point(544, 368), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton5.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/extractht_r.png',
              wx.BITMAP_TYPE_PNG))

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_HOMEFRAMERICHTEXTCTRL2,
              parent=self.panel1, pos=wx.Point(192, 336), size=wx.Size(472,
              188), style=wx.richtext.RE_MULTILINE,
              value=u'Camera Parameters....')
        self.richTextCtrl2.SetLabel(u'richText')
        self.richTextCtrl2.SetEditable(False)
        self.richTextCtrl2.Enable(False)

        self.result = wx.Button(id=wxID_HOMEFRAMERESULT,
              label=u'Show Results--->', name=u'result', parent=self.panel1,
              pos=wx.Point(224, 256), size=wx.Size(139, 52), style=0)
        self.result.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.result.Enable(False)
        self.result.Bind(wx.EVT_BUTTON, self.OnResultButton,
              id=wxID_HOMEFRAMERESULT)

        self.browse_calib = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEBROWSE_CALIB,
              labelText='Select a directory:', newDirectory=False,
              parent=self.panel1, pos=wx.Point(268, 137), size=wx.Size(304, 48),
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.browse_calib.Enable(False)

        self.calibration = wx.Button(id=wxID_HOMEFRAMECALIBRATION,
              label=u'Select Folder', name=u'calibration', parent=self.panel1,
              pos=wx.Point(336, 38), size=wx.Size(147, 42), style=0)
        self.calibration.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.calibration.Bind(wx.EVT_BUTTON, self.OnCalibrationButton,
              id=wxID_HOMEFRAMECALIBRATION)

        self.calib_gauge = wx.Gauge(id=wxID_HOMEFRAMECALIB_GAUGE,
              name=u'calib_gauge', parent=self.panel1, pos=wx.Point(408, 272),
              range=100, size=wx.Size(260, 28), style=wx.GA_HORIZONTAL)
        self.calib_gauge.Enable(True)

        self.placemark = wx.Button(id=wxID_HOMEFRAMEPLACEMARK,
              label=u'Apply Placemarks', name=u'placemark', parent=self.panel5,
              pos=wx.Point(496, 400), size=wx.Size(128, 40), style=0)
        self.placemark.Bind(wx.EVT_BUTTON, self.OnPlacemarkButton,
              id=wxID_HOMEFRAMEPLACEMARK)

        self.not_found = wx.Button(id=wxID_HOMEFRAMENOT_FOUND,
              label=u'sensor width not found', name=u'not_found',
              parent=self.panel1, pos=wx.Point(40, 184), size=wx.Size(152, 31),
              style=0)
        self.not_found.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.not_found.Enable(True)
        self.not_found.Bind(wx.EVT_BUTTON, self.OnNot_foundButton,
              id=wxID_HOMEFRAMENOT_FOUND)

        self.sense = wx.TextCtrl(id=wxID_HOMEFRAMESENSE, name=u'sense',
              parent=self.panel1, pos=wx.Point(32, 248), size=wx.Size(112, 21),
              style=0, value=u'Enter sensor_width')
        self.sense.SetEditable(False)

        self.mm = wx.StaticText(id=wxID_HOMEFRAMEMM, label=u'mm', name=u'mm',
              parent=self.panel1, pos=wx.Point(150, 253), size=wx.Size(17, 13),
              style=0)
        f=open(r"C:\3d-Model\bin\camera_calibration\camera_database.txt",'r')
        file1=f.readlines()
        self.combo_box_sense = wx.ComboBox(choices=file1,
              id=wxID_HOMEFRAMECOMBO_BOX_SENSE, name=u'combo_box_sense',
              parent=self.panel1, pos=wx.Point(24, 143), size=wx.Size(210, 21),
              style=0, value=u'sensor_width')
        self.combo_box_sense.SetLabel(u'sensor_width')
        self.combo_box_sense.Bind(wx.EVT_COMBOBOX,
              self.OnCombo_box_senseCombobox, id=wxID_HOMEFRAMECOMBO_BOX_SENSE)

        self.sensorButton = wx.Button(id=wxID_HOMEFRAMESENSORBUTTON,
              label=u'Sensor Width Entered', name=u'sensorButton',
              parent=self.panel1, pos=wx.Point(32, 288), size=wx.Size(120, 23),
              style=0)
        self.sensorButton.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.sensorButton.Enable(False)
        self.sensorButton.Bind(wx.EVT_BUTTON, self.OnSensorButtonButton,
              id=wxID_HOMEFRAMESENSORBUTTON)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def unzip(self,path):
        self.visualisegauge.Enable(True)
        os.chdir(path)
        filenames = []
        totalLength=0
        for files in os.listdir("."):
            if files.endswith(".kmz"):
                totalLength +=1
        self.visualisegauge.SetValue(0)       
        self.visualisegauge.SetRange(totalLength)
        count = 0
        for files in os.listdir("."):
            if files.endswith(".kmz"):
                fh = open(files,'rb')
                z = zipfile.ZipFile(fh)
                count += 1
                for name in z.namelist():
                    outpath = path +'\\' + fh.name[:-4]
                    z.extract(name,outpath)
                self.visualisegauge.SetValue(count)
                fh.close()

    def OnHelpHelpMenu(self, event):
        os.chdir(r'C:\3d-Model\docs')
        os.system('COMPLETE_DOCUMENTATION.pdf')
        event.Skip()

    def OnHelpAboutMenu(self, event):
        event.Skip()
        
    def choice(self):
        f=open(r"C:\3d-Model\bin\camera_calibration\camera_database.txt",'r')
        file=f.readlines()
        return file

    def OnFileNewMenu(self, event):
        fd=Dialog.create(self).ShowModal()
        path,projName2 = Dialog.Dialog1.GetValues()
        ##############
        #box=wx.MessageDialog(None,path+projName2,'New Project Name',wx.OK)
        #answer = box.ShowModal()
        #box.Destroy()
        #print path+"\\"+projName2
        os.mkdir(path+"\\"+projName2)
        os.mkdir(path+"\\"+projName2+"\\"+"input")
        os.mkdir(path+"\\"+projName2+"\\"+"output")
        os.chdir(wrk_drr)
        namefile = open('curr_proj.txt','w')
        namefile.write(str(path)+"\\"+str(projName2))
        namefile.close()
        os.chdir(r"C:\3d-Model\bin\database")
        os.system("DemoDatabase.py")
        print "Database Made"
        os.chdir(r"C:\3d-Model\bin\database")
        os.system("App4.py")
        print "add column"
        
        ##############
        fd.EndModal()
        fd.Destroy()
        
        event.Skip()

    def OnFileExitMenu(self, event):
        self.Close()
        event.Skip()
        
    

    def OnVisualiseGEButton(self, event):
        global path
        global projName2
        global wrk_drr
        #path,projName2 = Dialog.Dialog1.GetValues()
        wildcard = "kmz (*.kmz)|*.kmz|"\
           "All files (*.*)|*.*"
##############################################################################################################
        os.chdir(wrk_drr)
        fil = open('curr_proj.txt','r')
        pth = fil.readline()
        dlg = wx.FileDialog(
            self, message="Choose a file",
            #defaultDir=r"C:\pSApp\output", 
            defaultDir=pth+"\\output",  
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
        # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
        
        spaceLength = len(paths)
        
        #path = r'C:\pSApp\output'#####################################################   put project name here
        self.unzip(pth+"\\output")
        
        pathStr = ""
        for i in range(spaceLength):
            paths[i] = (paths[i])[:-4]
            pathStr += " "
            pathStr += paths[i] + '\\doc.kml'
        pathStr += ' '+pth+'\\output\\Placemark.kml'
        try:
            os.chdir(r'C:\Program Files (x86)\Google\Google Earth\client')#################   put local name here
            sys = os.system('googleearth.exe ' + pathStr)
        except:
            os.chdir(r'C:\Program Files\Google\Google Earth\client')
            os.system('googleearth.exe ' + pathStr)
        event.Skip()

    def OnNewBuildingButton(self, event):
        self.allTogether.Enable(True)
        self.oneBYone.Enable(True)
        self.FootprintEx.Enable(True)
        event.Skip()

    def OnFootprintExButton(self, event):
        try:
            os.chdir(r'C:\Program Files (x86)\Google\Google Earth\client')#################   put local name here
            sys = os.system('googleearth.exe')
        except:
            os.chdir(r'C:\Program Files\Google\Google Earth\client')
            os.system('googleearth.exe')
        #abc=subprocess.Popen([sys.executable,r"C:\Users\Kaustubh\Desktop\tryyy.py"])
        event.Skip()

    def OnFootprocessButton(self, event):           ###########put error check ie if user puts 1 dir for footex and does other thing
        global wrk_drr
        self.footprocessgauge.Enable(True)       
        str = self.dirBrowseButton1.GetValue()
        flag = True
        if(len(str) != 0):
##            num = len(wrk_drr)#os.getcwd())
##            if((os.getcwd()[num-12:num]=='3d-modelling')!=True):
##                os.chdir(os.getcwd()+'\\3d-modelling')
##            dr = os.getcwd()
            os.chdir(wrk_drr+'\\3d-modelling')
            fw = open('temp.txt','w')
            str = str.replace("\\", "\\\\" )
            fw.write(str)
            fw.close()
            flag = True
        else:
            box=wx.MessageDialog(None,'Please specify the folder','Warning',wx.OK)
            answer = box.ShowModal()
            box.Destroy()
            flag = False
        
        if(self.oneBYone.GetValue()==True and flag):
            tot_range=1
            t_old=0.0
            t_new=0.0
            self.footprocessgauge.SetValue(0)       
            self.footprocessgauge.SetRange(tot_range)
            
            #os.chdir(r'C:\pSApp\tempFiles')
            os.chdir(wrk_drr+'\\3d-modelling')
            f=open("temp.txt")
            line_count=0
    
            for line in f:
                line_count=line_count+1
                if(line_count==1):
                    l=line
                    for files in os.listdir(l):
                        if files.endswith(".kml"):
                            f_name=files                    
                    t_old=os.path.getmtime(l+'\\\\'+f_name)
                    break
                
            #os.chdir(r'C:\pSApp\execute')
            os.chdir(wrk_drr+'\\3d-modelling')
            os.system('foot_manual.py')
            
            
            t_new=os.path.getmtime(l+'\\\\'+f_name)
            if(t_old==t_new): 
                self.footprocessgauge.SetValue(1)       
            
        if(self.allTogether.GetValue()==True and flag):
            tot_range=0
            t_old=0.0
            t_new=0.0
            self.footprocessgauge.SetValue(0)    
                
            #os.chdir(r'C:\pSApp\tempFiles')
            os.chdir(wrk_drr+'\\3d-modelling')
            f=open("temp.txt")
            line_count=0
    
            for line in f:
                line_count=line_count+1
                if(line_count==1):
                    l=line
                    x=os.listdir(l)
                    iterator=len(os.listdir(l))
                    for i in range(iterator):
                        for files in os.listdir(l+'\\\\'+x[i]):                 
                            if files.endswith(".kml"):
                                tot_range+=1
                    break
                    
            self.footprocessgauge.SetRange(tot_range)

            iterator=len(os.listdir(l))
            for i in range(iterator):
                for files in os.listdir(l+'\\\\'+x[i]):                 
                    if files.endswith(".kml"):
                        f_name=files
                       
                        #os.chdir(r'C:\pSApp\tempFiles')
                        os.chdir(wrk_drr+'\\3d-modelling')
                        fw = open('temp.txt','w')
                        fw.write(l+'\\\\'+x[i])
                        fw.close()
                        
                        t_old=os.path.getmtime(l+'\\\\'+x[i]+'\\\\'+f_name)
                        #os.chdir(r'C:\pSApp\execute')
                        os.chdir(wrk_drr+'\\3d-modelling')
                        os.system('foot_manual.py')
                        t_new=os.path.getmtime(l+'\\\\'+x[i]+'\\\\'+f_name)
                if(t_old<=t_new):
                    self.footprocessgauge.SetValue(i+1)
        event.Skip()

    def OnDrawbuildButton(self, event):
        self.timer.Start(10,False)
        global draw_flag
        draw_flag=1
        str = self.dirBrowseButton1.GetValue()
        flag = True
        if(len(str) != 0):
            os.chdir(wrk_drr+'\\3d-modelling')           
            fw = open('temp.txt','w')
            str = str.replace("\\", "\\\\" )
            fw.write(str)
            fw.close()
            #os.chdir(dr)
            #os.chdir(r"C:\Program Files (x86)\Google\Google SketchUp 8")
            #os.system("SketchUp.exe")
            #subprocess.call("SketchUp.exe")
            os.chdir('.\..\..\\resources\\Google SketchUp 8')
            os.system("SketchUp.exe")
            
        else:
            box=wx.MessageDialog(None,'Please specify the folder','Warning',wx.OK)
            answer = box.ShowModal()
            box.Destroy()
        event.Skip()

    def OnOneBYoneRadiobutton(self, event):
        self.drawbuild.Enable(True)
        self.footprocess.Enable(True)
        event.Skip()

    def OnAllTogetherRadiobutton(self, event):
        self.drawbuild.Enable(True)
        self.footprocess.Enable(True)
        event.Skip()

    def OnTimerTimer(self, event):
        global draw_flag
        global proceed_flag
        global calib_flag
        if (draw_flag==1):
            
            os.chdir(wrk_drr+"\\3d-modelling")###############change
            progressFile = open('temp_for_display.txt','r')
            self.richTextCtrl1.SetValue(progressFile.read())
##################################################################################################            
        if(proceed_flag==1):
            
            print "\nupdated: ",
            print time.ctime()
            f = open("C:\\3d-Model\\bin\\segmentation_files\\progress.txt","r")
                #Read whole file into data
            code = f.read()
            print code
            if code=="canny":
                    self.canny.SetBitmapLabel(self.canny_image)
                    self.Update()
                    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
                         myFile.write("")
            if code=="contour":
                    self.contour.SetBitmapLabel(self.contour_image)
                    self.Update()
                    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
                         myFile.write("")
            if code=="segment":
                    self.segment.SetBitmapLabel(self.segment_image)
                    self.Update()
                    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
                         myFile.write("")
            if code=="crop":
                    self.crop.SetBitmapLabel(self.crop_image)
                    self.Update()
                    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
                         myFile.write("")
                    self.finish.Enable(True)
                    self.timer.Stop()
                    proceed_flag=0

        if calib_flag==1:
            self.calib_gauge.Enable(True) 
            f = open("C:\\3d-Model\\bin\\camera_calibration\\value.txt","r")
            gauge_value = f.read()
            gauge_value_int=int(gauge_value)
            self.calib_gauge.SetValue((gauge_value_int))
            f = open("C:\\3d-Model\\bin\\camera_calibration\\finish.txt","r")
            code = f.read()
            if code=="finish":
                print "finish calibration"
                progressFile = open(r'C:\3d-Model\bin\camera_calibration\calib_temp.txt','r')
                self.richTextCtrl2.SetValue(progressFile.read())
                with open('C:\\3d-Model\\bin\\camera_calibration\\finish.txt', 'w') as myFile:
                    myFile.write("")
                #with open('C:\\3d-Model\\bin\\camera_calibration\\calib_temp.txt', 'w') as myFile:
                #    myFile.write("")
                with open('C:\\3d-Model\\bin\\camera_calibration\\value.txt', 'w') as myFile:
                    myFile.write("0")
                self.timer.Stop()
                calib_flag=0
                
            
            
        event.Skip()
###os.path.getmtime(r'c:\pSApp\tempFiles\temp_for_display.txt')

###Segmentation Panel
    def Image_init(self):
        canny_image = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\Cannyedge_g.png"
        self.canny_image = wx.Bitmap(canny_image)
        contour_image= r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\contour_g.png"
        self.contour_image = wx.Bitmap(contour_image)
        segment_image = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\segment_g.png"
        self.segment_image = wx.Bitmap(segment_image)
        crop_image = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\image_g.png"
        self.crop_image = wx.Bitmap(crop_image)
        canny_image_r = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\Cannyedge_r.png"
        self.canny_image_r = wx.Bitmap(canny_image_r)
        contour_image_r= r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\contour_r.png"
        self.contour_image_r = wx.Bitmap(contour_image_r)
        segment_image_r = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\segment_r.png"
        self.segment_image_r = wx.Bitmap(segment_image_r)
        crop_image_r = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\image_r.png"
        self.crop_image_r = wx.Bitmap(crop_image_r)
        
        #self.timer = wx.Timer(self)
        #self.Bind(wx.EVT_TIMER, self.update, self.timer)
        

    def OnSegmentationButton(self, event):
        self.browsefiles.Enable(flagbrowse)
        self.show.Enable(flagshow)
        self.Image_init()
        event.Skip()

    def OnShowButton(self, event):
        image_file = self.browsefiles.GetValue()
        with open('C:\\3d-Model\\bin\\segmentation_files\\path.txt', 'w') as myFile:
            myFile.write(image_file)
        img_org = Image.open(image_file)
        # get the size of the original image
        width_org, height_org = img_org.size
        # set the resizing factor so the aspect ratio can be retained
        # factor > 1.0 increases size
        # factor < 1.0 decreases size
        factor = .10
        width = int(width_org * factor)
        height = int(height_org * factor)
        # best down-sizing filter
        img_anti = img_org.resize((width, height), Image.ANTIALIAS)
        # split image filename into name and extension
        name, ext = os.path.splitext(image_file)
        # create a new file name for saving the result
        new_image_file = "C:\\3d-Model\\bin\\segmentation_files\\pic_resize.jpg"
        img_anti.save(new_image_file)
        #print("resized file saved as %s" % new_image_file)
        bmp = wx.Image(new_image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        width = bmp.GetWidth()
        height = bmp.GetHeight()
        # show the bitmap, you need to set size, image's upper
        # left corner anchors at panel coordinates (5, 5)
        wx.StaticBitmap(self.panel3, -1, bmp, pos=(450,20), size=(width, height))
        self.mask_button.Enable(True)
        self.change.Enable(True)
        event.Skip()

    def OnChangeButton(self, event):
        self.browsefiles.Enable(False)
        self.show.Enable(False)
        self.change.Enable(False)
        self.mask_button.Enable(False)
        self.proceed.Enable(False)
        event.Skip()

    def OnProceedButton(self, event):
        global proceed_flag
        proceed_flag=1
        self.timer.Start(1000,False)
        pid = subprocess.Popen([sys.executable, "C:\\3d-Model\\bin\\segmentation_files\\canny_main.py"]) # call subprocess
        self.abort.Enable(True)
        event.Skip()

    def OnAbortButton(self, event):
        self.Close()
        event.Skip()

    def OnFinishButton(self, event):
        self.abort.Enable(False)
        self.browsefiles.Enable(False)
        self.show.Enable(False)
        self.change.Enable(False)
        self.proceed.Enable(False)
        self.mask_button.Enable(False)
        self.canny.SetBitmapLabel(self.canny_image_r)
        self.Update()

        self.contour.SetBitmapLabel(self.contour_image_r)
        self.Update()

        self.segment.SetBitmapLabel(self.segment_image_r)
        self.Update()

        self.crop.SetBitmapLabel(self.crop_image_r)
        self.Update()
        self.finish.Enable(False)
        event.Skip()

    def OnMask_buttonButton(self, event):
        box = wx.MessageDialog(None,"Do you want to do masking ?","Warning",wx.YES_NO)
        answer = box.ShowModal()
        box.Destroy()
        if answer == wx.ID_YES:
            #pid = subprocess.Popen([sys.executable, "C:\\3d-Model\\bin\\masking\\App2.py"])
            os.chdir(r"C:\3d-Model\bin\masking")
            os.system("App2.py")
            #pid = subprocess.Popen([sys.executable, "C:\\3d-Model\\bin\\masking\\App2.py"])
            self.proceed.Enable(True)
        else:
            
            self.proceed.Enable(True)
        event.Skip()

    def OnButton1Button(self, event):
        path=r'C:\3d-Model\resources'
        full_path=path+'\sfm_georef_2.3.exe'
        os.system('%s' %full_path)
        self.bitmapButton3.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/georef_g.png',
            wx.BITMAP_TYPE_PNG))
            

    def OnButton3Button(self, event):
        path=r"C:\3d-Model\resources\osm-bundler\osm-bundlerWin32\RunBundler.py --photos="
        path2=self.dirBrowseButton2.GetValue()
        path3=r"C:/3d-Model/bin/point_cloud/coordinates.txt"
        if not(os.path.isdir(path2)):
            box2=wx.MessageDialog(None,'Invalid path. Enter the correct path','Warning',wx.OK)
            ans2=box2.ShowModal()
            box2.Destroy()
        else:
            os.system(r"C:/3d-Model/bin/point_cloud/gps.py "+path2+" "+path3)
            os.system(r"C:/3d-Model/bin/point_cloud/name.py "+path2)
            pathf=path+path2
            box=wx.MessageDialog(None,'Do not close the bundler output window when RunBundler process is over.','Warning',wx.OK)
            answer=box.ShowModal()
            box.Destroy() 
            #os.sytem(r"C:/3d-Model/bin/point_cloud/gps.py "+path2+" "+"C:/3d-Model/bin/point_cloud/coordinates.txt")
            c=os.system('%s' %pathf)
            if c==0:
                self.bitmapButton1.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/runbundler_g.png',
                wx.BITMAP_TYPE_PNG))
                self.textCtrl1.Show(True)
                self.button4.Show(True)
                self.dirBrowseButton2.Show(False)
                self.button1.Show(False)
                self.dirBrowseButton3.Show(True)
                self.button5.Show(False)
                self.button3.Show(False)
            else:
                box3=wx.MessageDialog(None,'Invalid path. Enter the correct path','Warning',wx.OK)
                ans3=box3.ShowModal()
                box3.Destroy()
                
            
        

    def OnButton4Button(self, event):
        path=r"C:\3d-Model\resources\osm-bundler\osm-bundlerWin32\RunPMVS.py --bundlerOutputPath="
        path2=self.textCtrl1.GetValue()
        pathf=path+path2
        path4=self.dirBrowseButton3.GetValue()
        p1=r'C:\3d-model\bin\point_cloud\copy.py '+path2+' '+path4
        if not (os.path.isdir(path2)):
            box2=wx.MessageDialog(None,'Invalid path. Enter the correct path','Warning',wx.OK)
            ans2=box2.ShowModal()
            box2.Destroy()
        else:
            co=os.system('%s' %pathf)
            if co==0:
                os.system('%s' %p1)
                self.bitmapButton2.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/runpmvs_g.png',
                wx.BITMAP_TYPE_PNG))
                self.button5.Show(False)
                self.button1.Show(True)
                self.dirBrowseButton3.Show(False)
                self.textCtrl1.Show(False)
                self.button4.Show(False)
            else:
                box3=wx.MessageDialog(None,'Invalid path. Enter the correct path','Warning',wx.OK)
                ans3=box3.ShowModal()
                box3.Destroy()
                
                
    def OnButton6Button(self, event):
        self.Close()

    def OnButton5Button(self, event):
        self.dirBrowseButton2.Show(False)
        self.button5.Show(False)
        self.button4.Show(False)
        self.button1.Show(True)
        self.dirBrowseButton3.Show(False)
        self.textCtrl1.Show(False)

    def OnOpenPointCloudButton(self, event):
        os.chdir(wrk_drr)
        f = open('curr_proj.txt','r')
        path = f.readline()
        str1 = r'\input'
        os.system('start explorer.exe '+path+str1)
        #os.chdir(r'C:\3d-Model\resources\CloudCompare')
        path2 = self.fileBrowseButton1.GetValue()
        os.system(path2)
        self.bitmapButton4.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/pickpoints_g.png',
              wx.BITMAP_TYPE_PNG))
        self.OpenPointCloud.Show(False)
        self.Height.Show(True)
        self.dirBrowseButton4.Show(True)
        self.fileBrowseButton1.Show(False)
        
            
        
        event.Skip()

    def OnHeightButton(self, event):
        paths=self.dirBrowseButton4.GetValue()
        f = open('curr_proj.txt','r')
        path = f.readline()
        str1 = r'\input'
        
        path2=r'C:\3d-Model\bin\point_cloud\Utm_height.py '+paths+ ' ' +path+str1
        '''box=wx.MessageDialog(None,path2,"Title",wx.OK)
        ans = box.ShowModal()
        box.Destroy()'''
        os.system(path2)
        self.bitmapButton5.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/extractht_g.png',
              wx.BITMAP_TYPE_PNG))
##################camera calibration
    

    def OnResultButton(self, event):
        path_calib = self.browse_calib.GetValue()
        print path_calib
        with open('C:\\3d-Model\\bin\\camera_calibration\\path.txt', 'w') as myFile:
                         myFile.write(path_calib)

        f = open("C:\\3d-Model\\bin\\camera_calibration\\path.txt","r")
                #Read whole file into data
        path=f.read()+"\\*.jpg"

        args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
        args = dict(args)
        try: img_mask = img_mask[0]
        except: img_mask = path
        img_names = glob(img_mask)
        global calib_flag
        calib_flag=1
        value_calib=len(img_names)
        print value_calib
        pid = subprocess.Popen([sys.executable, "C:\\3d-Model\\bin\\camera_calibration\\run_calib.py"])

        self.calib_gauge.SetRange(int(value_calib))
        self.timer.Start(500,False)
        
        
        event.Skip()

    def OnCalibrationButton(self, event):
        self.browse_calib.Enable(True)
        self.result.Enable(True)
        event.Skip()
####################
    def OnFileLoadprojMenu(self, event):
        fd=loadproject.create(self).ShowModal()
        xyz=fd.ShowModal()
        #fd.EndModal()
        fd.Destroy()
        event.Skip()

    def OnPlacemarkButton(self, event):
        os.chdir(r"C:\3d-Model\bin\3d-modelling")
        os.system("addPlacemark_new.py")
        event.Skip()

    def OnCheckListBox1Checklistbox(self, event):
        event.Skip()

    def OnCheckListBox1Listbox(self, event):
        event.Skip()

    def OnButton2Button(self, event):
        event.Skip()

    def OnCombo_box_senseCombobox(self, event):
        cbo = event.GetEventObject()
        value = cbo.GetValue()
        strg=str(value)
        print type(strg)
        print strg
        for i in strg:
            if i=='-':
                sensor_value=strg[strg.find("-")+1:strg.find("\n")]
                print sensor_value
                with open(r'C:\3d-Model\bin\camera_calibration\sensor_value.txt', 'w') as myFile:
                    myFile.write(sensor_value)
        event.Skip()

    def OnNot_foundButton(self, event):
        self.sense.SetEditable(True)
        self.sensorButton.Enable(True)
        event.Skip()

    def OnSensorButtonButton(self, event):
        sensor_value = self.sense.GetValue()
        print sensor_value
        with open(r'C:\3d-Model\bin\camera_calibration\sensor_value.txt', 'w') as myFile:
            myFile.write(sensor_value)
        event.Skip()
        

            
