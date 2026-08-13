### create a file election.csv for the folliwng data 

import pandas as pd
import matplotlib.pyplot as plt

# Election data
data = {
    "Party": ["UML", "CPN", "RPP", "NC", "RSP", "Others", "SSP"],
    "Votes": [145000, 200000, 150000, 1700000, 510000, 350000, 300000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create election.csv file
df.to_csv("election.csv", index=False)

# Display the data
print(df)

# pie chart
plt.pie(
    df["Votes"],
    labels=df["Party"],
    autopct="%1.1f%%",
    startangle=90
)

# plt.title("Election Results")
# plt.axis("equal")
plt.show()
