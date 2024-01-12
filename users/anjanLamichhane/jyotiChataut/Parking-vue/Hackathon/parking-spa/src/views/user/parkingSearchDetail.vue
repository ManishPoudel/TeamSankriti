<template>
  <section class="bg-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:py-20 lg:px-8">
      <div class="">
        <div class="grid grid-cols-2 md:grid-cols-2 gap-8">
          <div>
            <div class="max-w-2xl lg:max-w-4xl mx-auto text-center">
              <h2 class="text-3xl font-extrabold text-gray-900">
                Nearby
              </h2>
              <p class="mt-4 text-lg text-gray-500">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
              </p>
            </div>
            <div class="bg-gray-800 p-4">
              <h1 class="text-2xl font-bold mb-4">Places</h1>
              <!-- Replace the items below with dynamic data from your backend -->
              <div class="mb-2">
                <div class="text-gray-700">1. Example Place 1</div>
                <div class="text-sm">Address 1, City 1</div>
              </div>
              <div class="mb-2">
                <div class="text-gray-700">2. Example Place 2</div>
                <div class="text-sm">Address 2, City 2</div>
              </div>
              <!-- Add more items as needed -->
            </div>
          </div>
          <div class="rounded-lg overflow-hidden h-screen">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d28276.13854840178!2d85.32403237809672!3d27.71460108811497!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb1855e30f65e9%3A0x6eaec8d6b3073ec7!2sKathmandu%2C%20Nepal!5e0!3m2!1sen!2snp!4v1642279102453!5m2!1sen!2snep
"
              width="100%"
              height="90%"
              style="border: 0"
              allowfullscreen=""
              loading="lazy"
            ></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {};
</script>
