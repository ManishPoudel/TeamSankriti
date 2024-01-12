
// layouts

import Admin from "../layouts/Admin.vue";
import Auth from "../layouts/Auth.vue";

// views for Admin layout

import Dashboard from "../views/admin/Dashboard.vue";
import Settings from "../views/admin/Settings.vue";
import Tables from "../views/admin/Tables.vue";
import Maps from "../views/admin/Maps.vue";

// views for Auth layout

import Login from "../views/auth/Login.vue";
import Register from "../views/auth/Register.vue";
import forgotPassword from "../views/auth/forgotPassword.vue";
import changePassword from "../views/auth/changePassword.vue";

// views without layouts

import Profile from "../views/Profile.vue";
import Index from "../layouts/Index.vue";

//views for User Profile
import userProfile from "../views/user/profile/userProfile.vue";
import mainPage from "../views/user/mainPage.vue";
import searchResult from "../views/user/parkingSearchDetail.vue";

import UserIndex from "../views/user/index.vue"
// routes

const routes = [
  {

    // admin section routes
    path: "/admin",
    redirect: "/admin/dashboard",
    component: Admin,
    children: [
      {
        path: "/admin/dashboard",
        component: Dashboard,
      },
      {
        path: "/admin/settings",
        component: Settings,
      },
      {
        path: "/admin/tables",
        component: Tables,
      },
      {
        path: "/admin/maps",
        component: Maps,
      },
      {
        path: "/profile",
        component: Profile,
      },
    ],
  },


  // auth sections routes
  {
    path: "/auth",
    redirect: "/auth/login",
    component: Auth,
    children: [
      {
        path: "/auth/login",
        component: Login,
      },
      {
        path: "/auth/register",
        component: Register,
      },
      {
        path: "/auth/forgotPassword",
        component: forgotPassword,
      },
      {
        path: "/auth/changePassword",
        component: changePassword,
      }
    ],
  },


  // users sections all routes
  {
    path: "/user",
    redirect: "/",
    component: UserIndex,
    children: [
      {
        path: "/",
        component: mainPage,
      },
      {
        path: "/landing",
        component: mainPage,
      },
      {
        path: "/search/result",
        component: searchResult,
      },

      {
        path: "/userProfile",
        component: userProfile,
      },
    ]
  },

  { path: "/:pathMatch(.*)*", redirect: "/" },
];

export default routes;