from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Airbnb scraper'
LONG_DESCRIPTION = 'Airbnb scraper'

setup(
    name="AirbnbScraper",
    version=VERSION,
    author="Arnoldas Januska",
    author_email="<januska.arnoldas@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'selenium'],
    keywords=['python', 'airbnb', 'scraper'],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)
