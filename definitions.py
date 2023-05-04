# ================================== download info ================================== #
# (web_url, storing_path)
DOWNLOAD_CSV = [
    ("https://media.taiwan.net.tw/XMLReleaseALL_public/Scenic_Spot_C_f.csv", "download/Scenic_Spot_C_f.csv"),
    ("https://media.taiwan.net.tw/XMLReleaseALL_public/Restaurant_C_f.csv", "download/Restaurant_C_f.csv"),
    ("https://media.taiwan.net.tw/XMLReleaseALL_public/Hotel_C_f.csv", "download/Hotel_C_f.csv"),
    ("https://media.taiwan.net.tw/XMLReleaseALL_public/Activity_C_f.csv", "download/Activity_C_f.csv")
]

# ================================== csv field attributes ================================== #
ATTRACTION_CSV_ATTR = [
    "Id",
    "Name",
    "Description",
    "Zipcode",
    "Add",
    "Region",
    "Town",
    "Tel",
    "Website",
    "Map",
    "Px",
    "Py",
    "Parkinginfo",
    "Attraction_type"
]

SCENIC_SPOT_CSV_ATTR = [
    "Id",
    "Toldescribe",
    "Travellinginfo",
    "Opentime",
    "Ticketinfo",
    "Remarks",
    "Keyword"
]

RESTAURANT_CSV_ATTR = [
    "Id",
    "Opentime"
]

ACTIVITY_CSV_ATTR = [
    "Id",
    "Org",
    "Cycle",
    "Travellinginfo",
    "Charge",
    "Remarks"
]

HOTEL_CSV_ATTR = [
    "Id",
    "Fax",
    "Serviceinfo",
    "TotalNumberofRooms",
    "TotalNumberofPeople",
    "LowestPrice",
    "CeilingPrice"
]

# ================================== database table attributes ================================== #
ATTRACTION_TYPE = [
    "Scenic_spot",
    "Restaurant",
    "Hotel",
    "Activity"
]

# ================================== handle csv info ================================== #
TEMP_SUBSET_CSV = [
    "temp/Scenic_spot_temp.csv",
    "temp/Restaurant_temp.csv",
    "temp/Hotel_temp.csv",
    "temp/Activity_temp.csv"
]

TEMP_ATTRACTION_CSV = "temp/Attraction_temp.csv"

# ================================== environment file ================================== #
DOTENV = ".env"
ENVVAR_KEY = ["TPD_HOST", "TPD_PORT", "TPD_USER", "TPD_PASSWORD", "TPD_DB"]
