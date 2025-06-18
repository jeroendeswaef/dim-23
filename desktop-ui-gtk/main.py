import gi
import sys
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Dim23")
        self.set_default_size(200, 100)
        existing_window = builder.get_object('main-window')
        image = builder.get_object("main-image")
        existing_window.remove(image)
        
        if imagePath:
            image.set_from_file(imagePath)
        self.add(image)
        
builder = Gtk.Builder()
builder.add_from_file("main.glade")

imagePath = sys.argv[1] if len(sys.argv) > 1 else None

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()