from database import DatabaseConnection

class QueryEngine:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()
    
    def top_scorers(self, league, limit):
        sql = """SELECT p.player_name, s.goals, s.assists, s.rating
                FROM Players p, Stats s
                WHERE p.player_id = s.player_id
                AND s.league_name = %s
                ORDER BY s.goals DESC
                LIMIT %s"""
        return self.db.execute_query(sql, (league,limit))
    
    def top_assist_players(self, league, limit):
        sql = """SELECT p.player_name, s.assists, s.goals, s.rating
                FROM Players p, Stats s
                WHERE p.player_id = s.player_id
                AND s.league_name = %s
                ORDER BY s.assists DESC
                LIMIT %s"""
        return self.db.execute_query(sql, (league,limit))
    
    def defensive_leaders(self, league, limit):
        sql = """SELECT p.player_name, s.tackles, s.interceptions, s.saves
                FROM Players p, Stats s
                WHERE p.player_id = s.player_id
                AND s.league_name = %s
                ORDER BY s.tackles DESC
                LIMIT %s"""
        return self.db.execute_query(sql, (league,limit))
    
    def compare_players(self, player_names):
        sql = """SELECT p.player_name, s.goals, s.assists, s.rating, s.tackles
                FROM Players p, Stats s
                WHERE p.player_id = s.player_id
                AND p.player_name = ANY(%s)"""
        return self.db.execute_query(sql,(player_names,))
    
    def player_search(self, name):
        sql = """SELECT p.player_id, p.player_name, p.position, p.league_name, p.market_value
                FROM Players p, PlayerLeague l
                WHERE p.player_id = l.player_id
                AND p.player_name = %s"""
        return self.db.execute_query(sql, (name,))
    
    def league_summary(self, league):
        sql = """SELECT COUNT(p.player_id), AVG(s.goals), AVG(s.assists), AVG(s.rating)
                FROM Players p, Stats s
                WHERE p.player_id = s.player_id
                AND s.league_name = %s"""
        return self.db.execute_query(sql, (league,))
    