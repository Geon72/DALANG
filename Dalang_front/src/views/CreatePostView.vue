<template>
  <div class="min-h-screen bg-gray-50">
      <NavigationBar />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold mb-4 bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent">
          Write a Post
        </h1>
        <p class="text-xl text-gray-600 mb-8">
          Share your thoughts with the community
        </p>
      </div>

      <div class="bg-white rounded-xl shadow-lg p-8 border border-gray-100">
        <form @submit.prevent="submitPost">
          <div class="space-y-6">
            <div>
              <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
              <input
                type="text"
                name="title"
                id="title"
                v-model="post.title"
                maxlength="100"
                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                placeholder="Enter your post title"
                required
              />
            </div>

            <div>
              <label for="content" class="block text-sm font-medium text-gray-700">Content</label>
              <div class="mt-1">
                <textarea
                  id="content"
                  name="content"
                  rows="5"
                  v-model="post.content"
                  class="block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  placeholder="Write your post content here"
                  required
                ></textarea>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-4 sm:grid-cols-3">
              <div v-for="(hashtag, index) in ['hashtag1', 'hashtag2', 'hashtag3']" :key="hashtag">
                <label :for="hashtag" class="block text-sm font-medium text-gray-700">Hashtag {{ index + 1 }}</label>
                <input
                  type="text"
                  :name="hashtag"
                  :id="hashtag"
                  v-model="post[hashtag]"
                  maxlength="15"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  :placeholder="`#hashtag${index + 1}`"
                />
              </div>
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
              <button
                type="submit"
                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Submit Post
              </button>
            </div>
          </div>
        </form>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted} from 'vue';
import { XCircleIcon } from 'lucide-vue-next';
import NavigationBar from '@/components/NavigationBar.vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router' // router import 추가

const router = useRouter() // router 정의
const post = ref({
  title: '',
  content: '',
  hashtag1: '',
  hashtag2: '',
  hashtag3: '',
});

const errorMessage = ref('');

const store = useCounterStore();
const token = store.token

const submitPost = async () => {
  try {
    if (!token) {
      throw new Error('Authentication required');
    }

    const response = await fetch('http://localhost:8000/articles/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      },
      body: JSON.stringify(post.value),
    });

    if (!response.ok) {
      if (response.status === 401) {
        throw new Error('Authentication failed. Please log in again.');
      }
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

<style scoped>
.rounded-xl {
  border-radius: 1rem;
}

.shadow-lg {
  box-shadow: 0 10px 15px -3px rgba(17, 85, 131, 0.1),
    0 4px 6px -2px rgba(17, 85, 131, 0.05);
}

/* Hover effects */
.bg-white {
  transition: transform 0.3s ease;
}

.bg-white:hover {
  transform: translateY(-2px);
}

/* Glass morphism effect */
.bg-white {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .p-8 {
    padding: 1.5rem;
  }

  .text-5xl {
    font-size: 2.5rem;
  }

  .text-xl {
    font-size: 1.125rem;
  }
}
</style>