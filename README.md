# lr_assingment_ice


## Using the code

1. Set up a python environment and load `requirements.txt` e.g.

   > `python3 -m venv .env`

   > `source .env/bin/activate`

   > `pip install -r requirements.txt`

2. Checking paths: at the moment the setup code in the task notebooks uses `pathlib.Path`, and assumes you are running the code from within `task_notebooks` - if needed, you can change the paths at the top of each notebook

3. Download the data (see below for detail), make `data/`, and move the data file to `data/` 



## Data

This project uses ICE Arrests data from https://deportationdata.org/. The specific data used:
*  **2024-ICFO-39357 (Sept 2023 - Late Jun. 2025)** - NOTE, this is *not* the newest data that was released on Monday 11th Aug

The data from https://deportationdata.org/ is provided as .xlsx files. These use quite a lot of memory to read in, as there is a lot of type information encoded (and generally excel files are quite large). 

If you have sufficient memory on your machine, you can use the .xlsx files (the code is set up to work for either .xlsx or csv). If you are running into memory issues (you can try reading in the arrests data and check the number of rows in the df = 265185), then convert the excel file to a csv:


### Converting data to csv (for ease of processing and memory to read it in):
* `xlsx2csv data/arrests-0923-0625.xlsx data/arrests-0923-0625.csv`
* `sed -i 1,6d data/arrests-0923-0625.csv`
* NB - there is something weird in the excel datetime formatting, and it has converted to a 12 hour clock (17.41:00 -> 05.41.00)
	* This means it should not be used for anything looking at time of day of arrest 
	* For most of the analysis this can be used though


## Next steps:

* Making code more reproducable:
	* Most of the work has been done in notebooks so far, as this is explorative work. The notebooks are great for showing thinking, but not for producing reproducible code (important if we wanted to use more data, such as looking at historic data or setting up the code to process easily when new data is released). 
	* The next step would be to take the key processing functions and code (e.g. facility and county code) from the notebooks and standardise in `process_data.py`
* 
	