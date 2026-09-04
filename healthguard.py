print("==========================================")
print("              HEALTHGUARD")
print("       SMART SCHOOL HEALTH SYSTEM")
print("==========================================")

# -------------------------------
# INPUTS
# -------------------------------

temperature = float(input("Enter classroom temperature (C): "))
water = int(input("How many glasses of water today? "))

print()
print("CLASSROOM NOISE CHECK")
print("Enter noise level from 0 to 100")
noise = int(input("Noise level: "))

# -------------------------------
# TEMPERATURE
# -------------------------------

if temperature < 30:
    temperature_status = "SAFE"
elif temperature < 35:
    temperature_status = "WARNING"
else:
    temperature_status = "HIGH HEAT ALERT"

# -------------------------------
# HYDRATION
# -------------------------------

if water < 4:
    hydration_status = "LOW"
elif water < 7:
    hydration_status = "MODERATE"
else:
    hydration_status = "GOOD"

# -------------------------------
# NOISE
# -------------------------------

if noise < 40:
    noise_status = "QUIET"
elif noise < 70:
    noise_status = "MODERATE"
else:
    noise_status = "HIGH NOISE"

# -------------------------------
# RISK SCORE
# -------------------------------

risk_score = 0

if temperature >= 35:
    risk_score += 2
elif temperature >= 30:
    risk_score += 1

if water < 4:
    risk_score += 2
elif water < 7:
    risk_score += 1

if noise >= 70:
    risk_score += 2
elif noise >= 40:
    risk_score += 1

# -------------------------------
# OVERALL RISK
# -------------------------------

if risk_score == 0:
    overall_status = "LOW RISK"
    recommendation = "Environment looks comfortable."

elif risk_score <= 2:
    overall_status = "MODERATE RISK"
    recommendation = "Drink water and consider reducing classroom noise."

else:
    overall_status = "HIGH RISK"
    recommendation = "Take action: hydrate, take a break and reduce classroom noise."

# -------------------------------
# FINAL DASHBOARD
# -------------------------------

print()
print("╔══════════════════════════════════════╗")
print("║           HEALTHGUARD               ║")
print("║      SCHOOL HEALTH DASHBOARD        ║")
print("╠══════════════════════════════════════╣")
print(f"║ Temperature   : {temperature} C")
print(f"║ Heat status   : {temperature_status}")
print(f"║ Water intake  : {water} glasses")
print(f"║ Hydration     : {hydration_status}")
print(f"║ Noise level   : {noise}/100")
print(f"║ Noise status  : {noise_status}")
print(f"║ Risk score    : {risk_score}")
print(f"║ Overall       : {overall_status}")
print("╠══════════════════════════════════════╣")
print("║ RECOMMENDATION:")
print(f"║ {recommendation}")
print("╚══════════════════════════════════════╝")

print()
print("==========================================")
print("        HEALTHGUARD ANALYSIS DONE")
print("==========================================")



print("\n==========================================")
print("        DATA SCIENCE ANALYSIS")
print("==========================================")

# Sample student/environment data
data = [
    [35, 3, 80, 6],
    [25, 8, 30, 0],
    [32, 4, 70, 5],
    [28, 6, 50, 2],
    [36, 2, 85, 7],
    [24, 9, 25, 0],
    [30, 5, 60, 3],
    [34, 3, 75, 6],
    [26, 7, 40, 1],
    [31, 4, 65, 4]
]

print("\nDATASET")
print("Temperature | Water | Noise | Risk")

for row in data:
    print(row[0], "C       |", row[1], "   |", row[2], "   |", row[3])

# Average calculations
avg_temp = sum(row[0] for row in data) / len(data)
avg_water = sum(row[1] for row in data) / len(data)
avg_noise = sum(row[2] for row in data) / len(data)
avg_risk = sum(row[3] for row in data) / len(data)

print("\n==========================================")
print("              ANALYSIS RESULT")
print("==========================================")

print("Average temperature :", round(avg_temp, 2), "C")
print("Average water intake:", round(avg_water, 2), "glasses")
print("Average noise level :", round(avg_noise, 2), "/100")
print("Average risk score  :", round(avg_risk, 2))

print("\nKEY INSIGHT:")

if avg_noise > 60:
    print("High classroom noise is a major concern.")

if avg_water < 6:
    print("Students need better water reminders.")

if avg_temp > 30:
    print("Classroom heat may affect concentration.")

print("\n==========================================")
print("       DATA SCIENCE ANALYSIS COMPLETE")
print("==========================================")


print("\n==========================================")
print("        FINAL DATA SCIENCE INSIGHTS")
print("==========================================")

# Find highest risk case
highest_risk = max(data, key=lambda x: x[3])

# Find highest noise
highest_noise = max(data, key=lambda x: x[2])

# Find lowest water intake
lowest_water = min(data, key=lambda x: x[1])

print("\nHIGHEST RISK CASE")
print("Temperature :", highest_risk[0], "C")
print("Water       :", highest_risk[1], "glasses")
print("Noise       :", highest_risk[2], "/100")
print("Risk score  :", highest_risk[3])

print("\nHIGHEST NOISE")
print("Noise level :", highest_noise[2], "/100")

print("\nLOWEST WATER INTAKE")
print("Water intake:", lowest_water[1], "glasses")

print("\n==========================================")
print("             FINAL FINDINGS")
print("==========================================")

print("1. Low water intake is linked with higher risk.")
print("2. High classroom temperature increases concern.")
print("3. High classroom noise can affect learning.")
print("4. Combined environmental factors increase risk.")

print("\n==========================================")
print("       HEALTHGUARD PROJECT COMPLETE")
print("==========================================")
