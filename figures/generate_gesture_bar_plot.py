import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

################################# CHANGE NUMBERS HERE #################################
# Then run the file to generate the new plot. It will update the figure in the readme, as the generated figure will replace the old one.
# Dataset: Gesture names and number of videos
data = {
    "OKAY": 81,
    "YOU": 78,
    "ME": 83,
    "LEVEL": 76,
    "LEFT": 85,
    "RIGHT": 79,
    "ASCEND": 82,
    "DESCEND": 75,
    "BUDDY UP": 80,
    "FOLLOW ME": 77,
    "STOP": 84
}

synchronized_additional = 20  # each class has 20 synchronized samples

######################################################################################3#

df = pd.DataFrame(list(data.items()), columns=["Gesture", "Original Videos"])
df["Synchronized Videos"] = synchronized_additional
df["Total"] = df["Original Videos"] + df["Synchronized Videos"]

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
date_string = f"{month}-{day}-{year}"

# Plotting
plt.figure(figsize=(12, 6))
bar1 = plt.bar(df["Gesture"], df["Original Videos"], label='Original Videos')
bar2 = plt.bar(df["Gesture"], df["Synchronized Videos"], bottom=df["Original Videos"], color='skyblue', label='Synchronized Videos')

plt.title(f"Number of Videos per Gesture Class ({date_string})", fontsize=14)
plt.xlabel("Gesture", fontsize=12)
plt.ylabel("Number of Videos", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.yticks()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Highlight max and min values in the original videos
max_idx = df["Original Videos"].idxmax()
min_idx = df["Original Videos"].idxmin()
bar1[max_idx].set_color('green')
bar1[min_idx].set_color('red')

plt.tight_layout()
plt.savefig("figures/gesture_bar_plot.png")
