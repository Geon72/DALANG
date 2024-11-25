<template>
  <article 
    class="bg-white rounded-lg overflow-hidden border border-[#F5F5F5] hover:shadow-lg transition-shadow duration-200 cursor-pointer"
    @click="navigateToDetail"
  >
    <!-- Featured Image -->
    <div class="aspect-video overflow-hidden">
      <img :src="`https://picsum.photos/seed/${post.id}/600/400`" :alt="post.title"
        class="w-full h-full object-cover hover:scale-105 transition-transform duration-200" />
    </div>

    <!-- Content -->
    <div class="p-4">
      <!-- Title -->
      <h2 class="text-lg font-bold mb-2 text-[#4A524D] line-clamp-2 hover:text-[#44AAE2] transition-colors">
        {{ post.title }}
      </h2>

      <!-- Preview -->
      <p class="text-sm text-[#4A524D] mb-4 line-clamp-3">
        {{ post.content }}
      </p>

      <!-- Meta -->
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center gap-2">
          <img :src="`https://picsum.photos/seed/author${post.author_username}/100/100`" :alt="post.author_username"
            class="w-6 h-6 rounded-full" />
          <span class="text-xs text-[#4A524D]">{{ post.author_username }}</span>
        </div>
        <span class="text-xs text-gray-500">{{ formatDate(post.created_at) }}</span>
      </div>

      <!-- Engagement -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <button class="flex items-center gap-1 text-sm text-gray-500 hover:text-[#44AAE2] transition-colors"
            @click="$emit('toggle-like', post.id)">
            <Heart :class="{ 'fill-[#44AAE2] text-[#44AAE2]': post.isLiked }" class="w-4 h-4" />
            <span>{{ post.like_count || 0 }}</span>
          </button>
          <div class="flex items-center gap-1 text-sm text-gray-500">
            <MessageCircle class="w-4 h-4" />
            <span>{{ post.comment_count || 0 }}</span>
          </div>
        </div>
      </div>

      <!-- Tags -->
      <div class="flex flex-wrap gap-2 mt-3">
        <span v-for="tag in getTags(post)" :key="tag" v-if="tag"
          class="text-xs text-[#44AAE2] hover:text-[#115583] transition-colors">
          #{{ tag }}
        </span>
      </div>
    </div>
  </article>
</template>

<script setup>
import { Heart, MessageCircle } from 'lucide-vue-next'
import { useRouter } from 'vue-router'
const router = useRouter()

const props = defineProps({
  post: Object
})

const navigateToDetail = () => {
  router.push(`/articles/${props.post.id}`)
}

const formatDate = (date) => {
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(new Date(date))
}

const getTags = (post) => {
  return [post.hashtag1, post.hashtag2, post.hashtag3].filter(Boolean)
}


</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>