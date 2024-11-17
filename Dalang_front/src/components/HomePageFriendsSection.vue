<template>
    <section class="mb-12">
      <h2 class="text-3xl font-bold text-[#115583] mb-6">Friends' Activities</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="friend in friends" :key="friend.name" class="bg-white rounded-lg shadow-md overflow-hidden">
          <img :src="friend.avatar" :alt="friend.name" class="w-full h-32 object-cover">
          <div class="p-4">
            <h3 class="text-lg font-semibold text-[#4A524D] mb-2">{{ friend.name }}</h3>
            <p class="text-[#92B3B5] text-sm">{{ friend.activity }}</p>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  defineProps({
    friends: {
      type: Array,
      required: true
    }
  })
  </script>