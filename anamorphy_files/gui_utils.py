def eraseBackground(w, dc, bmp):
    # Add a picture to the background
    if not dc:
        dc = wx.ClientDC(w)
        rect = w.GetUpdateRegion().GetBox()
        dc.SetClippingRect(rect)
    dc.Clear()
    if bmp is None:
        return

    # tile        
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
