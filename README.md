# App backend

## Constitution
Python 3.8.3   
Framework : Django  3.2.6

## Local:

### Installation
Actualization: 24.8.2021  
`$ pip install -r requirements/local.txt`  

### Run application:
`python manage.py runserver --settings=config.settings.local`

### Best practies

#### Wrapper which verifies pep8, pyflakes and circular complexity
`$ flake8 --output-file=output.txt`

#### Python code formatter:
`$ black directory/`
 
## Production:

### Installation
`$ pip install -r requirements/production.txt`  
