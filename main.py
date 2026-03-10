from input_system.camera_input import start_camera
from simulation.virtual_world import start_simulation
from models.world_model import WorldModel

def main():
    print("Starting Mini World Model AI System")

    camera_data = start_camera()
    sim_env = start_simulation()

    wm = WorldModel()
    wm.run(camera_data, sim_env)

if __name__ == "__main__":
    main()
