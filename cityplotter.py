import gmplot
apikey = 'AIzaSyAO-r75d8IVw3xwou82zXbABZnrNUFSKGY'

gmap = gmplot.GoogleMapPlotter.from_geocode('Durham, USA', apikey=apikey)
gmap.draw("cityplotter.html")