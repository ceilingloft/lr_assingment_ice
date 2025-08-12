# lr_assingment_ice


### Converting data to csv (for ease of processing and memory to read it in):
* `xlsx2csv data/arrests-0923-0625.xlsx data/arrests-0923-0625.csv`
* `sed -i 1,6d data/arrests-0923-0625.csv`
* NB - there is something weird in the excel datetime formatting, and it has converted to a 12 hour clock (17.41:00 -> 05.41.00)
	* This means it should not be used for anything looking at time of day of arrest 
	* For most of the analysis this can be used thhough



### Next steps:

* Data processing:
	* xlsx files take quite a while to load - if we want to use more data (e.g. look at historic data, or set up code to process when new data is released etc.), then it's probably worth converting them to csvs (e.g. using `xlsx2csv`)
	