<template>
    <div id="mapContainer" class="overflow-hidden z-0"></div>
  </template>
  
  <script>
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";
  
  export default {
    name: "LeafletMap",
    data() {
      return {
        map: null,
        latitude: null,
        longitude: null,
      };
    },
    created() {
      const success = (position) => {
        this.latitude = position.coords.latitude;
        this.longitude = position.coords.longitude;
        // console.log(this.latitude, this.longitude);
         // Initialize Leaflet map
      const map = L.map("mapContainer").setView([this.latitude, this.longitude], 15);
  
      // Add OpenStreetMap tile layer
      L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);
  
      const markerCoordinates = [[this.latitude, this.longitude]];
  
      markerCoordinates.forEach((coords) => {
        L.marker(coords).addTo(map);
      });
      };
  
      const error = (err) => {
        console.error(err);
      };
  
      // This will open permission popup
      navigator.geolocation.getCurrentPosition(success, error);
    },
    onBeforeUnmount() {
      if (this.map) {
        this.map.remove();
      }
    },
  };
  </script>
  
  