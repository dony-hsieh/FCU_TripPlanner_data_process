import pathlib

from database import Database
from definitions import *
from utils import *


def download_gov_attraction_data():
    for url, fp in DOWNLOAD_CSV:
        fp = str(pathlib.Path(fp).absolute())
        status = download_csv(url, fp)
        print(f"[*] Downloading of \"{fp}\": {status}")


def extract_attraction_data():
    attraction_csv_data = []
    attrs = [SCENIC_SPOT_CSV_ATTR, RESTAURANT_CSV_ATTR, HOTEL_CSV_ATTR, ACTIVITY_CSV_ATTR]
    for i, dcsv in enumerate(DOWNLOAD_CSV):
        # load csv file
        load_fp = str(pathlib.Path(dcsv[1]).absolute())
        current_attraction_csv_data = load_csv(load_fp, ATTRACTION_CSV_ATTR)  # load as Attraction class
        for cur_attraction_row in current_attraction_csv_data:
            if "Attraction_type" in cur_attraction_row:
                cur_attraction_row["Attraction_type"] = ATTRACTION_TYPE[i]
        attraction_csv_data += current_attraction_csv_data
        subset_csv_data = load_csv(load_fp, attrs[i])  # load as Attraction.<Subset> class

        # store temp csv file
        store_fp = str(pathlib.Path(TEMP_SUBSET_CSV[i]).absolute())
        store_csv(store_fp, subset_csv_data)  # store Attraction.<Subset> temp csv
        print(f"[*] \"{store_fp}\" has been written {len(subset_csv_data)} rows")

    store_fp = str(pathlib.Path(TEMP_ATTRACTION_CSV).absolute())
    store_csv(store_fp, attraction_csv_data)  # store Attraction temp csv
    print(f"[*] \"{store_fp}\" has been written {len(attraction_csv_data)} rows")


def insert_attraction_data_to_database():
    # prepare statements and args
    sql_load_statements = {}
    attraction_temp_fp = f"{pathlib.Path(TEMP_ATTRACTION_CSV).absolute()}"
    subset_temp_fp = [f"{pathlib.Path(fp)}" for fp in TEMP_SUBSET_CSV]
    attraction_attr_mapping = [f"`{attr}`" for attr in ATTRACTION_CSV_ATTR]
    subset_attr_mapping = [
        ["`Attraction_id`"] + [f"`{attr}`" for attr in SCENIC_SPOT_CSV_ATTR[1:]],
        ["`Attraction_id`"] + [f"`{attr}`" for attr in RESTAURANT_CSV_ATTR[1:]],
        ["`Attraction_id`"] + [f"`{attr}`" for attr in HOTEL_CSV_ATTR[1:]],
        ["`Attraction_id`"] + [f"`{attr}`" for attr in ACTIVITY_CSV_ATTR[1:]]
    ]
    sql_basic_load_statement = """
            LOAD DATA LOCAL INFILE %s
            REPLACE
            INTO TABLE {}
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\r\n'
            IGNORE 1 ROWS
            ({});
        """
    sql_load_statements["Attraction"] = sql_basic_load_statement.format("`Attraction`", ",".join(attraction_attr_mapping)).strip()
    for i, key in enumerate(("Scenic_spot", "Restaurant", "Hotel", "Activity")):
        sql_load_statements[key] = sql_basic_load_statement.format(f"`{key}`", ",".join(subset_attr_mapping[i])).strip()

    # execute insertion
    db = Database()
    print("[*] Start to execute loading data")
    db.execute_CUD(sql_load_statements["Attraction"], (attraction_temp_fp,))
    db.execute_CUD(sql_load_statements["Scenic_spot"], (subset_temp_fp[0],))
    db.execute_CUD(sql_load_statements["Restaurant"], (subset_temp_fp[1],))
    db.execute_CUD(sql_load_statements["Hotel"], (subset_temp_fp[2],))
    db.execute_CUD(sql_load_statements["Activity"], (subset_temp_fp[3],))


def process_gov_attraction_data():
    # 1. download gov attraction data
    download_gov_attraction_data()
    # 2. attract data from csv files (handle and write temp csv)
    extract_attraction_data()
    # 3. build "LOAD DATA" sql statements
    # 4. insert csv to database
    insert_attraction_data_to_database()
    print("[*] Process \"process_gov_attraction_data()\" end")


if __name__ == "__main__":
    process_gov_attraction_data()