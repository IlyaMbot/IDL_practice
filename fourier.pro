!path=!path+':./astron/pro'

size = 512

file=dialog_pickfile()
print,file
original = readfits(file)
original = original > 0
a = rebin(original, size, size)

ffTransform = FFT(a, -1)
power = SHIFT(ALOG(ABS(ffTransform)^2), size/2, size/2)
;surface, power

window, 0, xsize = size, ysize = size, xpos = 0, ypos = 0
;tvscl, power
tv, power
end
