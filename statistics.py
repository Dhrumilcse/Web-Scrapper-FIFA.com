import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas

player_ids = pandas.read_csv("player_ids.csv")
ids = player_ids["Ids"]
list = []
base_url="https://www.fifa.com/worldcup/_libraries/players/player/"
for pages in ids:
    d = OrderedDict()
    print(base_url+str(pages)+"/_player-statistics.html")
    request = requests.get(base_url+str(pages)+"/_player-statistics.html")
    content = request.content
    soup = BeautifulSoup(content,"html.parser")

    #General statistics
    MatchesPlayed = soup.find("div",{"class":"fi-p__profile-number__number"})
    if(MatchesPlayed == None):
        d['Matches Played']=''
        list.append(d)
        print("Cleared..")
        continue
    else:
        d['Matches Played'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[0].text.replace("\n","").strip()
    d['Minutes Played'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[1].text.replace("\n","").strip()
    d['Distance Covered (KM)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[2].text.replace("\n","").strip()
    d['Distance Covered In Possession (KM)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[3].text.replace("\n","").strip()
    d['Distance Covered NOT In Possession (KM)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[4].text.replace("\n","").strip()

    #Goals statistics
    d['Goals Socred'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[6].text.replace("\n","").strip()
    d['Penalties Scored'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[7].text.replace("\n","").strip()
    d['Goals Scored With Left Foot'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[8].text.replace("\n","").strip()
    d['Goals Scored With Right Foot'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[9].text.replace("\n","").strip()
    d['Headed Goals'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[10].text.replace("\n","").strip()
    d['Goals Scored By Backheel']  = soup.find_all("div",{"class":"fi-p__profile-number__number"})[11].text.replace("\n","").strip()

    #Attempts Statistics
    d['Attempts'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[12].text.replace("\n","").strip()
    d['Attempts On Target'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[13].text.replace("\n","").strip()
    d['Attempts Off Target'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[14].text.replace("\n","").strip()
    d['Shots Blocked'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[15].text.replace("\n","").strip()
    d['Attempts Against Woodwork'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[16].text.replace("\n","").strip()
    d['Shots From Free-kick'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[17].text.replace("\n","").strip()
    d['Attempts Inside The Area'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[18].text.replace("\n","").strip()
    d['Attempts Outside The Area'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[19].text.replace("\n","").strip()
    d['Attempts On Target From Inside The Area'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[20].text.replace("\n","").strip()
    d['Attempts On Target From Outside The Area'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[21].text.replace("\n","").strip()

    #Passing, Crossing, Dribbling
    d['Assists'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[22].text.replace("\n","").strip()
    d['Total Passes'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[23].text.replace("\n","").strip()
    d['Passes Completed'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[24].text.replace("\n","").strip()
    d['Short Passes Completed'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[25].text.replace("\n","").strip()
    d['Medium Passes Completed'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[26].text.replace("\n","").strip()
    d['Long Passes Completed'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[27].text.replace("\n","").strip()
    d['Crosses Attempted'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[28].text.replace("\n","").strip()
    d['Crosses Completed'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[29].text.replace("\n","").strip()
    d['Deliveries Into Penalty Area'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[30].text.replace("\n","").strip()
    d['Dribbles Into Penalty Area'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[31].text.replace("\n","").strip()
    d['Corners'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[32].text.replace("\n","").strip()
    d['Throws'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[33].text.replace("\n","").strip()

    #Defending
    d['Tackles'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[34].text.replace("\n","").strip()
    d['Tackles Won'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[35].text.replace("\n","").strip()
    d['Lost Balls'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[36].text.replace("\n","").strip()
    d['Tackles Suffered'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[37].text.replace("\n","").strip()
    d['Recovered Balls'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[38].text.replace("\n","").strip()
    d['Clearances'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[39].text.replace("\n","").strip()
    d['Blocks'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[40].text.replace("\n","").strip()
    d['Saves'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[41].text.replace("\n","").strip()
    d['Save Rate (%)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[42].text.replace("\n","").replace("%","").strip()
    d['Goal kicks successfully reaching a team-mate (%)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[43].text.replace("\n","").replace("%","").strip()

    #Fouls, Offsides, Discipline
    d['Red Cards'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[44].text.replace("\n","").strip()
    d['Yellow Cards'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[45].text.replace("\n","").strip()
    d['Fouls Committed'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[46].text.replace("\n","").strip()
    d['Fouls Causing Penalty'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[47].text.replace("\n","").strip()
    d['Fouls Suffered'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[48].text.replace("\n","").strip()
    d['Offsides'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[49].text.replace("\n","").strip()

    #Append dictionary to list
    list.append(d)
    print("Clear..")

#Create a pandas DataFrame to store data
df = pandas.DataFrame(list)
#print(df.values)
#Conver dataframe to CSV
df.to_csv("Statistics-try.csv", index = False)
