<template>
  <div class="border-t border-[#DBDBDB] mb-4">
    <div class="flex justify-center py-4">
      <button @click="activeTab = 'photos'" :class="[
        'mx-4 text-xs font-semibold uppercase flex items-center transition-colors',
        activeTab === 'photos' ? 'text-[#262626]' : 'text-[#8E8E8E]'
      ]">
        <GridIcon class="w-4 h-4 mr-1" /> 사진
      </button>
      <button @click="activeTab = 'posts'" :class="[
        'mx-4 text-xs font-semibold uppercase flex items-center transition-colors',
        activeTab === 'posts' ? 'text-[#262626]' : 'text-[#8E8E8E]'
      ]">
        <FileTextIcon class="w-4 h-4 mr-1" /> 글
      </button>
    </div>
  </div>

  <div v-if="activeTab === 'photos'" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
    <div v-for="photo in photos" :key="photo.id" class="aspect-square">
      <img :src="`https://picsum.photos/seed/${photo.id}/300/300`" :alt="'Photo ' + photo.id"
        class="w-full h-full object-cover">
    </div>
  </div>

  <div v-else class="space-y-6">
    <div v-for="post in posts" :key="post.id"
      class="border-b border-[#DBDBDB] pb-6 last:border-b-0 hover:bg-gray-50 transition-colors">
      <h3 class="text-lg font-semibold mb-2">{{ post.title }}</h3>
      <p class="text-gray-600 mb-2 line-clamp-3">{{ post.content }}</p>
      <div class="flex justify-between items-center text-sm text-gray-500">
        <span>{{ post.date }}</span>
        <div class="flex items-center space-x-4">
          <span class="flex items-center">
            <HeartIcon class="w-4 h-4 mr-1" />
            {{ post.likes }}
          </span>
          <span class="flex items-center">
            <MessageCircleIcon class="w-4 h-4 mr-1" />
            {{ post.comments }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { GridIcon, FileTextIcon, HeartIcon, MessageCircleIcon } from 'lucide-vue-next'

const activeTab = ref('photos')

const photos = ref([
  { id: 1 },
  { id: 2 },
  { id: 3 },
  { id: 4 },
  { id: 5 },
  { id: 6 },
  { id: 7 },
  { id: 8 },
  { id: 9 },
])

const posts = ref([
  {
    id: 1,
    title: "My First Blog Post",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    date: "2023-05-15",
    likes: 24,
    comments: 5
  },
  {
    id: 2,
    title: "Exploring Vue 3",
    content: "Vue 3 brings exciting new features like the Composition API, which allows for better code organization and reuse. In this post, we'll explore some of the key benefits and how to get started with Vue 3.",
    date: "2023-05-20",
    likes: 42,
    comments: 8
  },
  {
    id: 3,
    title: "Tailwind CSS Tips and Tricks",
    content: "Tailwind CSS is a utility-first CSS framework that can significantly speed up your development process. Here are some tips and tricks to make the most out of Tailwind in your projects.",
    date: "2023-05-25",
    likes: 37,
    comments: 12
  }
])
</script>

<style scoped>
/* Add any additional styles here */
</style>