<template>
  <div class="border-t border-[#DBDBDB] mb-4">
    <div class="flex justify-center py-4">
      <button @click="activeTab = 'myPosts'" :class="[
        'mx-4 text-xs font-semibold uppercase flex items-center transition-colors',
        activeTab === 'myPosts' ? 'text-[#262626]' : 'text-[#8E8E8E]'
      ]">
        <FileTextIcon class="w-4 h-4 mr-1" /> 내가 쓴 글
      </button>
      <button @click="activeTab = 'likedPosts'" :class="[
        'mx-4 text-xs font-semibold uppercase flex items-center transition-colors',
        activeTab === 'likedPosts' ? 'text-[#262626]' : 'text-[#8E8E8E]'
      ]">
        <HeartIcon class="w-4 h-4 mr-1" /> 내가 좋아요한 글
      </button>
    </div>
  </div>

  <div v-if="activeTab === 'myPosts'" class="space-y-6">
    <div v-for="post in sortedMyPosts" :key="post.id"
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

  <div v-if="activeTab === 'likedPosts'" class="space-y-6">
    <div v-for="post in sortedLikedPosts" :key="post.id"
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
import { ref, computed } from 'vue'
import { FileTextIcon, HeartIcon, MessageCircleIcon } from 'lucide-vue-next'

const activeTab = ref('myPosts')

const props = defineProps({
  myPosts: {
    type: Array,
    required: true
  },
  likedPosts: {
    type: Array,
    required: true
  }
})

// created_at 타임스탬프를 사용하여 최신순 정렬
const sortedMyPosts = computed(() => {
  return [...props.myPosts].sort((a, b) => 
    new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
  ).reverse()
})

const sortedLikedPosts = computed(() => {
  return [...props.likedPosts].sort((a, b) => 
    new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
  ).reverse()
})
</script>

<style scoped></style>