# Program to calculate the first 1,000,000 terms of the series: 1 - 1/3 + 1/5 - 1/7 + ...

# Number of terms
num_terms = 1000000

# Calculating the series
result = 0.0
for i in range(num_terms):
    term = (-1) ** i / (2 * i + 1)  # Calculate the term
    result += term  # Add the term to the result

# Multiply the total by 4
total = result * 4

# Print the result
print(total)