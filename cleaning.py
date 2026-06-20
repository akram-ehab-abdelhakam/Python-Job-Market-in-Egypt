import pandas as pd
import sqlite3

df = pd.read_csv(r"D:\Universety\Level 2\S2\Data Mining\project\data minig proj\Data before cleaning.csv")

#========================================================
df = df.drop_duplicates()
df = df.drop(columns=["salary"])
#========================================================
df["location"] = df["location"].str.strip()
df["location"] = df["location"].str.replace(r"Egypt\s*,\s*", "", regex=True).str.strip()
#========================================================


def extract_city(location):

    if pd.isna(location):
        return "Cairo"

    parts = str(location).split(",")
    city = parts[0].strip()

    if city == "Egypt" and len(parts) > 1:
        city = parts[1].strip().replace("Egypt", "").strip()

    if city == "" or city == "Egypt":
        return "Egypt"

    return city
df["location"] = df["location"].apply(extract_city)
df["location"] = df["location"].replace("Al Jizah", "Giza")
df = df[df["location"] != "Egypt"]
#========================================================

df["skills"] = df["skills"].fillna("Not Mentioned").str.strip()
df["job title"] = df["job title"].fillna("Unknown")
df["company name"] = df["company name"].fillna("Unknown")
#======================================================
df["job title"] = df["job title"].str.title().str.strip()
df["company name"] = df["company name"].str.title().str.strip()
df["location"] = df["location"].str.title().str.strip()
df["skills"] = df["skills"].str.title().str.strip()

print ("============================================================================================================================================================")
print("Nulls:\n", df.isnull().sum())
print("Shape:", df.shape)
print ("============================================================================================================================================================")
conn = sqlite3.connect("jobs.db")
df.to_sql("job_offers", conn, if_exists="replace", index=False)
print("Data inserted! Rows:", len(df))

print ("=======================================================================================================================================================")





