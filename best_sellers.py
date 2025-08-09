import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/edersonmarcellus/Downloads/bestsellers.csv')

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())


df.dropna(inplace=True)  # Remove rows with missing values
print(df.isnull().sum())  # Check for any remaining missing values

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating":"Rating"}, inplace=True)  # Rename columns

df['Price'] = df['Price'].astype(float)  # Convert Price to float
df['Reviews'] = df['Reviews'].astype(int)  # Convert Reviews to int

author_counts = df['Author'].value_counts()  # Count occurrences of each author
print(author_counts)

average_rating = df['Rating'].mean()  # Calculate average rating
print(f"Average Rating: {average_rating:.2f}")

# Find the top 5 best-selling books
top_books = df.nlargest(5, 'Reviews')
print("Top 5 Best-Selling Books:")
print(top_books[['Title', 'Author', 'Reviews']])