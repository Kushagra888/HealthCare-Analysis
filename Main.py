import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('healthcare_data.csv')
data['Age'] = data['Age'].str.extract(r'(\d+)', expand=False).astype(float)

def summarize_data(data):
    print(data[['Age', 'Admission_Deposit']].describe())
    sns.histplot(data['Age'], kde=True, bins=30, color='blue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Patients')
    plt.show()

def admission_trends(data):
    sns.countplot(x='Severity of Illness', hue='Type of Admission', data=data, palette='viridis')
    plt.title('Admissions by Severity')
    plt.xlabel('Severity')
    plt.ylabel('Count')
    plt.legend(title='Admission Type')
    plt.show()

def hospital_heatmap(data):
    perf = data.groupby(['Hospital_region_code', 'Hospital_code'])['Available Extra Rooms in Hospital'].mean().unstack()
    sns.heatmap(perf, annot=True, cmap='coolwarm', fmt='.1f')
    plt.title('Hospital Performance')
    plt.xlabel('Hospital Code')
    plt.ylabel('Region Code')
    plt.show()

print("Healthcare Data Analysis")
summarize_data(data)
admission_trends(data)
hospital_heatmap(data)
