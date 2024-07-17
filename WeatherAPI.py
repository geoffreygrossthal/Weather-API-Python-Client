@@ -1,25 +1,32 @@
import requests

def get_weather(api_key, location, aqi='no'):
    base_url = "http://api.weatherapi.com/v1/current.json"
    query = {'key': api_key, 'q': location, 'aqi': aqi}

    response = requests.get(base_url, params=query)

    if response.status_code == 200:
        data = response.json()
        # Print relevant information from the response
        print(f"Weather in {data['location']['name']}, {data['location']['country']}:")
        print(f"Temperature: {data['current']['temp_c']} degrees Celsius")
        print(f"Condition: {data['current']['condition']['text']}")
    else:
        print(f"Failed to retrieve weather data: {response.status_code}")
        print(response.text)  # Print the response text for further debugging

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key
    api_key = '3a6e356b738a4199b99151954241107'
    location = 'London'

    get_weather(api_key, location)
