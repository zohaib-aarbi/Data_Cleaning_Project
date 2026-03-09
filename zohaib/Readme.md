# Data Cleaning Project – Customer Banking Dataset

## Project Overview

In real-world data analysis, raw datasets are rarely clean. They often contain missing values, duplicate records, inconsistent text formatting, incorrect data types, and extreme outliers.

This project demonstrates a **complete data cleaning pipeline using Python** to transform a messy customer banking dataset into a clean and structured dataset ready for analysis and machine learning.

The entire process was implemented using **Python with the Pandas library**, along with visualization tools for data inspection.

---

# Tools & Technologies

* Python
* Pandas (Data manipulation and cleaning)
* Matplotlib (Data visualization)
* Seaborn (Statistical visualization)

---

# Dataset Description

The dataset contains customer information from a banking system.

Main columns include:

| Column      | Description                         |
| ----------- | ----------------------------------- |
| CustomerID  | Unique identifier for each customer |
| Name        | Customer name                       |
| Age         | Age of the customer                 |
| Gender      | Gender of the customer              |
| City        | City where the customer lives       |
| AccountType | Type of bank account                |
| Balance     | Account balance                     |
| LoanStatus  | Loan status of the customer         |
| Email       | Customer email address              |
| JoinDate    | Date the customer joined the bank   |

The raw dataset contains **missing values, duplicates, inconsistent text formats, and outliers**, which were addressed in this project.

---

# Data Cleaning Workflow

The cleaning pipeline follows a structured process:

1. Data Loading
2. Data Exploration
3. Handling Missing Values
4. Fixing Data Types
5. Removing Duplicate Records
6. Standardizing Text Data
7. Feature Engineering
8. Outlier Detection & Removal
9. Exporting the Clean Dataset

---

# Step-by-Step Explanation of Code

## 1. Import Required Libraries

The project begins by importing essential libraries used for data manipulation and visualization.

* **Pandas** → used for data cleaning and manipulation.
* **Matplotlib** → used for plotting charts.
* **Seaborn** → used for advanced statistical visualizations.

These libraries form the core toolkit for most professional data analysts.

---

## 2. Load Dataset

The dataset is loaded into a Pandas DataFrame.

This allows structured operations such as filtering, aggregation, and cleaning.

The dataset is stored in a variable called `df` which represents the main working DataFrame.

---

## 3. Data Exploration (Optional Analysis)

Several commands are included to explore the dataset before cleaning:

### Dataset Structure

Provides a concise summary including:

* column names
* number of non-null values
* data types

This helps identify missing values and incorrect data types.

### Statistical Summary

Displays key statistics such as:

* mean
* standard deviation
* minimum and maximum values
* percentiles

This is useful for detecting unusual values and potential outliers.

### Duplicate Check

Counts duplicate records in the dataset, especially based on the `CustomerID`.

### Missing Value Inspection

Shows the total missing values in each column.

These exploratory checks help determine the required cleaning steps.

---

# Handling Missing Values

Missing values were handled using different strategies depending on the column type.

### Name Column

Missing customer names were replaced with:

"Unknown"

This ensures that the dataset remains consistent without losing records.

---

### Age Column

Missing ages were filled using the **median age** of the dataset.

Median is preferred because it is less affected by extreme values compared to the mean.

---

### Gender Column

Missing gender entries were replaced with:

"Unknown"

This keeps the dataset consistent while acknowledging missing information.

---

### City Column

Missing city values were filled with:

"Unknown"

---

### Account Type Column

Missing account types were filled with:

"Unavailable"

This indicates the account type information was not recorded.

---

### Balance Column

Missing balances were replaced with:

0

This assumes that if balance data is missing, the account may have no recorded balance.

---

### Loan Status Column

Missing loan status entries were replaced with:

"Missing"

---

### Email Column

Missing email addresses were filled with:

"Not provided"

---

# Data Type Conversion

To ensure accurate analysis, the data types were corrected.

### Join Date Conversion

The `JoinDate` column was converted from text format to a **datetime object**.

This enables:

* date calculations
* time-based analysis
* sorting by date

---

### Numeric Type Conversion

Two columns were converted from floating point to integers:

* Age
* Balance

Since these values represent whole numbers, converting them improves data consistency.

---

# Removing Duplicate Records

Duplicate records were removed based on the **CustomerID** column.

This ensures that each customer appears only once in the dataset.

Removing duplicates prevents incorrect analysis such as double-counting customers.

---

# Text Cleaning and Standardization

Text data often contains inconsistent capitalization and extra spaces.

To standardize the dataset:

### Name Column

* Converted to title case
* Removed extra spaces

Example:

```
"  john smith  " → "John Smith"
```

---

### City Column

Standardized using title case and trimming whitespace.

---

### Account Type Column

Ensures consistent formatting across all account types.

---

### Loan Status Column

Standardized capitalization.

---

### Gender Column Standardization

Gender values often appear in multiple inconsistent formats such as:

```
M
Male
m
F
female
```

These were standardized using the following process:

1. Remove whitespace
2. Convert to lowercase
3. Replace abbreviations
4. Convert to title case

Final standardized values:

```
Male
Female
Unknown
```

---

# Feature Engineering

Two new columns were created to enrich the dataset.

---

### Balance_PKR Column

A formatted column representing account balance with currency.

Example:

```
50000 → "50000 Rs"
```

This makes the balance easier to interpret when displaying the data.

---

### Gender_Code Column

The gender column was encoded into numerical values using categorical encoding.

Example encoding:

| Gender  | Code |
| ------- | ---- |
| Female  | 0    |
| Male    | 1    |
| Unknown | 2    |

This transformation is useful for **machine learning models**, which require numerical inputs.

---

# Outlier Detection and Removal

Outliers were detected in the **Balance column** using the **Interquartile Range (IQR) method**.

### IQR Formula

IQR = Q3 − Q1

Where:

* Q1 = 25th percentile
* Q3 = 75th percentile

Outlier boundaries were calculated as:

Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR

Any balance values outside this range were considered extreme outliers.

These rows were filtered to create a cleaned dataset.

Removing outliers improves the reliability of statistical analysis.

---

# Data Visualization (Optional)

A boxplot was prepared using Seaborn to visually inspect balance distribution and confirm outlier removal.

Boxplots help identify:

* skewed distributions
* extreme values
* central data spread

---

# Final Clean Dataset

After completing all cleaning steps:

* Missing values were handled
* Duplicates were removed
* Data types were corrected
* Text fields were standardized
* New features were created
* Outliers were filtered

The final cleaned dataset was exported to:

```
cleaned_data/cleaned_data.csv
```

This dataset is now ready for:

* data analysis
* visualization
* machine learning models
* business insights

---

# Sample Output

The script prints the first 20 rows of the cleaned dataset to verify the transformations.

---

# Key Skills Demonstrated

This project demonstrates practical skills required in real data analyst roles:

* Data cleaning with Pandas
* Handling missing values
* Duplicate detection
* Data type corrections
* Text standardization
* Feature engineering
* Outlier detection using IQR
* Data export and documentation

---

# Conclusion

Data cleaning is one of the most critical steps in the data analysis pipeline.

This project demonstrates how a messy real-world dataset can be transformed into a reliable dataset suitable for analysis and modeling using Python.

---

# Author

Zohaib Aarbi
Data Analyst Project Portfolio
