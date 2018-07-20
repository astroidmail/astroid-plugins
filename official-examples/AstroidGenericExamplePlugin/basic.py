import gi
gi.require_version ('Astroid', '0.2')
from gi.repository import GObject, Astroid

print ("basic: plugin loading..")

# this one doesn't do anything at the moment

class BasicPlugin (GObject.Object, Astroid.Activatable):
  object = GObject.property (type=GObject.Object)

  def do_activate (self):
    print ('basic: activate')

  def do_deactivate (self):
    print ('basic: deactivate')


  def do_get_tag_colors (self, tag, bg):
    return [ '#000000', '#ffffff0f' ]


