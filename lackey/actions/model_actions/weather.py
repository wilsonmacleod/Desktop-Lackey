from ...models import db, WeatherConfig

class ShouldWeatherUpdate():
    def checkConfig():
        config = WeatherConfig.query.all()
        if config == []:
            return False
        else:
            return config
