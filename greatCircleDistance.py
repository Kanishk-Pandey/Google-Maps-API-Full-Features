# Import the math module
import math
 
#Haversine formula copied off the internet 
def gcdist(lat1, lon1, lat2, lon2):
    # Begin building the code for the Great Circle Distance Formula
    # The radius in KM. We'll discuss conversion later.
    R = 6378.137
 
    # formula requires we convert all degrees to radians
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
 
    lat_span = lat1 - lat2
    lon_span = lon1 - lon2
 
    a = math.sin(lat_span / 2) ** 2
    b = math.cos(lat1)
    c = math.cos(lat2)
    d = math.sin(lon_span / 2) ** 2
 
    dist = 2 * R * math.asin(math.sqrt(a + b * c * d))
 
    return dist
 
# call the function chapel hill to durham
print(gcdist(35.934148621283974, -79.05441011753976, 36.001668809949706, -78.9382286021942))
