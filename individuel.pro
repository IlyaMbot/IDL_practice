!path = !path+':./astron/pro'

size1 = 1024

;opens an example file and resizes it

;file = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_euv_12s.2011-08-10T093446Z.304.image_lev1.fits"
file = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_uv_24s.2011-08-09T080043Z.1600.image_lev1.fits"

original = readfits(file, header)
original = original > 1
original = original < 3000

a = rebin(original, size1, size1)

; picture's constants: cenrtes and resolution
var = sxpar(header, 'NAXIS1') / 2
var1 = sxpar(header, 'NAXIS2') / 2
rsl = sxpar(header, 'CDELT1') ;resolution 
size2 = sxpar(header, 'NAXIS1') / size1

ax = (indgen(size1) - var / size2) * rsl * size2
ay = (indgen(size1) - var1 / size2) * rsl * size2

;create a new window
window, 0, xsize = size1, ysize = size1, xpos = 0, ypos = 0
contour, a, ax, ay, xstyle = 1, ystyle = 1, charsize = 1.5, levels = max(a)*0

px = round(!d.x_size*(!x.window[1] - !x.window[0]))
py = round(!d.x_size*(!y.window[1] - !y.window[0]))

xsize1 = !d.x_size * (!x.window[1] - !x.window[0])
ysize1 = !d.y_size * (!y.window[1] - !y.window[0])
xshift = !d.x_size * !x.window[0]
yshift = !d.y_size * !y.window[0]

;plots in win. image and contour
a1 = congrid(a, px, py)
tvscl, a1, xsize = xsize1, ysize = ysize1, xshift, yshift
contour, a, ax, ay, /noerase, xstyle = 1, ystyle = 1, charsize = 1.5, levels = max(a)*0.5


;setting coordinates for a new win.
cursor, x, y, /data, wait = 1, /down 
cursor, x1, y1, /data, wait = 1, /up 

print, x , y
plots, x, y, psym=1, /data
print
print, x1 , y1 
plots, x1, y1, psym=1, /data

xdat = x
ydat = y

x = (x / (rsl * size2) + var / size2) 
y = (y / (rsl * size2) + var1 / size2)
x1 = (x1 / (rsl * size2) + var / size2)
y1 = (y1 / (rsl * size2) + var1 / size2)

print, x , y
plots, x, y, psym=1, /data
print
print, x1 , y1 
plots, x1, y1, psym=1, /data

;same as 'a' but for the cut image area 'p'
p = original((x * size2) : (x1 * size2), (y * size2) : (y1 * size2))
ax1 = indgen(n_elements(p[*,0])) * rsl + xdat 
ay1 = indgen(n_elements(p[0,*])) * rsl + ydat 

window, 1, xsize = (x1 - x) * size2 * 2, ysize = (y1 - y) * size2 * 2, xpos = 0, ypos = 0

contour, p, ax1, ay1, xstyle = 1, ystyle = 1, charsize = 1.5, levels = max(a)*0

px1 = round(!d.x_size * (!x.window[1] - !x.window[0]))
py1 = round(!d.y_size * (!y.window[1] - !y.window[0]))
xshift = !d.x_size * !x.window[0]
yshift = !d.y_size * !y.window[0]

p1 = congrid(p, px1, py1)
tvscl, p1, xsize = xsize1, ysize = ysize1, xshift, yshift
contour, p, ax1, ay1, /noerase, xstyle = 1, ystyle = 1, charsize = 1.5

end
