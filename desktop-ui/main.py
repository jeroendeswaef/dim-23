import sys
from generated.MainFrame import MainFrame
import wx

class PhotoCtrl(wx.App):
    def __init__(self, imagePath=None):
        wx.App.__init__(self)
        self.frame = MainFrame(None) #wx.Frame(None, title='Photo Control')
        self.PhotoMaxSize = 240
        if imagePath:
            self.frame.m_staticText1.SetLabel(imagePath) 
            img = wx.Image(imagePath, wx.BITMAP_TYPE_ANY)
            # scale the image, preserving the aspect ratio
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.PhotoMaxSize
                NewH = int(self.PhotoMaxSize * H / W)
            else:
                NewH = self.PhotoMaxSize
                NewW = int(self.PhotoMaxSize * W / H)

            img = img.Scale(NewW,NewH)

            self.frame.mainBitmap.SetBitmap(wx.Bitmap(img))
      
        self.frame.Show()
        
if __name__ == '__main__':
    print(sys.argv)
    imagePath = sys.argv[1] if len(sys.argv) > 1 else None
    app = PhotoCtrl(imagePath)
    app.MainLoop()