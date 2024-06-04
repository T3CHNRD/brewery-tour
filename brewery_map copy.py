import folium
from geopy.geocoders import Nominatim

# List of breweries with their city and state
breweries = [
    ("1 For All", "Livonia, MI"),
    ("Abberant", "Howell, MI"),
    ("Allagash", "Portland, ME"),
    ("Arbor", "Ann Arbor, MI"),
    ("Arclight", "Watervliet, MI"),
    ("Arctic Circle", "Chesterfield, MI"),
    ("Ascension", "Novi, MI"),
    ("Austin Street", "Portland, ME"),
    ("Baffin", "St. Clair Shores, MI"),
    ("Battery Steele", "Portland, ME"),
    # Add remaining breweries
]

# Initialize the geolocator
geolocator = Nominatim(user_agent="brewery_locator")

# Create a map centered around a central point in the US
m = folium.Map(location=[43.0, -85.0], zoom_start=5)

# Geocode each brewery and add it to the map
for brewery in breweries:
    location = geolocator.geocode(brewery[1])
    if location:
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=brewery[0],
        ).add_to(m)

# Save the map to an HTML file
m.save("breweries_map.html")
