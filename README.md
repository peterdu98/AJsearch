# Article and Journal search (AJsearch) - web application (Flask)

AJsearch is the web application for searching academic articles or journals. The app aims to support researchers or readers to search for articles or journals that are relevant to their desired topics. Unlike other search engines, the app uses NLP and machine learning algorithms to find top similar results for a given query.

The project includes 3 main components to build such as data crawling pipeline, recommended models, and user interface (UI). 
* Data will be crawled from [arXiv.org](https://arxiv.org/), and the code can be extended to crawl other websites.
* Natural Language Processing (NLP) and machine learning techniques will be used to build and evaluate the recommended model respectively.
* The UI will be implemented after the model has been made.

## Project showcase
The app is hosted at [http://ajsearch.azurewebsites.net/](http://ajsearch.azurewebsites.net/)

## Tasks
- [x] Crawl data from arXiv
- [x] Implement automated data crawling pipeline
- [x] Design and implement User Interface
- [x] Implement data models and connect Azure SQL Database
- [x] Implement and experiment recommended models
- [x] Build pipelines for getting data and running the recommended model

## Tech Stack:
1. HTML, CSS, JavaScript
2. Flask
3. Bootstrap
4. Azure Cloud
5. SQL

## Requirements
1. Python version 3.7 or above

## How to run the app
1. Clone the project 

```
git clone https://ajsearch.scm.azurewebsites.net/
```

2. Install dependencies

```
pip install requirements.txt
```

3. Customise your .env file (dbstring is required)

```
vi .env
```

4. Copy and paste the binary file of your model into the `./app/model/` folder (optional)
5. Create a `./app/data/` folder to put your data for seeding database
6. Modify a data model in a `models.py` file (Optional)
5. Create database

```
flask db_create
```

6. Seed data points into your database

```
flask db_seed
```

7. Run the app

```
flask run
```

## References
1. [arXiv website](https://arxiv.org/)
