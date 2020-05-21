class NBA_Urls():
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
    # Your API email: wilsonmacleodtwo@gmail.com
    # Your API token: be4f7b03d3934147be82ddc25caf2aa4
    # Your API plan: Free Tier
        
    def headers():
        return { 'X-Auth-Token': 'be4f7b03d3934147be82ddc25caf2aa4' }
    
    def urls_(url_name, comp='PL'):
        url_dict = {
            'general_competition': f'https://api.football-data.org/v2/competitions/{comp}/', # ['currentSeason']
            'matches': f'https://api.football-data.org/v2/competitions/{comp}/matches', #optional +?matchday={matchday}'
            'table': f'https://api.football-data.org/v2/competitions/{comp}/standings',
            'scorers': f'https://api.football-data.org/v2/competitions/{comp}/scorers'
        }
        return url_dict[url_name]

class NFL_Urls(): # DEPRECATED
    #https://stackoverflow.com/a/59970147
    def urls(url_name):
        url_dict = {
            'currentWeek': 'http://www.nfl.com/feeds-rs/currentWeek.json',
            'week': 'http://www.nfl.com/ajax/scorestrip?', # +season={season}&seasonType={seasonType}&week={week}'
            'liveupdate': 'http://www.nfl.com/liveupdate/game-center/' #+{game_id}/{game_id}_gtd.json'
        }
        return url_dict[url_name]