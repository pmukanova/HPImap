# House price index map


## Step2: Project Proposal

### Overview
* Problem statement formation: Make HPI* map to find desirable areas to buy or invest in real estate. Make the process of buying a house easier and mobile.
* Context: Correlate the map with county characteristics in the US to enrich the data. Analyze data by states, possibly by zip.   
* Criteria for success: Building an interactive map for users to select areas with Low HPI and high score
* Scope of solution space : an interactive map, database, web app. 

### Data source(s)
1. Data.Census.gov 
1. 2019 Data Profiles | American Community Survey | US Census Bureau

> _* *HPI -House Price Index. A house price index (HPI) measures the price changes of residential housing as a percentage change from some specific start date (which has HPI of 100)*_

### Goals:
1. __Make the process of buying a house easier and mobile:__ Help users identify great opportunities by looking at changes in the Housing price index by USA county level in each year since 2009.
1. __Target Audience:__ Users who want to purchase a house can benefit from this project because the solution will offer not only HPI but also will have a scoring field for schools, colleges, estimate crime rates, education levels and average income of the area. 
1. __Data used:__ Data will be extracted from census.gov using census API.

### Specifications
> As a result of the migration of wealthier residents and more upscale businesses into less-affluent urban areas, the fundamental complexion of the neighborhood is transformed: demographics shift, the physical of the area characteristics evolve, and most notably, housing prices rise (Maciag, 2015).


## Step3: Data Collection
The American Community Survey (ACS) is an ongoing survey that provides data every year which is ACS 1-year estimate. 
The 5-year estimates from the ACS are "period" estimates that represent data collected over a period of time. The primary advantage of using multiyear estimates is the increased statistical reliability of the data for less populated areas and small population subgroups.

* Example Call for 5 year estimate: `api.census.gov/data/2019/acs/acs5/profile?get=group(DP02)&for=county:*&key=YOUR_KEY_GOES_HERE` 
* Example Call for 1 year estimate: `api.census.gov/data/2019/acs/acs1/profile?get=group(DP02)&for=county:*&key=YOUR_KEY_GOES_HERE`

As you can see we are pulling data on for all counties in US. The group parameter will change according which profile information we are looking for. As for year, we will have to call it in a loop to constract the API from 2009 to 2019. 

## Step4: Data Exploration
### Data Profiles
Data Profiles contain broad social, economic, housing, and demographic information. The data are presented as population counts and percentages. There are over 1,000 variables in this dataset for each profile.

Since the column names have id instead of names, I will need a reference table to look up the meaning of each column in datasets. 
Example: Variable DP02_0002PE, “Family households (families)”, represents the percent estimate for table DP02 row number 2.

### Variables
I extracted variables for each year from 2009 to 2019 from census API and plan to use it as a reference table. 
* Example Call for 5 year estimate for 2019: `https://api.census.gov/data/2019/acs/acs5/profile/variables.json` 
* Example Call for 1 year estimate for 2019: `https://api.census.gov/data/2019/acs/acs1/profile/variables.json`

During the exploration step I noticed some values are unusefull since they don't have rational numerical values. Those values need to be cleaned or dropped.I plan to clean it on loading step using Spark. Please, refer to following table for explanation of annotation values for more understanding. 

![image](https://user-images.githubusercontent.com/9127333/147526263-dd4e13f6-ad2b-44f2-921a-4c48c6d572d4.png)


## Step5: : Prototyping Your Data Pipeline
During the prototyping step I had to automate the process of extracting, transforming and loading the data from data.census.gov. 

### Extract
I wrote OOP python class named **CensusDataProfiles** to constract API calls using requests library. By defining a base url and passing a group name and a year as a parameter we make those calls. The class downloads 10 csv files(2009-2019) for each profile group which is:
* DP02 - social characteristics
* DP03 - Economic characteristics
* DP04 - housing characteristics
* DP05 - demographic characteristics

I wrote another OOP python class named **CensusVariables** which is inherits from parent class **CensusDataProfiles** and downloads variables - data dictionary for each year for all the data profiles at ones. 

### Transform 
I used pandas dataframe to drop null values: 
```
df = df.dropna(axis='columns', how='all')
```
### Load
The extracted and cleaned data gets written in Azure blob storage by creating spark Dataframe and mounting the cloud folder. 
```
sparkDF=spark.createDataFrame(df)
sparkDF.write.mode("overwrite").parquet('dbfs:/mnt/FileStore/MountFolder/census_data/{}/{}_{}_year_estimate.parquet'.format(self.group_name,year,self.estimate))
```

## Data Model 
As you can see I used Star Schema and my main table will be housing characteristics. Other entities can be easily joined using county id and users can get sophisticated data for the area they looking for. 

![Census Data Profiles ER Diagram (1)](https://user-images.githubusercontent.com/9127333/147698656-0976b7e1-ada4-4fb2-a902-b104ce58f312.png)


## Step6: Scale Your Prototype
I chose to use Azure Databricks for scaling since the data does not need to be pulled regularly. The census data gets updated once a year. Databricks was the great solution offering cluster with Spark API comparing to Azure Data Factory which uses GUI to integrate data and do not offer much flexibility. I chose Databricks because it implements a programmatic approach that provides the flexibility of fine-tuning codes to optimize performance. 

Another point to note is, befor pulling the data, I mounted a storage account container to write data and for that we have to give credentials like:
```
 `storageAccountName = 'censusstorage'`
 `storageAccountAccessKey ='____________________________________________________'`
 `blobContainerName = 'firstcontainer'`
```
## Step7: Create The Deployment Architecture
![Deployment_Architecture](https://user-images.githubusercontent.com/9127333/147524495-e3b60ce2-c6af-40f4-9149-2a75372c664e.jpeg)
As architecture shows I make to API calls: one for Data profiles, second for yearly variables and write the data in blob storages using Azure Databricks. 
After that I intent to dump the data into Azure CosmosDB so data analytics can run their analysis using Azure Analysis services. Moreover, I built a monitoring dashboard using Azure Monitor to monitor the resources my pipeline is using.

## Step 8: Build a Monitoring Dashboard
![image](https://user-images.githubusercontent.com/9127333/147698040-0a4e9963-c6e0-429b-83b5-1432175d826b.png)

Link to the Azure Monitor: [Census Dashboard]( https://portal.azure.com/#@perizatmenardgmail.onmicrosoft.com/dashboard/arm/subscriptions/818dc134-6e7c-41a1-91e1-7bd398371a23/resourceGroups/dashboards/providers/Microsoft.Portal/dashboards/288897f7-5fb4-47d6-a662-2c4281604c73 )

## Conclusion 
The dataset is cleaned and ready for analysis. It includes data for social, economic, housing, and demographic information of counties in US.


