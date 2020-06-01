from gi.repository import Gtk
clicks=0
css = """
GtkLabel{
    font: 16;
}
"""
class wmain(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Clicker!",resizable=0)
        Gtk.Window.set_default_size(self, 192,128)
        self.box = Gtk.Box(orientation="vertical")
        self.label = Gtk.Label(label=str(clicks)+" Clicks")
        self.btn = Gtk.Button(label="Click me!")
        self.btn.connect("clicked",self.btn_clicked)
        self.box.pack_start(self.label, 1, 1, 1)
        self.box.pack_start(self.btn, 0, 0, 1)
        self.add(self.box)
    def btn_clicked(self, widget):
        global clicks
        clicks+=1
        self.label.set_label(str(clicks)+" Clicks")
win = wmain()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()