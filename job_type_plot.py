import pandas as pd
import matplotlib.pyplot as plt

def count_occurrences(csv_file, column_name, target_string):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Count the occurrences of the target string in the specified column
    occurrences = df[column_name].str.count(target_string).sum()
    
    return occurrences

csv_file = "postings.csv"  # Replace "your_file.csv" with the path to your CSV file
column_name = "job_type"   # Replace "ColumnName" with the name of the column you want to search
target_string = "Remote"     # Specify the target string you want to count

# Count the occurrences of the target string in the specified column

high = ["Senior", "Sr", "Principle", "Staff", "Lead"]
entry = ["Associate", "Junior"]

target_strings = ["Remote", "Hybrid", "Onsite"]
target_counts = []
target_percents = []
for type in target_strings:
    target_counts.append(count_occurrences(csv_file, column_name, type))

total = sum(target_counts)

for count in target_counts:
    target_percents.append(f"{round(count / total * 100, 1)}%")

print(f"{target_counts[0]} remote jobs ({target_percents[0]}), {target_counts[1]} hybrid jobs ({target_percents[1]}), and {target_counts[2]} onsite jobs ({target_percents[2]}).")
x_label = [f"{target_counts[0]} Remote ({target_percents[0]})", f"{target_counts[1]} Hybrid ({target_percents[1]})", f"{target_counts[2]} Onsite ({target_percents[2]})"]

# Optional: Plot a bar chart to visualize the result
plt.bar(x_label, target_counts)
plt.ylabel('Count')
plt.title('Job Types of "Data Engineer" roles on LinkedIn')
plt.show()
