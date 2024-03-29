import os
from os.path import join, dirname
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
#import pafy

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

nextPageToken = None

youtube = build('youtube', 'v3', developerKey=os.environ.get("API_KEY"))

request = youtube.channels().list(
    part='statistics',
    forUsername="addicteda1"
)


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


url = str(input("enter youtube vdo url: "))

#print(response, end="\n\n\n")

request2 = youtube.commentThreads().list(
    part="snippet,replies",
    videoId=f"{video_id(url)}",
    maxResults=101
)

response = request2.execute()
i = 1
while response:
    for item in response["items"]:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        print(f"{i}:    {user} = {comment}", end="\n\n\n")
        replycount = item['snippet']['totalReplyCount']
        if replycount >= 1:
            # print(f"\t\t{replycount}")
            for reply in item['replies']['comments']:
                reply_user = str(reply['snippet']['authorDisplayName'])
                reply = reply['snippet']['textDisplay']
                print(f"\t\t{reply_user} = {reply}\n")

        i += 1
        # break # just to fetch the very first comment
    break
    


'''
Resources:
1. https://www.geeksforgeeks.org/how-to-extract-youtube-comments-using-youtube-api-python/
2. https://developers.google.com/youtube/v3/docs/commentThreads/list
3. https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md
PLEASE NOTICE DONT USE FUNCTION(here print_comments()) or ur nextPageToken will not update and only 50 comments are gonna print. use `While True`(example: look at walter_bergmann.py)
'''
