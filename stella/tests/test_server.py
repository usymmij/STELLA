import carla

def test_connection():
    client = carla.Client('10.8.0.6', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

if __name__=="__main__":
    test_connection()

