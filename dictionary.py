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
points = {}

# Add new member
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

# loop member in dictionary
for k, v in scores.items():
    print(v)
