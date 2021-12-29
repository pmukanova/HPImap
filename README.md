# Open-ended Capstone 
# House price index map

* Perizat Menard
* Email: p.mukanova@gmail.com
* Skype: p.mukanova

## Step2: Project Proposal

### Overview
* Problem statement formation: Make HPI* map to find desirable areas to buy or invest in real estate. Make the process of buying a house easier and mobile.
* Context: Correlate the map with county characteristics in the US to enrich the data. Analyze data by states, possibly by zip.   
* Criteria for success: Building an interactive map for users to select areas with Low HPI and high score
* Scope of solution space : an interactive map, database, web app. 

### Data source(s)
1. Data.Census.gov 
1. 2019 Data Profiles | American Community Survey | US Census Bureau

_* *HPI -House Price Index. A house price index (HPI) measures the price changes of residential housing as a percentage change from some specific start date (which has HPI of 100)*_

### Goals:
1. __Make the process of buying a house easier and mobile:__ Help users identify great opportunities by looking at changes in the Housing price index by USA county level in each year since 2009.
1. __Target Audience:__ Users who want to purchase a house can benefit from this project because the solution will offer not only HPI but also will have a scoring field for schools, colleges, estimate crime rates, education levels and average income of the area. 
1. __Data used:__ Data will be extracted from census.gov using census API.

### Specifications
 As a result of the migration of wealthier residents and more upscale businesses into less-affluent urban areas, the fundamental complexion of the neighborhood is transformed: demographics shift, the physical of the area characteristics evolve, and most notably, housing prices rise (Maciag, 2015).

### Milestones
#### Extract
* Download data from sources listed in Section Overview #5. Host it Azure Storage Account. 
#### Transform
* Use pandas and spark dataframes to do manipulations with data.
#### Load
* Load the data to Azure Blob storage using Spark.

## Step3: Data Collection
The American Community Survey (ACS) is an ongoing survey that provides data every year which is ACS 1-year estimate. 
The 5-year estimates from the ACS are "period" estimates that represent data collected over a period of time. The primary advantage of using multiyear estimates is the increased statistical reliability of the data for less populated areas and small population subgroups.

Example Call: api.census.gov/data/2019/acs/acs5/profile?get=group(DP02)&for=us:1&key=YOUR_KEY_GOES_HERE 

## Step4: Data Exploration
Data Profiles contain broad social, economic, housing, and demographic information. The data are presented as population counts and percentages. There are over 1,000 variables in this dataset for each profile.

Since the column names have id instead of names, I will need a refernce table to look up the meaning of ech column. 

Example: Variable DP02_0002PE, “Family households (families)”, represents the percent estimate for table DP02 row number 2.
I extracted variables for each year from census API and plan to use it as a reference table. 

During the exploration step I noticed some values are unusefull since they don't have rational numerical values. Those values needs to be cleaned or droped.I plan to clean it on loading step using Spark. Please, refer to following table for explanation of annotation values for more understanding. 
![image](https://user-images.githubusercontent.com/9127333/147526263-dd4e13f6-ad2b-44f2-921a-4c48c6d572d4.png)

After Exploraing data in this dataset, I came to following Data Model:
![Census Data Profiles ER Diagram](https://user-images.githubusercontent.com/9127333/147525097-94563c5f-5216-486b-8645-3d46c5369fd1.png)

## Step5: : Prototyping Your Data Pipeline
During the prototyping step I had to automate the process of extracting, transforming and loading the data from data.census.gov. 

### Extract
I wrote python script to constract API calls using request library. 

### Transform 
Using spark I transformed pandas dataframe to spark's to drop null values. 

### Load
The extracted and cleaned data gets written in Azure blob storages. 


## Step6: Scale Your Prototype
I chose to use Azure Databricks for scaling since the data does not need to be pulled regularly. The census data gets updated once a year. Databricks was the great solution offering cluster with Spark framework comparing to Azure Data Factory which comes with overhead of scheduling and monitoring pipeline. 

## Step7: Create The Deployment Architecture
![Deployment_Architecture](https://user-images.githubusercontent.com/9127333/147524495-e3b60ce2-c6af-40f4-9149-2a75372c664e.jpeg)
As architecture shows I make to API calls: one for Data profiles, second for yearly variables and write the data in blob storages using Azure Databricks. 
After that I intent to dump the data into Azure CosmosDB so data analytics can run their analysis using Azure Analysis services. 

## Step 8: Build a Monitoring Dashboard
Link to the Azure Monitor: https://portal.azure.com/#@perizatmenardgmail.onmicrosoft.com/dashboard/arm/subscriptions/818dc134-6e7c-41a1-91e1-7bd398371a23/resourceGroups/dashboards/providers/Microsoft.Portal/dashboards/288897f7-5fb4-47d6-a662-2c4281604c73 

## Conclusion 



