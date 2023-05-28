# IMDb Ratings Converter

This repository contains the Python script `imdb_ratings_csv_to_json.py`, designed to convert IMDb movie ratings from a CSV file to a JSON file. This is particularly useful for individuals who wish to manipulate their IMDb ratings data for a variety of purposes including data analysis, machine learning, or personal projects. The script is tailored to accept the CSV file downloaded directly from the IMDb website - encompassing all ratings from your IMDb account - and adjust it to a format that's easier to manipulate for multiple applications.

## Getting Started

1. Download your IMDb ratings data in CSV format from the IMDb website.

   1. This can be achieved by navigating to imdb.com, logging in, and selecting "Your Ratings".
   2. Within the "Your Ratings" page, select the menu button on the right. ![IMDB "Your Ratings" menu screenshot](https://github.com/fjbarrett/IMDbRatings2JSON/blob/main/account-ratings.png?raw=true)
   3. Select export and download your ratings as a CSV file.

2. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/fjbarrett/IMDbRatings2JSON.git
   ```

3. Position your downloaded CSV file in the same directory as the script.

## Usage

To operate the script, navigate to the directory that contains the script and execute the following command in the terminal:

```shell
python imdb_ratings_csv_to_json.py your_ratings.csv
```

Substitute `ratings.csv` with the filename of your IMDb ratings CSV file. The script will produce a JSON file named `movies.json` in the same directory.

This procedure is advantageous when you wish to transfer a significant amount of ratings into ChatGPT and request a film recommendation. At present, directly copying the complete ratings.csv from imdb.com and pasting into chat.openai.com is not viable due to the large volume of text. However, the output .json from this script is significantly less bulky, allowing for easy pasting into ChatGPT.

This is handy if you want to copy and paste a large quantity of ratings into ChatGPT and have it recommend a film. Currently, copying the entire ratings.csv from imdb.com and pasting into chat.openai.com is not possible because it is too much text. The .json from this output however, is much thinner and allows for pasting into ChatGPT.

## Quick Tip for Securing Movie Recommendations from ChatGPT

When transferring your movie ratings into ChatGPT from the generated `movies.json` file, make it clear to ChatGPT that you are seeking a recommendation for a movie that is not already listed. Otherwise, it may suggest movies you have already watched.

## Future ideas

In an ideal scenario, this Python script would take the `ratings.csv` file, interact with the OpenAI API to offer the recommendation, and subsequently output a movie title directly to the command-line. Integrating the OpenAI API represents the next evolutionary step in leveraging ChatGPT for film recommendations - a function at which it has proven adept.
