import gmplot
apikey = 'AIzaSyAO-r75d8IVw3xwou82zXbABZnrNUFSKGY'
gmap = gmplot.GoogleMapPlotter.from_geocode('Durham, USA', apikey=apikey)
gmap.directions(
    (35.934148621283974, -79.05441011753976),
    (36.001668809949706, -78.9382286021942),
    travel_mode = 'DRIVING',
    waypoints=[
        (35.97784180109238, -78.96777517521043)
    ]
)
gmap.draw('directions.html')