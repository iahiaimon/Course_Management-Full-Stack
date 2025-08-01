import React, { useState } from "react";
import axios from "axios";

import { AuthContext } from "./AuthContext";

// Define the AuthProvider component, which will wrap children components and provide authentication context
export function AuthProvider({ children }) {
  // State to store the authentication token, initialized from localStorage if available
  const [token, setToken] = useState(localStorage.getItem("token") || "");
  // State to store the current page (either 'profile' if logged in, or 'login' if not)
  const [page, setPage] = useState(token ? "profile" : "login");

  // Function to handle user login
  const login = async (username, password) => {
    // Send POST request to obtain JWT token
    const res = await axios.post("http://localhost:8000/api/token/", {
      username,
      password,
    });
    const data = res.data;
    // Save the access token in state and localStorage
    setToken(data.access); // Use 'access' instead of 'token'
    localStorage.setItem("token", data.access); // Use 'access' instead of 'token'
    // Navigate to the profile page after login
    setPage("profile");
  };

  // Function to handle user logout
  const logout = () => {
    setToken(""); // Clear the token from state
    localStorage.removeItem("token"); // Remove the token from localStorage
    setPage("login"); // Navigate to the login page
  };

  // Function to handle user registration
  const register = async (username, email, password, role) => {
    // Send POST request to register a new user
    await axios.post("http://localhost:8000/api/register/", {
      username,
      email,
      password,
      role,
    });
    // After registration, navigate to the login page
    setPage("login");
  };

  const category = async (title, description) => {
    // Send POST request to create a new category
    await axios.post("http://localhost:8000/api/category/", {
      title,
      description,
    });
    // After creating a new category, navigate to the profile page
    setPage("category");
  };

  // Helper function to navigate to a specific page
  const goTo = (pageName) => setPage(pageName);

  // Provide the authentication context to child components
  return (
    <AuthContext.Provider
      value={{ token, login, logout, register, page, goTo ,category }}
    >
      {children}
    </AuthContext.Provider>
  );
}
