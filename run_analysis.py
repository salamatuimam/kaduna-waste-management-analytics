

# Reanalysis of aggregated Master's thesis results.
# This is not the original survey analysis.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

N = 400

# Counts from the Master's thesis tables
counts = [
    ("High or very high population density", 188 + 136, "Table 4.2"),
    ("Daily household waste generation", 276, "Table 4.3"),
    ("Population growth linked to more waste", 324, "Table 4.4"),
    ("Waste collection rated ineffective", 180 + 128, "Table 4.5"),
    ("Waste infrastructure rated inadequate", 192 + 88, "Table 4.6"),
    ("Collection occasional or never", 160 + 36, "Table 4.7"),
]

rows = []
for name, count, source in counts:
    assert 0 <= count <= N
    rows.append((name, round(count / N * 100, 1), source))

# Percentages reported in thesis figures
rows.extend([
    ("Unaware of waste management policies", 76.0, "Figure 4.2"),
    ("Willing to join waste programs", 77.0, "Figure 4.3"),
])

results = pd.DataFrame(
    rows, columns=["indicator", "percent", "source"]
)

print(results.to_string(index=False))

output = Path("results")
output.mkdir(exist_ok=True)
results.to_csv(output / "key_metrics.csv", index=False)

fig, ax = plt.subplots(figsize=(11, 6))

ax.barh(
    results["indicator"],
    results["percent"],
    color="steelblue"
)

ax.invert_yaxis()
ax.set_xlim(0, 110)
ax.set_xlabel("Share of respondents (%)")
ax.set_title("Kaduna North: Survey Indicators (N=400)")

for i, value in enumerate(results["percent"]):
    ax.text(value + 1, i, f"{value:.0f}%", va="center")

fig.subplots_adjust(
    left=0.41, right=0.94, top=0.90, bottom=0.12
)

fig.savefig(output / "key_indicators.png", dpi=160)

print("Analysis complete. Results saved.")
