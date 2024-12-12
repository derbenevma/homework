# Задание 3
import pandas as pd
df = pd.read_csv("NISPUF17.csv", sep=',')
dfMale = df[df["SEX"] == 1]
dfFemale = df[df["SEX"] == 2]

maleCpx = dfMale[(dfMale["HAD_CPOX"] == 1) & (dfMale["P_NUMVRC"] > 0)].shape[0]/dfMale[(dfMale["HAD_CPOX"] == 2) & (dfMale["P_NUMVRC"] > 0)].shape[0]
femaleCpx = dfFemale[(dfFemale["HAD_CPOX"] == 1) & (dfFemale["P_NUMVRC"] > 0)].shape[0]/dfFemale[(dfFemale["HAD_CPOX"] == 2) & (dfFemale["P_NUMVRC"] > 0)].shape[0]

print(
    {"male": round(maleCpx, 4),
        "female": round(femaleCpx, 4)}
)
