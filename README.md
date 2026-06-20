# 🧠 Python Job Market in Egypt – End-to-End Data Mining Project

[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?logo=kaggle)](https://www.kaggle.com/datasets/akramehab/tanqeeb-egypt-jobs-dataset-web-scraping-csv)

> **An end-to-end data pipeline**: Scraping → Cleaning → Database → Analysis → Visualization → Machine Learning.  
> This project analyzes the **Python job market in Egypt** using data scraped from Wuzzuf and Tanqeeb.

---

## 📌 Overview
The Egyptian tech job market is booming, but data on it is scattered. This project solves that by building a complete data mining pipeline:

1. **Web Scraping**: Extracted live job postings from `Wuzzuf` and `Tanqeeb`.
2. **Data Cleaning**: Standardized cities, handled missing values, removed duplicates, and dropped irrelevant columns.
3. **Database Storage**: Stored the cleaned data in an SQLite database (`jobs.db`) for efficient querying.
4. **Analytics (SQL)**: Ran complex queries to uncover trends like top job titles, top hiring companies, and skill demands.
5. **Visualization**: Built insightful charts (bar charts, pie charts, heatmaps) using Matplotlib & Seaborn.

The dataset gained traction on **Kaggle with 22 upvotes** and inspired 2–3 community members to build their own analysis notebooks on top of it!

---

## 📊 Key Insights at a Glance
- **Most In-Demand Role**: `Senior Data Engineer` (16 listings).
- **Top Hiring Company**: `Joveo Ai` (32 job postings).
- **Job Location**: **Cairo** dominates with **81.1%** of all listings.
- **Top Job Category**: **AI / ML** (104 listings), followed by Development and Software Eng.
- **Employment Type**: **Full-Time** positions make up the vast majority (325 jobs).

---

## 📂 Project Structure
```bash
Python-Job-Market-in-Egypt/
│
├── data/                          # Sample datasets (Full data available on Kaggle)
│   ├── sample_before_cleaning.csv
│   └── sample_after_cleaning.xls
│
├── notebooks/                     # Jupyter Notebooks
│   └── v.ipynb                    # Main visualization & analysis notebook
│
├── scripts/                       # Python scripts
│   ├── tanqeeb.py                 # Scraper for Tanqeeb.com
│   ├── wuzuff.py                  # Scraper for Wuzzuf.net
│   ├── cleaning.py                # Data preprocessing and SQLite insertion
│   └── Queries.py                 # SQL query executions for insights
│
├── outputs/                       # Generated visualizations
│   ├── plot1_top_job_titles.png
│   ├── plot2_top_companies.png
│   ├── plot3_location_pie.png
│   ├── plot4_job_categories.png
│   ├── plot5_employment_type.png
│   └── plot6_heatmap.png
│
├── community_notebooks/           # Notebooks from the Kaggle community
│   └── (coming soon)
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
