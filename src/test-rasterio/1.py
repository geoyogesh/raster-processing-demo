# %matplotlib inline

from osgeo import gdal
import rasterio
import matplotlib.pyplot as plt
import os

import warnings
warnings.filterwarnings("always")
import numpy as np
np.seterr(divide='ignore', invalid='ignore')


def ndvi(red, nir):
    """Calculate NDVI."""
    return (nir - red) / (nir + red)


# Here's the red band from a landsat 8 scene.

base_path = '/Users/yogeshd/Documents/GitHub/raster-processing-demo/src/test-rasterio/data/landsat/LC08_L1TP_015034_20180708_20180717_01_T1'
L8_RED_fn = os.path.join(base_path, 'LC08_L1TP_015034_20180708_20180717_01_T1_B4.TIF')
L8_NIR_fn = os.path.join(base_path, 'LC08_L1TP_015034_20180708_20180717_01_T1_B5.TIF')
L8_QA_fn = os.path.join(base_path, 'LC08_L1TP_015034_20180708_20180717_01_T1_BQA.TIF')

'''
base_path = '/Users/yogeshd/Documents/GitHub/raster-processing-demo/src/test-rasterio/data/landsat/1'
L8_RED_fn = os.path.join(base_path, 'LC08_L1TP_042034_20130605_20170310_01_T1_B4_120x120.TIF')
L8_NIR_fn = os.path.join(base_path, 'LC08_L1TP_042034_20130605_20170310_01_T1_B5_120x120.TIF')
L8_QA_fn = os.path.join(base_path, 'LC08_L1TP_042034_20130605_20170310_01_T1_BQA_120x120.TIF')
'''

ds = gdal.Open(L8_RED_fn)

# Let's extract and plot the pixel values
pixel_values = ds.ReadAsArray()
plt.imshow(pixel_values)
plt.colorbar()

# and here's the geospatial projection Well-Known Text and the Affine Geotransform
print(ds.GetProjection())
print(ds.GetGeoTransform())

with rasterio.open(L8_RED_fn) as dem_raster:
    pixel_values = dem_raster.read(1)  # band number
    print(dem_raster.crs)   # This is returned as a dict version of the PROJ.4 format string.
    print(dem_raster.transform)  # Returns the GDAL-style Affine Geotransform. (will be deprecated in rasterio 1.0)


red_ds = gdal.Open(L8_RED_fn)
red_band = red_ds.GetRasterBand(1)
red = red_band.ReadAsArray()
plt.imshow(red)
plt.colorbar()

nir_ds = gdal.Open(L8_NIR_fn)
nir_band = nir_ds.GetRasterBand(1)
nir = nir_band.ReadAsArray()
plt.imshow(nir)
plt.colorbar()

plt.imshow(ndvi(red, nir))
plt.colorbar()

nir_ds = gdal.Open(L8_NIR_fn)
nir_band = nir_ds.GetRasterBand(1)
nir = nir_band.ReadAsArray()
plt.imshow(nir)
plt.colorbar()


# This band does not have a nodata value!
print(red_band.GetNoDataValue())


qa_ds = gdal.Open(L8_QA_fn)
qa_band = qa_ds.GetRasterBand(1)
qa = qa_band.ReadAsArray()


def ndvi_with_nodata(red, nir, qa):
    ndvi = (nir - red) / (nir + red)
    ndvi[qa == 1] = -1
    return ndvi


ndvi = ndvi_with_nodata(red, nir, qa)
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()


with rasterio.open(L8_RED_fn) as red_raster:
    source_crs = red_raster.crs
    source_transform = red_raster.transform

with rasterio.open('data/output/ndvi.tif', 'w', driver='GTIff',
                   height=ndvi.shape[0],    # numpy of rows
                   width=ndvi.shape[1],     # number of columns
                   count=1,                        # number of bands
                   dtype=rasterio.dtypes.float64,  # this must match the dtype of our array
                   crs=source_crs,
                   transform=source_transform) as ndvi_raster:
    ndvi_raster.write(ndvi, 1)  # optional second parameter is the band number to write to
    ndvi_raster.nodata = -1  # set the raster's nodata value


print('completed..')
