# Luminous-TechnoX
**Problem Statement** - Develop a Time-of-Use (ToU) and Time-of-Day (ToD) based platform for solar energy optimization, focused on dynamic electricity pricing. The goal is to maximize savings for households and businesses with solar panels by shifting energy usage during cheaper tariffs and using stored solar energy during peak hours.

**Our Approach**

![image](https://github.com/user-attachments/assets/bf698503-31b1-4844-9048-140fad2866b8)

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





# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
