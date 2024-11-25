<template>
  <form @submit.prevent="submitPost">
    <div class="space-y-6">
      <CreatePostFormInput label="Title" v-model="post.title" :maxlength="100" placeholder="Enter your post title" requi
        red />

      <div>
        <label for="content" class="block text-sm font-medium text-gray-700">Content</label>
        <div class="mt-1">
          <textarea id="content" v-model="post.content" rows="5"
            class="block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Write your post content here" required></textarea>
        </div>
      </div>

      <div class="grid grid-cols-1 gap-4 sm:grid-cols-3">
        <FormInput v-for="(hashtag, index) in ['hashtag1', 'hashtag2', 'hashtag3']" :key="hashtag"
          :label="`Hashtag ${index + 1}`" v-model="post[hashtag]" :maxlength="15"
          :placeholder="`#hashtag${index + 1}`" />
      </div>

      <div v-if="errorMessage" class="rounded-md bg-red-50 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <XCircleIcon class="h-5 w-5 text-red-400" aria-hidden="true" />
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-red-800">Error</h3>
            <div class="mt-2 text-sm text-red-700">
              <p>{{ errorMessage }}</p>
            </div>
          </div>
        </div>
      </div>

      <div>
        <button type="submit"
          class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Submit Post
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const router = useRouter()
const store = useCounterStore()

const submitPost = async () => {
  try {
    const response = await fetch('http://localhost:8000/articles/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${store.token}`
      },
      body: JSON.stringify(post.value),
    });

    if (!response.ok) {
      throw new Error('Failed to create post');
    }

    post.value = { title: '', content: '', hashtag1: '', hashtag2: '', hashtag3: '' };
    alert('Post created successfully!');
    router.push('/community') // 커뮤니티 페이지로 이동
  } catch (error) {
    errorMessage.value = error.message;
  }
};
</script>