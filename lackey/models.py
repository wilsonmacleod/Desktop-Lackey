import datetime 
from flask_sqlalchemy import SQLAlchemy

from lackey.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class CalendarTasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    target_date = db.Column(db.String(80), nullable=False) # day,month,year
    time = db.Column(db.String(80), nullable=True) 
    recurring = db.Column(db.Boolean, 
                        nullable=False,
                        default=False)
    interval = db.Column(db.Integer,
                        nullable=True,
                        default=7)
    color = db.Column(db.String(80), 
                        nullable=False,
                        default="4ecdc4")

    def __repr__(self):
        return_dict = {
            "id": self.id, 
            "task": self.task, 
            "description": self.description,
            "target_date": self.target_date, 
            "time": f"{self.time}",
            "recurring": f"{self.recurring}",
            "interval": self.interval,
            "color": self.color
            }
        return f"{return_dict}"

class WeatherConfig(db.Model):
    city = db.Column(db.String(80), primary_key=True) #default city we want
    woied = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return_dict = {
            "city": self.city, 
            "woied": self.woied,
            }
        return f"{return_dict}"


class WeatherForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80)) # format = '2020-05-03'
    weather_state_name = db.Column(db.String(80), nullable=False)
    icon_link = db.Column(db.String(80), nullable=False)
    min_temp = db.Column(db.Float, nullable=False) # float
    max_temp = db.Column(db.Float, nullable=False) # float
    humidity = db.Column(db.Float, nullable=False) # pct
    wind_speed = db.Column(db.Float, nullable=False) # mph
    predictability = db.Column(db.Integer, nullable=False) # pct
    woied = db.Column(db.String(80), nullable=False)
    entered_date = db.Column(db.String(80), 
                    nullable=False,
                    default=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def __repr__(self):
        return_dict = {
            "date": self.date, 
            "weather_state_name": self.weather_state_name,
            "icon_link": self.icon_link, 
            "min_temp": self.min_temp,
            "max_temp": self.max_temp, 
            "humidity": self.humidity,
            "wind_speed": self.wind_speed, 
            "predictability": self.predictability,
            "woied": self.woied,
            "entered_date": self.entered_date
            }
        return f"{return_dict}"

class FinanceConfig(db.Model):
    stock_symbol = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return_dict = {
            "stock_symbol": self.stock_symbol, 
            "name": self.name, 
            }
        return f"{return_dict}"

class FinanceTempStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String(80))
    date = db.Column(db.String(80), nullable=False)
    opening = db.Column(db.Integer, nullable=False)
    high = db.Column(db.Integer, nullable=False)
    low = db.Column(db.Integer, nullable=False)
    close = db.Column(db.Integer, nullable=False)
    change = db.Column(db.String(80), nullable=False)
    entered_date = db.Column(db.DateTime, 
                nullable=False,
                default=datetime.datetime.now())

    def __repr__(self):
        return_dict = {
            "stock_symbol": self.stock_symbol, 
            "date": self.date, 
            "opening": self.opening, 
            "high": self.high, 
            "low": self.low, 
            "close": self.close,
            "change": self.change,
            "entered_date": f"{self.entered_date}"
            }
        return f"{return_dict}"

class FinanceInvestment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String(80))
    shares_count = db.Column(db.Integer, nullable=False)
    price_per_share = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return_dict = {
            "stock_symbol": self.stock_symbol,
            "shares_count": self.shares_count, 
            "price_per_share": self.price_per_share, 
            "date": self.date
            }
        return f"{return_dict}"

class NBAScoreBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(80), nullable=False)
    team_abbr = db.Column(db.String(80), nullable=False)
    team_city_name = db.Column(db.String(80), nullable=False)
    team_name = db.Column(db.String(80), nullable=False)
    record = db.Column(db.String(80), nullable=False)
    quarter_scores = db.Column(db.Text, nullable=False) # dict stored as str
    entered_date = db.Column(db.String(80), 
            nullable=False,
            default=datetime.datetime.now().strftime('%Y-%m-%d'))

    def __repr__(self):
        return_dict = {
            "game_id": self.game_id,
            "team_abbr": self.team_abbr, 
            "team_city_name": self.team_city_name,
            "team_name": self.team_name, 
            "record": self.record,
            "quarter_scores": self.quarter_scores, 
            }
        return f"{return_dict}"

class NBAStandings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    team_city = db.Column(db.String(80), nullable=False)
    team_name = db.Column(db.String(80), nullable=False)
    conference = db.Column(db.String(80), nullable=False) # east, west
    data = db.Column(db.Text, nullable=False) # dict stored as str
    entered_date = db.Column(db.String(80), 
            nullable=False,
            default=datetime.datetime.now().strftime('%Y-%m-%d'))

    def __repr__(self):
        return_dict = {
            "rank": self.rank,
            "team_city": self.team_city, 
            "team_name": self.team_name,
            "conference": self.conference,
            "data": self.data
            }
        return f"{return_dict}"

class NBALeaders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False) # (Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Efficiency)|
    rank = db.Column(db.String(80), nullable=False)
    player = db.Column(db.String(80), nullable=False)
    team_abbr = db.Column(db.String(80), nullable=False)
    stats = db.Column(db.Text, nullable=False) # dict stored as str
    entered_date = db.Column(db.String(80), 
            nullable=False,
            default=datetime.datetime.now().strftime('%Y-%m-%d'))

    def __repr__(self):
        return_dict = {
            "category": self.category, 
            "rank": self.rank,
            "player": self.player,
            "team_abbr": self.team_abbr,
            }
        return f"{return_dict}"

class SoccerScoreboard(db.Model):
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

class EPLTable(db.Model):
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


class NFLScoreBoard(db.Model):
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
