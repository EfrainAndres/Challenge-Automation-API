"""Retrieves data from DuckDuckGo's api feature tests."""

import requests
import re

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from tests.e2e.src.api import (
    getDogsImages,
    getDogeCoinLinks
)

@scenario('../features/DuckDuckGo.feature', 'Search for dogs and print a list of all images retrieved')
def test_search_for_dogs_and_print_a_list_of_all_images_retrieved():
    """Search for 'dogs' and print a list of all images retrieved."""

@scenario('../features/DuckDuckGo.feature', 'Search for dogecoin and print a list of all urls')
def test_search_for_dogecoin_and_print_a_list_of_all_urls():
    """Search for dogecoin and print a list of all urls."""

@given('User want to send a request to DuckDuckGo API')
def user_want_to_send_a_request_to_duckduckgo_api():
    """User want to send a request to DuckDuckGo API."""
    global responseDog
    global responseDogeCoin

@when('User sends a request to the DuckDuckGo API with the search parameter with the value dogs')
def user_sends_a_request_to_the_duckduckgo_api_with_the_search_parameter_with_the_value_dogs():
    """User sends a request to the DuckDuckGo API with the search parameter with the value dogs"."""
    responseDog = getDogsImages("dogs")

    global dataDog
    dataDog = responseDog.json()

@then('User verifies the list of all images retrieved')
def user_verifies_the_list_of_all_images_retrieved():
    """User verifies the list of all images retrieved."""
    allImages = dataDog["results"]

    print("All images link with Dog search")
    for allImage in allImages:
        print(allImage["image"])

@when('User sends a request to the DuckDuckGo API with the search parameter with the value dogecoin')
def user_sends_a_request_to_the_duckduckgo_api_with_the_search_parameter_with_the_value_dogecoin():
    """User sends a request to the DuckDuckGo API with the search parameter with the value dogecoin."""
    responseDogeCoin = getDogeCoinLinks("dogecoin")

    global dataDogeCoin
    dataDogeCoin = responseDogeCoin.json()

@then('User verifies the list of all urls')
def user_verifies_the_list_of_all_urls():
    """User verifies the list of all urls."""
    urlResults = dataDogeCoin["Results"]

    for urlResult in urlResults:
        print(urlResult["FirstURL"])

    urlRelatedTopics = dataDogeCoin["RelatedTopics"]

    for urlRT in urlRelatedTopics:
        print(urlRT["FirstURL"])


