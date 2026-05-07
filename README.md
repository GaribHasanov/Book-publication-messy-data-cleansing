# 📚 Books Data Cleaning Pipeline

## Overview

This project focuses on cleaning and standardizing a messy public books dataset.  
The dataset contains inconsistencies such as:

- Special characters in text fields  
- Multilingual place names  
- Irregular formatting  
- Noisy and unstructured data  

The goal is to transform raw data into a clean, structured, and analysis-ready dataset.

---

## Data Cleaning Pipeline

### Step 1: Data Inspection
- Reviewed all dataset columns
- Identified missing values and inconsistencies
- Detected formatting issues and noisy text

---

### Step 2: Text Cleaning
- Converted text to lowercase
- Removed special characters using regex
- Standardized formatting across columns

---

### Step 3: Standardization (Place of Publication)
- Used external dataset (`world-cities.csv`)
- Matched city names with reference list
- Ensured consistency in place names

---

### Step 4: Translation
- Translated non-English entries into English
- Normalized multilingual data into a single language standard

---

### Step 5: Final Dataset
- Merged cleaned and matched data
- Removed duplicates
- Exported final structured dataset

---

## Tools Used

- Python  
- Pandas  
- Googletrans  
- Regex  

---

## Dataset Files

- `Images-Book.csv` → raw dataset  
- `world-cities.csv` → reference dataset  

---

## Output

The final output is a fully cleaned dataset exported as:

`cleaned_books.xlsx`

---

## Conclusion

This project demonstrates a complete data cleaning workflow including:

- Data preprocessing  
- Text normalization  
- External dataset matching  
- Translation-based cleaning  
- Final structured export  

The result is a clean and analysis-ready dataset suitable for further data science tasks.
