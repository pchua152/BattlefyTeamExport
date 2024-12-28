import requests
import csv
import json
import os


def start():
    link = input("Paste the a link of any page from the battlefy tour\n")
    print(export_to_excel(link))
    
def get_id(link):
    battlefy_link = link.split('/')
    battlefy_id = battlefy_link[5]
    return battlefy_id

def get_tour_name(link):
    requests.session
    

def export_to_excel(battlefy_link: str):
    
    battlefy_id = get_id(battlefy_link)
    
    
    try:
        if(battlefy_id):
            requesturl = f'https://dtmwra1jsgyb0.cloudfront.net/tournaments/{battlefy_id}/teams'
            htmldata = requests.get(requesturl)
            data = json.loads(htmldata.content.decode('utf-8'))
            result = {}
            for s in data:
                result[s['captain']['username']] = ((s['name'], s['customFields'][1]['value']))
            
            cur_directory = os.getcwd()
            target_location = f'{cur_directory}\\tourteams'
            if not os.path.exists(target_location):
                os.mkdir(target_location)
            with open(f'{target_location}\\teams.csv','w',newline='',encoding = 'utf-8') as csvfile:
                headers = ['BattlefyName', 'IGN', 'Pokepaste']
                teamwrite = csv.writer(csvfile)
                teamwrite.writerow(headers)
                for x,y in result.items():
                    teamwrite.writerow([x,y[0],f'=HYPERLINK("{y[1]}")'])
                    
    
        return "Teams written to teams.csv"
    except:
        return "Invalid link"
    

if __name__ == "__main__":   
    start()