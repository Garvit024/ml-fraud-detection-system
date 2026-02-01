# 🚨 ML-Based Credit Card Fraud Detection System

## 📌 Project Overview
This project builds a **production-grade Machine Learning pipeline** to detect fraudulent credit card transactions using advanced classification models and real-world transaction data. The system is designed to **maximize fraud recall while minimizing false positives**, ensuring high detection accuracy without disrupting genuine customer transactions.

The solution processes **500K+ transaction records**, performs **feature engineering**, trains **multiple ML models**, and deploys a **scalable fraud prediction pipeline** using Python, SQL, and CI/CD workflows.

---

## 🎯 Business Problem
Credit card fraud results in **billions of dollars of financial losses annually** and significantly impacts customer trust.

Key challenges:
- Highly **imbalanced datasets** (<0.2% fraud cases)
- High **false negative cost** (missed fraud → financial loss)
- Need for **real-time detection with high precision & recall**

### Objective:
Build a system that:
- Accurately detects fraudulent transactions
- Reduces false negatives
- Maintains high system scalability and deployment readiness

---

## 🧠 Solution Approach

### 1. Data Understanding & Processing
- Processed **500K+ transaction records**
- Cleaned and standardized transactional features
- Handled missing values and extreme outliers
- Performed **feature scaling & normalization**

### 2. Feature Engineering
- Transaction velocity metrics  
- User behavior profiling  
- Amount deviation tracking  
- Frequency and temporal features  

These features helped capture **fraud patterns beyond raw transaction values**.

### 3. Modeling
Trained and evaluated multiple models:
- Logistic Regression
- Random Forest
- XGBoost (Final Model)

### Final Model:
**XGBoost Classifier**
- Accuracy: **91%**
- High recall to minimize fraud misses
- Robust handling of class imbalance

---

## 🏗️ System Architecture

Raw Data (CSV / SQL)
↓
Data Cleaning & Feature Engineering
↓
Model Training (XGBoost)
↓
Model Serialization (Joblib)
↓
SQL + Python Inference Pipeline
↓
Fraud Prediction Output


---

## ⚙️ Tech Stack

| Category | Tools |
|------------|--------|
| Programming | Python |
| ML Framework | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Database | SQL |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Model Storage | Joblib |

---

## 📊 Results & Impact

| Metric | Value |
|----------|---------|
| Transactions processed | 500K+ |
| Model Accuracy | 91% |
| False Negative Reduction | 18% |
| Fraud Recall | High |
| Pipeline Automation | Enabled |

### Business Impact:
- Reduced fraud loss exposure
- Faster fraud detection
- Scalable deployment-ready architecture

---

## 🚀 How to Run the Project

### Clone Repository
```bash
git clone https://github.com/your-username/Walmart-Sales-Analysis.git
cd Walmart-Sales-Analysis
