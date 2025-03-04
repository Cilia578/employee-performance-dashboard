import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('employee_performance.csv')

sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))


avg_performance = df.groupby('Department')['Performance_Score'].mean().reset_index()
sns.barplot(x='Department', y='Performance_Score', data=avg_performance, ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Average Performance Score by Department')
axes[0, 0].set_ylabel('Average Performance Score')
axes[0, 0].set_xlabel('Department')


sns.scatterplot(x='Tasks_Completed', y='Performance_Score', data=df, ax=axes[0, 1], hue='Department', palette='viridis')
axes[0, 1].set_title('Tasks Completed vs. Performance Score')
axes[0, 1].set_ylabel('Performance Score')
axes[0, 1].set_xlabel('Tasks Completed')


sns.boxplot(x='Job_Role', y='Hours_Worked', data=df, ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Distribution of Hours Worked by Job Role')
axes[1, 0].set_ylabel('Hours Worked')
axes[1, 0].set_xlabel('Job Role')
axes[1, 0].tick_params(axis='x', rotation=45)

sns.histplot(df['Performance_Score'], bins=20, kde=True, ax=axes[1, 1], color='blue')
axes[1, 1].set_title('Distribution of Performance Scores')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_xlabel('Performance Score')

plt.tight_layout()
plt.savefig('employee_performance_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()