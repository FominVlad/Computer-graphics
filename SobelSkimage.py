
from scipy import ndimage,misc
from skimage import filters
from PIL import Image
import scipy

a = Image.open('images/moon.jpg')
b = filters.sobel(a)

b = scipy.misc.toimage(b)
b.save('images/moon_sobel.jpg')
