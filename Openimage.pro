!path=!path+':./astron/pro'
file=dialog_pickfile()
print,file
a = readfits(file)
a = rebin(a,512,512)
window,xsize=512,ysize=512,xpos=0,ypos=0
tvscl,a
end
