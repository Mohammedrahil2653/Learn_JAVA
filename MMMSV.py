import pandas as pd

data={
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],    
    'rating': [4.5, 3.8, 4.2, 4.0, 4.7]
}
df = pd.DataFrame(data)
print(df)

mean_age =df['age'].mean()
mean_rating = df['rating'].mean()       
print(f"Mean Age: {mean_age}")
print(f"Mean Rating: {mean_rating}")
median_age = df['age'].median()
median_rating = df['rating'].median()
print(f"Median Age: {median_age}")
print(f"Median Rating: {median_rating}")
mode_age = df['age'].mode()[0]
mode_rating = df['rating'].mode()[0]    
print(f"Mode Age: {mode_age}")
print(f"Mode Rating: {mode_rating}")

variance_age = df['age'].var()
variance_rating = df['rating'].var()
print(f"Variance Age: {variance_age}")
print(f"Variance Rating: {variance_rating}")
std_dev_age = df['age'].std()
std_dev_rating = df['rating'].std()
print(f"Standard Deviation Age: {std_dev_age}")
print(f"Standard Deviation Rating: {std_dev_rating}")