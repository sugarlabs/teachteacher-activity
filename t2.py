#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from gi.repository import WebKit
from gi.repository.WebKit import WebView

from sugar3.activity import activity
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarButton


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

        toolbarbox = ToolbarBox()
        self.set_toolbar_box(toolbarbox)

        toolbar = Gtk.Toolbar()

        button = ActivityToolbarButton(self)
        toolbarbox.toolbar.insert(button, -1)

        self.goBack = ToolButton('go-left')
        self.goBack.set_tooltip("Go Back")
        self.goBack.connect('clicked', self.back_clicked)
        toolbar.insert(self.goBack, -1)

        self.home = ToolButton('go-home')
        self.home.set_tooltip("Home")
        self.home.connect('clicked', self.home_clicked)
        toolbar.insert(self.home, -1)

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

        toolbarbox.toolbar.insert(ToolbarButton(page=toolbar, icon_name='toolbar-edit'), -1)

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbarbox.toolbar.insert(separator, -1)

        stop_button = StopButton(self)
        toolbarbox.toolbar.insert(stop_button, -1)

        scroll = Gtk.ScrolledWindow()
        self.set_canvas(scroll)

        self.webview = WebView()
        self.webview.load_uri('http://147.47.120.20/~tsquare/menu.php')
        scroll.add(self.webview)

        toolbar.show_all()
        toolbarbox.show_all()
        toolbarbox.toolbar.show_all()
        self.show_all()

        print "AT END OF THE CLASS"

