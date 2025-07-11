# weather_app.py
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "zh_cn"
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
            return weather
        else:
            print(f"错误: {data['message']}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"网络错误: {e}")
        return None

def main():
    # 替换为你自己的API key (可在 https://openweathermap.org 免费注册获取)
    API_KEY = "YOUR_API_KEY"  
    
    print("简易天气查询")
    print("输入'退出'结束程序")
    
    while True:
        city = input("\n请输入城市名称: ")
        if city.lower() == "退出":
            break
            
        weather = get_weather(city, API_KEY)
        if weather:
            print(f"\n{weather['city']}的天气:")
            print(f"温度: {weather['temp']}°C (体感 {weather['feels_like']}°C)")
            print(f"天气状况: {weather['description']}")
            print(f"湿度: {weather['humidity']}%")
            print(f"风速: {weather['wind']} m/s")
        else:
            print("无法获取天气信息")

if __name__ == "__main__":
    main()