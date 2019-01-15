#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas

#Empty list to store data
id_list = []

request = requests.get("https://www.fifa.com/worldcup/players/_libraries/byposition/[id]/_players-list")
soup = BeautifulSoup(request.content,"html.parser")

#Iterate to find all IDs
for ids in range(0,736):
    all = soup.find_all("a","fi-p--link")[ids]
    id_list.append(all['data-player-id'])

#Data Frame to store scrapped data
df = pandas.DataFrame({
"Ids":id_list
})
df.to_csv('player_ids.csv', index = False)
print(df)
