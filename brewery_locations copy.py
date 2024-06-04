# Importing required libraries
import requests

# Define breweries with additional breweries added
breweries = {
    "1 For All": "Livonia, MI",
    "Abberant": "Howell, MI",
    "Aberrrant Ales Brewery": "Howell, MI",
    "Allagash": "Portland, ME",
    "Arbor": "Ann Arbor/Plymouth, MI",
    "Arclight": "Watervliet, MI",
    "Arctic Circle": "Chesterfield, MI",
    "Ascension": "Novi, MI",
    "Austin Street": "Portland, ME",
    "Baffin": "St. Claire Shores, MI",
    "Battery Steele": "Portland, ME",
    "Bearded Lamb": "Plymouth, MI",
    "Big Lake": "Holland, MI",
    "Bissell Brothers": "Portland, ME",
    # Add all the breweries here...
}

breweries_extended = {
    "Block": "Howell, MI",
    "Blue Skies": "Auburn Hills, MI",
    "Brew Dog": "Cleveland, OH",
    "Brewery Becker": "Brighton, MI",
    "Burzurk": "Grand Haven, MI",
    "Cadillac Straits": "Madison Heights, MI",
    "Canton Brew Works": "Canton, MI",
    "Coopersville Brewing": "Coopersville, MI",
    "Copper Hop": "St. Claire Shores, MI",
    "Dark Horse": "Marshall, MI",
    "Definitive": "Portland, ME",
    "Dog & Pony Show": "Oak Park, MI",
    "Drafting Table": "Wixom, MI",
    "Erie Brewing": "Erie, PA",
    "Eternity": "Howell, MI",
    "Farm Club": "Traverse City, MI",
    "Farmington Brewing": "Farmington, MI",
    "Feathered Friend": "Concord, NH",
    "Ferndale Project": "Ferndale, MI",
    "Fetch": "Whitehall, MI",
    "Fiddlehead": "Shelburne, VT",
    "Five Shores": "Beulah, MI",
    "Foam": "Burlington, VT",
    "Foulmouthed": "Portland, ME",
    "Foundation": "Portland, ME",
    "Founders": "Grand Rapids, MI",
    "Fresh Coast": "Traverse City, MI",
    "Goodfire": "Portland, ME",
    "Grand Armory": "Grand Haven, MI",
    "Great White Buffalo": "Northville, MI",
    "GravCap": "Oxford, MI",
    "Griffin Claw": "Rochester Hills, MI",
    "Guardian": "Saugatuck, MI",
    "Haymarket": "Bridgman, MI",
    "Heights": "Farmington, MI",
    "Home Grown": "Oxford, MI",
    "Homes": "Ann Arbor, MI",
    "Hop Lot": "Suttons Bay, MI",
    "Jamesport": "Ludington, MI",
    "Jamex": "St. Claire Shores, MI",
    "Lake Ann Brewing": "Lake Ann, MI",
    "Livery": "Benton Harbor, MI",
    "Loaded Dice": "Troy, MI",
    "Lone Pine": "Portland, ME",
    "Lunkenheimer": "Weedsport, NY",
    "Macatawa Ales": "Holland, MI",
    "Maine Beer Co": "Freeport, ME",
    "Mast Landing": "Freeport, ME",
    "Middlecoast": "Traverse City, MI",
    "Mitten": "Northport, MI",
    "New Holland": "Holland, MI",
    "North Center": "Northville, MI",
    "North Grove": "Montague, MI",
    "North Peak": "Traverse City, MI",
    "North Pier": "Benton Harbor, MI",
    "Northville Winery and Brewing": "Northville, MI",
    "Oddside": "Grand Haven, MI",
    "One Drop": "Oxford, MI",
    "Our Brewing": "Holland, MI",
    "Parker's Hilltop": "Clarkston, MI",
    "Paw Paw Brewing": "Paw Paw, MI",
    "Pigeon Hill": "Muskegon, MI",
    "Portland Zoo": "Portland, ME",
    "Rare Bird": "Traverse City, MI",
    "Right Brain": "Traverse City, MI",
    "Rising Tide": "Portland, ME",
    "Rochester Mills": "Auburn Hills, MI",
    "Rustic Leaf": "Waterford, MI",
    "Salty Pecker": "Muskegon, MI",
    "Saugatuck Brewing": "Douglas, MI",
    "Seedz": "Union Pier, MI",
    "Shorts": "Bellaire, MI",
    "Silver Harbor": "St. Joseph, MI",
    "Silver Spruce": "Traverse City, MI",
    "St. Ambrose": "Beulah, MI",
    "Starving Artist": "Ludington, MI",
    "Stormcloud": "Frankfort, MI",
    "Supernatural": "Livonia, MI",
    "The Alchemist": "Stowe, VT",
    "The Filling Station": "Traverse City, MI",
    "The Highway Brewery": "West Branch, MI",
    "The Livery": "Benton Harbor, MI",
    "The Mitten": "Northport, MI",
    "The Workshop": "Traverse City, MI",
    "Third Life": "Manistee, MI",
    "Townies": "Ann Arbor, MI",
    "Trail Point": "Allendale, MI",
    "Transient": "Bridgman, MI",
    "Tree House": "Charlton, MA",
    "Trippelroot": "Zeeland, MI",
    "Unexpected": "Oak Park, MI",
    "Unruly": "Muskegon, MI",
    "Urbanrest": "Ferndale, MI",
    "Von Trapp": "Stowe, VT",
    "Watermark": "Stevensville, MI",
    "Waypost": "Fennville, MI",
    "Wax Wings": "Kalamazoo, MI",
    "Wolverine State": "Ann Arbor, MI",
    "Zero Gravity": "Burlington, VT",
}

# Create a dictionary to store brewery locations
brewery_locations = {}

# Iterate through breweries and get their coordinates
for brewery, location in breweries.items():
    try:
        # Make a request to OpenStreetMap Nominatim API to get coordinates
        url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json&limit=1"
        response = requests.get(url)
        data = response.json()
        
        # If coordinates are found, add them to brewery_locations dictionary
        if data:
            brewery_locations[brewery] = {
                'name': brewery,
                'location': (float(data[0]['lat']), float(data[0]['lon']))
            }
        else:
            print(f"Location not found for {brewery}")
    except Exception as e:
        print(f"Error processing {brewery}: {str(e)}")

# Generate HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<title>Breweries Map</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>
<body>

<h1>Breweries Map</h1>

<!--The div element for the map -->
<div id="map" style="height: 600px;"></div>

<script>
// Initialize the map
var map = L.map('map').setView([39.8283, -98.5795], 4); // Default to the center of the US

// Add the OpenStreetMap tiles as the base layer of the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}}).addTo(map);

// Add markers to the map
var breweries = {brewery_locations};

for (var brewery in breweries) {{
    L.marker(breweries[brewery]['location']).addTo(map)
        .bindPopup(breweries[brewery]['name']);
}}
</script>

</body>
</html>
"""

# Write HTML content to file
with open("breweries_map.html", "w") as f:
    f.write(html_content)

