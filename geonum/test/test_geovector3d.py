import pytest
import geonum.geovector3d as mod

def test_GeoVector3D___init__NO_INPUT():
    with pytest.raises(ValueError):
        mod.GeoVector3D()