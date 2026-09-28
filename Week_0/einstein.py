# Get mass from the user and convert it to an integer
mass = int(input("m: "))

# Speed of light
c = 300000000

# Calculate E = mc²
energy = mass * c ** 2

# Display the result
print(f"E: {energy}")