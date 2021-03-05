class NBA_Urls():
    def headers():
        return {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://stats.nba.com/',
        'Pragma': 'no-cache',
        }

    def scoreboard_url(date):
        #https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/scoreboardv2.md
        return f"https://stats.nba.com/stats/scoreboardv2?DayOffset=0&GameDate={date}&LeagueID=00"
    
    def leaguestandings(season):
        #https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/leaguestandings.md
        return f'https://stats.nba.com/stats/leaguestandings?LeagueID=00&Season={season}&SeasonType=Regular+Season&SeasonYear=' ###
    
    def leaders(scope, season, category):
        #https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/homepageleaders.md
        return f'https://stats.nba.com/stats/homepageleaders?GameScope=Season&LeagueID=00&PlayerOrTeam=Player&PlayerScope={scope}&Season={season}&SeasonType=Regular+Season&StatCategory={category}'


class Soccer_Urls():
    
    def urls_(url_name, comp='PL'):
        url_dict = {
            'general_competition': f'https://api.football-data.org/v2/competitions/{comp}/', # ['currentSeason']
            'matches': f'https://api.football-data.org/v2/competitions/{comp}/matches', #optional +?matchday={matchday}'
            'table': f'https://api.football-data.org/v2/competitions/{comp}/standings',
            'scorers': f'https://api.football-data.org/v2/competitions/{comp}/scorers'
        }
        return url_dict[url_name]