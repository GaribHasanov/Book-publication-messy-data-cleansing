# 📚 Public Books Dataset – Data Cleaning Pipeline

## Overview

This project focuses on **data cleaning and standardization** of a messy public books dataset.  
The dataset originally contains inconsistent formatting, multilingual entries, and noisy textual data.

The main goal is to transform raw data into a **clean, structured, and analysis-ready dataset**.

---

## Problem Statement

The dataset includes:

- Inconsistent place names (cities/countries)
- Special characters and noise symbols
- Multilingual entries
- Unstandardized formatting across columns

---

## Solution Approach (Data Cleaning Pipeline)

### 1. Data Profiling
A full inspection of all dataset columns was performed to identify:

- Null or empty values  
- Irregular text formats  
- Encoding issues  
- Non-standard place names  

---

### 2. Cleaning "Place of Publication"

Key transformations:

- Lowercasing all text values  
- Removing special characters using regex  
- Standardizing city names using external reference dataset  
- Translating non-English entries into English  

---

### 3. Reference Dataset Integration

A standardized city reference dataset (`world-cities.csv`) was used to:

- Validate existing values  
- Match correct city names  
- Identify unmatched or noisy records  

---

### 4. Data Matching Strategy

- Exact matches → directly accepted  
- Non-matches → translated into English  
- Re-attempted matching after translation  
- Remaining unmatched rows flagged for further processing  

---

### 5. Final Output

The final dataset contains:

- Clean and standardized place names  
- Consistent formatting across all fields  
- Duplicate-free structured data  
- Exported as Excel file for analysis  

---

## 📁 Project Structure
