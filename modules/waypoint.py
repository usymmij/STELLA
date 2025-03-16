import carla

class Waypoint:

    def __init__(self, latitude, longitude, altitude=0.0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def to_geolocation(self):
        #Converts the waypoint to a CARLA GeoLocation.
        return carla.GeoLocation(latitude=self.latitude, longitude=self.longitude, altitude=self.altitude)

    def print(self):
        return f"Waypoint(latitude={self.latitude}, longitude={self.longitude}, altitude={self.altitude})"