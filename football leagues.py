import requests

API_KEY = "d433254dcd10416bb396e1c84640050b"

leagues = {
    1: {"name": "La Liga", "code": "PD"},
    2: {"name": "Champions League", "code": "CL"},
    3: {"name": "Premier League", "code": "PL"},
    4: {"name": "Bundesliga", "code": "BL1"}
}

def get_standings(league_code, year):
    url = "https://api.football-data.org/v4/competitions/" + league_code + "/standings"
    headers = {"X-Auth-Token": API_KEY}
    params = {"season": year}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: data shoma peyda nashod"

def print_leagues():
    print("\nLeague ha:")
    for i in leagues:
        print(str(i) + ". " + leagues[i]["name"])

def print_years():
    print("\n saal :")
    years = [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016 ]
    for i, year in enumerate(years):
        print(str(i+1) + ". " + str(year) + "/" + str(year+1))
    return years

def show_standings(data):
    if 'standings' in data:
        print("\nStandings:")
        print(" position | Team | baazi | emtiaz")
        print("-" * 40)
        for team in data['standings'][0]['table']:
            print(f"{team['position']} | {team['team']['name']} | {team['playedGames']} | {team['points']}")
    else:
        print("chizi baraye namayesh vojod nadarad :)")

def main():
    while True:
        print_leagues()
        choice = input("league khod ra beyne  (1 ta 4) entekhab konid ya dokme 'q' ra baraye khoroj bezanid: ")
        
        if choice == 'q':
            break

        if choice not in ['1', '2', '3', '4']:
            print("etelaate vared shode eshtebah ast. lotfan dobare talash konid:")
            continue

        years = print_years()
        year_choice = input("sale khod ra beyne (1 ta 5) entekhab konid : ")

        if year_choice not in ['1', '2', '3', '4', '5','6','7','8']:
            print("etelaate vared shode eshtebah ast. lotfan dobare talash konid:")
            continue

        league = leagues[int(choice)]
        year = years[int(year_choice) - 1]

        print("gereftane etelaat az: " + league['name'] + " dar " + str(year) + "...")
        standings = get_standings(league['code'], year)

        if type(standings) is dict:
            show_standings(standings)
        else:
            print(standings)

        input("baraye bargash te menu asli (ENTER) ra vared konid")

main()