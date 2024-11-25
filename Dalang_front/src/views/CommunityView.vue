<template>
  <div class="min-h-screen bg-gray-50">
    <NavigationBar />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- 상단 탭 네비게이션 -->
      <div class="mb-6">
        <h2 class="text-3xl font-bold mb-4">커뮤니티</h2>
        <div class="border-b border-gray-200">
          <nav class="-mb-px flex space-x-8">
            <a v-for="tab in tabs" :key="tab.id" @click.prevent="switchTab(tab.id)" :class="[
              currentTab === tab.id
                ? 'border-[#0088CC] text-[#0088CC]'
                : 'border-transparent text-gray-500 hover:text-[#0088CC] hover:border-[#0088CC]',
              'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm transition-colors duration-200 ease-in-out cursor-pointer'
            ]">
              {{ tab.name }}
            </a>
          </nav>
        </div>
      </div>
      <main class="max-w-screen-xl mx-auto px-4 py-8">
        <!-- Loading State -->
        <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-5">
          <div v-for="n in 10" :key="n" class="animate-pulse">
            <div class="bg-gray-200 aspect-video rounded-lg mb-4"></div>
            <div class="space-y-3">
              <div class="h-6 bg-gray-200 rounded w-3/4"></div>
              <div class="h-4 bg-gray-200 rounded"></div>
              <div class="h-4 bg-gray-200 rounded w-5/6"></div>
            </div>
          </div>
        </div>

        <!-- Feed Empty State -->
        <div v-else-if="currentTab === 'feed' && (!isLoggedIn || !hasFollowers)"
          class="flex flex-col items-center justify-center py-20">
          <div class="relative w-full max-w-md mb-12">
            <div class="flex flex-col items-center space-y-8">
              <h2 class="text-2xl font-bold text-gray-900">
                새로운 피드가 없네요.
              </h2>
              <button @click="switchToTrending"
                class="px-6 py-3 bg-[#44AAE2] text-white rounded-md hover:bg-[#115583] transition-colors">
                인기 작가 둘러보기
              </button>
            </div>
          </div>
        </div>

        <!-- Posts Grid -->
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-5">
          <CommunityPostCard v-for="post in displayedPosts" :key="post.id" :post="post" @toggle-like="toggleLike" />

          <!-- Load More Button -->
          <div v-if="hasMorePosts" class="col-span-full flex justify-center mt-8">
            <button @click="loadMorePosts"
              class="px-6 py-2 bg-[#44AAE2] text-white rounded-md hover:bg-[#115583] transition-colors">
              {{ isExpanded ? '줄이기' : '더보기' }}
            </button>
          </div>
        </div>
      </main>

      <!-- Write Post Button -->
      <button
        class="fixed bottom-6 right-6 bg-[#44AAE2] text-white rounded-full p-4 shadow-lg hover:bg-[#115583] transition-colors"
        aria-label="글쓰기">
        <PenSquare class="w-6 h-6" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { PenSquare } from 'lucide-vue-next'
import CommunityPostCard from '@/components/CommunityPostCard.vue'
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter' // 스토어 import

const store = useCounterStore()
const currentTab = ref('trending')
const loading = ref(true)
const posts = ref([])
const displayedPosts = ref([])
const postsPerPage = 10
const currentPage = ref(1)
const isLoggedIn = ref(false) // Simulate authentication state
const hasFollowers = ref(false) // Simulate follower state
const isExpanded = ref(false)
const initialPostCount = 10
const expandedPostCount = 20
const switchToTrending = () => {
  switchTab('trending')
}

const tabs = [
  { id: 'trending', name: '트렌딩' },
  { id: 'recent', name: '최신' },
  { id: 'feed', name: '피드' }
]

const hasMorePosts = computed(() => {
  return !isExpanded.value && posts.value.length > displayedPosts.value.length
})

const generateDummyPosts = (count, type) => {
  const topics = ['Vue.js', 'React', 'Angular', 'Svelte', 'Node.js']
  const tags = ['Frontend', 'Backend', 'DevOps', 'UI/UX', 'Testing']

  return Array(count).fill().map((_, i) => ({
    id: i + 1,
    title: `${topics[i % topics.length]}로 웹 애플리케이션 만들기 ${i + 1}`,
    preview: `${topics[i % topics.length]}를 사용하여 현대적인 웹 애플리케이션을 구축하는 방법을 상세히 알아봅니다. 컴포넌트 설계부터 상태관리, 성능 최적화까지 다룹니다.`,
    image: `https://picsum.photos/seed/${type}${i}/600/400`,
    author: {
      name: `개발자${i + 1}`,
      avatar: `https://picsum.photos/seed/author${i}/100/100`
    },
    date: new Date(Date.now() - Math.floor(Math.random() * 10000000000)),
    likes: type === 'trending' ? 50 + Math.floor(Math.random() * 950) : Math.floor(Math.random() * 100),
    comments: type === 'trending' ? 10 + Math.floor(Math.random() * 90) : Math.floor(Math.random() * 20),
    tags: tags.sort(() => 0.5 - Math.random()).slice(0, 3),
    isLiked: false
  }))
}

const fetchPosts = async (tabId) => {
  loading.value = true
  try {
    let endpoint = 'http://localhost:8000/articles/'
    if (tabId === 'trending') {
      endpoint += 'trending/'
    } else if (tabId === 'recent') {
      endpoint += 'recent/'
    } else if (tabId === 'feed') {
      endpoint += 'feed/'
    }
    const response = await axios.get(endpoint, {
      headers: {
        'Authorization': `Token ${store.token}`
      }
    })
    console.log('Fetched posts:', response.data) // 데이터 로깅
    posts.value = response.data
    displayedPosts.value = posts.value.slice(0, initialPostCount)
    isExpanded.value = false
  } catch (error) {
    console.error('Failed to fetch posts:', error)
  } finally {
    loading.value = false
  }
}


const sortPosts = () => {
  if (currentTab.value === 'trending') {
    posts.value.sort((a, b) => (b.likes + b.comments) - (a.likes + a.comments))
  } else if (currentTab.value === 'recent') {
    posts.value.sort((a, b) => b.date - a.date)
  }
  // For 'feed' tab, we assume the posts are already filtered for followed authors
}

const switchTab = async (tabId) => {
  currentTab.value = tabId
  currentPage.value = 1
  await fetchPosts(tabId)
}

onMounted(() => {
  fetchPosts(currentTab.value)
})
const loadMorePosts = () => {
  if (isExpanded.value) {
    // 줄이기
    displayedPosts.value = posts.value.slice(0, initialPostCount)
    isExpanded.value = false
  } else {switchTab 
    // 더보기
    displayedPosts.value = posts.value.slice(0, expandedPostCount)
    isExpanded.value = true
  }
}

const toggleLike = async (postId) => {
  try {
    const response = await axios.post(`/api/articles/${postId}/like/`)
    const updatedPost = response.data
    const index = posts.value.findIndex(p => p.id === postId)
    if (index !== -1) {
      posts.value[index] = updatedPost
    }
  } catch (error) {
    console.error('Failed to toggle like:', error)
  }
}


</script>

<style scoped>
.grid {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(1, 1fr);
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (min-width: 1280px) {
  .grid {
    grid-template-columns: repeat(5, 1fr);
  }
}
</style>