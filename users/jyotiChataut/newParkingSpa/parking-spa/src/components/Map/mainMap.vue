<template></template>

<script>
import * as maptilersdk from "@maptiler/sdk";
import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";

export default {
  name: "LeafletMap",
  data() {
    return {
      map: null,
      latitude: null,
      longitude: null,
    };
  },
  mounted() {
    maptilersdk.config.apiKey = "oRYkqFeukqB4YhHMO7CX";

    // Check if the container exists before creating the map
    const mapContainer = document.getElementById("map");
    if (!mapContainer) {
      console.error("Map container not found.");
      return;
    }

    // Create a new map with an initial center and zoom level
    const map = new maptilersdk.Map({
      container: mapContainer,
      style: maptilersdk.MapStyle.STREETS,
      zoom: 3,
      center: [-94.77, 38.57],
    });

    // Check if the Geolocation API is available
    if ("geolocation" in navigator) {
      // Get the user's current position
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;

          // Update the map center with the user's current position
          map.setCenter([longitude, latitude]);
          map.setZoom(12); // You can adjust the zoom level as needed

          // Create a popup with your desired description
          const popup = new maptilersdk.Popup()
            .setLngLat([longitude, latitude])
            .setHTML(
              "<h3>Your Location</h3><p>This is your current location.</p>"
            )
            .addTo(map);

          // Add a marker at the user's current position
          const marker = new maptilersdk.Marker()
            .setLngLat([longitude, latitude])
            .addTo(map);

          // Optionally, close the popup when the marker is clicked
          marker.setPopup(popup);
        },
        (error) => {
          console.error("Error getting current location:", error.message);
        }
      );
    } else {
      console.error("Geolocation not supported.");
    }

    const gc = new GeocodingControl({});
    map.addControl(gc, "top-left");
  },
  mounted() {
    maptilersdk.config.apiKey = "oRYkqFeukqB4YhHMO7CX";

    // Check if the container exists before creating the map
    const mapContainer = document.getElementById("map");
    if (!mapContainer) {
      console.error("Map container not found.");
      return;
    }

    // Create a new map with an initial center and zoom level
    const map = new maptilersdk.Map({
      container: mapContainer,
      style: maptilersdk.MapStyle.STREETS,
      zoom: 12,
      center: [85.324, 27.7172], // Kathmandu coordinates
    });

    // Array of places in Kathmandu with coordinates and popup values
    const places = [
      {
        coordinates: [85.324, 27.7172],
        popupContent:
          "<h3>Kathmandu Durbar Square</h3><p>An ancient palace with rich history.</p>",
      },
      {
        coordinates: [85.3081, 27.714],
        popupContent:
          "<h3>Swayambhunath Stupa</h3><p>A UNESCO World Heritage Site.</p>",
      },
      {
        coordinates: [85.342, 27.7065],
        popupContent:
          "<h3>Pashupatinath Temple</h3><p>A sacred Hindu temple complex.</p>",
      },
      {
        coordinates: [85.3554, 27.6915],
        popupContent:
          "<h3>Boudhanath Stupa</h3><p>One of the largest stupas in the world.</p>",
      },
    ];

    // Iterate over places and add markers
    places.forEach((place) => {
      const { coordinates, popupContent } = place;

      // Create a marker at the place's coordinates
      const marker = new maptilersdk.Marker().setLngLat(coordinates).addTo(map);

      // Create a popup with dynamic content
      const popup = new maptilersdk.Popup()
        .setLngLat(coordinates)
        .setHTML(popupContent);

      // Attach the popup to the marker click event
      marker.setPopup(popup);

      // Optionally, open the popup when the marker is clicked
      marker.on("click", () => {
        popup.addTo(map);
      });
    });

    const gc = new GeocodingControl({});
    map.addControl(gc, "top-left");
  },
  onBeforeUnmount() {},
};
</script>