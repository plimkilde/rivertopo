from rivertopo.snapping import SnapResult

import numpy as np

import bisect

def get_snap_results_by_feature(snap_results):
    snap_results_by_feature = {}
    for snap_result in snap_results:
        feature = snap_result.feature
        if feature in snap_results_by_feature:
            # Insert this SnapResult to preserve ordering by chainage
            bisect.insort(snap_results_by_feature[feature], snap_result, key=lambda snap_result: snap_result.chainage)
        else:
            snap_results_by_feature[feature] = [snap_result]

    return snap_results_by_feature

def feature_interp(snap_results, chainage, offset):
    

def raster_interp(parameterized_raster, snap_results_by_feature):
    unique_features = np.unique(parameterized_raster.feature)
    interp_raster = np.full_like(parameterized_raster.feature, np.nan)
    for feature_id in unique_features:
        feature_mask = parameterized_raster.feature == feature_id
        interp_raster[feature_mask] = 
