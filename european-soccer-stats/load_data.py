import pandas
from database import DatabaseConnection

class LoadData:
    def __init__(self):
        self.profiles_path = 'data/all_player_profiles.csv'
        self.stats_path = 'data/all_player_stats.csv'
        self.db = DatabaseConnection()

    def load_profiles(self):
        df = pandas.read_csv(self.profiles_path)
        return df
    def load_stats(self):
        df = pandas.read_csv(self.stats_path)
        return df
    
    def clean_profiles(self, df):
        df = df.dropna(subset=["player_id", "name", "league"])
        df = df.drop_duplicates(subset=["player_id"])
        return df
    
    def clean_stats(self, df):
        df = df.dropna(subset=["player_id", "league"])
        df = df.drop_duplicates(subset=["player_id"])
        return df
    
    def insert_players(self, df):
        self.db.connect()
        for index, row in df.iterrows():
            sql = """INSERT INTO Players (player_id, player_name, position, market_value, league_name)
                     VALUES (%s, %s, %s, %s, %s)
                     ON CONFLICT (player_id) DO NOTHING"""
            self.db.execute_query(sql, (int(row["player_id"]), row["name"], row["position"], float(row["market_value"]), row["league"]), fetchable=False)
        print("Players inserted")
        self.db.disconnect()

    def insert_stats(self, df):
        self.db.connect()
        for index, row in df.iterrows():
            sql = """INSERT INTO Stats (player_id, league_name, appearances, matches_started, minutes_played,
                     goals, assists, expected_goals, expected_assists, rating, total_shots,
                     shots_on_target, yellow_cards, red_cards, tackles, interceptions, saves)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                     ON CONFLICT (player_id, league_name) DO NOTHING"""
            self.db.execute_query(sql, (
                int(row["player_id"]), row["league"], int(row["appearances"]),
                int(row["matches_started"]), int(row["minutes_played"]), int(row["goals"]),
                int(row["assists"]), float(row["expected_goals"]), float(row["expected_assists"]),
                float(row["rating"]), int(row["total_shots"]), int(row["shots_on_target"]),
                int(row["yellow_cards"]), int(row["red_cards"]), int(row["tackles"]),
                int(row["interceptions"]), int(row["saves"])
            ), fetchable=False)
        print("Stats inserted")
        self.db.disconnect()
    
    def insert_leagues(self, df):
        self.db.connect()
        for league in df["league"].dropna().unique():
            sql = "INSERT INTO Leagues (league_name) VALUES (%s)"
            self.db.execute_query(sql, (league,), fetchable=False)
        print("Leagues inserted")
        self.db.disconnect()

    def insert_positions(self, df):
        self.db.connect()
        position_id = 1
        for pos in df["position"].dropna().unique():
            sql = "INSERT INTO Positions (position_id, position_name) VALUES (%s, %s)"
            self.db.execute_query(sql, (position_id, pos), fetchable=False)
            #increment the position id for each new one
            position_id += 1
        print("Positions inserted")
        self.db.disconnect()

    def insert_player_leagues(self, df):
        self.db.connect()
        for index, row in df.iterrows():
            sql = "INSERT INTO PlayerLeague (player_id, league_name) VALUES (%s, %s)"
            self.db.execute_query(sql, (int(row["player_id"]), row["league"]), fetchable=False)
        print("PlayerLeague inserted")
        self.db.disconnect()