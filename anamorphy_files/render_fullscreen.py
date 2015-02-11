"""FullScreen

This file explores various ways to toggle into fullscreen mode
"""

import wx


def render(parent_frame, renderMethod):
    frame = FullscreenFrame(None, renderMethod)
    frame.Show()


class Panel(wx.Panel):
    def __init__(self, parent, renderMethod):
        self.renderMethod = renderMethod
        self.ready = False
        super(Panel, self).__init__(parent)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKey)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetFocus()
        self.SetCursor(wx.StockCursor(wx.CURSOR_WAIT))
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseClick)

        # first paint must be deferred, to let the frame be really
        # fullscreen
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(100)

    def OnKey(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()

    def OnMouseClick(self, event):
        self.GetParent().Close()

    def OnPaint(self, event):
        if self.ready:
            self.renderMethod(self)
            self.SetCursor(wx.StockCursor(wx.CURSOR_BLANK))
        else:
            event.Skip()

    def OnTimer(self, event):
        self.timer.Stop()
        self.ready = True
        self.Refresh()


class FullscreenFrame(wx.Frame):
    def __init__(self, parent, renderMethod):
        super(FullscreenFrame, self).__init__(parent)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.panel = Panel(self, renderMethod)
        self.ShowFullScreen(True, wx.FULLSCREEN_ALL)

    def OnCloseWindow(self, event):
        self.Destroy()
