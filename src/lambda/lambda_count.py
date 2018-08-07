from __future__ import print_function
import json
import rasterio
import os
import numpy as np
from pprint import pprint
import collections

print('Loading function')

def handler(event, context):
    print('starting handler..')

def lambda_handler(event, context):
    print('starting..')
    land_cover_legend = {
        0:	'Water',
        1:	'Evergreen Needleleaf forest',
        2:	'Evergreen Broadleaf forest',
        3:	'Deciduous Needleleaf forest',
        4:	'Deciduous Broadleaf forest',
        5:	'Mixed forest',
        6:	'Closed shrublands',
        7:	'Open shrublands',
        8:	'Woody savannas',
        9:	'Savannas',
        10:	'Grasslands',
        11:	'Permanent wetlands',
        12:	'Croplands',
        13:	'Urban and built-up',
        14:	'Cropland/Natural vegetation mosaic',
        15:	'Snow and ice',
        16:	'Barren or sparsely vegetated',
        254:	'Unclassified',
        255:	'Fill Value'
    }
    
    land_cover_count = {
        0:	0,
        1:	0,
        2:	0,
        3:	0,
        4:	0,
        5:	0,
        6:	0,
        7:	0,
        8:	0,
        9:	0,
        10:	0,
        11:	0,
        12:	0,
        13:	0,
        14:	0,
        15:	0,
        16:	0,
        254: 0,
        255: 0
    }
    
    # reading the landcover raster
    land_cover_file = 's3://yogesh-test-123/mydataset_raw.tif'
    with rasterio.open(land_cover_file) as dem_raster:
        bbox = dem_raster.bounds
        mask_geom = {
                    'type': 'Feature',
                    'bbox': [bbox[0],bbox[1],bbox[2],bbox[3]],
                    'geometry': {
                        'type': 'Polygon',
                        'coordinates': [[
                            [bbox[0], bbox[1]],
                            [bbox[2], bbox[1]],
                            [bbox[2], bbox[3]],
                            [bbox[0], bbox[3]],
                            [bbox[0], bbox[1]]]]}
                        }
        '''
        pixel_values, out_transform = mask_tool(dem_raster, mask_geom,
                                                     crop=True, invert=False,
                                                     all_touched=False)
        '''
        pixel_values = dem_raster.read(1)  # band number
        print(pixel_values.shape)
        for key in land_cover_count.keys():
            land_cover_count[key] = np.count_nonzero(pixel_values == key)
    
    # populating the results
    result = []
    for key in land_cover_legend.keys():
        result.append({'index' : key,
                        'name': land_cover_legend[key],
                        'count': land_cover_count[key]
        })
        
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

if __name__ == "__main__":
    pprint(lambda_handler(None, None))
