import os
from os.path import join, dirname
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
# import sys

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
    
        

# url = str(input("enter youtube vdo url: "))
url = "https://youtube.com/playlist?list=PLr2jljBBtVJ-cnlB3fUW7IFQjr7s_3qvk"
# url = str(sys.argv[1])


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
            # print(item)
            '''
            thumbnails = item['snippet']['thumbnails']
  
            if 'maxres' in thumbnails:
                maxres = thumbnails['maxres']
                print(maxres)
                i += 1
                
            print("\n")

            '''
            position = item['snippet']['position']
            owner_name = item['snippet']['videoOwnerChannelTitle']
            vdo_ids.append(item['snippet']['resourceId']['videoId'])
            
    nextPageToken = response2.get('nextPageToken')
    if not nextPageToken:
        break

# print(vdo_ids)
i = 0
nextPageToken = None
# comments = []
while True:
    if i <= len(vdo_ids):
        if i == len(vdo_ids):
            break
        request2 = youtube.commentThreads().list(
            part="snippet, replies",
            videoId=f"{vdo_ids[i]}",
            maxResults=100,
            pageToken=nextPageToken
        )
        response = request2.execute()
    
        for item in response["items"]:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            if user == owner_name:
                print(f"\n{i}:   {comment}\n\n")
                # comments.append(comment)
            replycount = item['snippet']['totalReplyCount']
            if replycount >= 1:
                # print(f"\t\t{replycount}")
                for reply in item['replies']['comments']:
                    reply_user = str(reply['snippet']['authorDisplayName'])
                    if reply_user == owner_name:
                        reply = reply['snippet']['textDisplay']
                        print(f"\t\t\t{reply}\n")

        i += 1

# print([i for i in comments])
# for c in comments:
    # print(f"{c}\n")

# https://www.youtube.com/watch?v=HVf67CCJVYQ&list=UUN7Q4MfUn9gb9AKYaWPPBPg
