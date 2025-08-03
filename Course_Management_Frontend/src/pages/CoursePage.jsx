import React, { useState } from "react";
import { useAuth } from "../hooks/useAuth";

function CoursePage() {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    price: "",
    banner: "",
    duration: "",
    category: "",
  });

  const [message, setMessage] = useState("");
  const { course } = useAuth();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    const courseData = {
      title: formData.title,
      description: formData.description,
      price: Number(formData.price), // convert to number
      duration: Number(formData.duration), // convert to number
      category: Number(formData.category), // convert to number (for FK)
      // status: formData.status || "active", // ensure status is not undefined
    };

    try {
      await course(formData.title, formData.description);
      setMessage("A new Course has been created");
      setFormData({
        title: "",
        description: "",
        price: "",
        banner: "",
        duration: "",
        category: "",
      });
    } catch (err) {
      setMessage(
        err.response?.data?.detail ||
          err.message ||
          "Course creation failed | Try again."
      );
    }
    console.log(courseData);
  };

  return (
    <div className="w-full max-w-2xl mx-auto text-black">
      <div className="bg-white p-8 rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold mb-6 text-center text-blue-600">
          Create a new Course
        </h2>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M5.121 17.804A13.937 13.937 0 0112 15c2.5 0 4.847.655 6.879 1.804M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </span>
            <input
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
              placeholder="Title"
              name="title"
              value={formData.title}
              onChange={handleChange}
              required
              autoComplete="title"
            />
          </div>
          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M16 12a4 4 0 01-8 0 4 4 0 018 0z"
                />
              </svg>
            </span>
            <input
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
              placeholder="Description"
              type="text"
              name="description"
              value={formData.description}
              onChange={handleChange}
              autoComplete="description"
            />
          </div>

          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M16 12a4 4 0 01-8 0 4 4 0 018 0z"
                />
              </svg>
            </span>
            <input
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
              placeholder="Price"
              type="text"
              name="price"
              value={formData.price}
              onChange={handleChange}
              required
              autoComplete="price"
            />
          </div>

          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M16 12a4 4 0 01-8 0 4 4 0 018 0z"
                />
              </svg>
            </span>
            <input
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
              placeholder="Banner"
              type="file"
              name="banner"
              value={formData.banner}
              onChange={handleChange}
              autoComplete="banner"
            />
          </div>

          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M16 12a4 4 0 01-8 0 4 4 0 018 0z"
                />
              </svg>
            </span>
            <input
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
              placeholder="Duration"
              type="number"
              name="duration"
              value={formData.duration}
              onChange={handleChange}
              autoComplete="duration"
            />
          </div>

          <div className="relative">
            <span className="absolute left-3 top-2.5 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M16 12a4 4 0 01-8 0 4 4 0 018 0z"
                />
              </svg>
            </span>
            <input
              className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
              placeholder="Category"
              type="text"
              name="category"
              value={formData.category}
              onChange={handleChange}
              autoComplete="category"
            />
          </div>
          <button
            className="bg-blue-500 text-white py-2 rounded-lg font-semibold hover:bg-blue-600 transition shadow mt-2"
            type="submit"
          >
            Create Course
          </button>
        </form>
        {message && (
          <div
            className={`mt-3 text-center text-sm ${
              message.includes("success") ? "text-green-500" : "text-red-500"
            }`}
          >
            {message}
          </div>
        )}
      </div>
    </div>
  );
}

export default CoursePage;
