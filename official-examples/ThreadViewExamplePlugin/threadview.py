import gi
gi.require_version ('Astroid', '0.1')
gi.require_version ('Astroid', '0.1')
gi.require_version ('Gtk', '3.0')
gi.require_version ('WebKit', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit
from gi.repository import GObject, Astroid

print ("basic: plugin loading..")

class ThreadViewPlugin (GObject.Object, Astroid.ThreadViewActivatable):
    object = GObject.property (type=GObject.Object)
    thread_view = GObject.property (type = Gtk.Box)
    web_view = GObject.property (type = WebKit.WebView)

  def do_activate (self):
    print ('basic: activate')

  def do_deactivate (self):
    print ('basic: deactivate')

  def do_get_avatar_uri (self, email, type_, size):
    # return a valid <img src=""> uri
    return "http://..."

  def do_get_allowed_uris (self):
    # if your resource is not base64 encoded you need to specify
    # a list of uri prefixes that are allowed to be fetched.
    return []
