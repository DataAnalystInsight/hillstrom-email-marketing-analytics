from pathlib import Path
import pandas as pd
import requests
import certifi
from io import BytesIO

#1. Project
BASE_DIR = Path(__file__).resolve().parent

#2. Create folder
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "reports"
]

for folder in folders:
    (BASE_DIR / folder).mkdir(parents= True, exist_ok = True)

print("Project folders created")

#3. URL Hillstrom
url = (
    "https://raw.githubusercontent.com/W-Tran/uplift-modelling/"
    "master/data/hillstrom/"
    "Kevin_Hillstrom_MineThatData_E-MailAnalytics_"
    "DataMiningChallenge_2008.03.20.csv"
)

#4. Download data
response = requests.get(
    url,
    timeout=60,
    verify=certifi.where()
)

response.raise_for_status()

df = pd.read_csv(BytesIO(response.content)) 

#5. Save file 
output_path = BASE_DIR / "data/raw/hillstrom.csv"
df.to_csv(output_path, index = False)

#6. Check
print("\n Download complered!")
print("File:", output_path)
print("Dataset shape:", df.shape)
print("\nColumns :", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

