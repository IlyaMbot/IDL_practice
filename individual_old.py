import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

plt.style.use(astropy_mpl_style) #telling astropy about using plt

filename = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_uv_24s.2011-08-09T080043Z.1600.image_lev1.fits"
#filename = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_euv_12s.2011-08-10T093446Z.304.image_lev1.fits"
#filename = "/home/conpucter/GitHub/IDL_practice/aia.lev1.335A_2013-11-10T10_00_02.62Z.image_lev1.fits"

image_file = get_pkg_data_filename(filename)
image_data = fits.getdata(image_file, ext=0)
image_data = np.flip(image_data, 0)

#constants of the image intensity:
bottom_val = 0 
upper_val =  image_data.max()

#set up the needed level
percent = 40 # this var will be entered from the keyboard
level = 4000
print(upper_val, level)


image_data[image_data < bottom_val] = bottom_val
#image_data[image_data > upper_val] = upper_val

def intensity_searcher(image):
    pixel_position = np.argwhere(image  == image.max())
    pixel_position = pixel_position[0]
    print(pixel_position)
    return(pixel_position)


def avermass(image):
    pixel_position = ndimage.measurements.center_of_mass(image)
    print(pixel_position)
    return(pixel_position)


def general_plot(image, loop1 = None, loop2 = None):
    pixel11 = avermass(loop1)
    pixel12 = avermass(loop2)
    pixel21 = intensity_searcher(loop1)
    pixel22 = intensity_searcher(loop2)

    fig, ax = plt.subplots(1, 2)
    
    ax[0].grid(b=None)
    pmc = ax[0].imshow(image, cmap = 'nipy_spectral')
    #ax[0].plot(5+ pixel11[1], 25 + pixel11[0], 'wx', fillstyle='none', markersize=15)
    #ax[0].plot(32 + pixel12[1], 6 + pixel12[0], 'wx', fillstyle='none', markersize=15)
    ax[0].plot([5+ pixel11[1], 32 + pixel12[1]], [25 + pixel11[0], 6 + pixel12[0]],'wx' ,ls = '-', fillstyle='none', markersize=15)
    fig.colorbar(pmc, ax=ax[0])

    ax[1].grid(b=None)
    pmc = ax[1].imshow(image, cmap = 'nipy_spectral')
    #ax[1].plot(32 + pixel22[1], 6 + pixel22[0], 'wx', fillstyle='none', markersize=15)
    #ax[1].plot(5+ pixel21[1], 25 + pixel21[0], 'wx', fillstyle='none', markersize=15)
    ax[1].plot([5+ pixel21[1], 32 + pixel22[1]], [25 + pixel21[0], 6 + pixel22[0]],'wx' , ls = '-', fillstyle='none', markersize=15)
    fig.colorbar(pmc, ax=ax[1])

    #ax.plot(pixel2[1], pixel2[0], 'wx', fillstyle='none', markersize=15)
    
    plt.tight_layout()
    plt.savefig('/home/conpucter/GitHub/IDL_practice/ind/result.png', transparent=False, dpi=330, bbox_inches="tight")
    plt.show()


def plot_picture(image, cont, inf = 0, sup = 1, step = 1, colours = 'nipy_spectral' ):
    ''' It plots figures '''
    plt.figure()
    plt.grid(b=None)
    plt.imshow(image, cmap = colours)
    if cont == True:
        plt.contour(image, levels = range(inf, sup, step), inline=True, fontsize=15, cmap = 'nipy_spectral' )
    plt.plot()
    plt.colorbar()
    plt.show()


def loop_finder(image_input, roof):
    ''' This function finds all pionts > roof and check if there others near with same intensity
        as a result it returns a cut of image with all flares
    '''

    if roof == 0:
        plot_picture(image_input, False)
        return
    
    
    p = 2 #square's side size
    p2 = p*2


    check_area = image_input[
        (p + 1) : - p - 1,
        (p + 1) : - p - 1
        ]
    
    position = np.argwhere(check_area  >= roof)
        
    indexes = []
    ind = 0

    for point in position:  
        
        cut = image_input[
        point[0] + p + 1: point[0] + (p2 + 2 + 1),
        point[1] + p + 1: point[1] + (p2 + 2 + 1)  
        ]
                
        check_sum = 0
        for i in range(len(cut[0,:])):
            for j in range(len(cut[:,0])):
                check_sum += cut[i,j]
        
        check_sum /= p2**2

        if check_sum < roof:
           indexes.append(ind)
        ind +=1

    position = np.delete(position, indexes, 0)

    if len(position) == 0:
        print("No loops found :C")
        return
        
    size = 10
    loop_pic = image_input[
        np.amin(position[:,0]) - size : np.amax(position[:,0]) + size,
        np.amin(position[:,1]) - size : np.amax(position[:,1]) + size
        ]
    
    #plot_countour(loop_pic, level, 800, 100)
    #plot_picture(loop_pic, True, inf = level, sup = 10000 , step = 1000, colours = 'Greys')
    #plot_picture(loop_pic, False)
    
    return(loop_pic)


#your ad could be here 
    

loops = loop_finder(image_data, level)

#print(loops)
loop1 = loops[ 25 : 85, 5 : 30]
loop2 = loops[ 6 : , 32 : ]
#plot_picture(loop1, False)
#plot_picture(loop2, False)
general_plot(loops, loop1, loop2)