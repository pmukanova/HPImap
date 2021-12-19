import requests
import pandas as pd
import time


start = time.perf_counter()

PATH = "C:\\Users\perizatmenard\Documents\capstone_project"
group_names = ["DP02", "DP03", "DP04", "DP05"]
HOST = "https://api.census.gov/data"


class CensusDataProfiles:
    def __init__(self, profile_name,estimate):
        self.group_name = profile_name
        self.estimate =estimate

    
    def get_dataset(self):
        dataset = "acs/acs{}/profile".format(self.estimate)
        return dataset

    def get_path(self):
        path = '/'.join([PATH, self.group_name, ''])
        return path


    def get_predicates(self):
        predicates = {}
        get_vars = "group({})".format(self.group_name)
        predicates["get"] = get_vars
        predicates["for"] = "county:*"
        predicates["key"] = "e61340309f1ac39404000c3efba3d6921c359b66"
        return predicates


    def download_data_profiles(self):
        for year in range(2009, 2020):
            dataset = self.get_dataset()
            predicates = self.get_predicates()
            base_url = "/".join([HOST, str(year), dataset])
            result = requests.get(base_url, params=predicates)
            df = pd.DataFrame(columns=result.json()[0], data=result.json()[1:])
            df["year"] = year
            df["estimate"]=self.estimate
            print(df.head(3))
            my_path = self.get_path()
            fname = "{}_{}_year_estimate.csv".format(year,self.estimate)
            df.to_csv(my_path+fname)
        

social_data_for_1_year = CensusDataProfiles(group_names[0],1)
social_data_for_1_year.download_data_profiles()

economic_data_for_1_year=CensusDataProfiles(group_names[1],1)
economic_data_for_1_year.download_data_profiles()

housing_data_for_1_year = CensusDataProfiles(group_names[2],1)
housing_data_for_1_year.download_data_profiles()

demographic_data_for_1_year = CensusDataProfiles(group_names[3],1)
demographic_data_for_1_year.download_data_profiles()

social_data_for_5_year = CensusDataProfiles(group_names[0],5)
social_data_for_5_year.download_data_profiles()

economic_data_for_5_year = CensusDataProfiles(group_names[1],5)
economic_data_for_5_year.download_data_profiles()

housing_data_for_5_year = CensusDataProfiles(group_names[2],5)
housing_data_for_5_year.download_data_profiles()

demographic_data_for_5_year = CensusDataProfiles(group_names[3],5)
demographic_data_for_5_year.download_data_profiles()



class CensusVariables(CensusDataProfiles):

    def __init__(self,estimate):
        self.estimate = estimate


    def get_dataset(self):
        return super().get_dataset()
    
    def get_variables(self):
        for year in range(2009, 2020):
            dataset = self.get_dataset()
            base_url = "/".join([HOST, str(year), dataset,"variables"])
            result = requests.get(base_url)
            df = pd.DataFrame(data=result.json()[1:])
            fname = "{}_{}_year_variables.json".format(year,self.estimate) 
            path = PATH + "/variables/"
            df.to_json(path+fname)


    def create_mapping_file(self):
        for year in range(2009, 2020):
            variables_df = pd.read_json("C:\\Users\perizatmenard\Documents\capstone_project\\variables\\{}_{}_year_variables.json".format(year,self.estimate))
            mapping_df = variables_df[variables_df.columns[0:2]]
            fname = "{}_varibles_for_{}_year.csv".format(year,self.estimate) 
            path = PATH + "/variables/csv/"
            mapping_df.to_csv(path+fname)



variables_1_year = CensusVariables(1)
variables_1_year.get_variables()
variables_1_year.create_mapping_file()

variables_5_year = CensusVariables(5)
variables_5_year.get_variables()
variables_5_year.create_mapping_file()
        


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')