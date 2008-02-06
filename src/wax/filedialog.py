# filedialog.py

import wx
import waxobject

class FileDialog(wx.FileDialog, waxobject.WaxObject):

    def __init__(self, parent, title="Choose a file", default_dir="",
                 default_file="", wildcard="*.*", open=0, save=0, multiple=0,
                 must_exist=0, overwrite_prompt=0):
        style = 0
        if open:
            style |= wx.OPEN
        elif save:
            style |= wx.SAVE
        if multiple:
            style |= wx.MULTIPLE
        if must_exist:
            style |= wx.FD_FILE_MUST_EXIST
        if overwrite_prompt:
            style |= wx.OVERWRITE_PROMPT

        wx.FileDialog.__init__(self, parent, title, default_dir, default_file,
         wildcard, style)

    def ShowModal(self):
        """ Simplified ShowModal(), returning strings 'ok' or 'cancel'. """
        result = wx.FileDialog.ShowModal(self)
        if result == wx.ID_OK:
            return 'ok'
        else:
            return 'cancel'
