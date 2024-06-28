[![Pytest Tests](https://github.com/Samska/pytest-serverest/actions/workflows/pytest.yml/badge.svg)](https://github.com/Samska/pytest-serverest/actions/workflows/pytest.yml)
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
 ├── .github/                               
 │    ├── workflows/                        
 │        ├── pytest.yml                            # Configuration for the tests on CI              
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

## Continuous integration

This project has continuous integration with GitHub Actions. The configuration file is located at the path .github/workflows/k6.yml. Every time a push is made to the main branch, the pipeline is executed. With each execution, an artifact is generated with the test results and saved in that execution, as well as the results are published on the gh-pages and are available for consultation on this [page](https://samska.github.io/pytest-project/report.html).
