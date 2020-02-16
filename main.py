import folium
import pandas
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def read_file(path):
    '''
    (string) -> None

    Reads the file and adds all the
    '''
    print("HUY")
    # Setting up geopy
    geolocator = Nominatim(user_agent="LastGenius", timeout=1)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.01)

    print("HUY1")
    # Reading the file
    data = pandas.read_csv(path, error_bad_lines=False, warn_bad_lines=False)
    movie = data['movie']
    year = data['year']
    location = data['location']
    movie_data = zip(movie, year, location)

    used_locations_dict = dict()

    print("HUY2")
    with open('locations_final.csv', "w") as file:
        for movie in movie_data:
            try:
                location_name = movie[2].strip("/n")
                if location_name in used_locations_dict:
                    coordinates = used_locations_dict[location_name]
                else:
                    coordinates = geolocator.geocode(location_name)
                    coordinates = (coordinates.latitude, coordinates.longitude)
                    used_locations_dict[location_name] = coordinates
                print(movie, coordinates[0], coordinates[1])
                file.write(','.join([movie[0], movie[1], location_name, coordinates[0], coordinates[1]]))
            except:
                continue


def main():
    # year = input("Please enter a year you would like to have a map for: ")
    # lat, long = map((lambda x: float(x)), input("Please enter your location (format: lat, long): ").split(", "))
    path = "locations.csv"
    # map = folium.Map()
    read_file(path)
    # location_data = read_location(movies)
    # print(location_data)
    # map.save("map.html")


if __name__ == '__main__':
    main()

