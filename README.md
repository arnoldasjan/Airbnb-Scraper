# Airbnb Scraper

<img alt="airbnblogo" src="Airbnb-Logo.png" width="200">

## Introduction

This is the Airbnb scraper package that can help you to scrape listings of your wanted cities.

## Installation

``` 
pip install git+https://github.com/arnoldasjan/Airbnb-Scraper
```

## Usage

```
from AirbnbScraper import scraper

s = scraper.Scraper(city='Vilnius', country='Lithuania', number_of_listings=30)
df = s.scrape_city()
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)