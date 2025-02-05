# Function to classify temperature
def classify_temperature(temperature):
    if temperature > 40:
        return "Hot weather"
    elif 30 < temperature <= 40:
        return "Warm weather"
    elif 15 < temperature <= 30:
        return "Moderate temperature"
    elif 0 < temperature <= 15:
        return "Cold weather"
    elif -30 < temperature <= 0:
        return "Very cold weather"
    elif -50 <= temperature <= -30:
        return "Ice cold temperature"
    else:
        return "Temperature out of defined range"

# User input
temperature = float(input("Enter the temperature in °C: "))

# Classify and display the temperature
classification = classify_temperature(temperature)
print(f"The temperature is classified as: {classification}")
