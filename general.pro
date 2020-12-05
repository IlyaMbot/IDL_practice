!path = !path+':./astron/pro'

size1 = 1024

;opens example file and resizes it
file = dialog_pickfile()
original = readfits(file)
original = original > 1
a = rebin(original, size1, size1)



;create a new window
window, 0, xsize = size1, ysize = size1, xpos = 0, ypos = 0
contour, a, xstyle = 1, ystyle = 1, charsize = 1.5

px = round(!d.x_size*(!x.window[1] - !x.window[0]))
py = round(!d.x_size*(!y.window[1] - !y.window[0]))

xsize1 = !d.x_size * (!x.window[1] - !x.window[0])
ysize1 = !d.y_size * (!y.window[1] - !y.window[0])
xshift = !d.x_size * !x.window[0]
yshift = !d.y_size * !y.window[0]

;plots in win. image and cont.
a1 = congrid(a, px, py)
tvscl, a1, xsize = xsize1, ysize = ysize1, xshift, yshift
contour, a, /noerase, xstyle = 1, ystyle = 1, charsize = 1.5

