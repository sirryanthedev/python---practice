# (Letter grades - Dodona)

grade = int(input("grade: "))

if (grade < 0 or grade > 100):
    print("invalid input, the input should be a valid number (0-100)") 
elif 90 <= grade <= 100:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")


# Grading in the United States commonly takes on the form of five letter grades (A, B, C, D and F), with A being the highest and F being the lowest. Below is the grading system found to be most commonly used in United States public high schools for the conversion of numeric grades (percentages) to letter grades.

# letter grade	percentage
# A	90%-100%
# B	80%-89%
# C	70%-79%
# D	60%-69%
# F	< 60%

# Input
# A numeric grade (percentage) expressed as a positive integer (0-100)

# Output
# The letter grade corresponding to 
# s

# Example
# Input:
# 87
# Output:
# B