import gi
gi.require_version ('Astroid', '0.2')
gi.require_version ('Gtk', '3.0')
from gi.repository import GObject, Gtk, Astroid

print ("tagformat: plugin loading..")

class TagFormatPlugin (GObject.Object, Astroid.ThreadIndexActivatable):
  thread_index  = GObject.property (type = Gtk.Box)

  def do_activate (self):
    print ('tagformat: activate')

    ## Add a useful label to the ThreadIndex
    self.label = Gtk.Label ("Hullu!")
    self.thread_index.pack_end (self.label, True, True, 5)


  def do_deactivate (self):
    print ('tagformat: deactivate')

  def do_format_tags (self, background, tags, selected):
    # background: color of canvas the tags will be shown on
    # tags:       a list of tags
    #
    # returns: a Pango Markup string.

    ## IPython
    # demonstrats starting a IPython shell in the middle of the plugin, use
    # Ctrl+D to end it and continue execution.

    from IPython import embed
    # embed ()

    print ("got tags: ", tags)

    return ", ".join (tags)


