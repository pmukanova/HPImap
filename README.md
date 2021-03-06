# HPImap
Capstone Project 

* Perizat Menard
* Email: p.mukanova@gmail.com
* Skype: pmukanova

# Open-ended Capstone 
## Step2: Project Proposal

## Overview
* Problem statement formation: Make HPI* map to find desirable areas to buy or invest in real estate. Make the process of buying a house easier and mobile.
* Context: Correlate the map with zip code characteristics in the US to enrich the data. Analyze data by states, possibly by zip.   
* Criteria for success: Building an interactive map for users to select areas with Low HPI and high score
* Scope of solution space : an interactive map, database, web app. 

## Data source(s)
1. Data.Census.gov 
1. fhfa.gov
1. FHFA HPI County Map
1. superzip-example.html 
1. 2019 Data Profiles | American Community Survey | US Census Bureau

_* *HPI -House Price Index. A house price index (HPI) measures the price changes of residential housing as a percentage change from some specific start date (which has HPI of 100)*_

## Goals:
1. __Make the process of buying a house easier and mobile:__ Help users identify great opportunities by looking at changes in the Housing price index by USA or Census Division, State, MSA, Puerto Rico in each year since 1991.
1. __Target Audience:__ Users who want to purchase a house can benefit from this project because the solution will offer not only HPI but also will have a scoring field for schools, colleges, estimate crime rates, education levels and average income of the area. 
1. __Data used:__ Data will be extracted from FHFA.gov and census.gov. I will use API’s or download directly from websites. 

## Specifications
 As a result of the migration of wealthier residents and more upscale businesses into less-affluent urban areas, the fundamental complexion of the neighborhood is transformed: demographics shift, the physical of the area characteristics evolve, and most notably, housing prices rise (Maciag, 2015).

## Milestones
### Extract
* Download data from sources listed in Section Overview #5. Host it in Dockers. 
### Transform
* Use dataframes to do manipulations with data.
### Load
* Load the data to cloud storages and use visualization tools to make it interactive: D3.js.

