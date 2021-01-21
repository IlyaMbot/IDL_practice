import matplotlib.pyplot as plt
import numpy as np

from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

plt.style.use(astropy_mpl_style) #telling astropy about using plt

filename = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_uv_24s.2011-08-09T080043Z.1600.image_lev1.fits"
#filename = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_euv_12s.2011-08-10T093446Z.304.image_lev1.fits"

image_file = get_pkg_data_filename(filename)
image_data = fits.getdata(image_file, ext=0)

bottom_val = 0
top_val = 4000
image_data[image_data < bottom_val] = bottom_val
image_data[image_data > top_val] = top_val


def plot_picture(image):
    '''
    s = 800
    image = image[
        2048 - s: 2048 + s,
        2048 - s: 2048 + s
    ]
    '''
    plt.figure()
    plt.grid(b=None)
    plt.imshow(image, cmap='nipy_spectral')
    plt.plot()
    plt.colorbar()
    plt.show()


def loop_founder(image_input, roof):
    
    if roof == 0:
        plot_picture(image_input)
        return

    p = 2
    p2 = p*2

    position = np.argwhere(image_input >= roof)
    print(len(position))
    print('=)')

    indexes = []
    ind = 0
    for point in position:
        #print(point)
        
        cut = image_input[
        point[0] - p : point[0] + p,
        point[1] - p : point[1] + p
        ]
        
        check_sum = 0
        for i in range(p2):
            for j in range(p2):
                check_sum += cut[i,j]
        
        check_sum /= p2**2
        

        if check_sum < roof:
           indexes.append(ind)
        ind +=1
    position = np.delete(position, indexes, 0)
    print(len(position))
    
    
    loop_pic = image_input[
        np.amin(position[:,0]) - p2 : np.amax(position[:,0]) + p2,
        np.amin(position[:,1]) - p2 : np.amax(position[:,1]) + p2
        ]
    
    plot_picture(loop_pic)

loop_founder(image_data, 000)
