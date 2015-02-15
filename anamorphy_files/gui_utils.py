import constants

def eraseBackground(w, dc, bmp):        
    if not dc:
        dc = wx.ClientDC(w)
        rect = w.GetUpdateRegion().GetBox()
        dc.SetClippingRect(rect)

    if bmp is None:
        dc.Clear()
        return

    # Tile a picture to the background
    sz = w.GetClientSize()
    w = bmp.GetWidth()
    h = bmp.GetHeight()
    x = 0
    while x < sz.width:
        y = 0
        while y < sz.height:
            dc.DrawBitmap(bmp, x, y)
            y = y + h
        x = x + w        
    return
