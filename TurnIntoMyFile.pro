!path=!path+':./astron/pro'
size = 1024

file=dialog_pickfile()
original = readfits(file)
changed = rebin(original,size,size)
head = [2,size,size,1]


openw,1,'mas.my'
writeu,1,head
writeu,1,changed
close,1

openr,1, 'mas.my'
b = head
readu, 1, b
case b[3] of
1: n1 = fltarr(b[1], b[2])
2: n1 = fltarr(b[1], b[2])
endcase
readu, 1,n1
close, 1
window, xsize = size, ysize = size, xpos = 0, ypos = 0
tvscl,n1

end
