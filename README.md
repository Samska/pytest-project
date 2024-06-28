[![Badge ServeRest](https://img.shields.io/badge/API-ServeRest-green)](https://github.com/ServeRest/ServeRest/)

# Pytest Serverest Study

This is a sample project using Pytest for API and Web testing in the application https://serverest.dev and https://front.serverest.dev

## Pre-requisites

* Git
* Python

## Install

Clone this repo

```bash
  git clone https://github.com/Samska/pytest-project
```

Set up a virtual environment

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages

```bash
  pip install -r config/requirements.txt
```

## Running tests

`pytest` - Run all the tests

`pytest tests/web` - Run only web tests

`pytest tests/api` - Run only api tests

## Project structure

```
pytest-project/            
 ├── config/                                                                
 │    ├── requirements.txt                          # Required packages for the project
 ├── fixtures/                                                                
 │    ├── *                                         # Fixtures used in the tests such payloads and schemas 
 ├── reports/                                                              
 │    ├── *                                         # Reports created after the test execution                                                                
 ├── tests/                                         # Tests folder                               
 │    ├── api/                                      # API tests folder
 │        ├── utils/                                # Methods used for the api tests
 │        ├── *.py                                  # The tests itself           
 │    ├── web/                                      # Web tests folder
 │        ├── pages/                                # Methods used for the web tests
 │        ├── *.py                                  # The tests itself                 
 ├── .gitignore                                     # Untracked folder and files
 ├── config.py                                      # General configs such as base urls      
 ├── pytest.ini                                     # Used for logs, markers, timeouts and another configs for the pytest
 ├── README.md                                      # README with project overview and instructions
```