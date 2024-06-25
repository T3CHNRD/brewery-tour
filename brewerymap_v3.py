import folium

# Create a map object
m = folium.Map(location=[44.0, -72.0], zoom_start=5)

# Add custom banner as HTML
banner_html = """
<div style="position: fixed; top: 10px; left: 10px; background-color: white; border: 2px solid black; padding: 10px;">
    <h3>Brewery Information</h3>
    <p>Total number of breweries: 113 breweries</p>
    <p>Total number of cities: little over 50 cities</p>
    <p>Total number of states: 8 states</p>
</div>
"""
m.get_root().html.add_child(folium.Element(banner_html))

# Add brewery markers, closed brewery markers, and layer control as before

# Save the map to an HTML file
m.save("breweries_mapV3.html")


# Dictionary of tours with breweries and their coordinates
breweries_by_tour = {
    "2022 New England Tour": [
        ["Allagash", 43.6793, -70.2941],
        ["Austin Street", 43.6532, -70.2596],
        ["Battery Steele", 43.6615, -70.2780],
        ["Bissel Brothers", 43.65147289999999, -70.29046040000001],
        ["Brew Dog", 41.49270500000001, -81.69802399999999],
        ["Definitive", 43.7026293, -70.31912190000001],
        ["Erie Brewing Company", 42.111482, -80.1128909],
        ["Feathered Friend", 43.1945312, -71.5312096],
        ["Fiddlehead", 44.3661943, -73.23266079999999],
        ["Foam", 44.4791946, -73.21999900000002],
        ["Foundation", 43.6590993, -70.2568189],
        ["Goodfire", 43.6701814, -70.2559177],
        ["Lone Pine", 43.6700593, -70.2558802],
        ["Rising Tide", 43.66547750000001, -70.2572686],
        ["The Alchemist", 44.4759272, -72.7157139],
        ["Tree House", 42.13659120000001, -72.0123365],
        ["Mast Landing Brewing", 43.85758, -70.0836612],
        ["Maine Beer Company", 43.8394584, -70.12119109999999],
        ["Von Trapp", 44.470915, -72.7351224],
        ["Lunkenheimer", 43.0499113, -76.5626478],
        ["Portland Zoo", 43.6667361, -70.2549307],
        ["Zero Gravity", 44.4596487, -73.21370569999999],
        ["Foulmouthed", 43.64096989999999, -70.2551637],
        ["Foundation", 43.6590993, -70.2568189],
        ["Goodfire", 43.6701814, -70.2559177],
        ["Lone Pine", 43.6700593, -70.2558802],
        ["Lunkenheimer", 43.0499113, -76.5626478],
        ["Maine Beer Company", 43.8394584, -70.12119109999999]
    ],
    "2023 Michigan West Coast Tour": [
        ["Burzurk Brewery, Grand Haven, MI", 43.061029, -86.20656699999999],
        ["Coopersville Brewing, Coopersville, MI", 43.0639112, -85.9347667],
        ["Dark Horse, Marshall, MI", 42.2666327, -84.96368249999999],
        ["Farm Club, Traverse City, MI", 44.8331931, -85.68986609999999],
        ["Fetch, Whitehall, MI", 43.4100107, -86.34867919999999],
        ["Five Shores, Beulah, MI", 44.6294106, -86.0939302],
        ["Fresh Coast, Traverse City, MI", 44.7633743, -85.61846299999999],
        ["Grand Armory, Grand Haven, MI", 43.0633333, -86.23166669999999],
        ["Guardian Brewing, Saugatuck, MI", 42.6855157, -86.16395650000001],
        ["Haymarket, Bridgman, MI", 41.9488144, -86.5561563],
        ["Hop Lot, Suttons Bay, MI", 44.9683952, -85.6477381],
        ["James Port Brewing, Ludington, MI", 43.9521387, -86.44793299999999],
        ["Lake Ann Brewing, Lake Ann, MI", 44.7243364, -85.84295879999999],
        ["Livery, Benton Harbor, MI", 42.11809100000001, -86.45369000000001],
        ["Middlecoast, Traverse City, MI", 44.7632755, -85.61687429999999],
        ["Mitten, Northport, MI", 45.1298496, -85.6167741],
        ["North Pier, Saint Joseph, MI", 42.1141719, -86.4858826],
        ["North Peak, Traverse City, MI", 44.764378, -85.62846689999999],
        ["North Grove, Montague, MI", 43.4171438, -86.3545625],
        ["Odd Side Ales, Grand Haven, MI", 43.0646785, -86.2328527],
        ["Paw Paw Brewing, Paw Paw, MI", 42.2102444, -85.8958679],
        ["Pigeon Hill Brewing, Muskegon, MI", 43.2358263, -86.25661],
        ["Rare Bird, Traverse City, MI", 44.7599068, -85.6196475],
        ["Right Brain, Traverse City, MI", 44.7494479, -85.61950759999999],
        ["Salty Pecker, Norton Shores, MI", 43.1888315, -86.2507936],
        ["Saugatuck Brewing Company, Douglas, MI", 42.6325682, -86.2125854],
        ["Seedz, Union Pier, MI", 41.824014, -86.6963763],
        ["Short's Brewery, Bellaire, MI", 44.97626899999999, -85.210357],
        ["Silver Harbor, Saint Joseph, MI", 42.1086412, -86.4796334],
        ["Silver Spruce, Traverse City, MI", 44.75987079999999, -85.6140738],
        ["St. Ambrose, Beulah, MI", 44.6185796, -85.9969235],
        ["Starving Artist, Ludington, MI", 43.9438614, -86.3394244],
        ["Stormcloud, Frankfort, MI", 44.632695, -86.241075],
        ["The Filling Station, Traverse City, MI", 44.7581577, -85.6096419],
        ["The Highway Brewery, West Branch, MI", 44.276464, -84.237674],
        ["The Workshop, Traverse City, MI", 44.7652017, -85.62602179999999],
        ["Third Life, Manistee, MI", 44.25044370000001, -86.3160448],
        ["Transient, Bridgman, MI", 41.9431717, -86.5557264],
        ["Trail Point, Allendale, MI", 42.9728171, -85.9351257],
        ["Unruly Brewing, Muskegon, MI", 43.2360043, -86.25247619999999],
        ["Watermark, Stevensville, MI", 42.0131665, -86.5193687],
        ["Waypost, Fennville, MI", 42.5372238, -86.2155075],
        ["Wax Wings, Kalamazoo, MI", 42.3145923, -85.5389886],
        ["Arclight Brewing, Watervliet, MI", 42.19124235, -86.25939723]
    ],
    "2024 Local Tour": [
        ["Abberant", 42.6073, -83.9293],
        ["Aberrrant Ales Brewery, Howell, MI", 42.6076332, -83.9314247],
        ["Arbor, Ann Arbor/Plymouth, MI", 42.2709969, -83.7401339],
        ["Bearded Lamb, Plymouth, MI", 42.3792447, -83.4613125],
        ["Block Brewing, Howell, MI", 42.5944315, -83.9340902],
        ["Blue Skies, Auburn Hills, MI", 42.6335214, -83.2214221],
        ["Brewery Becker, Brighton, MI", 42.52971429999999, -83.7853463],
        ["Cadillac Straits, Madison Heights, MI", 42.4953198, -83.1062528],
        ["Dog and Pony Show, Oak Park, MI", 42.4883927, -83.193612],
        ["Eternity Brewing, Howell, MI", 42.5853401, -83.8728706],
        ["Ferndale Project, Ferndale, MI", 42.4506921, -83.1431145],
        ["Great White Buffalo, Northville, MI", 42.43093280000001, -83.4833769],
        ["Heights, Farmington, MI", 42.4644795, -83.37632180000001],
        ["Rustic Leaf, Waterford, MI", 42.6614189, -83.42853099999999],
        ["Unexpected Brewing, Oak Park, MI", 42.4884504, -83.1903366],
        ["Urbanrest Brewing, Ferndale, MI", 42.468031, -83.127763]
    ],
    "Random Ongoing Tour": [
    ["1 For All", 42.3684, -83.3527],
    ["Arctic Circle, Chesterfield, MI", 42.6960659, -82.79941939999999],
    ["Ascension", 42.4806, -83.4755],
    ["Big Lake, Holland, MI", 42.7913184, -86.10790999999999],
    ["Canton Brew Works, Canton, MI", 42.3486453, -83.46110469999999],
    ["Copper Hop, St. Claire Shores, MI", 42.4656722, -82.8985046],
    ["Drafting Table, Wixom, MI", 42.5245111, -83.5379346],
    ["Farmington Brewing, Farmington, MI", 42.4644795, -83.37632180000001],
    ["Ferndale Project, Ferndale, MI", 42.4506921, -83.1431145],
    ["Founders, Grand Rapids, MI", 42.9633599, -85.6680863],
    ["GravCap, Oxford, MI", 42.8252792, -83.2649536],
    ["Griffin Claw, Rochester Hills, MI", 42.6471305, -83.17023739999999],
    ["Home Grown, Oxford, MI", 42.825524, -83.2654333],
    ["Homes, Ann Arbor, MI", 42.2808256, -83.7430378],
    ["Jamex, St. Claire Shores, MI", 42.4565087, -82.9124162],
    ["One Drop, Oxford, MI", 42.8247524, -83.26466239999999],
    ["Our Brewing, Holland, MI", 42.7901694, -86.1037278],
    ["Parker's Hilltop, Clarkston, MI", 42.71003229999999, -83.4064624],
    ["New Holland, Holland, MI", 42.8184203, -86.11422999999999],
    ["North Center, Northville, MI", 42.4385213, -83.4832947],
    ["Macatawa Ales, Holland, MI", 42.7935833, -86.1092908],
    ["Loaded Dice, Troy, MI", 42.5503064, -83.13250959999999],
    ["Rochester Mills, Auburn Hills, MI", 42.6806946, -83.1313553],
    ["Supernatural, Livonia, MI", 42.36837, -83.35270969999999],
    ["Townies, Ann Arbor, MI", 42.2739665, -83.779095],
    ["Trippelroot, Zeeland, MI", 42.8120882, -86.01469929999999],
    ["Wolverine State, Ann Arbor, MI", 42.2808256, -83.7430378],
    ["Macatawa Ales, Holland, MI", 42.7935833, -86.1092908],
    ["stumblebum brewery, Troy, MI", 42.3623, -83.0859],  
    ],
    "Favorite": [
        ["Fiddlehead", 44.3661943, -73.23266079999999],
        ["Arclight Brewing, Watervliet, MI", 42.19124235, -86.25939723],
        ["Starving Artist, Ludington, MI", 43.9438614, -86.3394244],
        ["Eternity Brewing, Howell, MI", 42.5853401, -83.8728706],
        ["Definitive", 43.7026293, -70.31912190000001],
        ["Copper Hop, St. Claire Shores, MI", 42.4656722, -82.8985046],
        ["Transient, Bridgman, MI", 41.9431717, -86.5557264],
        ["Goodfire", 43.6701814, -70.2559177],
        ["Waypost, Fennville, MI", 42.5372238, -86.2155075],
        ["Lone Pine", 43.6700593, -70.2558802],
        ["Tree House", 42.13659120000001, -72.0123365]
        ["stumblebum brewery, Troy, MI", 42.3623, -83.0859]
    ]
}

