<template>
    <navbar />
    <main>
      <section class="relative w-full h-full min-h-screen bg-orange-200">
        <div class="py-16">
        <router-view />
        </div>
      </section>
    </main>
    <footer-component/>
</template>

<script>
import Navbar from "../../components/Navbars/IndexNavbar.vue";
import FooterComponent from "../../components/Footers/Footer.vue";

export default {
  components: {
    Navbar,
    FooterComponent,
  },
};
</script>
