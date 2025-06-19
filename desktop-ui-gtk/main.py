import gi
import sys
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from PictureView import PictureView

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Dim23")
        self.set_default_size(500, 200)
        
        if imagePath:
            picture_view = PictureView(imagePath)
            self.add(picture_view)
        
builder = Gtk.Builder()
builder.add_from_file("main.glade")

imagePath = sys.argv[1] if len(sys.argv) > 1 else None

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()