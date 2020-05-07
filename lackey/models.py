import datetime 
from flask_sqlalchemy import SQLAlchemy

from lackey.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class CalendarTasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entered_date = db.Column(db.DateTime, 
                        nullable=False,
                        default=datetime.datetime.now())
    task = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    target_date = db.Column(db.DateTime, nullable=True)
    recurring = db.Column(db.Boolean, 
                        nullable=False,
                        default=False)

class FinanceConfig(db.Model):
    stock_symbol = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    investment = db.Column(db.Float, nullable=False, default=0)
    
class GW2Fractals(db.Model):
    id = db.Column(db.String, primary_key=True) # today or tomorrow
    fractal_1 = db.Column(db.String(80), nullable=False)
    fractal_2 = db.Column(db.String(80), nullable=False)
    fractal_3 = db.Column(db.String(80), nullable=False)

class WeatherConfig(db.Model):
    city = db.Column(db.String(80), primary_key=True) #default city we want
    woied = db.Column(db.String(80), nullable=False)

class WeatherForecast(db.Model):
    date = db.Column(db.String(80), primary_key=True) # format = '2020-05-03'
    weather_state_name = db.Column(db.String(80), nullable=False)
    icon_link = db.Column(db.String(80), nullable=False)
    min_temp = db.Column(db.Float, nullable=False) # float
    max_temp = db.Column(db.Float, nullable=False) # float
    humidity = db.Column(db.Float, nullable=False) # pct
    wind_speed = db.Column(db.Float, nullable=False) # mph
    predictability = db.Column(db.Integer, nullable=False) # pct

class StaticNBAScoreBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entered_date = db.Column(db.DateTime, 
                    nullable=False,
                    default=datetime.datetime.now())
    game_id = db.Column(db.String(80), nullable=False)
    team_abbr = db.Column(db.String(80), nullable=False)
    team_city_name = db.Column(db.String(80), nullable=False)
    team_name = db.Column(db.String(80), nullable=False)
    record = db.Column(db.String(80), nullable=False)
    quarter_scores = db.Column(db.Text, nullable=False) # dict stored as str

#class NBAStandings(db.Model): ??

class NBALeaders(db.Model):
    category = db.Column(db.String(80), primary_key=True) # (Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Efficiency)|
    entered_date = db.Column(db.DateTime, 
                nullable=False,
                default=datetime.datetime.now())
    data = db.Column(db.Text, nullable=False) # dict stored as str

class StaticNFLScoreBoard(db.Model):
    current_week = db.Column(db.String(80), primary_key=True) 
    home_team = db.Column(db.String(80), nullable=False)
    home_box_score = db.Column(db.Text, nullable=False) # dict stored as str
    away_team = db.Column(db.String(80), nullable=False)
    away_box_score = db.Column(db.Text, nullable=False) # dict stored as str
    time_rem = db.Column(db.String(80), nullable=False)
    qtr = db.Column(db.String(80), nullable=False)

class SoccerConfig(db.Model):
    competition = db.Column(db.String(80), primary_key=True) # code 
    name = db.Column(db.String(80), nullable=False)

class StaticSoccerScoreboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition = db.Column(db.String(80), nullable=False)
    matchday = db.Column(db.Integer, nullable=False)
    home_team = db.Column(db.String(80), nullable=False) 
    away_team = db.Column(db.String(80), nullable=False) 
    status = db.Column(db.String(80), nullable=False) 
    winner = db.Column(db.String(80), nullable=True) 
    duration = db.Column(db.String(80), nullable=True) 
    scores = db.Column(db.Text, nullable=False) # dict stored as str

class StaticEPLTable(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(80), nullable=False)
    crest = db.Column(db.String(80), nullable=False)
    played_games = db.Column(db.String(80), nullable=False)
    won = db.Column(db.String(80), nullable=False)
    draw = db.Column(db.String(80), nullable=False)
    lost = db.Column(db.String(80), nullable=False)
    points = db.Column(db.String(80), nullable=False)
    goals_for = db.Column(db.String(80), nullable=False)
    goals_against = db.Column(db.String(80), nullable=False)
    goal_difference = db.Column(db.String(80), nullable=False)
    entered_date = db.Column(db.DateTime, 
            nullable=False,
            default=datetime.datetime.now())

class SoccerTopScorers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    number_goals = db.Column(db.String(80), nullable=False)
    entered_date = db.Column(db.DateTime, 
        nullable=False,
        default=datetime.datetime.now())
