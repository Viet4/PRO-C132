import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("final.csv")

X = []

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius,mass)
plt.title("Radius & Mass of the Stars")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(gravity,mass)
plt.title("Gravity & Mass of the Stars")
plt.xlabel("Gravity")
plt.ylabel("Mass")
plt.show()