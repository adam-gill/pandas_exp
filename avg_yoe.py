import pandas as pd
import re

# Read the CSV file
df = pd.read_csv('postings.csv')

yoe_list = []

# extract highest years of experience from a job posting (remove instances over 15 - considered outliers)
def get_yoe(text: str) -> int:
    if not isinstance(text, str):
        return None

    pattern = r"(\d+(?:-\d+)?\+?)\s*(years?)"
    matches = re.findall(pattern, text)
    nums = []

    for i in range(len(matches)):
        exp = re.findall(r"\d+", matches[i][0])
        for n in range(len(exp)):
            if int(exp[n]) > 15:
                exp.pop(n)

        if len(exp) != 0:
            num = int(exp[-1])
            nums.append(num)

    if len(nums) == 0:
        return None
    else:
        return max(nums)

# Loop through every 9th column of every row
for index, row in df.iterrows():
    for i, column_value in enumerate(row):
        if i % 9 == 0:  # Select every 9th column
            yoe = get_yoe(column_value)
            if yoe:
                yoe_list.append(yoe)

# print(yoe_list)

# This average is not 100% accurate, but I'm confident it is a very good representation of the data
# Years greater than 15 were filtered out (considered outliers)
# This taught me a lot about data engineering already, and how hard it is to parse through large amounts of data and filter out 
# unnecessary data!

avg = sum(yoe_list) / len(yoe_list)
print(f"The average number of required years of experience for a linkedin Data Engineer posting is {round(avg, 2)} years.")
