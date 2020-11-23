!path=!path+':./astron/pro'

size = 1024

file=dialog_pickfile()
original = readfits(file)
a = rebin(original, size, size)

window, 0, xsize=size, ysize=size, xpos=0, ypos=0
contour, a, xstyle=1, ystyle=1, charsize=1.5

px = round(!d.x_size*(!x.window[1] - !x.window[0]))
py = round(!d.x_size*(!y.window[1] - !y.window[0]))
a1 = congrid(a,px,py)

xsize1 = !d.x_size*(!x.window[1] - !x.window[0])
ysize1 = !d.y_size*(!y.window[1] - !y.window[0])
xshift = !d.x_size*!x.window[0]
yshift = !d.y_size*!y.window[0]


tvscl, a1, xsize=xsize1, ysize=ysize1, xshift, yshift
contour, a, /noerase, xstyle=1, ystyle=1, charsize=1.5



cursor, x, y, /data, wait=1, /down
 
cursor,x1,y1,/data, wait=1, /up 

print, x, y
plots, x, y, psym=1, /data

print, x1, y1
plots, x1, y1, psym=1, /data
p = a(x:x1, y:y1)

window, 1, xsize=x1-x, ysize=y1-y, xpos=0, ypos=0

tvscl, p

end

