import pandas as pd
import sqlite3

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 30)

conn = sqlite3.connect("jobs.db")
print ("=============================================================================================================================================================")


print ("Show the first 10 rows: ")
q1 = pd.read_sql_query("SELECT * FROM job_offers LIMIT 10", conn)
print(q1.to_string())
print ("============================================================================================================================================================")


print ("Show the first 10 rows of job offers in Cairo: ")
q2 = pd.read_sql_query("""
    SELECT * FROM job_offers 
    WHERE location = 'Cairo'
    LIMIT 10
""", conn)
print(q2.to_string())
print ("============================================================================================================================================================")


print ("Show the first 10 rows of job offers with known company names: ")
q3 = pd.read_sql_query("""
    SELECT * FROM job_offers 
    WHERE [company name] != 'Unknown'
    LIMIT 10
""", conn)
print(q3.to_string())
print ("=============================================================================================================================================================")


print("Number of job offers per city: ")
q4 = pd.read_sql_query("""
    SELECT location, COUNT(*) as total
    FROM job_offers
    GROUP BY location
    ORDER BY total DESC
""", conn)
print(q4.to_string())
print("============================================================================================================================================================")


print("Top 10 companies with most job offers: ")
q5 = pd.read_sql_query("""
    SELECT [company name], COUNT(*) as total
    FROM job_offers
    GROUP BY [company name]
    ORDER BY total DESC
    LIMIT 10
""", conn)
print(q5.to_string())
print("============================================================================================================================================================")

print("Top 10 most common job titles: ")
q6 = pd.read_sql_query("""
    SELECT [job title], COUNT(*) as total
    FROM job_offers
    GROUP BY [job title]
    ORDER BY total DESC
    LIMIT 10
""", conn)
print(q6.to_string())
print("============================================================================================================================================================")


print("Cities with more than 10 job offers: ")
q7 = pd.read_sql_query("""
    SELECT location, COUNT(*) as total
    FROM job_offers
    GROUP BY location
    HAVING total > 10
    ORDER BY total DESC
""", conn)
print(q7.to_string())
print("============================================================================================================================================================")


print("Top 10 most common skills excluding Not Mentioned: ")
q8 = pd.read_sql_query("""
    SELECT skills, COUNT(*) as total
    FROM job_offers
    WHERE skills != 'Not Mentioned'
    GROUP BY skills
    ORDER BY total DESC
    LIMIT 10
""", conn)
print(q8.to_string())
print("============================================================================================================================================================")


print("Number of job offers per company in Cairo: ")
q9 = pd.read_sql_query("""
    SELECT [company name], COUNT(*) as total
    FROM job_offers
    WHERE location = 'Cairo'
    AND [company name] != 'Unknown'
    GROUP BY [company name]
    ORDER BY total DESC
    LIMIT 10
""", conn)
print(q9.to_string())
print("============================================================================================================================================================")


print("Companies with jobs in more than one city: ")
q10 = pd.read_sql_query("""
    SELECT [company name], COUNT(DISTINCT location) as cities, COUNT(*) as total_jobs
    FROM job_offers
    WHERE [company name] != 'Unknown'
    GROUP BY [company name]
    HAVING cities > 1
    ORDER BY total_jobs DESC
""", conn)
print(q10.to_string())
print("============================================================================================================================================================")