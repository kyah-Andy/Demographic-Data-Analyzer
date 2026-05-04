import os
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data", "adult.data.csv")

# Column names (dataset has no headers)
columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary"
]

# Load dataset
df = pd.read_csv(file_path, names=columns, skipinitialspace=True)

# Clean text columns (VERY IMPORTANT)
df["education"] = df["education"].str.strip()
df["salary"] = df["salary"].str.strip()

# -------------------------
# 1. Race count
race_count = df["race"].value_counts()

# -------------------------
# 2. Average age of men
average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

# -------------------------
# 3. % with Bachelors degree
percentage_bachelors = round(
    (df["education"] == "Bachelors").mean() * 100,
    1
)

# -------------------------
# 4. Higher education rich
higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
rich = df["salary"] == ">50K"

higher_education_rich = round(
    (df[higher_education & rich].shape[0] / df[higher_education].shape[0]) * 100,
    1
)

# -------------------------
# 5. Lower education rich
lower_education_rich = round(
    (df[~higher_education & rich].shape[0] / df[~higher_education].shape[0]) * 100,
    1
)

# -------------------------
# 6. Minimum hours worked
min_work_hours = df["hours-per-week"].min()

# -------------------------
# 7. % of rich among min workers
min_workers = df[df["hours-per-week"] == min_work_hours]
rich_min_workers = min_workers[min_workers["salary"] == ">50K"]

rich_percentage = round(
    (len(rich_min_workers) / len(min_workers)) * 100,
    1
)

# -------------------------
# 8. Country with highest % earning >50K
country_wealth = (
    df[df["salary"] == ">50K"]["native-country"].value_counts()
    / df["native-country"].value_counts()
) * 100

highest_earning_country = country_wealth.idxmax()
highest_earning_country_percentage = round(country_wealth.max(), 1)

# -------------------------
# 9. Top occupation in India (>50K)
top_IN_occupation = (
    df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    ["occupation"]
    .value_counts()
    .idxmax()
)
