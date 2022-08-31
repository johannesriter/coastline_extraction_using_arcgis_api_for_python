import os
import glob
from zipfile import *

import arcgis
import arcpy
from arcpy.management import PolygonToLine
from datetime import datetime
import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
from arcgis.raster.analytics import convert_feature_to_raster, convert_raster_to_feature
from arcgis.geoanalytics.manage_data import clip_layer
from arcgis.raster.functions import equal_to, greater_than, clip, apply, extract_band, stretch

