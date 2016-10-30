#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import os


class MainWindow(wx.Frame):
    """We simply derive a new class of Frame
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100),
                          pos=(0, 0))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        # Setting up the menu
        filemenu = wx.Menu()
        helpmenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets
        menuOpen = filemenu.Append(wx.ID_OPEN, '&Open...', 'Open a file')
        menuSave = filemenu.Append(wx.ID_SAVE, '&Save', 'Save the file')
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, 'Save as...', 'Save as')
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, 'E&xit', 'Terminate the program')

        menuAbout = helpmenu.Append(wx.ID_ABOUT, '&About',
                                    'Information about this program')

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '&File')  # Adding the menu to the MenuBar
        menuBar.Append(helpmenu, '&Help')
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the frame content

        # Bind event handle
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)

        # properties
        self.filename = ''
        self.dirname = ''

        self.Show(True)

    def __save(self):
        f = open(os.path.join(self.dirname, self.filename), 'w')
        f.write(self.control.GetValue())
        f.close()

    def OnOpen(self, event):
        """Open a file
        """
        self.dirname = ''
        dlg = wx.FileDialog(self, 'Choose a file', self.dirname, '', '*.*',
                            wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self, event):
        if self.filename == '':
            self.OnSaveAs(event)
        else:
            self.__save()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(self, 'Save as', self.dirname, '', '*.*', wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.__save()
        dlg.Destroy()

    def OnAbout(self, event):
        # A message dialog box with an OK button.
        dlg = wx.MessageDialog(self, 'A small text editor\n  Author: furzoom',
                               'About Small Editor', wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished

    def OnExit(self, event):
        self.Close(True)  # Close the frame


if __name__ == '__main__':
    # app = wx.App(True, 'log/editor.log')
    app = wx.App(False)
    frame = MainWindow(None, 'Small editor')
    print('hello')
    app.MainLoop()
