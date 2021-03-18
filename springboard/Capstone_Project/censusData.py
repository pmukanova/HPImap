import requests
import pandas as pd
import concurrent.futures
import time

start = time.perf_counter()

PATH = '/Users/perizatmenard/springboard/Capstone_Project'
group_names = ["DP02", "DP03", "DP04", "DP05"]


def census_request():
    HOST = "https://api.census.gov/data"
    dataset = "acs/acs1/profile"
    return HOST, dataset


def get_path(group_name):
    path = '/'.join([PATH, group_name, ''])
    return path


def get_predicates(group_name):
    predicates = {}
    get_vars = "group({})".format(group_name)
    predicates["get"] = get_vars
    #get_vars = ["DP02_" + str(i+1).zfill(4) + "E" for i in range(154)]
    #get_vars = "group(DP02)"
    #predicates["for"] = "metropolitan%20statistical%20area/micropolitan%20statistical%20area:*"
    predicates["for"] = "county:*"
    predicates["key"] = "e61340309f1ac39404000c3efba3d6921c359b66"
    return predicates


def download_census_tables(group_name):
    for year in range(2011, 2020):
        HOST, dataset = census_request()
        predicates = get_predicates(group_name)
        base_url = "/".join([HOST, str(year), dataset])
        result = requests.get(base_url, params=predicates)
        df = pd.DataFrame(columns=result.json()[0], data=result.json()[1:])
        df["year"] = year
        print(df.head(3))
        my_path = get_path(group_name)
        fname = "{}.csv".format(year)
        df.to_csv(my_path+fname)


with concurrent.futures.ThreadPoolExecutor() as executor:
    print("Getting Data...")
    executor.map(download_census_tables, group_names)

"""
download_census_tables(group_names[0])
download_census_tables(group_names[1])
download_census_tables(group_names[2])
download_census_tables(group_names[3])
"""

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
