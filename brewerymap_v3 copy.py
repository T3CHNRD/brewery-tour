import folium

# Dictionary of tours with breweries and their coordinates
breweries_by_tour = {
    "2022 New England Tour": [
        ("Allagash", 43.6793, -70.2941),
        ("Austin Street", 43.6532, -70.2596),
        ("Battery Steele", 43.6615, -70.2780),
        # Rest of the breweries for this tour...
    ],
    "2023 Michigan West Coast Tour": [
        ("Arbor", 42.2808, -83.7430),
        ("Arclight", 42.1842, -86.2553),
        # Rest of the breweries for this tour...
    ],
    "2024 Local Tour": [
        ("Abberant", 42.6073, -83.9293),
        ("Aberrrant Ales Brewery", 42.6076332, -83.9314247),
        ("Arbor", 42.2808256, -83.7430378),
        # Rest of the breweries for this tour...
    ],
    "Random": [
        ("1 For All", 42.3684, -83.3527),
        ("Arctic Circle", 42.6666, -82.8339),
        ("Ascension", 42.4806, -83.4755),
        # Rest of the breweries for this tour...
    ]
}

# List of closed breweries
closed_breweries = [
    ("Foulmouthed (closed)", 43.64096989999999, -70.2551637),
    ("Guardian (closed)", 42.6855157, -86.16395650000001),
    ("Macatawa Ales (closed)", 42.7935833, -86.1092908),
    ("North Center (closed)", 42.4385213, -83.4832947),
    ("One Drop (closed)", 42.8284296, -83.2708872),
    ("Salty Pecker (closed)", 43.1888315, -86.2507936),
    ("Townies (closed)", 42.2739665, -83.779095)
]

# Tour colors
tour_colors = {
    "2022 New England Tour": "green",
    "2023 Michigan West Coast Tour": "purple",
    "2024 Local Tour": "orange",
    "Random": "brown"
}

# Create a map centered around a central point in the US
m = folium.Map(location=[43.0, -85.0], zoom_start=5)

# Create feature groups for each tour
tour_layers = {}
for tour, breweries in breweries_by_tour.items():
    tour_layers[tour] = folium.FeatureGroup(name=tour)
    color = tour_colors.get(tour, "blue")  # Default color is blue
    for brewery in breweries:
        folium.Marker(
            location=[brewery[1], brewery[2]],
            popup=brewery[0],
            icon=folium.Icon(color=color, icon='beer', prefix='fa')
        ).add_to(tour_layers[tour])
    m.add_child(tour_layers[tour])

# Add closed breweries to the map
closed_layer = folium.FeatureGroup(name="Closed Breweries", show=False)
for brewery in closed_breweries:
    folium.Marker(
        location=[brewery[1], brewery[2]],
        popup=brewery[0],
        icon=folium.Icon(color='red', icon='beer', prefix='fa')
    ).add_to(closed_layer)
m.add_child(closed_layer)

# Add layer control to the map
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save("breweries_mapV3.html")
