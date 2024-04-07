import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def get_youtube_title(video_url):
    try:
        # Make a GET request to the YouTube video URL
        response = requests.get(video_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the title element
        title_element = soup.find('title')

        # Extract the title text
        video_title = title_element.text.strip()

        return video_title
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_youtube_comments(video_url,video_title):
    driver = webdriver.Chrome()

    try:
        # Open the video URL
        driver.get(video_url)
        time.sleep(5)  # Waiting for the video to load
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(20):
            body.send_keys(Keys.END)
            time.sleep(1)

        # Extract comments and usernames
        comments = driver.find_elements(By.CSS_SELECTOR, '#content-text')
        usernames = driver.find_elements(By.CSS_SELECTOR, '#author-text')
        comment_list = [(user.text, comment.text) for user, comment in zip(usernames, comments)]

        # Save comments to CSV file
        with open(f'{video_title}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Username', 'Comment'])
            for user, comment in comment_list:
                writer.writerow([user, comment])

        print(f'Comments extracted and saved to {video_title}.csv')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the webdriver
        driver.quit()

# Example usage
video_url = "https://www.youtube.com/watch?v=LIWHz4g_n_w"
video_title = get_youtube_title(video_url).split('-')[0]
extract_youtube_comments(video_url,video_title)
