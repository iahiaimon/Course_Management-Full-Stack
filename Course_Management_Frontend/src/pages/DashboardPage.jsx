import React, { useState, useEffect } from "react";
import { useAuth } from "../hooks/useAuth";
import ProfilePage from "./ProfilePage";
import UsersPage from "./UsersPage";
import RegisterPage from "./RegisterPage";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import CategoryPage from "./CategoryPage";
import CategoryListPage from "./CategoryListPage";
import CoursePage from "./CoursePage";
import CourseListPage from "./CourseListPage";
import axios from "axios";

function DashboardPage() {
  const { logout, token } = useAuth();
  const [user, setUser] = useState({
    username: "User",
    role: "student",
    email: "user@email.com",
  });
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [showProfile, setShowProfile] = useState(false);
  const [currentPage, setCurrentPage] = useState("dashboard");
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    // Fetch user data to determine if admin
    if (token) {
      axios
        .get("http://localhost:8000/api/account/", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((res) => {
          const data = res.data;
          console.log("DashboardPage - User profile data:", data);
          setUser(data);
          setIsAdmin(data.role === "admin");
        })
        .catch((error) => {
          console.error("Error fetching user data:", error);
        });
    }
  }, [token]);

  // Redirect non-admin users away from admin-only pages when role changes
  useEffect(() => {
    if (!isAdmin && (currentPage === "users" || currentPage === "register")) {
      setCurrentPage("dashboard");
    }
  }, [isAdmin, currentPage]);

  const navItems = [
    {
      label: "Dashboard",
      icon: <i class="fa-solid fa-cloud"></i>,
      onClick: () => {
        setCurrentPage("dashboard");
        setShowProfile(false);
      },
      active: currentPage === "dashboard" && !showProfile,
    },
    // Only show Users and Register pages for admins
    ...(isAdmin
      ? [
          {
            label: "Users",
            icon: <i class="fa-solid fa-user"></i>,
            onClick: () => {
              setCurrentPage("users");
              setShowProfile(false);
            },
            active: currentPage === "users",
          },
          {
            label: "Register User",
            icon: <i class="fa-solid fa-circle-user"></i>,
            onClick: () => {
              setCurrentPage("register");
              setShowProfile(false);
            },
            active: currentPage === "register",
          },

          {
            label: "Add Category",
            icon: <i class="fa-solid fa-layer-group"></i>,
            onClick: () => {
              setCurrentPage("category");
              setShowProfile(false);
            },
            active: currentPage === "category",
          },

          {
            label: "Category List",
            icon: <i class="fa-solid fa-table-cells-large"></i>,
            onClick: () => {
              setCurrentPage("categoryList");
              setShowProfile(false);
            },
            active: currentPage === "categoryList",
          },

          {
            label: "Add Course",
            icon: <i class="fa-brands fa-discourse"></i>,

            onClick: () => {
              setCurrentPage("course");
              setShowProfile(false);
            },
            active: currentPage === "course",
          },

          {
            label: "Course List",
            icon: <i class="fa-solid fa-table-list"></i>,
            onClick: () => {
              setCurrentPage("courseList");
              setShowProfile(false);
            },
            active: currentPage === "courseList",
          },
        ]
      : []),
  ];

  const renderContent = () => {
    switch (currentPage) {
      case "profile":
        return <ProfilePage />;
      case "users":
        return <UsersPage />;
      case "register":
        return <RegisterPage />;
      case "category":
        return <CategoryPage />;
      case "categoryList":
        return <CategoryListPage />;
      case "course":
        return <CoursePage />;
      case "courseList":
        return <CourseListPage />;
      case "dashboard":
      default:
        return (
          <div className="w-full text-center">
            <h2 className="text-3xl font-bold text-blue-600 mb-4">
              Welcome to your Dashboard!
            </h2>
            <p className="text-gray-500 text-lg mb-6">
              Use the sidebar to navigate your LMS features.
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
              <div className="bg-white p-5 rounded-xl shadow border border-gray-100 hover:shadow-md transition-all">
                <h3 className="text-lg font-semibold text-gray-800 mb-2">
                  Quick Stats
                </h3>
                <p className="text-gray-600 text-sm">
                  View your learning progress and achievements.
                </p>
              </div>
              <div className="bg-white p-5 rounded-xl shadow border border-gray-100 hover:shadow-md transition-all">
                <h3 className="text-lg font-semibold text-gray-800 mb-2">
                  Recent Courses
                </h3>
                <p className="text-gray-600 text-sm">
                  Continue where you left off in your courses.
                </p>
              </div>
              <div className="bg-white p-5 rounded-xl shadow border border-gray-100 hover:shadow-md transition-all">
                <h3 className="text-lg font-semibold text-gray-800 mb-2">
                  Notifications
                </h3>
                <p className="text-gray-600 text-sm">
                  Stay updated with important announcements.
                </p>
              </div>
            </div>
          </div>
        );
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-blue-50 via-white to-green-50 flex">
      <Sidebar
        sidebarOpen={sidebarOpen}
        setSidebarOpen={setSidebarOpen}
        navItems={navItems}
      />
      <div className="flex-1 flex flex-col min-h-screen">
        <Topbar
          user={user}
          showProfile={showProfile}
          setShowProfile={setShowProfile}
          logout={logout}
          setCurrentPage={setCurrentPage}
        />
        <main className="flex-1 p-6 sm:p-8 bg-transparent overflow-auto w-full flex justify-center">
          <div className="w-full max-w-6xl">{renderContent()}</div>
        </main>
      </div>
    </div>
  );
}

export default DashboardPage;
