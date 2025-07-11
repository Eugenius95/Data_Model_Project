import numpy as pd
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# import scikitlearn as sns


df = pd.read_csv("/Users/eugenemonama/Machine_learning/student_habits.csv")

#duplicates = df.duplicated()
# print(duplicates) #check duplicate

# missing_counts = df.isnull().sum()
# print(missing_counts) #missing counts

# Develop a StudentAnalyzer class with methods to
# Calculate mean/median study time by mental health tier
# 
min_value_study = df['study_hours_per_day'].min()
print(min_value_study)

median_study = df['study_hours_per_day'].median()
print(median_study)


correlation_sleep_exam = df['sleep_hours'].corr(df['exam_score'])
print(f"Correlation between sleep_hours  and exam_score: {correlation_sleep_exam}")


df['z_score'] = stats.zscore(df['social_media_hours'])
outliers_zscore = df[abs(df['z_score']) > 3]


print("\nOutliers using Z-score method:")
print(outliers_zscore)

# print(df.head(5))j
#Visualisations Histogram,ScatterBox and 

plt.hist(df['study_hours_per_day'], bins=10, edgecolor='black', color='tan') # Add edge color for better visibility
plt.xlabel('Study hours')
plt.ylabel('Exam_Results')
plt.title('Histogram of study_hours_per_day')
plt.show()


plt.scatter(df['sleep_hours'], df['exam_score'], color='brown')
# Add title and labels
plt.title("Simple Scatter Plot")
plt.xlabel("Sleeping Hours")
plt.ylabel("Exam Score")
plt.show()

# df.boxplot(column=['exam_score','diet_quality'])
df[['exam_score', 'diet_quality']].plot(kind='box', title='Box Plots of Multiple Columns')
plt.title("Simple Scatter Plot")
# Display the plot
plt.show()
# print(df.head(5))


x = df[['study_hours_per_day','social_media_hours','age']]
y = df['exam_score']

model = LinearRegression()
model.fit(x, y)

exam = pd.DataFrame([{
    'study_hours_per_day': 2.2,
    'social_media_hours': 6.2,
    'age': 23
}])


predicted_score = model.predict(exam)[0]
print(f"Predicted exam_score: {predicted_score:.2f}")
