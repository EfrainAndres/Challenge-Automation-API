# Southern Backend Challenge

Build a small script that retrieves data from duckduckgo's api ( DuckDuckGo
 Instant Answer API ):
1. Search for 'dogs' and print a list of all images retrieved
2. Search for 'dogecoin' and print a list of all urls


## Installation
- The code has been tested on Python 3.9.4 and Windows 11
- `Pip` is required
- `Pytest`, `PytestBDD` and `Request` libraries were used

1. Clone repository:
```
git clone https://github.com/EfrainAndres/Challenge-Automation-API.git
```

2. Create Virtual Enviroment
- The idea is create this virtual enviroment, in the same folder (Challenge-Automation-API):
```
python -m venv venv
```
- Then we should activate the virtual enviroment:
```
myenv\Scripts\activate
```
Install the dependencies:
```
pip install -r requirements.txt
```

Running the tests:
- We can run the tests with the next commands:
```
make e2etest
```
Or
```
pytest tests/e2e -s --gherkin-terminal-reporter -vv --html=report.html --capture=tee-sys
```

## Test Report
- When running the tests, a folder called `report` is generated and inside the folder there is a file called `index.html` we open this file in the browser and we will be able to see the status of the test execution.
  - Test 1: Search for `dogs` and print a list of all images retrieved
  - Test 2: Search for `dogecoin` and print a list of all urls