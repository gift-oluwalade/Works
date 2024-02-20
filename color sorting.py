# Define the colors and their frequencies
colors = {'GREEN': 10, 'YELLOW': 4, 'BROWN': 6, 'BLUE': 16, 'PINK': 6, 'ORANGE': 6, 'CREAM': 2, 'WHITE': 12}

# Calculate the mean color
mean_color = max(colors, key=colors.get)
mean_color_percentage = (colors[mean_color] / sum(colors.values())) * 100
print(f'The mean color of shirt is {mean_color} with a percentage of {mean_color_percentage:.2f}%')

# Calculate the most worn color
most_worn_color = max(colors, key=colors.get)
most_worn_color_percentage = (colors[most_worn_color] / sum(colors.values())) * 100
print(f'The most worn color throughout the week is {most_worn_color} with a percentage of {most_worn_color_percentage:.2f}%')

# Calculate the median color
sorted_colors = sorted(colors.items(), key=lambda x: x[1], reverse=True)
median_color = sorted_colors[len(colors) // 2][0]
median_color_percentage = (colors[median_color] / sum(colors.values())) * 100
print(f'The median color is {median_color} with a percentage of {median_color_percentage:.2f}%')

# Calculate the variance of the colors
mean_color_frequency = colors[mean_color]
variance = sum((color - mean_color_frequency) ** 2 for color in colors.values()) / len(colors)
print(f'The variance of the colors is {variance:.4f}')

# Calculate the probability of a color being red
total_shirts = sum(colors.values())
red_probability = colors['RED'] / total_shirts
print(f'The probability of a color being red is {red_probability:.4f}')

# Save the colors and their frequencies in a postgresql database
import psycopg2

# Connect to the postgresql database
connection = psycopg2.connect(
    database="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor object
cursor = connection.cursor()

# Create the shirt_colors table
cursor.execute("""
CREATE TABLE shirt_colors (
    id SERIAL PRIMARY KEY,
    color VARCHAR(20) NOT NULL,
    frequency INTEGER NOT NULL
)
""")

# Insert the colors and their frequencies into the shirt_colors table
for color, frequency in colors.items():
    cursor.execute("""
    INSERT INTO shirt_colors (color, frequency)
    VALUES (%s, %s)
    """, (color, frequency))

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()