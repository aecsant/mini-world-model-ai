import pybullet as p
import pybullet_data

def start_simulation():
    p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.loadURDF("plane.urdf")
    return "Simulation Ready"
