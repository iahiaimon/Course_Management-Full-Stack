import React, { useState, useEffect } from "react";
import axios from "axios";
import { useAuth } from "../hooks/useAuth";
import Avatar from "../components/Avatar";

function CategoryListPage() {
  const { token } = useAuth();
  const [allCategories, setAllCategories] = useState([]);
  const [isCurrentUserAdmin, setIsCurrentUserAdmin] = useState(false);

  useEffect(() => {
    const checkAdminAndFetchCategories = async () => {
      try {
        const profileResponse = await axios.get(
          "http://localhost:8000/api/account/",
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        const currentUserData = profileResponse.data;
        console.log("Current user profile:", currentUserData);

        if (currentUserData.role === "admin") {
          setIsCurrentUserAdmin(true);

          const categoriesResponse = await axios.get(
            "http://localhost:8000/api/category/",
            {
              headers: { Authorization: `Bearer ${token}` },
            }
          );

          const categoriesList = categoriesResponse.data;
          console.log("All categories:", categoriesList);

          if (Array.isArray(categoriesList)) {
            setAllCategories(categoriesList);
          }
        } else {
          setIsCurrentUserAdmin(false);
          throw new Error("You are not an admin");
        }
      } catch (error) {
        console.error("There was a problem:", error);
      }
    };

    checkAdminAndFetchCategories();
  }, [token]);

  // If the user is not an admin, show an access denied message
  if (!isCurrentUserAdmin) {
    return (
      <div className="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-md text-center">
        <h2 className="text-2xl font-bold mb-4 text-red-600">
          Sorry, You Can't View This Page
        </h2>
        <p className="text-gray-600">
          Only admin users can see the list of all category. If you think this
          is a mistake, please contact your administrator.
        </p>
      </div>
    );
  }

  // If the user is an admin, show the table of all category
  return (
    <div className="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-6xl text-center">
      <h2 className="text-2xl font-bold mb-6 text-green-600">
        All Category List
      </h2>
      <div className="overflow-x-auto rounded-lg text-black">
        <table className="min-w-full border border-gray-200 rounded-lg overflow-hidden">
          <thead className="bg-blue-50">
            <tr>
              <th className="border px-4 py-2 text-center">ID</th>
              <th className="border px-4 py-2 text-left">Title</th>
              <th className="border px-4 py-2 text-left">Status</th>
              <th className="border px-4 py-2 text-left">Number of Course</th>
            </tr>
          </thead>
          <tbody>
            {allCategories.map((category) => (
              <tr key={category.id}>
                <td className="border px-4 py-2 font-semibold">
                  {category.id}
                </td>
                <td className="border px-4 py-2 font-semibold">
                  {category.title}
                </td>
                <td className="border px-4 py-2">
                  {category.is_active ? "Active" : "Inactive"}
                </td>
                <td className="border px-4 py-2 capitalize">
                  {Array.isArray(category.course)
                    ? category.course.length
                    : 0}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default CategoryListPage;
