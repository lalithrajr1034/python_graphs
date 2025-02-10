import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("flights_data.csv")
df_filtered = df[df["Year"].isin([2019, 2020])]

average_distance = df_filtered.groupby("Year")["Distance"].mean()

plt.figure(figsize=(8, 5))
average_distance.plot(kind="bar", color=["blue", "orange"], alpha=0.8)
plt.title("Average Flight Distance (2019 vs 2020)")
plt.xlabel("Year")
plt.ylabel("Average Distance (miles)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

destination_ids = [11778, 11267]
dest_flight_counts = (
    df_filtered[df_filtered["DestinationAirportID"].isin(destination_ids)]
    .groupby(["Year", "DestinationAirportID"])
    .size()
    .unstack()
)

dest_flight_counts.plot(kind="bar", figsize=(8, 5), color=["blue", "orange"])
plt.title("Number of Flights by Destination Airport")
plt.xlabel("Year")
plt.ylabel("Number of Flights")
plt.xticks(rotation=0)
plt.legend(title="Destination Airport ID")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

fig = px.sunburst(
    df_filtered,
    path=["Year", "DestinationAirportID"],
    values="Distance",
    color="Year",
    title="Sunburst Plot of Flights by Year and Destination",
)

fig.show(renderer="browser")
