import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("data.csv")
plt.rcParams.update({"font.size": 30})
ax = sales.plot.bar(x="quarter", y="sales", legend=False,
                    color="#1C758A", figsize=(12, 4.5), rot=0)
ax.set_xlabel("Quarter")
ax.set_ylabel("TPY Thousands")
plt.tight_layout()
plt.savefig("chart.png", dpi=120, bbox_inches="tight",
            bbox_extra_artists=[ax.yaxis.label])
print("Mean sales:", sales["sales"].mean())
