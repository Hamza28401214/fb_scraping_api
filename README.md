# fb_scraping_api
scraping service using fastapi
# Scraping service with fastapi
## Data source:
Real madrid club official facebook page (public) 
## Project : 
Aims to extract public data from Real madrid facebook page
# installation 
- Use python 3.x

run the following command after cloning the repository:
#### create virtual environment
```bash
> python -m venv env
> cd env/scripts
> activate
> cd ../..
```
#### install requirements
```bash
> pip install -r requirements.txt
```

# run the API: 

```bash
> python main.py
```
### follow this link to start scraping : http://127.0.0.1:8000/scraping
### follow this link to see the data from db : http://127.0.0.1:8000/get_data


# run tests:
```bash
> python -m unittest    tests.tests.TestReadFromDb
```


# Conclusion :
    -   all system logs are stored under this directory : logs/record.log



