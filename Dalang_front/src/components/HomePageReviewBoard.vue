<template>
  <section>
    <h2 class="text-3xl font-bold text-[#115583] mb-6">Review Board</h2>
    <div class="bg-white rounded-lg shadow-md p-6">
      <div v-for="review in reviews" :key="review.id" class="mb-6 pb-6 border-b border-gray-200 last:border-b-0">
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center">
            <img :src="review.avatar" :alt="review.name" class="w-10 h-10 rounded-full mr-3">
            <div>
              <h4 class="font-semibold text-[#4A524D]">{{ review.name }}</h4>
              <div class="flex">
                <StarIcon v-for="i in 5" :key="i" :class="[i <= review.rating ? 'text-[#CBC7A4]' : 'text-gray-300']" />
              </div>
            </div>
          </div>
          <button @click="reportReview(review.id)" class="text-[#92B3B5] hover:text-[#115583]">
            <FlagIcon />
          </button>
        </div>
        <p class="text-[#4A524D] mb-2">{{ review.content }}</p>
        <div class="flex items-center space-x-4">
          <button @click="likeReview(review.id)" class="flex items-center text-[#92B3B5] hover:text-[#44AAE2]">
            <ThumbsUpIcon class="mr-1" /> {{ review.likes }}
          </button>
          <button @click="toggleComments(review.id)" class="flex items-center text-[#92B3B5] hover:text-[#44AAE2]">
            <MessageCircleIcon class="mr-1" /> {{ review.comments.length }}
          </button>
        </div>
        <div v-if="review.showComments" class="mt-4 space-y-2">
          <div v-for="comment in review.comments" :key="comment.id" class="bg-gray-50 p-2 rounded">
            <p class="text-sm text-[#4A524D]"><span class="font-semibold">{{ comment.name }}:</span> {{ comment.content
              }}</p>
          </div>
          <form @submit.prevent="addComment(review.id)" class="flex mt-2">
            <input v-model="newComment" type="text" placeholder="Add a comment"
              class="flex-grow px-3 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-[#44AAE2]">
            <button type="submit"
              class="bg-[#44AAE2] text-white px-4 py-2 rounded-r-md hover:bg-[#115583]">Post</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { StarIcon, FlagIcon, ThumbsUpIcon, MessageCircleIcon } from 'lucide-vue-next'

const props = defineProps({
  reviews: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['reportReview', 'likeReview', 'toggleComments', 'addComment'])

const newComment = ref('')

const reportReview = (id) => {
  emit('reportReview', id)
}

const likeReview = (id) => {
  emit('likeReview', id)
}

const toggleComments = (id) => {
  emit('toggleComments', id)
}

const addComment = (id) => {
  if (newComment.value.trim()) {
    emit('addComment', { id, comment: newComment.value.trim() })
    newComment.value = ''
  }
}
</script>