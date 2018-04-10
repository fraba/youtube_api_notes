#!/usr/bin/python
# Modified from https://github.com/spnichol/youtube_tutorial

import json

from apiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = json.load(open('developer_key.json'))['DEVELOPER_KEY']

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


results = youtube.commentThreads().list(part="snippet,replies",
                                            videoId='FIQ8594dMcU',
                                            textFormat="plainText").execute()
print results['items'][0]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

results = youtube.commentThreads().list(part="snippet,replies",
                                            videoId='FIQ8594dMcU',
                                            textFormat="plainText",
                                            pageToken=results['nextPageToken']).execute()
print results['items'][0]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
