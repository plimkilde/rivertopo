from osgeo import ogr
import numpy as np

from rivertopo.snapping import snap_points, SnapResult

ogr.UseExceptions()

def test_snap_points():
    linestring = ogr.Geometry(ogr.wkbLineString)
    linestring.AddPoint(0.0, 0.0)
    linestring.AddPoint(4.0, 3.0)
    linestring.AddPoint(6.0, 3.0)
    linestring.AddPoint(9.0, 7.0)

    feature_id = 42

    points = np.array([
        [1.0, 1.0],
        [4.5, 3.5],
        [5.5, 2.5],
    ])

    expected_results = [
        SnapResult(feature=42, segment=0, chainage=0.28, offset=-0.2),
        SnapResult(feature=42, segment=1, chainage=0.25, offset=-0.5),
        SnapResult(feature=42, segment=1, chainage=0.75, offset=0.5),
    ]

    snap_results = snap_points(points, feature_id, linestring)

    assert [actual.feature for actual in snap_results] == [expected.feature for expected in expected_results]
    assert [actual.segment for actual in snap_results] == [expected.segment for expected in expected_results]
    assert np.allclose([actual.chainage for actual in snap_results], [expected.chainage for expected in expected_results])
    assert np.allclose([actual.chainage for actual in snap_results], [expected.chainage for expected in expected_results])
