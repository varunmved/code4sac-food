import simplejson, urllib
from flask import Flask

app = Flask(__name__)

@app.route("/<float:lat>/<float:longi>")
def getlatLong(lat,longi):
  orig_lat = str(lat) 
  orig_lng = str(longi) 
  
  dest_lat = str(38.79679)
  dest_lng = str(-121.270001) 

  orig_coord = orig_lat, orig_lng
  dest_coord = dest_lat, dest_lng

  url1 ='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + orig_lat + ',' + orig_lng
  url2 = '&destinations=' + dest_lat + ',' + dest_lng
  url3 = '&mode=transit&key=AIzaSyDDDS1uGbOkErUSkZSz_emsuvwCGT8dBSI'
  #url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false&key=AIzaSyDDDS1uGbOkErUSkZSz_emsuvwCGT8dBSI".format(str(orig_coord),str(dest_coord))
  url = url1 + url2 + url3

  result= simplejson.load(urllib.urlopen(url))
  #return str(result['duration'])
  return str(result)
  #print(result)
  #driving_time = result['rows'][0]['elements'][0]['duration']['value']
  #print(driving_time)

if __name__ == "__main__":
    app.run()
