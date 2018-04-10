#!/usr/bin/python
# Modified from https://github.com/spnichol/youtube_tutorial

import json

from apiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = json.load(open('developer_key.json'))['DEVELOPER_KEY']

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def get_comments(youtube, video_id):
  results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText"
  ).execute()

  for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print "Comment by %s: %s" % (author, text)

  return results["items"]

# Get comments (not replies from ISBkB9j4a00)
get_comments(youtube, 'ISBkB9j4a00')
