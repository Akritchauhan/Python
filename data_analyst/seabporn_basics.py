import seaborn as sms
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
penguins=sms.load_dataset("penguins")
print(penguins.head())

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())

sms.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
sms.set_style("whitegrid")
sms.set_context("notebook")
sms.set_palette("Set2")
plt.show()


sms.scatterplot(data=penguins, x="species", y="body_mass_g", hue="island", style="sex",alpha=0.7)
plt.show()

sms.stripplot(data=penguins, x="species", y="body_mass_g",hue="island",dodge=True, jitter=True)
plt.show()

sms.swarmplot(data=penguins, x="species", y="body_mass_g",hue="island",dodge=True)
sms.set_context("notebook")
sms.set_style("whitegrid")
plt.show()


sms.histplot(data=penguins, x="body_mass_g", hue="species", kde=True)
plt.show()

sms.regressionplot(data=penguins, x="flipper_length_mm", y="body_mass_g",scatter_kws={"color":"blue"}, line_kws={"color":"red"})
plt.show()

sms.lineplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", marker="o")
plt.show()

#joint plot
sms.jointplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", kind="scatter")
plt.show()

#bar plot
sms.barplot(data=penguins, x="species", y="body_mass_g", hue="island", ci=None)
plt.show()

#count plot
sms.countplot(data=penguins, x="species", hue="island")
plt.show()

#box plot
sms.boxplot(data=penguins, x="species", y="body_mass_g", hue="island")
plt.show()

# violin plot
sms.violinplot(data=penguins, x="species", y="body_mass_g", hue="island", split=True)
plt.show()

sms.violinplot(data=penguins, x="species", y="body_mass_g", hue="island", split=True, inner="quartile")
sms.swarnplot(data=penguins, x="species", y="body_mass_g", hue="island", split=True, color="k", alpha=0.7)
plt.show()


# KDE plot
sms.kdeplot(data=penguins, x="body_mass_g", hue="species", fill=True)
plt.show()

# heatmap
columns=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
sms.heatmap(data=penguins[columns].corr(), annot=True, cmap="coolwarm")
plt.show()

# Rug plot
sms.rugplot(data=penguins, x="body_mass_g", hue="species")
plt.show()

#pair plot
sms.pairplot(data=penguins, hue="species", diag_kind="kde")
plt.show()

#pair grid
g=sms.PairGrid(data=penguins, hue="species")
g.map_upper(sms.scatterplot)
g.map_lower(sms.kdeplot, fill=True)
g.map_diag(sms.histplot, kde=True)
g.add_legend()
plt.show()