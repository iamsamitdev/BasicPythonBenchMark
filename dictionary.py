# Create new dictionary
scores = {
    'John': 2200,
    'Marry': 1240,
    'Alisa': 3200,
    'Bobby': 980
}

# Read some member in dictionary
print(scores)
print(scores['Bobby'])

# Add new member
scores['Susan'] = 2500
print(scores)

# Create empty dictionary
points = {'mr_a': 10.2, 'mr_b': 15.4, 'mr_c': 22.8}

print(points)

# loop member in dictionary
for v in scores.values():
    print(v)
