import requests 
from bs4 import BeautifulSoup
import csv

# create data array with headers
data = []
headers = ['number', 'first_name', 'last_name', 'school_class', 'positions', 'bats', 'throws', 'team']
data.append(headers)

# open website and create BeautifulSoup object
r = requests.get('http://www.gsacsports.org/roster/25/3')
c = r.content
soup = BeautifulSoup(c,"html.parser")

# find all of the teams
for team in soup.find_all('div', {'class': 'box-content'}):
    teamTag = team.find('h2')
    if teamTag:
        teamName = teamTag.text

    # find all of the players
    for row in team.find_all('tr', {'class':"rosterRow"}):
        num = row.find('td', {'class': 'rosterNum'}).text
        name = row.find('td', {'class': 'rosterName'}).text
        fl = name.split()
        clas = row.find('td', {'class': 'rosterClass'}).text
        pos = row.find('td', {'class': 'rosterPos'}).text
        batsThrows = row.find('td', {'class': 'rosterBatThrow'}).text
        bt = batsThrows.split('/') 

        d = [num, fl[0], fl[1], clas, pos, bt[0], bt[1], teamName]
        data.append(d)

# write data to the csv
f = open('otherRosters.csv', 'w')

with f:
    writer = csv.writer(f)
    writer.writerows(data)

print('Complete')