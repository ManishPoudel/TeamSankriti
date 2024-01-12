
<template>
  <div
    class="absolute w-full h-full bg-center bg-cover"
  >
    <span
      id="blackOverlay"
      class="w-full h-full absolute opacity-75 bg-black"
    ></span>

    <div class=" h-screen w-screen flex flex-col justify-center items-center">
      <div class="m-5">
      <leaflet-map/>
      </div>
      <!-- <form action="/search" class="max-w-[480px] w-full px-4">
        <div class="relative flex justify-center items-center">
          <input
            type="text"
            class="w-1/2 border h-12 shadow p-4 rounded-full"
            placeholder="search"
            autocomplete="off"
          />
          <button>
            <svg
              class="text-white h-5 w-5 absolute fill-current"
              xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              version="1.1"
              x="0px"
              y="0px"
              viewBox="0 0 56.966 56.966"
              style="enable-background: new 0 0 56.966 56.966"
              xml:space="preserve"
            >
              <path
                d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"
              ></path>
            </svg>
          </button>
        </div>
      </form> -->
    </div>
  </div>
</template>

<script>
  import image from "../../assets/img/map1.jpeg"
  import LeafletMap from "../../components/Map/mainMap.vue"
export default {
    data() {
    return {
      image: image,
    };
  },
components:{
  LeafletMap
}
};
</script>

