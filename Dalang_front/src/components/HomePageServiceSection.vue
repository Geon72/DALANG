<template>
    <section class="mb-12">
      <h2 class="text-3xl font-bold text-[#115583] mb-6">Our Services</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="service in services" :key="service.name" class="bg-white rounded-lg shadow-md overflow-hidden">
          <img :src="service.image" :alt="service.name" class="w-full h-48 object-cover">
          <div class="p-4">
            <h3 class="text-xl font-semibold text-[#4A524D] mb-2">{{ service.name }}</h3>
            <p class="text-[#92B3B5]">{{ service.description }}</p>
            <router-link :to="service.route" class="mt-4 inline-block bg-[#44AAE2] text-white py-2 px-4 rounded hover:bg-[#115583] transition-colors">
              Learn More
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  defineProps({
    services: {
      type: Array,
      required: true
    }
  })
  </script>