# %matplotlib inline

from osgeo import gdal
import rasterio
import matplotlib.pyplot as plt
import os

# Here's the red band from a landsat 8 scene.
base_path = '/Users/yogeshd/Documents/GitHub/raster-processing-demo/src/test-rasterio/data/landsat/LC08_L1TP_015034_20180708_20180717_01_T1'
L8_RED_fn = os.path.join(base_path, 'LC08_L1TP_015034_20180708_20180717_01_T1_B4.TIF')

ds = gdal.Open(L8_RED_fn)

# Let's extract and plot the pixel values
pixel_values = ds.ReadAsArray()
plt.imshow(pixel_values)
plt.colorbar()

# and here's the geospatial projection Well-Known Text and the Affine Geotransform
print(ds.GetProjection())
print(ds.GetGeoTransform())
