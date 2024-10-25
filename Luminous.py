import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error

# Generate dummy data
np.random.seed(42)
data_size = 100
dates = pd.date_range(start='2023-01-01', periods=data_size, freq='H')
units_consumed = np.random.randint(10, 100, size=data_size)
cost_per_unit = np.random.uniform(0.5, 5.0, size=data_size)  # Price per unit between 0.5 and 5.0

# Create a DataFrame
df = pd.DataFrame({
    'date': dates,
    'units_consumed': units_consumed,
    'cost_per_unit': cost_per_unit
})

# Extract features
df['hour'] = df['date'].dt.hour
df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month

# Define features and target variable
X = df[['hour', 'day_of_week', 'month']]
y = df['cost_per_unit']

# Split the data into training and testing sets (70-30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate MAPE and MAE
mape = mean_absolute_percentage_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
accuracy = 100 - mape

# Print accuracy and MAPE
print(f'MAPE: {mape:.2f}')
print(f'Accuracy: {accuracy:.2f}%')

# Plotting Actual vs Predicted values
plt.figure(figsize=(12, 6))
plt.plot(y_test.values, label='Actual Price per Unit', marker='o')
plt.plot(y_pred, label='Predicted Price per Unit', marker='x')
plt.title('Actual vs Predicted Price per Unit')
plt.xlabel('Sample Index')
plt.ylabel('Price per Unit')
plt.legend()
plt.grid()
plt.show()

# Input from user for prediction
input_date = input("Enter the date (YYYY-MM-DD): ")
input_time = input("Enter the time (HH:MM, 24-hour format): ")
input_datetime = pd.to_datetime(f"{input_date} {input_time}")

# Prepare input features for prediction
input_hour = input_datetime.hour
input_day_of_week = input_datetime.dayofweek
input_month = input_datetime.month
input_features = pd.DataFrame([[input_hour, input_day_of_week, input_month]], columns=['hour', 'day_of_week', 'month'])

# Predict price per unit for the given input
predicted_price_per_unit = model.predict(input_features)
print(f"Predicted price per unit for {input_datetime}: ${predicted_price_per_unit[0]:.2f}")
