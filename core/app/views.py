from django.shortcuts import render
import json
import urllib.request # make a request to api
# Create your views here.


def index(request):

    if request.method == 'POST':

        city = request.POST['city']

        '''
        api key might be expired use own api_key
        '''

        # source contain Json data from Api

        source = urllib.request.urlopen(

             'http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid = your_api_key' 
        ).read()

        # converting Json data to a directory
        list_of_data = json.loads(source)

        # data variable list_of_data
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate' : str(list_of_data['crood']['lon']) + ' ' + str(list_of_data['crood']['lat']),
            'temp': str(list_of_data['main']['temp']) + 'k',
            'pressure' : str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
        }

        print(data)

    else:
        data = {}

    return render(request,'index.html',data)
