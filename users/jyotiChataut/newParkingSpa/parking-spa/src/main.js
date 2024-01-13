import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";
import "@maptiler/sdk/dist/maptiler-sdk.css";
import "@maptiler/geocoding-control/style.css";


// styles

import "@fortawesome/fontawesome-free/css/all.min.css";
import "./assets/styles/tailwind.css";
import "./assets/styles/index.css";

// mouting point for the whole app

import App from "./App.vue";
import routes from "./routes/routes";
import "./plugins/axios"//docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls;

import axios from "axios";
const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.config.globalProperties.$axios = axios;

app.use(router)
.mount("#app");
