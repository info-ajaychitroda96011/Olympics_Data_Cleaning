# 🏅 Olympics Data Cleaning & Analysis Project

## 📊 Project Overview
This project focuses on cleaning, transforming, and analyzing historical Olympics data to generate meaningful insights related to medal distribution, country-wise performance, and athlete participation. The primary objective is to prepare raw, inconsistent data into a clean and analysis-ready format and present insights through an interactive dashboard.

The project demonstrates strong skills in **data cleaning, preprocessing, exploratory data analysis (EDA), and dashboard-driven insights**, making it suitable for real-world data analyst and data scientist roles.

---

## 📸 Dashboard Preview
![Olympics Analysis Dashboard](Screenshot-2025-12-15-122500.png)

---

## 🧹 Data Cleaning Objectives
The raw Olympics dataset contained multiple data quality issues. The following cleaning steps were performed:

- Handled missing and null values in athlete, medal, and country columns  
- Standardized country/region names for consistency  
- Removed duplicate records  
- Converted data types for year, medals, and numeric fields  
- Created derived columns such as **total medals (Gold + Silver + Bronze)**  
- Filtered and validated records for accurate analysis  

---

## 📈 Analysis Performed
The cleaned dataset was used to perform multiple analytical tasks:

- **Overall Medal Tally** across all Olympic years  
- **Country-wise Medal Analysis** (Gold, Silver, Bronze, Total)  
- **Year-wise Trends** in medal counts  
- **Athlete-wise Performance Analysis**  
- **Top Performing Countries** based on total medals  

---

## 🖥️ Features
The interactive website provides the following functionalities:

- **Medal Tally View** with Gold, Silver, Bronze, and Total counts  
- Dynamic filters for **Year** and **Country**  
- Country-wise ranking based on medal performance  
- Clean tabular visualization for easy comparison  
- Multiple analysis modes:
  - Overall Analysis  
  - Country-wise Analysis  
  - Athlete-wise Analysis  

---

## 🧰 Tools & Technologies Used
- **Python** – Data cleaning and preprocessing  
- **Pandas & NumPy** – Data manipulation and transformation  
- **Streamlit** – Interactive dashboard development  
- **Matplotlib / Seaborn** – Data visualization  
- **Jupyter Notebook** – Exploratory Data Analysis  
- **CSV Dataset** – Raw Olympics data  

---

## 📂 Dataset Information
- **Source:** Historical Olympics Dataset (Public Dataset)  
- **Format:** CSV  
- **Records:** 100,000+  
- **Time Period:** Multiple Olympic years  

---


## ▶️ How to Run the Project 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/info-ajaychitroda96011/Olympics_Data_Cleaning.git

2. **Changed Directory(Go to project disrectory):**
   ```bash
   cd olympics-analysis

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
---




