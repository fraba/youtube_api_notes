# YouTube API notes

In this repository  I provide my notes on how to use YouTube API for research purposes.

## Google APIs Client Library for Python installation

[Details](https://developers.google.com/youtube/v3/quickstart/python)

Install with

```
pip install --upgrade google-api-python-client
```
and 

```
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```

## Authentication

The simplest way to authenticate an app is to follow these steps:

1. Go to your [Google Cloud Console](https://console.cloud.google.com/);
2. Go to your API dashboard or manager (or whatever is called when you read this);
3. You now need to create an **API key** (it might be under "Create credentials").

The **API key** is everything you'll need to authenticate your app. To execute the `youtube_api_script_template.py` store your **API key** in `developer_key_template.json` and rename it as `developer_key.json`.

You can execute the script with

```
python youtube_api_script_template.py 
```

and if everything works you should get the comment posted below [this video](https://www.youtube.com/watch?v=JLqvnFRiP24):

> Comment by Ethan Chew: Brent, may you point to the database and website you show at 1:18?  That utility would be useful for my research with spaceports and the space industry and market.

### Additional details on authentication

The function [build()](http://google.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build) create a resource to interact with the Google API. In this case we use it with the service `youtube`.

## Get comments

The function to request comments and replies is `commentThreads()`. 

This line return comments and replies (note: `part="snippet,replies"`) for [this video](https://www.youtube.com/watch?v='ISBkB9j4a00')
```python
results = youtube.commentThreads().list(part="snippet,replies", videoId='ISBkB9j4a00', textFormat="plainText").execute()
```
## Get related videos

The function to request related videos is the `search()` function with the parameters `relatedToVideoId` set to the video id and `type="video"`.

```python
results = youtube.search().list(part="snippet", relatedToVideoId='jaVSuYdEFks', type="video",maxResults=20).execute()
```

Related videos (different from *recommended videos*) do appear in the right column of a YouTube video page along with recommended videos. In the table below I compare the 20 video recommendations returned by the API with the 20 video recommendations offered to me on the YouTube for the same video

|API|Web|
|:----:|:-----:|
|1     |5      |
|2     |8     |
|3     |1     |
|4     |2      |
|5     |      |
|6     |      |
|7     |12     |
|8     |9     |
|9     |      |
|10   |1      |
|11   |      |
|12   |3      |
|13   |      |
|14   |      |
|15   |     |
|16   |      |
|17   |      |
|18   | 17    |
|19   | 13    |
|20   |     |

## API Response

A typical API response looks like this

```
{
  "kind": string,
  "etag": etag,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    .. Resource ..
  ]
}
```

## Pagination

The parameter to set to request the following page is  `pageToken`  from the value `nextPageToken` of the list. See `youtube_api_script_paginating.py` for a working example. 
