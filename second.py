from flask import Flask, render_template
from flask import request, redirect
import json
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage_weather.html")


@app.route('/temp')
def temp():
    city = str(request.args.get('city'))
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + str(city) + "&APPID=c38019c217f2038ea26bcef66f597bb1&units=metric")
    weather = response.json()
    response2 =requests.get("https://api.teleport.org/api/urban_areas/slug:" + str(city) + "/scores/")
    scores = response2.json()
    #print(type(scores['status']))
    
    #summaryOfCity = scores['summary']    
    #print('HERE')
    #print ("RESPONSE")
    #print(summaryOfCity)
    #print ("END RESPONSE")

    if 'status' in scores.keys():
        
        if scores['status'] == 404:
            print('HERE2')
            summaryOfCity = "<p> no description </p>"
        #scores = response2.json()
        
    else:
        print('HERE3')
        summaryOfCity = scores['summary']
    #elif response2 == <Response [404]>:
        #print('HERE3')
        
    
    
    temp = str(weather['main']['temp'])
    temp_float = float(weather['main']['temp'])
    if temp_float >= 40.0:
        backgroundlink = "https://images.unsplash.com/photo-1527181617732-cd814bc53892?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=65d56247536cc2acd48bf97ca7660a89&w=1000&q=80"
    elif temp_float >= 25.0:
        backgroundlink = "https://media.istockphoto.com/photos/art-summer-vacation-ocean-beach-picture-id510152502?k=6&m=510152502&s=612x612&w=0&h=dBUs641JFQv3yCxWRnFqG23k_atj7CHu7NxoT29Z2Y4="
    elif temp_float >= 15.0:
        backgroundlink = "http://s3.envato.com/files/240940379/stevanzz_02635.jpg"
    elif temp_float >= 10.0:
        backgroundlink = "https://www.lumixgexperience.panasonic.co.uk/app/uploads/gallery/Patricia/P1030055-rainy-day-in-London.jpg"
    elif temp_float >= 4.0:
        backgroundlink = "https://metrouk2.files.wordpress.com/2016/12/rexfeatures_7666554d.jpg?w=748&h=498&crop=1"
    elif temp_float >= -5.0:
        backgroundlink = "https://wallpapertag.com/wallpaper/full/b/d/3/446352-beautiful-winter-snow-background-2880x1920-for-android-40.jpg"
    else:
        backgroundlink =  "http://images.glaciermedia.ca/polopoly_fs/1.23186971.1519797290!/fileImage/httpImage/image.jpg_gen/derivatives/landscape_804/snow-days-28-2272018-jpg.jpg"
    
    #returnStr = "<a href='/'>back</a><br/>"
    #returnStr = returnStr + temp
    return render_template("results_weather.html", city = city, temp = temp, backgroundlink = backgroundlink, summaryOfCity = summaryOfCity)

if __name__ == "__main__":
          app.run(debug=True, port = 5000)
