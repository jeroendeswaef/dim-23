import sys
from generated.MainFrame import MainFrame
import wx

class PhotoCtrl(wx.App):
    def mainBitmap_onSize(self, e=None):
        W, H = self.frame.mainBitmap.Size
        print('On size %dx%d' % (W, H))
        if W != self.lastW and H != self.lastH:
            if self.imagePath:
                img = wx.Image(imagePath, wx.BITMAP_TYPE_ANY)
                if W > H:
                    NewW = W
                    NewH = int(W * H / W)
                else:
                    NewH = H
                    NewW = int(H * W / H)

                img = img.Scale(NewW,NewH)
                self.frame.mainBitmap.SetBitmap(wx.Bitmap(img))
                self.lastW = W
                self.lastH = H
        e.Skip()

    def __init__(self, imagePath=None):
        self.imagePath = imagePath
        self.lastW = None
        self.lastH = None
        wx.App.__init__(self)
        self.frame = MainFrame(None) 
       
        self.frame.mainBitmap.Bind( wx.EVT_SIZE, self.mainBitmap_onSize )
      
        self.frame.Show()
        
if __name__ == '__main__':
    print(sys.argv)
    imagePath = sys.argv[1] if len(sys.argv) > 1 else None
    app = PhotoCtrl(imagePath)
    app.MainLoop()