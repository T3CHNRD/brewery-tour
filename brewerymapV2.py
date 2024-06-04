import folium
from folium import FeatureGroup

# List of breweries with their coordinates (latitude, longitude)
breweries = [
    ("1 For All", 42.3684, -83.3527),
    ("Abberant", 42.6073, -83.9293),
    ("Allagash", 43.6793, -70.2941),
    ("Arbor", 42.2808, -83.7430),
    ("Arclight", 42.1842, -86.2553),
    ("Arctic Circle", 42.6666, -82.8339),
    ("Ascension", 42.4806, -83.4755),
    ("Austin Street", 43.6532, -70.2596),
    ("Baffin", 42.4970, -82.8909),
    ("Battery Steele", 43.6615, -70.2780),
    ("Aberrrant Ales Brewery", 42.6076332, -83.9314247),
    ("Arbor", 42.2808256, -83.7430378),
    ("Arctic Circle", 42.6960659, -82.79941939999999),
    ("Bearded Lamb", 42.3792447, -83.4613125),
    ("Big Lake", 42.7913184, -86.10790999999999),
    ("Bissel Brothers", 43.65147289999999, -70.29046040000001),
    ("Block Brewing", 42.5944315, -83.9340902),
    ("Blue Skies", 42.6335214, -83.2214221),
    ("Brew Dog", 41.49270500000001, -81.69802399999999),
    ("Brewery Becker", 42.52971429999999, -83.7853463),
    ("Burzurk Brewery", 43.061029, -86.20656699999999),
    ("Cadillac Straits", 42.4953198, -83.1062528),
    ("Canton Brew Works", 42.3486453, -83.46110469999999),
    ("Coopersville Brewing", 43.0639112, -85.9347667),
    ("Copper Hop", 42.4656722, -82.8985046),
    ("Dark Horse", 42.2666327, -84.96368249999999),
    ("Definitive", 43.7026293, -70.31912190000001),
    ("Dog and Pony Show", 42.4883927, -83.193612),
    ("Drafting Table", 42.5245111, -83.5379346),
    ("Erie Brewing Company", 42.111482, -80.1128909),
    ("Eternity Brewing", 42.5853401, -83.8728706),
    ("Farm Club", 44.8331931, -85.68986609999999),
    ("Farmington Brewing", 42.4644795, -83.37632180000001),
    ("Feathered Friend", 43.1945312, -71.5312096),
    ("Ferndale Project", 42.4506921, -83.1431145),
    ("Fetch", 43.4100107, -86.34867919999999),
    ("Fiddlehead", 44.3661943, -73.23266079999999),
    ("Five Shores", 44.6294106, -86.0939302),
    ("Foam", 44.4791946, -73.21999900000002),
    ("Foulmouthed (closed)", 43.64096989999999, -70.2551637),
    ("Foundation", 43.6590993, -70.2568189),
    ("Founders", 42.9633599, -85.6680863),
    ("Fresh Coast", 44.7633743, -85.61846299999999),
    ("Goodfire", 43.6701814, -70.2559177),
    ("Grand Armory", 43.0633333, -86.23166669999999),
    ("Great White Buffalo", 42.43093280000001, -83.4833769),
    ("GravCap", 42.8252792, -83.2649536),
    ("Griffin Claw", 42.6471305, -83.17023739999999),
    ("Guardian Brewing", 42.6855157, -86.16395650000001),
    ("Haymarket", 41.9488144, -86.5561563),
    ("Heights", 42.4644795, -83.37632180000001),
    ("Home Grown", 42.825524, -83.2654333),
    ("Homes", 42.2808256, -83.7430378),
    ("Hop Lot", 44.9683952, -85.6477381),
    ("James Port Brewing", 43.9521387, -86.44793299999999),
    ("Jamex", 42.4565087, -82.9124162),
    ("Lake Ann Brewing", 44.7243364, -85.84295879999999),
    ("Livery", 42.11809100000001, -86.45369000000001),
    ("Loaded Dice", 42.5503064, -83.13250959999999),
    ("Lone Pine", 43.6700593, -70.2558802),
    ("Lunkenheimer", 43.0499113, -76.5626478),
    ("Macatawa Ales", 42.7935833, -86.1092908),
    ("Maine Beer Company", 43.8394584, -70.12119109999999),
    ("Mast Landing Brewing", 43.85758, -70.0836612),
    ("Middlecoast", 44.7632755, -85.61687429999999),
    ("Mitten", 45.1298496, -85.6167741),
    ("New Holland", 42.790068, -86.10419999999999),
    ("North Center", 42.4385213, -83.4832947),
    ("North Grove", 43.4171438, -86.3545625),
    ("North Peak", 44.764378, -85.62846689999999),
    ("North Pier", 42.1141719, -86.4858826),
    ("Northville Winery and Brewing", 42.4311464, -83.4832692),
    ("Odd Side Ales", 43.0646785, -86.2328527),
    ("One Drop", 42.8284296, -83.2708872),
    ("Our Brewing", 42.7901694, -86.1037278),
    ("Parker's Hilltop", 42.71003229999999, -83.4064624),
    ("Paw Paw Brewing", 42.2102444, -85.8958679),
    ("Pigeon Hill Brewing", 43.2358263, -86.25661),
    ("Portland Zoo", 43.6667361, -70.2549307),
    ("Rare Bird", 44.7599068, -85.6196475),
    ("Right Brain", 44.7494479, -85.61950759999999),
    ("Rising Tide", 43.66547750000001, -70.2572686),
    ("Rochester Mills", 42.6806946, -83.1313553),
    ("Rustic Leaf", 42.6614189, -83.42853099999999),
    ("Salty Pecker", 43.1888315, -86.2507936),
    ("Saugatuck Brewing Company", 42.6325682, -86.2125854),
    ("Seedz", 41.824014, -86.6963763),
    ("Short's Brewery", 44.97626899999999, -85.210357),
    ("Silver Harbor", 42.1086412, -86.4796334),
    ("Silver Spruce", 44.75987079999999, -85.6140738),
    ("St. Ambrose", 44.6185796, -85.9969235),
    ("Starving Artist", 43.9438614, -86.3394244),
    ("Stormcloud", 44.632695, -86.241075),
    ("Supernatural", 42.36837, -83.35270969999999),
    ("The Alchemist", 44.4759272, -72.7157139),
    ("The Filling Station", 44.7581577, -85.6096419),
    ("The Highway Brewery", 44.276464, -84.237674),
    ("The Mitten", 45.1298496, -85.6167741),
    ("The Workshop", 44.7652017, -85.62602179999999),
    ("Third Life", 44.25044370000001, -86.3160448),
    ("Townies", 42.2739665, -83.779095),
    ("Trail Point", 42.9728171, -85.9351257),
    ("Transient", 41.9431717, -86.5557264),
    ("Tree House", 42.13659120000001, -72.0123365),
    ("Trippelroot", 42.8120882, -86.01469929999999),
    ("Unexpected Brewing", 42.4884504, -83.1903366),
    ("Unruly Brewing", 43.2360043, -86.25247619999999),
    ("Urbanrest Brewing", 42.468031, -83.127763),
    ("Von Trapp", 44.470915, -72.7351224),
    ("Watermark", 42.0131665, -86.5193687),
    ("Waypost", 42.5372238, -86.2155075),
    ("Wax Wings", 42.3145923, -85.5389886),
    ("Wolverine State", 42.2808256, -83.7430378),
    ("Zero Gravity", 44.4596487, -73.21370569999999)
]

