from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Reanalysis of aggregated Master's thesis data
# Individual survey responses are not available.

base = Path(__file__).resolve().parent

# Load research data
df = pd.read_csv(base / "survey_summary.csv")

# Check data consistency
assert (df["total"] > 0).all()
assert (df["count"] >= 0).all()
assert (df["count"] <= df["total"]).all()

# Calculate percentages
df["percentage"] = (
    df["count"] / df["total"] * 100
).round(1)

# Display analytical results
print(df.to_string(index=False))

# Create output folder
output = base / "results"
output.mkdir(exist_ok=True)

df.to_csv(output / "key_metrics.csv", index=False)

# Visualize findings
fig, ax = plt.subplots(figsize=(11, 6))

ax.barh(
    df["indicator"],
    df["percentage"],
    color="steelblue"
)

ax.invert_yaxis()
ax.set_xlim(0, 110)
ax.set_xlabel("Percentage of respondents (%)")
ax.set_title("Waste Management Survey: Kaduna North")

for i, value in enumerate(df["percentage"]):
    ax.text(value + 1, i, f"{value:.1f}%", va="center")

fig.subplots_adjust(left=0.43, right=0.94)
fig.savefig(
    output / "key_indicators.png",
    dpi=160
)

print("Analysis completed successfully.")
