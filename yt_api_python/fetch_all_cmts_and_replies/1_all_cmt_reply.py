import os, sys
from os.path import join, dirname
from cherrypy import url
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

nextPageToken=None

youtube = build('youtube', 'v3', developerKey=os.environ.get("API_KEY"))

owner = "CodeWithHarry"
i = 1
while True:
    request2 = youtube.commentThreads().list(
        part="snippet, replies",
        videoId=f"{sys.argv[1]}",
        maxResults=100,
        pageToken=nextPageToken
    )
    response2 = request2.execute()
    
    for item in response2['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            print(f"\n{user}    {comment}\n\n")
            i += 1
            replycount = item['snippet']['totalReplyCount']
            if replycount >= 1:
                for reply in item['replies']['comments']:
                    reply_user = str(reply['snippet']['authorDisplayName'])
                    reply = reply['snippet']['textDisplay']
                    print(f"\t\t\t{reply_user}:{reply}\n")
                    i += 1
    print(i)
            
    nextPageToken = response2.get('nextPageToken')
    if not nextPageToken:
        break



# https://www.youtube.com/watch?v=HVf67CCJVYQ&list=UUN7Q4MfUn9gb9AKYaWPPBPg
