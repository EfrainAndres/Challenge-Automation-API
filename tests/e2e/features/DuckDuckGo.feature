Feature: Retrieves data from DuckDuckGo's api

    Background: 
        Given User want to send a request to DuckDuckGo API

    Scenario: Search for dogs and print a list of all images retrieved
        When User sends a request to the DuckDuckGo API with the search parameter with the value dogs
        Then User verifies the list of all images retrieved

    Scenario: Search for dogecoin and print a list of all urls
        When User sends a request to the DuckDuckGo API with the search parameter with the value dogecoin
        Then User verifies the list of all urls