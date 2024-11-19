<template>
  <div class="min-h-screen bg-white">
    <!-- Header Navigation -->
    <header class="sticky top-0 bg-white border-b z-10">
      <nav class="max-w-screen-xl mx-auto px-4">
        <div class="flex items-center justify-between h-14">
      
          <div class="flex space-x-6">
            <button v-for="tab in tabs" :key="tab.id" @click="switchTab(tab.id)"
              class="relative py-4 px-2 text-[#4A524D] hover:text-[#44AAE2] transition-colors"
              :class="{ 'text-[#44AAE2]': currentTab === tab.id }">
              {{ tab.name }}
              <div class="absolute bottom-0 left-0 w-full h-0.5 bg-[#44AAE2] transition-transform duration-200"
                :class="currentTab === tab.id ? 'scale-x-100' : 'scale-x-0'"></div>
            </button>
          </div>
        </div>
      </nav>
    </header>

    <!-- Main Content -->
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

      <!-- Feed Empty State 부분을 수정 -->
      <div v-else-if="currentTab === 'feed' && (!isLoggedIn || !hasFollowers)"
        class="flex flex-col items-center justify-center py-20">
        <div class="relative w-full max-w-md mb-12">
          <!-- Empty Feed Illustration -->
          <div class="flex flex-col items-center space-y-8">
            <h2 class="text-2xl font-bold text-gray-900">
              새로운 피드가 없네요.
            </h2>
            <button class="px-6 py-3 bg-[#44AAE2] text-white rounded-md hover:bg-[#115583] transition-colors">
              인기 작가 둘러보기
            </button>
          </div>
        </div>
      </div>

      <!-- Posts Grid -->
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-5">
        <article v-for="post in displayedPosts" :key="post.id"
          class="bg-white rounded-lg overflow-hidden border border-[#F5F5F5] hover:shadow-lg transition-shadow duration-200">
          <!-- Featured Image -->
          <div class="aspect-video overflow-hidden">
            <img :src="post.image" :alt="post.title"
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
              {{ post.preview }}
            </p>

            <!-- Meta -->
            <div class="flex items-center justify-between mb-4">
              <div class="flex items-center gap-2">
                <img :src="post.author.avatar" :alt="post.author.name" class="w-6 h-6 rounded-full" />
                <span class="text-xs text-[#4A524D]">{{ post.author.name }}</span>
              </div>
              <span class="text-xs text-gray-500">{{ formatDate(post.date) }}</span>
            </div>

            <!-- Engagement -->
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <button class="flex items-center gap-1 text-sm text-gray-500 hover:text-[#44AAE2] transition-colors"
                  @click="toggleLike(post.id)">
                  <Heart :class="{ 'fill-[#44AAE2] text-[#44AAE2]': post.isLiked }" class="w-4 h-4" />
                  <span>{{ post.likes }}</span>
                </button>
                <div class="flex items-center gap-1 text-sm text-gray-500">
                  <MessageCircle class="w-4 h-4" />
                  <span>{{ post.comments }}</span>
                </div>
              </div>
            </div>

            <!-- Tags -->
            <div class="flex flex-wrap gap-2 mt-3">
              <span v-for="tag in post.tags" :key="tag"
                class="text-xs text-[#44AAE2] hover:text-[#115583] transition-colors">
                #{{ tag }}
              </span>
            </div>
          </div>
        </article>
        <!-- Load More Button -->

        <!-- Posts Grid 부분의 더보기 버튼을 중앙 정렬로 수정 -->
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
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { Heart, MessageCircle, PenSquare, Check } from 'lucide-vue-next'

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

const fetchPosts = async () => {
  loading.value = true
  await new Promise(resolve => setTimeout(resolve, 1000))
  posts.value = generateDummyPosts(expandedPostCount)
  sortPosts()
  displayedPosts.value = posts.value.slice(0, initialPostCount)
  isExpanded.value = false
  loading.value = false
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
  loading.value = true

  try {
    posts.value = generateDummyPosts(20, tabId)
    sortPosts()
    displayedPosts.value = posts.value.slice(0, postsPerPage)
  } catch (error) {
    console.error('Failed to fetch posts:', error)
  } finally {
    loading.value = false
  }
}

const loadMorePosts = () => {
  if (isExpanded.value) {
    // 줄이기
    displayedPosts.value = posts.value.slice(0, initialPostCount)
    isExpanded.value = false
  } else {
    // 더보기
    displayedPosts.value = posts.value.slice(0, expandedPostCount)
    isExpanded.value = true
  }
}


const toggleLike = (postId) => {
  const post = posts.value.find(p => p.id === postId)
  if (post) {
    post.isLiked = !post.isLiked
    post.likes += post.isLiked ? 1 : -1
  }
}

const formatDate = (date) => {
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date)
}

onMounted(() => {
  fetchPosts()
})

watch(currentTab, () => {
  fetchPosts()
})
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