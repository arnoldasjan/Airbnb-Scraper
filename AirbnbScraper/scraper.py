import pandas as pd
import time
import random
import re
import os
from selenium import webdriver
import sys


class Scraper:
    """Airbnb scraper class that uses Selenium and scrapes data from listings
    after city search.

    Attributes
        * driver : Selenium Chrome Webdriver

    Methods
        * driver - gets the current driver
        * get_page - tries to get specified URL
        * find_listings - finds all listings in a specified Airbnb URL
        * find_header - find listing's header
        * get_apartment_type - gets listing's apartment's type
        * get_district - gets listing's district
        * get_title - gets listing's title
        * get_listing_data - gets listing's data
        * get_guests - parses guests from listing's data
        * get_bedrooms - parses bedrooms from listing's data
        * get_beds - parses beds from listing's data
        * get_baths - parses baths from listing's data
        * get_amenities - gets a list of amenities
        * get_price - gets price per night
        * get_rating - gets listing's rating
        * get_reviews - gets listing's reviews number
        * check_if_superhost - checks if listing's owner is a superhost
        * get_listing_url - gets listing's url
        * get_image_url - gets front image url
        * scrape_one_city - scrapes one city
        * scrape_listings - scrapes number of listings specified
    """

    def __init__(self, number_of_listings: int, city: str, country: str) -> None:
        self.__number_of_listings = number_of_listings
        self.__city = city
        self.__country = country
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        try:
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            self.__driver = webdriver.Chrome(
                executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                options=chrome_options,
            )
        except TypeError:
            self.__driver = webdriver.Chrome("chromedriver", options=chrome_options)

    @property
    def driver(self) -> webdriver:
        """
        Returns the current Selenium Chromedriver
        :return: Selenium Chromedriver
        """
        return self.__driver

    def get_page(self, url: str) -> str:
        """Goes to a specified URL using driver and returns status
        :param url:
        :return: Status of method str
        """
        try:
            self.driver.get(url)
            return "OK"
        except:
            return "FAILED"

    def find_listings(self) -> list:
        """Uses driver to get all the listings in a page.
        :return: List of listings' containers
        """
        try:
            listings = self.driver.find_elements_by_class_name("_8s3ctt")
        except:
            listings = None
        return listings

    @staticmethod
    def find_header(listing) -> list:
        """Finds header of a listing, splits it and returns list of strings
        :param listing: Listing container
        :return: List of apartment type and district
        """
        try:
            header = listing.find_element_by_class_name("_b14dlit").text.split(" in ")
        except:
            header = None
        return header

    @staticmethod
    def get_apartment_type(header) -> str:
        """Parses apartment type from header element
        :param header: Header element from listing
        :return: listing's apartment type str
        """
        try:
            apartment_type = header[0]
        except:
            apartment_type = None
        return apartment_type

    @staticmethod
    def get_district(header) -> str:
        """Parses district from header element
        :param header: Header element from listing
        :return: listing's district str
        """
        try:
            district = header[1]
        except:
            district = None
        return district

    @staticmethod
    def get_title(listing) -> str:
        """Gets listing's title
        :param listing: Listing container
        :return: listing's title str
        """
        try:
            title = listing.find_element_by_class_name("_5kaapu").text
        except:
            title = None
        return title

    @staticmethod
    def get_listing_data(listing) -> list:
        """Gets data from listings about number of guests,
        baths, beds and bedrooms
        :param listing: Listing Container
        :return: List of listing's data
        """
        try:
            data = listing.find_elements_by_class_name("_kqh46o")[0].text.split(" · ")
        except:
            data = None
        return data

    @staticmethod
    def get_guests(data) -> int:
        """Parses and returns number of guests from listing's data list
        :param data: Data element from listing's container
        :return: number of guests int
        """
        try:
            guests = int(data[0].split()[0])
        except:
            guests = None
        return guests

    @staticmethod
    def get_bedrooms(data) -> str:
        """Parses and returns number of bedrooms from listing's data list
        :param data: Data element from listing's container
        :return: bedrooms str
        """
        try:
            bedrooms = data[1].split()[0]
        except:
            bedrooms = None
        return bedrooms

    @staticmethod
    def get_beds(data) -> int:
        """Parses and returns number of beds from listing's data list
        :param data: Data element from listing's container
        :return: number of beds int
        """
        try:
            beds = int(data[2].split()[0])
        except:
            beds = None
        return beds

    @staticmethod
    def get_baths(data) -> str:
        """Parses and returns baths from listing's data list
        :param data: Data element from listing's container
        :return: baths str
        """
        try:
            baths = data[3]
        except:
            baths = None
        return baths

    @staticmethod
    def get_amenities(listing) -> list:
        """Gets list of amenities from listing
        :param listing: Listing Container
        :return: List of amenities strings
        """
        try:
            amenities = listing.find_elements_by_class_name("_kqh46o")[1].text.split(
                " · "
            )
        except:
            amenities = None
        return amenities

    @staticmethod
    def get_price(listing) -> float:
        """Gets listing's price per night
        :param listing: Listing Container
        :return: Listing's price float
        """
        try:
            price = float(re.findall(
                "\d+", listing.find_element_by_class_name("_olc9rf0").text
            )[0])
        except:
            price = None
        return price

    @staticmethod
    def get_rating(listing) -> float:
        """Gets listing's rating if it has one
        :param listing: Listing Container
        :return: Listing's rating float
        """
        try:
            rating = listing.find_element_by_class_name("_10fy1f8").text
        except:
            rating = None

        return rating

    @staticmethod
    def get_reviews(listing) -> int:
        """Gets listing's number of reviews if it has it
        :param listing: Listing Container
        :return: Listing's number of reviews int
        """
        try:
            reviews = int(re.findall(
                "\d+", listing.find_element_by_class_name("_a7a5sx").text
            )[0])
        except:
            reviews = None

        return reviews

    @staticmethod
    def check_if_superhost(listing) -> bool:
        """Checks if listing's owner is a superhost
        :param listing: Listing Container
        :return: True if the owner is a superhost, else False
        """
        try:
            listing.find_element_by_class_name("_ufoy4t")
            is_superhost = True
        except:
            is_superhost = False

        return is_superhost

    @staticmethod
    def get_listing_url(listing) -> str:
        """Gets listing's URL
        :param listing: Listing Container
        :return: Listing's URL str
        """
        try:
            listing_url = listing.find_element_by_class_name("_mm360j").get_attribute(
                "href"
            )
        except:
            listing_url = None

        return listing_url

    @staticmethod
    def get_image_url(listing) -> str:
        """Gets listing's front image's URL
        :param listing: Listing Container
        :return: Listing's front image's URL str
        """
        try:
            image_url = listing.find_element_by_class_name("_9ofhsl").get_attribute(
                "src"
            )
        except:
            try:
                image_url = listing.find_element_by_class_name("_6tbg2q").get_attribute(
                    "src"
                )
            except:
                try:
                    image_url = listing.find_element_by_class_name(
                        "_1cb9q3xq"
                    ).get_attribute("src")
                except:
                    image_url = None

        return image_url

    def scrape_one_listing(self, listing) -> dict:
        """Does the whole scraping procedure for one listing element
        :param listing: Listing Container
        :return: Dictionary with parsed data from a listing
        """
        header = self.find_header(listing)

        if header:
            apartment_type = self.get_apartment_type(header)
            district = self.get_district(header)
        else:
            apartment_type = district = None

        title = self.get_title(listing)

        data = self.get_listing_data(listing)

        if data:
            guests = self.get_guests(data)
            bedrooms = self.get_bedrooms(data)
            beds = self.get_beds(data)
            baths = self.get_baths(data)
        else:
            guests = bedrooms = beds = baths = None

        amenities = self.get_amenities(listing)

        price = self.get_price(listing)

        rating = self.get_rating(listing)

        reviews = self.get_reviews(listing)

        is_superhost = self.check_if_superhost(listing)

        listing_url = self.get_listing_url(listing)

        image_url = self.get_image_url(listing)

        dictionary = {
            "title": title,
            "city": self.__city,
            "country": self.__country,
            "apartment_type": apartment_type,
            "district": district,
            "guests": guests,
            "bedrooms": bedrooms,
            "beds": beds,
            "baths": baths,
            "amenities": amenities,
            "price": price,
            "rating": rating,
            "reviews": reviews,
            "is_superhost": is_superhost,
            "listing_url": listing_url,
            "image_url": image_url,
        }

        return dictionary

    def scrape_city(self) -> pd.DataFrame:
        """Scrapes and returns the dataframe with the listings data from Airbnb
        based on city, country and the number of listings wanted
        :return: pandas Dataframe with scraped data
        """

        items_count = 0
        dictionaries = []

        while items_count < self.__number_of_listings:

            url = (
                f"https://www.airbnb.com/s/homes?tab_id=home_tab&refinement_paths[]=/homes"
                f"&date_picker_type=flexible_dates"
                f"&query={self.__city}, {self.__country}"
                f"&search_type=pagination"
                f"&items_offset={items_count}"
            )

            status = self.get_page(url)

            if status == "OK":
                listings = self.find_listings()

                if listings:
                    for listing in listings:

                        sys.stdout.write("\r")
                        sys.stdout.write(
                            f"Scraping {self.__city}, {self.__country}: {items_count+1} from {self.__number_of_listings}"
                        )
                        sys.stdout.flush()

                        listing_data = self.scrape_one_listing(listing)

                        dictionaries.append(listing_data)

                        items_count += 1

                        if items_count == self.__number_of_listings:
                            break

                else:
                    print("No more listings found")
                    break

                time.sleep(random.uniform(2, 3))

            else:
                break

        return pd.DataFrame(data=dictionaries)
