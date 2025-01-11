import React from "react";
import ReactDOM from "react-dom/client"; // Use createRoot from React 18
import App from "./App";
import "./index.css"; // Optional: Your CSS file

// Find the root element in your HTML
const rootElement = document.getElementById("root");

// Create a root using createRoot
const root = ReactDOM.createRoot(rootElement);

// Render the application
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
