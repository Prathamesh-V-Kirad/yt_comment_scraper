# YouTube Comment Scraper

This Python script allows you to scrape comments from a YouTube video and save them to a CSV file. It utilizes Selenium, BeautifulSoup, and Requests libraries.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- Chrome WebDriver

## Installation
1. Install the required Python packages:
2. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your PATH.

## Usage
1. Import the necessary modules:
```python
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
```
# Example usage
```python
video_url = "https://www.youtube.com/watch?v=LIWHz4g_n_w"
video_title = get_youtube_title(video_url).split('-')[0]
extract_youtube_comments(video_url, video_title)
```

Feel free to adjust or expand upon it as needed!

## Note on Handling Errors
- If you encounter errors such as "element not found" or "HTTP error", try the following:
  - Check your internet connection and ensure that you have access to YouTube.
  - Verify that the video URL is correct and the video is accessible publicly.
  - Ensure that the Chrome WebDriver is installed correctly and compatible with your Chrome browser version.
  - If the script fails due to changes in YouTube's HTML structure, you may need to update the CSS selectors used to locate elements such as comments and usernames.
- If the video title contains emojis or special characters, it may cause encoding errors. Consider handling such cases by encoding the title appropriately or modifying the script to handle Unicode characters.
- Always monitor the script execution and error logs to identify and address any issues promptly.
