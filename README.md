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
2. Go to your API dashboard or manager (or whatever is called when you'll read this);
3. You now need to create an **API key** (it might be under "Create credentials").

The **API key** is everything you'll need to authenticate your app. To execute the `youtube_api_script_template.py` store your **API key** in `developer_key_template.json` and rename it as `developer_key.json`.

