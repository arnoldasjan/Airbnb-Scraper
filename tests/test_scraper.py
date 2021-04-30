import pandas as pd
import pytest
from AirbnbScraper.scraper import Scraper

scraper = Scraper(number_of_listings=20, city="London", country="United Kingdom")


def test_number_of_listings():
    assert scraper.number_of_listings == 20


def test_city():
    assert scraper.city == "London"


def test_country():
    assert scraper.country == "United Kingdom"


def test_get_page():
    assert (
        scraper.get_page(
            url=f"https://www.airbnb.com/s/homes?tab_id=home_tab&refinement_paths[]=/homes"
            f"&date_picker_type=flexible_dates"
            f"&query={scraper.city}, {scraper.country}"
            f"&search_type=pagination"
            f"&items_offset=0"
        )
        == "OK"
    )
    assert scraper.get_page("ssjsjsjs.com") == "FAILED"


def test_find_listings():
    listings = scraper.find_listings()
    assert len(listings) == 20


def test_scrape_city():
    df = scraper.scrape_city()
    assert type(df) == pd.DataFrame