# List of closed breweries
closed_breweries = [
    ["Foulmouthed (closed)", 43.64096989999999, -70.2551637],
    ["Guardian (closed)", 42.6855157, -86.16395650000001],
    ["Macatawa Ales (closed)", 42.7935833, -86.1092908],
    ["North Center (closed)", 42.4385213, -83.4832947],
    ["One Drop (closed)", 42.8284296, -83.2708872],
    ["Salty Pecker (closed)", 43.1888315, -86.2507936],
    ["Townies (closed)", 42.2739665, -83.779095]
]

# Tour colors
tour_colors = {
    "2022 New England Tour": "green",
    "2023 Michigan West Coast Tour": "darkblue",
    "2024 Local Tour": "orange",
    "Random Ongoing Tour": "darkpurple",
    "Favorite": "darkgreen"
}

# Create a map object
m = folium.Map(location=[44.0, -72.0], zoom_start=5)

# Add brewery markers to the map
for tour, breweries in breweries_by_tour.items():
    feature_group = folium.FeatureGroup(name=tour)
    color = tour_colors[tour]
    for brewery in breweries:
        name, lat, lon = brewery
        folium.Marker(
            location=[lat, lon],
            popup=name,
            icon=folium.Icon(color=color, icon='beer', prefix='fa')
        ).add_to(feature_group)
    feature_group.add_to(m)

# Add closed brewery markers to the map
closed_feature_group = folium.FeatureGroup(name="Closed Breweries")
for brewery in closed_breweries:
    name, lat, lon = brewery
    folium.Marker(
        location=[lat, lon],
        popup=name,
        icon=folium.Icon(color='red', icon='beer', prefix='fa')  # Red color for closed breweries
    ).add_to(closed_feature_group)
closed_feature_group.add_to(m)

# Add layer control to the map
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save("breweries_mapV3.html")
