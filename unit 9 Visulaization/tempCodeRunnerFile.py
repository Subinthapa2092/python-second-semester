ion.csv file
df.to_csv("election.csv", index=False)

# Display the data
print(df)

# pie chart
plt.pie(
    df["Votes"],