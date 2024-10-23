# Luminous-TechnoX

- **Problem Statement** - Develop a Time-of-Use (ToU) and Time-of-Day (ToD) based platform for solar energy optimization, focused on dynamic electricity pricing. The goal is to maximize savings for households and businesses with solar panels by shifting energy usage during cheaper tariffs and using stored solar energy during peak hours.

![image](https://github.com/user-attachments/assets/1e2a94b0-81f1-4d69-bf07-bd4bee24b70a)


- **Real-Time Tariff Monitoring** - This part fetches and processes real-time tariff data.
  - Backend - Python/Flask
  - Explanation: Creates an API to fetch dummy real-time tariffs and forecasts.
  - Deployment: Deploy this Flask app on Heroku or AWS Lambda.
- **Energy Consumption Analytics** – This part analyses energy consumption patterns and costs.
  - Backend - Python/Flask
  - Explanation: Analysis of energy consumption using Python.
  - Deployment: Deploy this on Heroku.
  - Frontend - React
  - Explanation: This displays energy consumption data and costs on a web dashboard.
  - Deployment: React app can be deployed on Netlify or Vercel.
- **Smart Scheduling of High-Energy Appliances**—This part schedules the use of high-energy devices when electricity prices are low.
  - Backend - Python/Flask
  - Explanation: This code schedules appliance usage during optimal periods (e.g., low tariffs).
  - Deployment: This Python code can be used with IoT devices to automate appliance usage.
- **Solar Energy Management (IoT Integration)**—This part ensures the proper management of generated solar energy.
  - Backend - MQTT Communication (Python)
  - Explanation: This code uses MQTT for IoT communication between solar panels, batteries, and the backend.
  - Deployment: This can be used with IoT devices or emulators.
- **Forecasting & Recommendations (Machine Learning)**—This part predicts or forecasts the future energy consumption.
  - Backend – Scikit-Learn (Python)
  - Explanation: This code predicts future energy consumption using Random Forest Regression.
  - Deployment: This can be deployed as a Flask API to serve predictions.
- **User Notifications & Alerts** – This part sets a notification system to send real-time alerts about high tariffs, and solar battery status.
  - Backend - Flask + Firebase Cloud Messaging
  - Explanation: Sends notifications via Firebase Cloud Messaging.
  - Deployment: Deploy this on Heroku.
  - Frontend - React Notification Display
  - Explanation: Displays notifications on the frontend.
  - Deployment: React app can be deployed on Netlify.












