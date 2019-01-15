#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas
from collections import OrderedDict

#Fetch data of Player's ID
player_ids = pandas.read_csv("player_ids.csv")
ids = player_ids["Ids"]

#Prive a base url and an empty list
base_url = "https://www.fifa.com/worldcup/players/player/"
player_list = []

#Iterate to scrap data of players from fifa.com
for pages in ids:
    #Using OrderedDict instead of Dict (See explaination)
    d=OrderedDict()
    #Fetching URLs one by one
    print(base_url+str(pages)+"/profile.html")
    request = requests.get(base_url+str(pages)+"/profile.html")
    #Data processing
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    #Scraping Data
    #Name #Country #Role #Age #Height #International Caps #International Goals
    d['Name'] = soup.find("div",{"class":"fi-p__name"}).text.replace("\n","").strip()
    print(d['Name'])
    d['Country'] = soup.find("div",{"class":"fi-p__country"}).text.replace("\n","").strip()
    d['Role'] = soup.find("div",{"class":"fi-p__role"}).text.replace("\n","").strip()
    d['Age'] = soup.find("div",{"class":"fi-p__profile-number__number"}).text.replace("\n","").strip()
    d['Height(cm)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[1].text.replace("\n","").strip()
    d['International Caps'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[2].text.replace("\n","").strip()
    d['International Goals'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[3].text.replace("\n","").strip()

#Append dictionary to list
player_list.append(d)
print(player_list)
#Create a pandas DataFrame to store data and save it to .csv
df = pandas.DataFrame(player_list)
df.to_csv('Players_info.csv', index = False)
print("Success \n")
