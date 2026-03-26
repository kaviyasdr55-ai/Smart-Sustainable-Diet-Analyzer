import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌱 Sustainable Diet Analyzer")

# -------------------------------
# MODULE 1 : USER PROFILE
# -------------------------------

st.header("1. User Profile")

name = st.text_input("Enter Name")
age = st.number_input("Age", 10, 100)
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")

diet_type = st.selectbox(
    "Diet Type",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

goal = st.selectbox(
    "Goal",
    ["Weight Loss", "Maintenance", "Weight Gain"]
)

# -------------------------------
# MODULE 2 : DAILY FOOD ENTRY
# -------------------------------
st.header("Daily Food Intake Entry")

breakfast = st.text_input("Enter Breakfast Items")
lunch = st.text_input("Enter Lunch Items")
dinner = st.text_input("Enter Dinner Items")
snacks = st.text_input("Enter Snacks")

# Create meals list
meals = [breakfast, lunch, dinner, snacks]

# Create daily food list
daily_food_list = []

if breakfast:
    daily_food_list.append(("Breakfast", breakfast))

if lunch:
    daily_food_list.append(("Lunch", lunch))

if dinner:
    daily_food_list.append(("Dinner", dinner))

if snacks:
    daily_food_list.append(("Snacks", snacks))


st.subheader("Daily Intake List")

if daily_food_list:
    for meal, food in daily_food_list:
        st.write(meal, ":", food)
else:
    st.write("No food items added yet")

# -------------------------------
# LOAD DATASET
# -------------------------------

df = pd.read_csv("food_dataset.csv")

# -------------------------------
# MODULE 3 : NUTRITION ANALYSIS
# -------------------------------

st.header("3. Nutritional Analysis")

# Simple predefined dataset
food_data = {
    "apple": {"calories": 52, "protein": 0.3, "carbs": 14, "fats": 0.2},
    "rice": {"calories": 130, "protein": 2.7, "carbs": 28, "fats": 0.3},
    "egg": {"calories": 155, "protein": 13, "carbs": 1.1, "fats": 11},
    "bread": {"calories": 265, "protein": 9, "carbs": 49, "fats": 3.2},
    "milk": {"calories": 42, "protein": 3.4, "carbs": 5, "fats": 1}
}

total_calories = 0
total_protein = 0
total_carbs = 0
total_fats = 0

# Calculate nutrients
for food in meals:
    food = food.lower()

    if food in food_data:
        total_calories += food_data[food]["calories"]
        total_protein += food_data[food]["protein"]
        total_carbs += food_data[food]["carbs"]
        total_fats += food_data[food]["fats"]

# Show summary
st.subheader("Total Intake Summary")

st.write("Total Calories:", total_calories)
st.write("Total Protein:", total_protein, "g")
st.write("Total Carbohydrates:", total_carbs, "g")
st.write("Total Fats:", total_fats, "g")
# -------------------------------
# MODULE 4 : SUSTAINABILITY SCORE
# -------------------------------

st.header("4. Sustainability Score")

# Food sustainability categories
food_type = {
    "apple": "plant",
    "rice": "plant",
    "chapati": "plant",
    "vegetables": "plant",
    "egg": "meat",
    "chicken": "meat",
    "bread": "processed",
    "burger": "processed",
    "pizza": "processed"
}

score = 0

# 2️⃣ Simple scoring logic
for food in meals:
    food = food.lower()

    if food in food_type:
        if food_type[food] == "plant":
            score += 10
        elif food_type[food] == "animal":
            score += 5
        elif food_type[food] == "processed":
            score += 3

# 3️⃣ Display sustainability score
st.write("Sustainability Score:", score)

# Overall sustainability rating
if score >= 30:
    rating = "High Sustainability"
elif score >= 15:
    rating = "Moderate Sustainability"
else:
    rating = "Low Sustainability"

st.write("Sustainability Rating:", rating)
# -------------------------------
# MODULE 5 : DIET QUALITY
# -------------------------------
st.header("5. Diet Quality Evaluation")

# Simple evaluation logic based on nutrition balance
if total_calories >= 400 and total_protein >= 15 and total_fats <= 20:
    diet_quality = "Healthy"

elif total_calories >= 250 and total_protein >= 8:
    diet_quality = "Moderate"

else:
    diet_quality = "Unhealthy"

# Display result
st.write("Diet Quality:", diet_quality)

# -------------------------------
# MODULE 6 : DIET SUGGESTIONS
# -------------------------------

st.header("6. Personalized Diet Suggestions")

suggestions = []

# Suggestions based on diet quality
if diet_quality == "Unhealthy":
    suggestions.append("Increase vegetable intake")
    suggestions.append("Reduce processed foods")
    suggestions.append("Add more protein-rich foods like beans, milk, eggs")

elif diet_quality == "Moderate":
    suggestions.append("Add more vegetables and fruits")
    suggestions.append("Improve protein intake")
    suggestions.append("Maintain balanced nutrients")

else:
    suggestions.append("Your diet is healthy. Maintain this balance")
    suggestions.append("Continue eating plant-based foods")
    suggestions.append("Stay hydrated and maintain portion control")

# Display suggestions
for tip in suggestions:
    st.write("•", tip)

# -------------------------------
# MODULE 7 : VISUALIZATION
# -------------------------------

import plotly.express as px

st.header("7. Progress Visualization")

# Sample trend data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

daily_calories = [1800, 1950, 1750, 2000, total_calories]
sustainability_scores = [20, 22, 19, 24, score]

# Chart 1: Daily Calorie Intake
fig1 = px.line(
    x=days,
    y=daily_calories,
    markers=True,
    title="Daily Calorie Intake Over Time",
    labels={"x": "Day", "y": "Calories"}
)

st.plotly_chart(fig1)

# Chart 2: Sustainability Score
fig2 = px.bar(
    x=days,
    y=sustainability_scores,
    title="Sustainability Score Over Time",
    labels={"x": "Day", "y": "Score"}
)

st.plotly_chart(fig2)

# -------------------------------
# MODULE 8 : FINAL REPORT
# -------------------------------

st.header("8. Diet Report Summary")

# Generate report text
report = f"""
SUSTAINABLE DIET ANALYZER REPORT

Name: {name}
Diet Type: {diet_type}
Goal: {goal}

Food Intake:
Breakfast: {breakfast}
Lunch: {lunch}
Dinner: {dinner}
Snacks: {snacks}

Nutrition Summary:
Calories: {total_calories}
Protein: {total_protein}
Carbohydrates: {total_carbs}
Fats: {total_fats}

Sustainability Score: {score}

Diet Quality: {diet_quality}

Suggestions:
"""

for tip in suggestions:
    report += f"- {tip}\n"

# 1️⃣ View report
st.text(report)

# 2️⃣ Download report
st.download_button(
    label="Download Diet Report",
    data=report,
    file_name="diet_report.txt",
    mime="text/plain"
)