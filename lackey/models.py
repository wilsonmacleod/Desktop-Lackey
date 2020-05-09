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
    target_date = db.Column(db.String(80), nullable=False)
    recurring = db.Column(db.Boolean, 
                        nullable=False,
                        default=False)

    def __repr__(self):
        return_dict = {
            "id": self.id, 
            "task": self.task, 
            "description": self.description,
            "target_date": self.target_date, 
            "recurring": f"{self.recurring}"
            }
        return f"{return_dict}"

class FinanceConfig(db.Model):
    stock_symbol = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    investment = db.Column(db.Float, nullable=False, default=0)

    def __repr__(self):
        return_dict = {
            "stock_symbol": self.stock_symbol, 
            "name": self.name, 
            "investment": self.investment
            }
        return f"{return_dict}"
    
class GW2Fractals(db.Model):
    id = db.Column(db.String, primary_key=True) # today or tomorrow
    fractal_1 = db.Column(db.String(80), nullable=False)
    fractal_2 = db.Column(db.String(80), nullable=False)
    fractal_3 = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return_dict = {
            "fractal_1": self.fractal_1, 
            "fractal_2": self.fractal_2, 
            "fractal_3": self.fractal_3
            }
        return f"{return_dict}"

class WeatherConfig(db.Model):
    city = db.Column(db.String(80), primary_key=True) #default city we want
    woied = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return_dict = {
            "city": self.city, 
            "woied": self.woied
            }
        return f"{return_dict}"


class WeatherForecast(db.Model):
    date = db.Column(db.String(80), primary_key=True) # format = '2020-05-03'
    weather_state_name = db.Column(db.String(80), nullable=False)
    icon_link = db.Column(db.String(80), nullable=False)
    min_temp = db.Column(db.Float, nullable=False) # float
    max_temp = db.Column(db.Float, nullable=False) # float
    humidity = db.Column(db.Float, nullable=False) # pct
    wind_speed = db.Column(db.Float, nullable=False) # mph
    predictability = db.Column(db.Integer, nullable=False) # pct

    def __repr__(self):
        return_dict = {
            "date": self.date, 
            "weather_state_name": self.weather_state_name,
            "icon_link": self.icon_link, 
            "min_temp": self.min_temp,
            "max_temp": self.max_temp, 
            "humidity": self.humidity,
            "wind_speed": self.wind_speed, 
            "predictability": self.predictability
            }
        return f"{return_dict}"

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

    def __repr__(self):
        return_dict = {
            "entered_date": self.entered_date, 
            "game_id": self.game_id,
            "team_abbr": self.team_abbr, 
            "team_city_name": self.team_city_name,
            "team_name": self.team_name, 
            "record": self.record,
            "quarter_scores": self.quarter_scores, 
            }
        return f"{return_dict}"

#class NBAStandings(db.Model): ??

class NBALeaders(db.Model):
    category = db.Column(db.String(80), primary_key=True) # (Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Efficiency)|
    entered_date = db.Column(db.DateTime, 
                nullable=False,
                default=datetime.datetime.now())
    data = db.Column(db.Text, nullable=False) # dict stored as str

    def __repr__(self):
        return_dict = {
            "category": self.category, 
            "entered_date": self.entered_date,
            "data": self.data
            }
        return f"{return_dict}"

class StaticNFLScoreBoard(db.Model):
    current_week = db.Column(db.String(80), primary_key=True) 
    home_team = db.Column(db.String(80), nullable=False)
    home_box_score = db.Column(db.Text, nullable=False) # dict stored as str
    away_team = db.Column(db.String(80), nullable=False)
    away_box_score = db.Column(db.Text, nullable=False) # dict stored as str
    time_rem = db.Column(db.String(80), nullable=False)
    qtr = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return_dict = {
            "current_week": self.current_week, 
            "home_team": self.home_team,
            "home_box_score": self.home_box_score, 
            "away_team": self.away_team,
            "away_box_score": self.away_box_score, 
            "time_rem": self.time_rem,
            "qtr": self.qtr            
            }
        return f"{return_dict}"

class SoccerConfig(db.Model):
    competition = db.Column(db.String(80), primary_key=True) # code 
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return_dict = {
            "competition": self.competition, 
            "name": self.name
            }
        return f"{return_dict}"

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

    def __repr__(self):
        return_dict = {
            "competition": self.competition, 
            "matchday": self.matchday,
            "home_team": self.home_team, 
            "away_team": self.away_team,
            "status": self.status, 
            "winner": self.winner,
            "duration": self.duration, 
            "scores": self.scores,
            }
        return f"{return_dict}"

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
    
    def __repr__(self):
        return_dict = {
            "rank": self.rank, 
            "team": self.team,
            "crest": self.crest, 
            "played_games": self.played_games,
            "won": self.won, 
            "draw": self.draw,
            "lost": self.lost, 
            "points": self.points,
            "goals_for": self.goals_for, 
            "goals_against": self.goals_against,
            "goal_difference": self.goal_difference, 
            "entered_date": self.entered_date,
            }
        return f"{return_dict}"

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

    def __repr__(self):
        return_dict = {
            "competition": self.competition, 
            "name": self.name,
            "nationality": self.nationality, 
            "team": self.team,
            "number_goals": self.number_goals, 
            "entered_date": self.entered_date
            }
        return f"{return_dict}"
