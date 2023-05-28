# IMDb Ratings Converter

This repository contains a Python script `imdb_ratings_csv_to_json.py` that converts IMDb movie ratings from a CSV file to a JSON file. This is useful for individuals who want to manipulate their IMDb ratings data for various purposes such as data analysis, machine learning, or other personal projects. This script is designed to take the CSV file downloaded directly from the IMDb website that includes all the ratings from your IMDb account and modify it in a way that makes it short enough to use for various applications.

## Getting Started

1. Download your IMDb ratings data in CSV format from the IMDb website.

   1. You can do this by navigating to imdb.com, logging in, and going to "Your Ratings"
   2. On the "Your Ratings" page, click the menu button on the right. ![IMDB "Your Ratings" menu screenshot](https://github.com/fjbarrett/IMDbRatings2JSON/blob/main/account-ratings.png?raw=true)
   3. Now click export and download your ratings as a CSV

2. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/fjbarrett/IMDbRatings2JSON.git
   ```

3. Place your downloaded CSV file in the same directory as the script.

## Usage

To run the script, navigate to the directory containing the script and execute the following command in the terminal:

```shell
python imdb_ratings_csv_to_json.py your_ratings.csv
```

Replace your_ratings.csv with the filename of your IMDb ratings CSV file. The script will output a JSON file named imdb_ratings.json in the same directory.

This is handy if you want to copy and paste a large quantity of ratings into ChatGPT and have it recommend a film. Currently, copying the entire ratings.csv from imdb.com and pasting into chat.openai.com is not possible because it is too much text. The .json from this output however, is much thinner and allows for pasting into ChatGPT.

## Quick tip for getting movie recommendations from ChatGPT

When you paste your movie ratings into ChatGPT from the created movies.json file, explain to ChatGPT that you want a recommendation for a movie that is not already on the list. Otherwise it usually gives recommendations for movies you may have seen.

## Future ideas

Ideally, this python script would take the ratings.csv and use the OpenAI API to provide the recommendation and simply spit out a movie title into the command-line. Integrating the OpenAI API is the next step in making it easier to use ChatGPT to recommend films, which I've found it does fairly well.
