from sugar.activity import activity
import logging
import hulahop
from sugar import env
import sys, os
import gtk
hulahop.startup(os.path.join(env.get_profile_path(), 'gecko'))	
from hulahop.webview import WebView
from sugar.graphics.toolbutton import ToolButton

class T2Activity(activity.Activity):
    def xois_clicked(self, widget, data=None):
        self.webview.load_uri('http://teach-teacher.ep.io/slides/1')

    def guide_clicked(self, widget, data=None):
        self.webview.load_uri('http://teach-teacher.ep.io/slides/17')

    def back_clicked(self, widget, data=None):
        if self.webview.get_web_navigation().canGoBack:
		self.webview.get_web_navigation().goBack()

    def home_clicked(self, widget, data=None):
        self.webview.load_uri('http://147.47.120.20/~tsquare/menu.php')

    def __init__(self, handle):
        print "running activity init", handle
        activity.Activity.__init__(self, handle)
        print "activity running"

        self.set_title('Teach Teacher')

        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
	toolbar = gtk.Toolbar()	

        self.goBack = ToolButton('go-left')
        self.goBack.set_tooltip("Go Back")
        self.goBack.connect('clicked', self.back_clicked)
        toolbar.insert(self.goBack, -1)
        self.goBack.show()

        self.home = ToolButton('go-home')
        self.home.set_tooltip("Home")
        self.home.connect('clicked', self.home_clicked)
        toolbar.insert(self.home, -1)
        self.home.show()
	
        self.xois = ToolButton('computer-xo')
        self.xois.set_tooltip("T's XO")
        self.xois.connect('clicked', self.xois_clicked)
        # toolbar.insert(self.xois, -1)
        # self.xois.show()

        self.guide = ToolButton('go-next')
        self.guide.set_tooltip("T's Guide")
        self.guide.connect('clicked', self.guide_clicked)
        # toolbar.insert(self.guide, -1)
        # self.guide.show()


	toolbar.show()
	toolbox.add_toolbar("Menu", toolbar)
        toolbox.show()
        
        self.webview = WebView()
	self.set_canvas(self.webview)
        self.webview.show()
        self.webview.load_uri('http://147.47.120.20/~tsquare/menu.php')


    
        print "AT END OF THE CLASS"
