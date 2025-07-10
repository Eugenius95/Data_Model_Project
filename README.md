# Data_Model_Project
A dive into the data model and some visualisation(Linear regression)

# 📊 Student Habits & Exam Score Prediction

This project explores how daily student habits such as study hours, sleep patterns, and social media usage impact exam performance. Using a cleaned dataset and linear regression, the model predicts exam scores based on these behavioural factors.

---

## 🚀 Project Objectives

- Clean and explore the dataset
- Identify key correlations (e.g., sleep vs. performance)
- Detect and handle outliers
- Visualise data for better insight
- Build and evaluate a linear regression model
- Predict exam scores based on student habits

---

## 🧠 Technologies Used

- **Python**
- **Pandas** for data manipulation
- **Matplotlib** for visualizations
- **SciPy** for statistical analysis
- **Scikit-learn** for machine learning (Linear Regression)

---

## 📁 Dataset

- File: `student_habits.csv`
- Source: [IBM Sample Data]  
- Features include:
  - `study_hours_per_day`
  - `sleep_hours`
  - `social_media_hours`
  - `diet_quality`
  - `exam_score`
  - `age`
  - `mental_health_tier`

---

## 📊 Visualizations

- Histogram: Study Hours Distribution
- Scatter Plot: Sleep Hours vs. Exam Score
- Box Plot: Exam Score & Diet Quality
- Z-Score Method: Outlier Detection in Social Media Use

---

## 🔍 Key Insights

- There is a positive correlation between sleep and exam performance.
- Outliers in social media use were detected using Z-scores.
- Linear regression provides a baseline model for predicting performance based on habits.

---

## 🤖 Model Prediction Example

```python
model.predict([{
  'study_hours_per_day': 2.2,
  'social_media_hours': 6.2,
  'age': 23
}])

