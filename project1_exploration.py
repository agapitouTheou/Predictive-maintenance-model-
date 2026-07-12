# PROJECT 1: EQUIPMENT FAILURE PREDICTION
# Week 1-2: Python Foundations

# ========== PART 1: BASIC PYTHON CONCEPTS ==========

# 1. Variables and Data Types
print("=== VARIABLES AND DATA TYPES ===")

equipment_name = "Diesel Pump 034"
operating_hours = 1523
temperature_celsius = 87.5
is_failed = False

print(f"Equipment: {equipment_name}")
print(f"Hours: {operating_hours}")
print(f"Temp: {temperature_celsius}°C")
print(f"Failed: {is_failed}")

# 2. Lists (multiple sensor readings)
print("\n=== LISTS (Sensor Data) ===")

sensor_readings = [85.2, 86.1, 87.3, 88.5, 89.2]
print(f"Temperature readings: {sensor_readings}")
print(f"First reading: {sensor_readings[0]}")
print(f"Last reading: {sensor_readings[-1]}")
print(f"Average: {sum(sensor_readings) / len(sensor_readings):.2f}°C")

# 3. Dictionaries (equipment info)
print("\n=== DICTIONARIES (Equipment Info) ===")

equipment = {
    'name': 'Diesel Pump 034',
    'model': 'CAT C15',
    'hours': 1523,
    'temperature': 87.5,
    'pressure': 2100,
    'vibration': 3.2,
    'status': 'Normal'
}

print(f"Equipment name: {equipment['name']}")
print(f"Status: {equipment['status']}")
print(f"Temperature: {equipment['temperature']}°C")

# 4. Functions (reusable code)
print("\n=== FUNCTIONS ===")

def check_equipment_health(temp, pressure, vibration):
    """
    Simple function to assess equipment health
    Returns: 'Healthy', 'Warning', or 'Critical'
    """
    if temp > 95 or pressure > 2300 or vibration > 4.0:
        return 'Critical'
    elif temp > 90 or pressure > 2200 or vibration > 3.5:
        return 'Warning'
    else:
        return 'Healthy'

# Test the function
status = check_equipment_health(87.5, 2100, 3.2)
print(f"Equipment status: {status}")

# 5. Loops (process multiple readings)
print("\n=== LOOPS ===")

equipment_list = [
    {'name': 'Engine 001', 'temp': 85.2},
    {'name': 'Engine 002', 'temp': 92.1},
    {'name': 'Engine 003', 'temp': 88.5}
]

print("Checking all equipment:")
for equipment in equipment_list:
    print(f"  {equipment['name']}: {equipment['temp']}°C")

# ========== PART 2: UNDERSTANDING YOUR DATA ==========
print("\n=== WHAT THIS MEANS FOR PREDICTIVE MAINTENANCE ===")
print("""
In real predictive maintenance:
- Temperature (like above) = bearing wear indicator
- Pressure (like above) = seal degradation
- Vibration (like above) = imbalance developing

21 years of mechanic experience lets INTERPRET these patterns.
The model learns from data.
""")