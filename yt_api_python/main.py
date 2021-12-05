import os
from os.path import join, dirname
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
#import pafy

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

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

request2 = youtube.commentThreads().list(
    part="snippet",
    videoId=f"{video_id(url)}",
    maxResults=69
)

response = request2.execute()
#print(response, end="\n\n\n")

def print_comments(response):
    for item in response["items"]:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        #replycount = item['snippet']['totalReplyCount']
        print(f"{user} = {comment}", end="\n\n\n")


print_comments(response)

'''
Resources:
1. https://www.geeksforgeeks.org/how-to-extract-youtube-comments-using-youtube-api-python/
2. https://developers.google.com/youtube/v3/docs/commentThreads/list
3. https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md
'''
