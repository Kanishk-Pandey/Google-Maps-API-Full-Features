from tracemalloc import start
import gmaps
import gmplot
import googleMapInitial


#gmaps.configure(api_key='AIzaSyAO-r75d8IVw3xwou82zXbABZnrNUFSKGY')
#start = '12443 De Sanka Ave, Saratoga, CA 95070, USA'
#end = '805 Greenwood Rd, Chapel Hill , NC 27514, USA'
#dirs = gmaps.directions(start, end)

new_york_coordinates = (40.75, -74.00)
gmaps.figure(center = new_york_coordinates, zoom_level=12)
