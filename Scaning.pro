!path=!path+':./astron/pro'

size = 2048

file = dialog_pickfile()
a = readfits(file,header)
c = rebin(a,size,size)

var = sxpar(header, 'CRPIX1')
var1 = sxpar(header, 'CRPIX2')
print,var,var1

m = c[*,var1]
m1 = m
n = c[var,*]
n1=n

for j=0, size-5 DO BEGIN 
		m1[j] = (m[j]+m[j+1]+m[j+2]+m[j+3]+m[j+4])/5 
		n1[j] = (n[j]+n[j+1]+n[j+2]+n[j+3]+n[j+4])/5
endfor

window,0, xsize = size/2, ysize = size/2, xpos = 0, ypos = 0
plot,m1, /data

window,1, xsize = size/2, ysize = size/2, xpos = size/2, ypos = 0
plot,n1, /data

head = [2,size,size,1]

openw,1,'scan1.my'
writeu,1,head
writeu,1,m1
close,1


openw,2,'scan2.my'
writeu,2,head
writeu,2,n1
close,2



;30min

end
