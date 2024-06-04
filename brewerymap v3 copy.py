import folium

# Dictionary of tours with breweries and their coordinates
breweries_by_tour = {
    "2022 New England Tour": [
        ("Allagash", 43.6793, -70.2941),
        ("Austin Street", 43.6532, -70.2596),
        ("Battery Steele", 43.6615, -70.2780),
        ("Bissel Brothers", 43.65147289999999, -70.29046040000001),
        ("Brew Dog", 41.49270500000001, -81.69802399999999),
        ("Definitive", 43.7026293, -70.31912190000001),
        ("Erie Brewing Company", 42.111482, -80.1128909),
        ("Feathered Friend", 43.1945312, -71.5312096),
        ("Fiddlehead", 44.3661943, -73.23266079999999),
        ("Foam", 44.4791946, -73.21999900000002),
        ("Foulmouthed (closed)", 43.64096989999999, -70.2551637),
        ("Foundation", 43.6590993, -70.2568189),
        ("Goodfire", 43.6701814, -70.2559177),
        ("Lone Pine", 43.6700593, -70.2558802),
        ("Rising Tide", 43.66547750000001, -70.2572686),
        ("The Alchemist", 44.4759272, -72.7157139),
        ("Tree House", 42.13659120000001, -72.0123365),
        ("Mast Landing Brewing", 43.85758, -70.0836612),
        ("Maine Beer Company", 43.8394584, -70.12119109999999),
        ("Von Trapp", 44.470915, -72.7351224),
        ("Lunkenheimer", 43.0499113, -76.5626478),
        ("Portland Zoo", 43.6667361, -70.2549307),
        ("Zero Gravity", 44.4596487, -73.21370569999999)
    ],
    "2023 Michigan West Coast Tour": [
        # Add the breweries for the 2023 Michigan West Coast Tour here
    ],
    "2024 Local Tour": [
        # Add the breweries for the 2024 Local Tour here
    ],
    "Random": [
        # Add the breweries for the Random tour here
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
    "2022 New England Tour": "orange",
    "2023 Michigan West Coast Tour": "blue",
    "2024 Local Tour": "green",
    "Random": "purple"
}

# Create a map centered around a central point in the US
m = folium.Map(location=[43.0, -85.0], zoom_start=5)

# Add each brewery to the map with respective colors
for tour, breweries in breweries_by_tour.items():
    color = tour_colors[tour]
    for brewery in breweries:
        folium.Marker(
            location=[brewery[1], brewery[2]],
            popup=brewery[0],
            icon=folium.Icon(color=color)
        ).add_to(m)

# Add closed breweries to the map
for brewery in closed_breweries:
    folium.Marker(
        location=[brewery[1], brewery[2]],
        popup=brewery[0],
        icon=folium.Icon(color='red')
    ).add_to(m)

# Save the map to an HTML file
m.save("breweries_map.html")

# Add the statistics information
stats_html = """
<div style="position: absolute; top: 10px; left: 10px; background-color: white; padding: 10px; border: 1px solid black; z-index: 9999;">
    <p><b>Total number of breweries:</b> 113 breweries</p>
    <p><b>Total number of cities:</b> 50 cities</p>
    <p><b>Total number of states:</b> 8 states</p>
</div>
"""

# Read the generated HTML file
with open("breweries_map.html", "r") as f:
    map_html = f.read()

# Combine the map HTML and stats HTML
final_html = map_html.replace('<body>', f'<body>{stats_html}')

# Save the final HTML to a file
with open("breweries_map.html", "w") as f:
    f.write(final_html)
