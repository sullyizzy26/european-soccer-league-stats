# European Soccer Stats

A command-line app for exploring player statistics across Europe's top soccer leagues, backed by a PostgreSQL database.

## Features

- Top scorers and top assisters by league
- Defensive leaders (tackles, interceptions, saves)
- Side-by-side player comparison
- Player search
- League-wide summary averages

## Database design

| Table | Purpose |
|---|---|
| `leagues` | League name (PK) and country |
| `players` | Player profile: name, position, market value, league (FK) |
| `stats` | Season stats per player per league (composite PK) |
| `playerleague` | Player ↔ league relationship |
| `positions` | Position lookup |

## Setup

Requires Python 3 and PostgreSQL.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a PostgreSQL database named `soccer_db` with the tables described above, then load the CSVs in `data/` using `load_data.py`.
3. Set your database credentials as environment variables (see `.env.example`):
   ```bash
   export DB_PASSWORD=your_password_here
   ```
   On Windows PowerShell: `$env:DB_PASSWORD="your_password_here"`
4. Run the app:
   ```bash
   python main.py
   ```

League and player names are case-sensitive, e.g. `Premier League`.
