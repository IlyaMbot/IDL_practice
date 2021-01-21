import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

plt.style.use(astropy_mpl_style) #telling astropy about using plt

filename = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_uv_24s.2011-08-09T080043Z.1600.image_lev1.fits"


image_file = get_pkg_data_filename(filename)
image_data = fits.getdata(image_file, ext=0)
image_data = np.flip(image_data, 0)
resolution = fits.getval(filename, "CDELT1")
size = 2048 * resolution

#constants of the image intensity:
min_val = 0
max_val =  image_data.max()


#set up the needed level
level = 4000 # setting up the lever for flares' searching
percent = 40 #same in percents

upper_val = 1000 # the highest value if image's intensity is too high 

#print(max_val, level)


image_data[image_data < min_val] = min_val
#image_data[image_data > upper_val] = upper_val


def avermass(image):
    pixel_position = ndimage.measurements.center_of_mass(image)
    #print(pixel_position)
    return(pixel_position)


def intensity_searcher(image):
    pixel_position = np.argwhere(image  == image.max())
    pixel_position = pixel_position[0]
    #print(pixel_position)
    return(pixel_position)


def general_plot(image, loop= None, loop1 = None, loop2 = None, loop3 = None):
    pixel10 = avermass(loop)
    pixel11 = np.array([avermass(loop1), avermass(loop2), avermass(loop3)])

    pixel20 = intensity_searcher(loop)
    pixel21 = np.array([intensity_searcher(loop1), intensity_searcher(loop2), intensity_searcher(loop3)])

    x = [5, 35, 48, 49 ]
    y = [25, 12, 73, 98]
    
    fig, ax = plt.subplots(2, 3)
    for i in range(3):
        ax[0,i].grid(b=None)
        pmc = ax[0,i].imshow(image, cmap = 'nipy_spectral')
       
        ax[0,i].plot(
            [(x[0]  + pixel10[1]), (x[i+1] + pixel11[i,1])],
            [(y[0] + pixel10[0]), (y[i+1]  + pixel11[i,0])],
            'wx' ,ls = '-', fillstyle='none', markersize=15
            )

        length1 = int(np.sqrt(((x[i+1] + pixel11[i,1]) - ( x[0]  + pixel10[1]))**2 + ((y[i+1]  + pixel11[i,0]) - (y[0] + pixel10[0]))**2)*resolution)
        ax[0,i].set_title("Aver\ndistance ~ {}\'\' ".format(length1))
        fig.colorbar(pmc, ax=ax[0,i])

    
    for i in range(3):
        ax[1,i].grid(b=None)
        pmc = ax[1,i].imshow(image, cmap = 'nipy_spectral')
       
        ax[1,i].plot(
            [(x[0]  + pixel20[1]), (x[i+1] + pixel21[i,1])],
            [(y[0] + pixel20[0]), (y[i+1]  + pixel21[i,0])],
            'wx' ,ls = '-', fillstyle='none', markersize=15
            )

        length1 = int(np.sqrt(((x[i+1] + pixel21[i,1]) - ( x[0]  + pixel20[1]))**2 + ((y[i+1]  + pixel21[i,0]) - (y[0] + pixel20[0]))**2)*resolution)
        ax[1,i].set_title("Bright\n distance ~ {}\'\' ".format(length1))
        fig.colorbar(pmc, ax=ax[1,i])

    
       
   
        
    plt.tight_layout()
    plt.savefig('/home/conpucter/GitHub/IDL_practice/ind/task3.png', transparent=False, dpi=880, bbox_inches="tight")
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
        
    indent = 10
    loop_pic = image_input[
        np.amin(position[:,0]) - indent : np.amax(position[:,0]) + indent,
        np.amin(position[:,1]) - indent : np.amax(position[:,1]) + indent
        ]
    
    '''
    print(np.amin(position[:,0]), np.amin(position[:,1]), "\n",
    np.amax(position[:,0]), np.amax(position[:,1])
    )
    '''
    #plot_picture(loop_pic, True, inf = level, sup = 10000 , step = 1000, colours = 'Greys')
    #plot_picture(loop_pic, False)
    
    return(loop_pic)


#your ad could be here 

loops = loop_finder(image_data, level)

loop1 = loops[ 25 : 85, 5 : 30]
#loop2 = loops[ 6 : , 32 : ]
loop2_1 = loops[ 12 : 74 , 35 : 54 ]
loop2_2 = loops[ 73 : 85 , 48 : 61 ]
loop2_3 = loops[ 98 : 143 , 49 : 78 ]
#plot_picture(loop2_1, False)

general_plot(loops, loop1, loop2_1, loop2_2, loop2_3)
