<template>
    <header class="flex mb-12">
      <div class="w-full md:w-1/3 pr-8">
        <div class="w-40 h-40 rounded-full overflow-hidden mx-auto md:mx-0">
          <img :src="user.profilePicture" alt="Profile Picture" class="w-full h-full object-cover">
        </div>
      </div>
      <div class="w-full md:w-2/3">
        <div class="flex flex-col md:flex-row items-center mb-4">
          <h1 class="text-3xl font-light mr-4">{{ user.username }}</h1>
          <button class="bg-[#FAFAFA] border border-[#DBDBDB] text-sm font-semibold py-1 px-4 rounded mt-2 md:mt-0">
            Edit Profile
          </button>
          <button class="ml-2 mt-2 md:mt-0">
            <SettingsIcon class="w-6 h-6 text-[#262626]" />
          </button>
        </div>
        <div class="flex justify-center md:justify-start mb-4">
          <div class="mr-8"><span class="font-semibold">{{ user.posts.length }}</span> posts</div>
          <div class="mr-8"><span class="font-semibold">{{ user.followers }}</span> followers</div>
          <div><span class="font-semibold">{{ user.following }}</span> following</div>
        </div>
        <div class="text-center md:text-left">
          <p class="font-semibold">{{ user.fullName }}</p>
          <p>{{ user.bio }}</p>
        </div>
      </div>
    </header>
  </template>
  
  <script setup>
  import { SettingsIcon } from 'lucide-vue-next'
  
  defineProps({
    user: {
      type: Object,
      required: true
    }
  })
  </script>