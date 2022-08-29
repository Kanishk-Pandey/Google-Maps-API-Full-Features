import gmplot

lat = [19.0590, 19.0810, 19.0850]
lang = [72.890, 72.910, 72.930]
gmapOne = gmplot.GoogleMapPlotter(19.0760, 72.8777, 15)

gmapOne.scatter(lat, lang, 'red', size = 50, marker = False)
gmapOne.plot(lat, lang, 'blue', edge_width = 2.5)

gmapOne.heatmap(lat, lang)
gmapOne.polygon(lat, lang, color = 'green')

gmapOne.draw("googleMapInitial.html")
