import os
from os.path import join, dirname
from cherrypy import url
from dotenv import load_dotenv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
# import sys

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

nextPageToken=None

youtube = build('youtube', 'v3', developerKey=os.environ.get("API_KEY"))

def video_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]
    
        

# url = str(input("enter youtube vdo url: "))
url = "https://www.youtube.com/watch?v=j8nAHeVKL08&list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL"
# url = str(sys.argv[1])


i = 0
while True:
    request2 = youtube.commentThreads().list(
        part="snippet, replies",
        videoId=f"{video_id(url)}",
        maxResults=100,
        pageToken=nextPageToken
    )
    response2 = request2.execute()
    for i in response2:
        print(i)
        print("\n")
    
    for i in response2['items']:
        print(i)
        print("\n")

    break
    
    # for item in response2['items']:
    #         owner_name = 'CodeWithHarry'
    #         comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    #         user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
    #         if user == owner_name:
    #             print(f"\n{comment}\n\n")
    #             # comments.append(comment)
    #         replycount = item['snippet']['totalReplyCount']
    #         if replycount >= 1:
    #             # print(f"\t\t{replycount}")
    #             for reply in item['replies']['comments']:
    #                 reply_user = str(reply['snippet']['authorDisplayName'])
    #                 if reply_user == owner_name:
    #                     reply = reply['snippet']['textDisplay']
    #                     print(f"\t\t\t{reply}\n")

            
    # nextPageToken = response2.get('nextPageToken')
    # if not nextPageToken:
    #     break



# https://www.youtube.com/watch?v=HVf67CCJVYQ&list=UUN7Q4MfUn9gb9AKYaWPPBPg
