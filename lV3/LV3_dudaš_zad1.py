import pandas as pd

df = pd.read_csv('mtcars.csv')

maxPotrosnja = df.sort_values(by ='mpg',ascending=True).head(5)
print("5 automobila s najvecom potrosnjom:\n", maxPotrosnja[['car', 'mpg']])

minPotrosnja8 = df[df.cyl == 8].sort_values(by = 'mpg', ascending=False).head(3)
print("\n8 cilindarski s najmanjom potrosnjom:\n", minPotrosnja8[['car', 'mpg']])

mean6 = df[df.cyl == 6]['mpg'].mean()
print(f"\n6 cilindarski srednja vrijednost: {mean6:f} mpg")

mean4wt = df[(df.cyl == 4) & (df.wt >= 2.0) & (df.wt <= 2.2)]['mpg'].mean()
print(f"\n4 cilindarski 2-2.2 u tisucama lbs srednja vrijednost: {mean4wt:f} mpg")

mCount = df.am.value_counts()
print(f"\nAutomatski (0): {mCount[0]}")
print(f"Rucni (1): {mCount[1]}")

am100hp = df[(df.am == 0) & (df.hp > 100)].shape[0]
print(f"\nAutomatski s preko 100hp : {am100hp}")

df['kg'] = df.wt * 453.592
print("\nMasa automobila u kg:\n", df[['car', 'kg']])
