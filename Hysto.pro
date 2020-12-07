!path=!path+':./astron/pro'

file = dialog_pickfile()
image = readfits(file)
image = rebin(image,512,512)
image = image > 10

plot, histogram(image)


end
