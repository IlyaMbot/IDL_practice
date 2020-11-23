!path=!path+':./astron/pro'

size1 = 1024

;opens example file and resizes it
file=dialog_pickfile()
original = readfits(file)
a = rebin(original, size1, size1)



;plotting a new window
window, 0, xsize=size1, ysize=size1, xpos=0, ypos=0
contour, a, xstyle=1, ystyle=1, charsize=1.5

px = round(!d.x_size*(!x.window[1] - !x.window[0]))
py = round(!d.x_size*(!y.window[1] - !y.window[0]))


xsize1 = !d.x_size*(!x.window[1] - !x.window[0])
ysize1 = !d.y_size*(!y.window[1] - !y.window[0])
xshift = !d.x_size*!x.window[0]
yshift = !d.y_size*!y.window[0]

a1 = congrid(a,px,py)
tvscl, a1, xsize=xsize1, ysize=ysize1, xshift, yshift
contour, a, /noerase, xstyle=1, ystyle=1, charsize=1.5


cursor, x, y, /data, wait=1, /down 
cursor, x1, y1, /data, wait=1, /up 

num = 2
print, x * num, y * num
plots, x, y, psym=1, /data

print, x1 * num, y1 * num
plots, x1, y1, psym=1, /data
p = original((x * num) : (x1 * num), (y * num) : (y1 * num))

size2 = 10

window, 1, xsize = (x1 - x) * size2, ysize = (y1 - y) * size2, xpos=0, ypos=0
tvscl, p, xsize = (x1 - x) * size2, ysize = (y1 - y) * size2, xshift, yshift
contour, p, xstyle=1, ystyle=1, charsize=1.5

px = round(!d.x_size*(!x.window[1] - !x.window[0]))
py = round(!d.x_size*(!y.window[1] - !y.window[0]))
xshift = !d.x_size*!x.window[0]
yshift = !d.y_size*!y.window[0]

p1 = congrid(p,px1,py1)
contour, p, /noerase, xstyle=1, ystyle=1, charsize=1.5

end

