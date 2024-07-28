import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://www.fantasypros.com/nfl/adp/overall.php'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the ADP data
    table = soup.find('table', {'id': 'data'})

    # Extract table headers
    headers = []
    for th in table.find('thead').find_all('th'):
        headers.append(th.text.strip())

    # Extract table rows
    rows = []
    for tr in table.find('tbody').find_all('tr'):
        cells = []
        for td in tr.find_all('td'):
            cells.append(td.text.strip())
        rows.append(cells)
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(rows, columns=headers)
    
    # Save the DataFrame to a CSV file
    df.to_csv('fantasypros_adp.csv', index=False)
    
    # Print a success message
    print('Data has been saved to fantasypros_adp.csv')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
