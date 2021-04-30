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

#### Sample dictionary of data collected from one listing

```
dictionary = {
            "title": 'HEART OF OLD TOWN - TRAKU STUDIO',
            "city": 'Vilnius',
            "country": 'Lithuania,
            "apartment_type": 'Entire apartment',
            "district": 'Vilnius',
            "guests": 2,
            "bedrooms": 'Studio',
            "beds": 1,
            "baths": 1,
            "amenities": "['Kitchen', 'Wifi', 'Free parking', 'Self check-in']",
            "price": 28.0,
            "rating": 4.65,
            "reviews": 214.0,
            "is_superhost": False,
            "listing_url": 'https://www.airbnb.com/rooms/12829595?adults=1&children=0&infants=0&check_in=2021-06-25&check_out=2021-06-27&previous_page_section_name=1000&federated_search_id=1070c68b-6c87-4f8a-9767-eb950a2c148d',
            "image_url": 'https://a0.muscache.com/im/pictures/90555ad6-3fd7-4e1d-b8a5-b0ec96d7ce16.jpg?im_w=720',
        }
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)