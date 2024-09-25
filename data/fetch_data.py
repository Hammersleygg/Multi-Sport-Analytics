#fetch_data.py
import requests
import pandas as pd

import requests
import pandas as pd

def fetch_data_mlb():
    # Define the starting year and number of years to fetch
    start_year = 2013
    num_years = 10

    # Create an empty list to store DataFrames
    all_data = []

    # Loop through the specified years
    for i in range(num_years):
        year = start_year + i  # Calculate the current year
        for offset in range(0, 100, 25):  # Get 0, 25, 50, 75 as offsets
            api_url = f'https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?&env=prod&season={year}&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset={offset}&sortStat=onBasePlusSlugging&order=desc'
            
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                # Check if 'stats' key exists and contains data
                if 'stats' in data and data['stats']:
                    df_mlb = pd.DataFrame(data['stats'])
                    # Append the DataFrame for this year to the list
                    all_data.append(df_mlb)
                else:
                    print(f"No player data returned for year {year} with offset {offset}.")
            else:
                print(f"Failed to fetch data for year {year} with offset {offset}. Status code: {response.status_code}")

    # Check if any data was collected before concatenating
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)

        # Handle missing values
        if final_df.isnull().values.any():
            final_df.fillna(0, inplace=True)

        # Save the combined data to a CSV file
        final_df.to_csv("data/mlb_data.csv", index=False)

        return final_df
    else:
        print("No data collected from the API.")
        return pd.DataFrame()  # Return 

def fetch_data_nba():
    api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Playoffs&StatCategory=PTS'
    
    # Make the API request
    r = requests.get(api_url)
    
    # Check if the request was successful
    if r.status_code == 200:
        # Extract the JSON data
        response_json = r.json()

        # Extract the headers (column names)
        column_headers = response_json['resultSet']['headers']

        # Extract the row data (actual data for each player)
        data = response_json['resultSet']['rowSet']

        # Create a DataFrame using the headers and data
        df_nba = pd.DataFrame(data, columns=column_headers)

        # Save to a CSV file
        df_nba.to_csv("data/nba_data.csv", index=False)
        return df_nba
    else:
        print(f"Failed to fetch data. Status code: {r.status_code}")

    if df_nba.isnull().values.any() == True:
        df_nba.fillna(0, inplace=True)

"""
def fetch_data_nfl():
    api_url = ''
"""
if __name__ == "__main__":
    fetch_data_mlb()
    #fetch_data_nba()