<template>
  <div>
    <navbar />
    <main>
      <div
        class="relative pt-16 pb-32 flex content-center items-center justify-center min-h-screen-75"
      >
        <div
          class="absolute w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80');
          "
        >
          <span
            id="blackOverlay"
            class="w-full h-full absolute opacity-75 bg-black"
          ></span>
        </div>
        <div class="container relative mx-auto">
          <div class="items-center flex flex-wrap">
            <div class="w-full lg:w-6/12 px-4 ml-auto mr-auto text-center">
              <div class="pr-12">
                <h1 class="text-white font-semibold text-5xl">
                  Jyoti story starts with uss.
                </h1>
                <button @click="jyoti()">
                  Click me
                </button>
                <p class="mt-4 text-lg text-blueGray-200">
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perspiciatis laborum molestias commodi nemo! Sapiente, dolor nisi voluptas placeat voluptate nobis atque. Perferendis commodi similique numquam dolore officia libero aspernatur quasi!
                </p>
              </div>
            </div>
          </div>
        </div>
        <div
          class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
          style="transform: translateZ(0);"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="text-blueGray-200 fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </div>

    </main>
    <footer-component />
  </div>
</template>
<script>
import Navbar from "../components/Navbars/IndexNavbar.vue";
import FooterComponent from "../components/Footers/Footer.vue";

import team1 from "../assets/img/team-1-800x800.jpg";
import team2 from "../assets/img/team-2-800x800.jpg";
import team3 from "../assets/img/team-3-800x800.jpg";
import team4 from "../assets/img/team-4-470x470.png";

export default {
  data() {
    return {
      team1,
      team2,
      team3,
      team4,
    };
  },
  components: {
    Navbar,
    FooterComponent,
  },
  methods:{
    jyoti(){
      console.log('its me');
    }
  }
};
</script>
