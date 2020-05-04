class Urls():
    def headers():
        return {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
        }
    def scoreboard():
        return (
       "https://stats.nba.com/stats/scoreboard?DayOffset=0&GameDate=2020-01-27&LeagueID=00"
        )

    def shotchart_data(player_id, season):
        return (
        "https://stats.nba.com/stats/shotchartdetail?Period=0&VsConference&LeagueID=00&"
        "LastNGames=0&TeamID=0&PlayerPosition&Location&Outcome&ContextMeasure=FGA&DateFrom&StartPeriod&"
        f"DateTo&OpponentTeamID=0&ContextFilter&RangeType&Season={season}&AheadBehind&PlayerID={player_id}&"
        "EndRange&VsDivision&PointDiff&RookieYear&GameSegment&Month=0&ClutchTime&EndPeriod&"
        "SeasonType=Regular+Season&SeasonSegment&GameID"
        )