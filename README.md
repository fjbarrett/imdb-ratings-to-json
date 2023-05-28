# IMDb Ratings Converter

This repository contains a Python script `imdb_ratings_csv_to_json.py` that converts IMDb movie ratings from a CSV file to a JSON file. This is useful for individuals who want to manipulate their IMDb ratings data for various purposes such as data analysis, machine learning, or other personal projects. This script is designed to take the CSV file downloaded directly from the IMDb website that includes all the ratings from your IMDb account and modify it in a way that makes it short enough to use for various applications.

## Getting Started

1. Download your IMDb ratings data in CSV format from the IMDb website.

   1. You can do this by navigating to imdb.com, logging in, and going to "Your Ratings"
   2. On this menu, click the menu button on the right. ![IMDB "Your Ratings" menu screenshot](https://github.com/fjbarrett/IMDbRatings2JSON/blob/main/account-ratings.png?raw=true)
   3. Now click export and download your ratings as a CSV

2. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/IMDb-Ratings-Converter.git
   ```

3. Place your downloaded CSV file in the same directory as the script.

## Usage

To run the script, navigate to the directory containing the script and execute the following command in the terminal:

```shell
python imdb_ratings_csv_to_json.py your_ratings.csv
```

Replace your_ratings.csv with the filename of your IMDb ratings CSV file. The script will output a JSON file named imdb_ratings.json in the same directory.

## License

This project is licensed under the terms of the MIT license.

Remember to replace "`yourusername`" with your actual GitHub username in the `git clone` command.

```shell
Please note that this is a simple README file. Depending on the complexity of your project and the needs of your users, you might want to provide more detailed instructions, add a section about how to contribute to your project, provide contact information, and so on.
```