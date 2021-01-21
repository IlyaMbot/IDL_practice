import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from scipy import ndimage
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.table import Table
from astropy.io import fits

plt.style.use(astropy_mpl_style) #telling astropy about using plt

filename = "/home/conpucter/GitHub/IDL_practice/ind/aia.lev1_uv_24s.2011-08-09T080043Z.1600.image_lev1.fits"

image_file = get_pkg_data_filename(filename)
image_data = fits.getdata(image_file, ext=0)
image_data = np.flip(image_data, 0)

#print(fits.getval(filename, "CDELT1"))

resolution = fits.getval(filename, "CDELT1")


def plot_picture(image, cont, inf = 0, sup = 1, step = 1, colours = 'nipy_spectral' ):
    ''' It plots figures '''
    size = 2048 * resolution
      
    fig, ax = plt.subplots(1, 1)
    ax.grid(b=None)

    pmc = ax.imshow(image, extent=[-size, size, -size, size], cmap = colours)
    
    if cont == True:
        ax.contour(image, levels = range(inf, sup, step), inline=True, fontsize=15, cmap = 'nipy_spectral' )

   
    fig.colorbar(pmc, ax=ax)
    
    plt.show()

plot_picture(image_data, False)