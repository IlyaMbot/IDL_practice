!path=!path+':./astron/pro'

size = 2048

openr,1, opened1=dialog_pickfile()
b = head
readu, 1, b
case b[3] of
1: nu1 = fltarr(b[1], b[2])
2: nu1 = fltarr(b[1], b[2])
endcase
readu, 1,nu1
close, 1
window, xsize = size, ysize = size, xpos = 0, ypos = 0
tvscl,nu1

end