# Define tours with respective breweries
new_england_tour = [
    "Allagash", "Austin Street", "Battery Steele", "Bissel Brothers", "Brew Dog",
    "Definitive", "Erie Brewing Company", "Feathered Friend", "Fiddlehead", "Foam",
    "Foulmouthed (closed)", "Foundation", "Goodfire", "Lone Pine", "Rising Tide",
    "The Alchemist", "Tree House", "Mast Landing Brewing", "Maine Beer Company",
    "Von Trapp", "Lunkenheimer", "Portland Zoo", "Zero Gravity", "Definitive"
]

michigan_west_coast_tour = [
    "Arclight","Big Lake","Burzurk Brewery","Coopersville Brewing","Dark Horse",
    "Farm Club", "Farmington Brewing", "Ferndale Project", "Fetch", "Five Shores", "Fresh Coast",
    "Grand Armory", "Great White Buffalo", "GravCap", "Griffin Claw", "Guardian Brewing",
    "Heights", "Home Grown", "Homes", "Hop Lot", "James Port Brewing", "Jamex",
    "Lake Ann Brewing", "Livery", "Loaded Dice", "Macatawa Ales", "Middlecoast", "Mitten",
    "New Holland", "North Center", "North Grove", "North Peak", "North Pier", "Northville Winery and Brewing",
    "Odd Side Ales", "One Drop", "Our Brewing", "Parker's Hilltop", "Paw Paw Brewing",
    "Pigeon Hill Brewing", "Rare Bird", "Right Brain", "Rochester Mills", "Rustic Leaf",
    "Salty Pecker", "Saugatuck Brewing Company", "Seedz", "Short's Brewery", "Silver Harbor",
    "Silver Spruce", "St. Ambrose", "Starving Artist", "Stormcloud", "Supernatural", 
    "The Filling Station", "The Highway Brewery", "The Workshop", "Third Life", "Townies",
    "Trail Point", "Transient", "Trippelroot", "Unexpected Brewing", "Unruly Brewing",
    "Urbanrest Brewing", "Watermark", "Waypost", "Wax Wings", "Wolverine State"
]

