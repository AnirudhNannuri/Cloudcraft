Ensure the following software is installed on your system before proceeding:
Node.js (v16 or higher) and npm – for running the React frontend
Python (v3.9 or higher) – for running the Flask backend
MongoDB – running locally or accessible via MongoDB Atlas
Git – to clone the repository

cloudcraft-frontend:
  Clone the git repository -> Move to cloudcraft-frontend 
  command - npm install -> Installs all the required packages and libraries 
  npm start - runs the frontend 

Backend: 
  I have used flask for the backend.
  pip install flask
  navigate to src folder in backend
  npx ts-node server.ts -> runs the back end at localhost:5000

MongoDB:
  Install mongoDB compass.
  Create two separate collections named:
  authDB -> user-credentials collection
  website-data -> websites (Stores the collected websites data)

Webscrapping:
  Navitgate to the webscrapper folder in project. 
  Run the scraper.py file -> python scraper.py
  
  
