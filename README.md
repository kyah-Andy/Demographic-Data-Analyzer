# 📊 Demographic Data Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellowgreen)
![NumPy](https://img.shields.io/badge/NumPy-Statistics-blue)

This project analyzes a demographic dataset from the **U.S. Census Bureau** to extract meaningful insights about population statistics, education levels, income, and occupation trends using **Python, Pandas, and NumPy**.

---

## 📌 Project Overview

The goal of this project is to answer real-world demographic questions such as:

- How many people belong to each race group?
- What is the average age of men?
- What percentage of people have a Bachelor's degree?
- What percentage of people with advanced education earn >50K?
- What is the minimum number of working hours per week?
- Which country has the highest percentage of high earners?
- What is the most common occupation in India for high earners?

---

## 📁 Dataset

The dataset contains census data with features such as:

- age
- workclass
- education
- education-num
- marital-status
- occupation
- race
- sex
- hours-per-week
- native-country
- salary

---

## 🛠️ Tools Used

- Python 🐍  
- Pandas 📊  
- NumPy 🔢  

---

## 📂 Project Structure

```text id="demo_struct_001"
Demographic Data Analyzer/  
│
├── demographic_data_analyzer.py  
├── main.py  
├── test_module.py  
├── Data  
    ├── adult.data.csv  
└── README.md
```
---
## 📊 Questions Solved
1️⃣ Race Count
Counts how many people belong to each race.
2️⃣ Average Age of Men
Calculates the average age of male individuals.
3️⃣ Education Level
Finds percentage of people with:
- Bachelor’s degree
- Higher education (Bachelors, Masters, Doctorate)
- Lower education
4️⃣ Income Analysis
Finds percentage of people earning:
- 50K overall
- 50K based on education level
5️⃣ Work Hours Analysis
Finds:
- Minimum working hours per week
- Percentage of people working minimum hours who earn >50K
6️⃣ Country & Occupation Insights
Finds:
- Country with highest percentage of high earners
- Most popular occupation for high earners in India
---
## ▶️ How to Run
1️⃣ Install dependencies
```
pip install pandas numpy
```
2️⃣ Run the program
```
python main.py
```
---
## 🧪 Run Tests
To validate the solution:
```
python -m unittest test_module.py
```
Expected output:
```
OK
```
## 📈 Key Insights
This project demonstrates:
- Real-world data cleaning and filtering
- Grouping and aggregation in Pandas
- Percentage-based statistical analysis
- Insight extraction from census data
---
## 👨‍💻 Author
## **Andy Razon**
🌐 Portfolio: https://andyrazon.website
---
📜 License
This project is part of the freeCodeCamp Data Analysis with Python Certification and is intended for educational purposes.