local_tour = [
    "Aberrrant Ales Brewery", "Arbor", "Arctic Circle", "Baffin", "Brewery Becker",
    "Dog and Pony Show", "Drafting Table", "Eternity Brewing", "Farm Club", "Farmington Brewing",
    "Ferndale Project", "Fetch", "GravCap", "Heights", "Home Grown", "Homes",
    "Jamex", "Loaded Dice", "Macatawa Ales", "Middlecoast", "New Holland",
    "One Drop", "Our Brewing", "Parker's Hilltop", "Right Brain", "Rustic Leaf","Dog and Pony Show",
    "Drafting Table", "Eternity Brewing",
    "Seedz", "Silver Spruce", "Supernatural", "Townies", "Trail Point",
    "Unexpected Brewing", "Unruly Brewing", "Urbanrest Brewing", "Wolverine State"
]

random_tour = [
    "Allagash", "Battery Steele", "Definitive", "Feathered Friend", "Fiddlehead",
    "Foam", "Foundation", "Goodfire", "Lone Pine", "Portland Zoo", "Zero Gravity"
]

# Create a map centered around a central point in the US
m = folium.Map(location=[43.0, -85.0], zoom_start=5)

# Define a function to add markers to a feature group
def add_breweries_to_feature_group(feature_group, breweries, brewery_list, color):
    for brewery in breweries:
        if brewery[0] in brewery_list:
            if brewery[0] == "Foulmouthed (closed)",:
                folium.Marker(
                    location=[brewery[1], brewery[2]],
                    popup=brewery[0],
                    icon=folium.Icon(color='red')
                ).add_to(feature_group)
            else:
                folium.Marker(
                    location=[brewery[1], brewery[2]],
                    popup=brewery[0],
                    icon=folium.Icon(color=color)
                ).add_to(feature_group)

# Create feature groups for each tour
new_england_tour_group = FeatureGroup(name="2022 New England Tour")
michigan_west_coast_tour_group = FeatureGroup(name="2023 Michigan West Coast Tour")
local_tour_group = FeatureGroup(name="2024 Local Tour")
random_tour_group = FeatureGroup(name="Random")

# Add breweries to respective feature groups with different colors
add_breweries_to_feature_group(new_england_tour_group, breweries, new_england_tour, 'orange')
add_breweries_to_feature_group(michigan_west_coast_tour_group, breweries, michigan_west_coast_tour, 'blue')
add_breweries_to_feature_group(local_tour_group, breweries, local_tour, 'green')
add_breweries_to_feature_group(random_tour_group, breweries, random_tour, 'purple')

# Add feature groups to the map
new_england_tour_group.add_to(m)
michigan_west_coast_tour_group.add_to(m)
local_tour_group.add_to(m)
random_tour_group.add_to(m)

# Add layer control to switch between tours
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save("breweries_mapV2.html")
