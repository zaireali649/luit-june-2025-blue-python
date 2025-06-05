import random  # Generate a random number
import math  # Do some math with the number
import emoji  # Add emoji reactions (pip install emoji)
import matplotlib.pyplot as plt  # Visualize with matplotlib (pip install matplotlib)
from datetime import datetime  # Display current date and time

# Generate random number
number = random.randint(0, 10)
print(f"\n🎲 Your random number is: {number}")

# Add a math twist
squared = math.pow(number, 2)
print(f"📐 Squared value: {squared}")

# Add emoji reaction
if number > 7:
    reaction = emoji.emojize("🎉 Big number! You're lucky!", language="alias")
elif number < 3:
    reaction = emoji.emojize("😢 Tiny number. Better luck next time.", language="alias")
else:
    reaction = emoji.emojize("😐 It's okay. Middle ground.", language="alias")

print(f"Reaction: {reaction}")

# Show current time
now = datetime.now()
print(f"🕒 Generated at: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Visualize the number
plt.bar(["Your Number"], [number], color='skyblue')
plt.title("Random Number Bar Chart")
plt.ylim(0, 10)
plt.ylabel("Value")
plt.show()
