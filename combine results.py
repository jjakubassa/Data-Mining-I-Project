import pandas as pd

# Read in the results from the first experiment
df_p01 = pd.read_csv("Data Mining I Project/final_results_p01.csv")
df_p001 = pd.read_csv("Data Mining I Project/final_results_p001.csv")

df = pd.concat([df_p01, df_p001], ignore_index=True)

# Generate LaTeX code for the table
latex_table = df.to_latex(index=False)

# Define the file path and name
file_path = "Data Mining I Project/estimator_scores.tex"

# Write the LaTeX code to the file
with open(file_path, "w") as f:
    f.write(latex_table)

print(f"LaTeX table saved to {file_path}")
