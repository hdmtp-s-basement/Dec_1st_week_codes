
import os
from os.path import join, dirname
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

nextPageToken=None

youtube = build('youtube', 'v3', developerKey=os.environ.get("API_KEY"))

def video_id(url):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]

def playlist_id(url):
    """
    Examples:
    - https://www.youtube.com/watch?v=HVf67CCJVYQ&list=UUN7Q4MfUn9gb9AKYaWPPBPg
    """
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('list')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]
    
        

url = "https://www.youtube.com/watch?v=HVf67CCJVYQ&list=UUN7Q4MfUn9gb9AKYaWPPBPg"

print("<ul>")

vdo_ids = []
while True:
    request3 = youtube.playlistItems().list(
        part="snippet",
        playlistId=f"{playlist_id(url)}",
        maxResults=50,
        pageToken=nextPageToken
    )
    response2 = request3.execute()
    
    for item in response2['items']:
            position = item['snippet']['position']
            owner_name = item['snippet']['videoOwnerChannelTitle']
            vdo_ids.append(item['snippet']['resourceId']['videoId'])
            
    nextPageToken = response2.get('nextPageToken')
    if not nextPageToken:
        break

i = 0
j = 1
while True:
    if i <= len(vdo_ids):
        if i == len(vdo_ids):
            break
        request2 = youtube.commentThreads().list(
            part="snippet",
            videoId=f"{vdo_ids[i]}",
            maxResults=50
        )
        try:
            response = request2.execute()
        
            for item in response["items"]:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                if user == owner_name:
                    if len(comment) >= 100:
                        print(f"<li>{j}."+" <a href=\"https://youtu.be/"+f"{vdo_ids[i]}"+"\""+"target=\"_blank\">" + f"{vdo_ids[i]}"+"</a> ::\n\n"+f"{comment}</li><br><br>")
                        j += 1
                
        except:
            pass

        i += 1

print("</ul>\n</body>\n</html>")
# https://www.youtube.com/watch?v=HVf67CCJVYQ&list=UUN7Q4MfUn9gb9AKYaWPPBPg
