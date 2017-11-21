"""geonum example script 2

Introduction into the GeoSetup class
"""

from geonum import GeoPoint, GeoVector3D, GeoSetup
from matplotlib.pyplot import show, close, rcParams
from os.path import join
from os import getcwd
### Set save directory for figures
save_path = join(getcwd(), "scripts_out")

rcParams["font.size"] = 12
def create_geosetup():
    s = GeoSetup() 
    
    #Create two GeoPoints for source and instrument
    source = GeoPoint(37.751005,  14.993435, name="source")
    camera = GeoPoint(37.73122,  15.1129, name="cam")
    
    # Add the two GeoPoints to the GeoSetup
    s.add_geo_points(source, camera)
    s.set_borders_from_points()
    
    # Create plume vector anchored at source pointing south with horizontal
    # orientation (elevation angle 0)
    plume = GeoVector3D(azimuth=180, dist_hor=s.magnitude,
                        elevation=0, anchor=source, name="plume")
    # Create viewing direction vector anchored at instrument pointing west
    # at elevation angle of 8deg
    view_dir = GeoVector3D(azimuth=270, dist_hor=s.magnitude,
                           elevation=8, anchor=camera, name="cam_view")
            
    # Add the two GeoVectors to the GeoSetup class                        
    s.add_geo_vectors(plume, view_dir)
    return s
    
def plot_geosetup(geosetup):
    # Now plot 2D and 3D overview maps
    map2d = geosetup.plot_2d()
    map3d = geosetup.plot_3d()
    
    show()
    
    return map2d, map3d
    
if __name__ == "__main__":
    close("all")
    s = create_geosetup()
    map2d, map3d = plot_geosetup(s)
    map2d.ax.figure.savefig(join(save_path, "ex2_out_1_map2D.png"))
    map3d.ax.figure.savefig(join(save_path, "ex2_out_2_map3D.png"))