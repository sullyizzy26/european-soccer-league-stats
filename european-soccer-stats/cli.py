from query_engine import QueryEngine

class CLI:
    def __init__(self):
        self.engine = QueryEngine()

    def display_menu(self):
        print("\n=== European Soccer Stats ===")
        print("1. Top Scorers")
        print("2. Top Assisters")
        print("3. Defensive Leaders")
        print("4. Compare Players")
        print("5. Search Player")
        print("6. League Summary")
        print("7. Exit")

    def print_table(self, rows, headers):
        print(" | ".join(headers))
        print("-"*60)
        for row in rows:
            print(" | ".join(str(x) for x in row))

    def handle_input(self, choice):
        if choice == "1":
            league = input("Enter league (Case Sensitive): ")
            num_players = int(input("How many players: "))
            results = self.engine.top_scorers(league, num_players)
            self.print_table(results, ["Name", "Goals", "Assists", "Rating"])

        elif choice == "2":
            league = input("Enter league (Case Sensitive): ")
            num_players = int(input("How many players: "))
            results = self.engine.top_assist_players(league, num_players)
            self.print_table(results, ["Name", "Assists", "Goals", "Rating"])

        elif choice == "3":
            league = input("Enter league (Case Sensitive): ")
            num_players = int(input("How many players: "))
            results = self.engine.defensive_leaders(league, num_players)
            self.print_table(results, ["Name", "Tackles", "Interceptions", "Saves"])

        elif choice == "4":
            names = input("Enter player names separated by commas (Case Sensitive): ")
            player_names = [(x.strip()) for x in names.split(",")]
            results = self.engine.compare_players(player_names)
            self.print_table(results, ["Name", "Goals", "Assists", "Rating", "Tackles"])

        elif choice == "5":
            name = input("Enter player name (Case Sensitive): ")
            results = self.engine.player_search(name)
            self.print_table(results, ["ID", "Name", "Position", "League", "Market Value"])

        elif choice == "6":
            league = input("Enter league (Case Sensitive): ")
            results = self.engine.league_summary(league)
            self.print_table(results, ["Players", "Avg Goals", "Avg Assists", "Avg Rating"])

        elif choice == "7":
            print("Goodbye!")
            return False

        return True
    
    def run(self):
        running = True
        while running:
            self.display_menu()
            choice = input("\nEnter choice: ")
            running = self.handle_input(choice)

