import sys
from generated.MainFrame import MainFrame
from PIL import Image, ImageOps
from PIL.ExifTags import TAGS, GPSTAGS, IFD
import wx
import piexif
import pickle

custom_tags = {'url_current'   : 'https://stackoverflow.com/q/52729428/1846249',
        'contains_fish' : False,
        3               : 0.14159265358979323, }

class PhotoCtrl(wx.App):
    def mainBitmap_onSize(self, e=None):
        W, H = self.frame.mainBitmap.Size
        print('On size %dx%d' % (W, H))
        if W != self.lastW and H != self.lastH:
            if self.imagePath:
                image = Image.open(self.imagePath).convert("RGB")
                rotated_im = ImageOps.exif_transpose(image)
                if W > H:
                    NewW = W
                    NewH = int(W * H / W)
                else:
                    NewH = H
                    NewW = int(H * W / H)

                im_resize = rotated_im.resize((NewW, NewH))
                width, height = im_resize.size
                bm = wx.Bitmap.FromBuffer(width, height, im_resize.tobytes())
                self.frame.mainBitmap.SetBitmap(bm)
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
    if imagePath:
        img = Image.open(imagePath)
        img_exif = img.getexif()
        if img_exif is None:
            print('Sorry, image has no exif data.')
        else:
            print('>>>>>>>>>>>>>>>>>>', 'Base tags', '<<<<<<<<<<<<<<<<<<<<')
            for k, v in img_exif.items():
                tag = TAGS.get(k, k)
                print(tag, v)

            for ifd_id in IFD:
                print('>>>>>>>>>', ifd_id.name, '<<<<<<<<<<')
                try:
                    ifd = img_exif.get_ifd(ifd_id)

                    if ifd_id == IFD.GPSInfo:
                        resolve = GPSTAGS
                    else:
                        resolve = TAGS

                    for k, v in ifd.items():
                        tag = resolve.get(k, k)
                        print(tag, v)
                except KeyError:
                    pass
        
        data = pickle.dumps(custom_tags)
        exif_dict = piexif.load(img.info["exif"])
        exif_dict.setdefault('Exif', {})
        exif_dict["Exif"] = exif_dict["Exif"] | { piexif.ExifIFD.UserComment: data }
        exif_bytes = piexif.dump(exif_dict)
        img.save(imagePath, exif=exif_bytes)
    
    app = PhotoCtrl(imagePath)
    app.MainLoop() 