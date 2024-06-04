import googlemaps
import time

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyBYuvLGrIIxnY20fUSAgXJqJo2k6UZFWbg')

# Full list of breweries
breweries = [
    "Aberrrant Ales Brewery, Howell, MI",
    "Arbor, Ann Arbor/Plymouth, MI",
    "Arctic Circle, Chesterfield, MI",
    "Bearded Lamb, Plymouth, MI",
    "Big Lake, Holland, MI",
    "Bissel Brothers, Portland, ME",
    "Block Brewing, Howell, MI",
    "Blue Skies, Auburn Hills, MI",
    "Brew Dog, Cleveland, OH",
    "Brewery Becker, Brighton, MI",
    "Burzurk Brewery, Grand Haven, MI",
    "Cadillac Straits, Madison Heights, MI",
    "Canton Brew Works, Canton, MI",
    "Coopersville Brewing, Coopersville, MI",
    "Copper Hop, St. Claire Shores, MI",
    "Dark Horse, Marshall, MI",
    "Definitive, Portland, ME",
    "Dog and Pony Show, Oak Park, MI",
    "Drafting Table, Wixom, MI",
    "Erie Brewing Company, Erie, PA",
    "Eternity Brewing, Howell, MI",
    "Farm Club, Traverse City, MI",
    "Farmington Brewing, Farmington, MI",
    "Feathered Friend, Concord, NH",
    "Ferndale Project, Ferndale, MI",
    "Fetch, Whitehall, MI",
    "Fiddlehead, Shelburne, VT",
    "Five Shores, Beulah, MI",
    "Foam, Burlington, VT",
    "Foulmouthed, Portland, ME",
    "Foundation, Portland, ME",
    "Founders, Grand Rapids, MI",
    "Fresh Coast, Traverse City, MI",
    "Goodfire, Portland, ME",
    "Grand Armory, Grand Haven, MI",
    "Great White Buffalo, Northville, MI",
    "GravCap, Oxford, MI",
    "Griffin Claw, Rochester Hills, MI",
    "Guardian Brewing, Saugatuck, MI",
    "Haymarket, Bridgman, MI",
    "Heights, Farmington, MI",
    "Home Grown, Oxford, MI",
    "Homes, Ann Arbor, MI",
    "Hop Lot, Suttons Bay, MI",
    "James Port Brewing, Ludington, MI",
    "Jamex, St. Claire Shores, MI",
    "Lake Ann Brewing, Lake Ann, MI",
    "Livery, Benton Harbor, MI",
    "Loaded Dice, Troy, MI",
    "Lone Pine, Portland, ME",
    "Lunkenheimer, Weedsport, NY",
    "Macatawa Ales, Holland, MI",
    "Maine Beer Company, Freeport, ME",
    "Mast Landing Brewing, Freeport, ME",
    "Middlecoast, Traverse City, MI",
    "Mitten, Northport, MI",
    "New Holland, Holland, MI",
    "North Center, Northville, MI",
    "North Grove, Montague, MI",
    "North Peak, Traverse City, MI",
    "North Pier, Saint Joseph, MI",
    "Northville Winery and Brewing, Northville, MI",
    "Odd Side Ales, Grand Haven, MI",
    "One Drop, Oxford, MI",
    "Our Brewing, Holland, MI",
    "Parker's Hilltop, Clarkston, MI",
    "Paw Paw Brewing, Paw Paw, MI",
    "Pigeon Hill Brewing, Muskegon, MI",
    "Portland Zoo, Portland, ME",
    "Rare Bird, Traverse City, MI",
    "Right Brain, Traverse City, MI",
    "Rising Tide, Portland, ME",
    "Rochester Mills, Auburn Hills, MI",
    "Rustic Leaf, Waterford, MI",
    "Salty Pecker, Norton Shores, MI",
    "Saugatuck Brewing Company, Douglas, MI",
    "Seedz, Union Pier, MI",
    "Short's Brewery, Bellaire, MI",
    "Silver Harbor, Saint Joseph, MI",
    "Silver Spruce, Traverse City, MI",
    "St. Ambrose, Beulah, MI",
    "Starving Artist, Ludington, MI",
    "Stormcloud, Frankfort, MI",
    "Supernatural, Livonia, MI",
    "The Alchemist, Stowe, VT",
    "The Filling Station, Traverse City, MI",
    "The Highway Brewery, West Branch, MI",
    "The Mitten, Northport, MI",
    "The Workshop, Traverse City, MI",
    "Third Life, Manistee, MI",
    "Townies, Ann Arbor, MI",
    "Trail Point, Allendale, MI",
    "Transient, Bridgman, MI",
    "Tree House, Charlton, MA",
    "Trippelroot, Zeeland, MI",
    "Unexpected Brewing, Oak Park, MI",
    "Unruly Brewing, Muskegon, MI",
    "Urbanrest Brewing, Ferndale, MI",
    "Von Trapp, Stowe, VT",
    "Watermark, Stevensville, MI",
    "Waypost, Fennville, MI",
    "Wax Wings, Kalamazoo, MI",
    "Wolverine State, Ann Arbor, MI",
    "Zero Gravity, Burlington, VT"
]

# Dictionary to hold brewery names and their coordinates
brewery_coordinates = {}

for brewery in breweries:
    try:
        geocode_result = gmaps.geocode(brewery)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            brewery_coordinates[brewery] = (location['lat'], location['lng'])
            print(f"{brewery}: {location['lat']}, {location['lng']}")
        else:
            print(f"{brewery}: Location not found")
        time.sleep(0.1)  # to respect the service usage limit
    except Exception as e:
        print(f"Error with {brewery}: {e}")

# Print the results
print("\nBrewery Coordinates:")
for brewery, coords in brewery_coordinates.items():
    print(f"{brewery}: {coords}")
