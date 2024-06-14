# WeatherApp
<img src="https://maxmautner.com/public/images/django.gif" align="center">


This is a simple weather application built using Django. The app allows users to get the current weather information for a specified city by fetching data from the OpenWeatherMap API.



### Features

- Fetches current weather data for a city.
- Displays temperature, pressure, humidity, country code, and coordinates.
- Uses MySQL database for backend storage.


### Prerequisites

- Python 3.x
- Django
- MySql
- OpenWeatherMap API key

### Installation

**1- Clone the repository:**

```
git clone https://github.com/amirhoseinshojaei/WeatherApp.git
```

**2- Set up a virtual environment and activate it:**

```
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`

```

**3- Install the required packages:**

```
pip install -r requirements.txt
```

**4- Set up your MySQL database:**

Create a database in MySQL and update the DATABASES settings in settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

**5- Apply migrations:**

```
python manage.py makemigrations
python manage.py migrate
`````

**6- Run the development server:**

```
python manage.py runserver
```

### Usage

1. Enter the name of the city for which you want to get the weather information.

2. Click the "Submit" button.

3. The weather data for the specified city will be displayed on the page.


### License

This project is licensed under the MIT License - see the <a href = 'LICENSE'>LICENSE</a> file for details.

