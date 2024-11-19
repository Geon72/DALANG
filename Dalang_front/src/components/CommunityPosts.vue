<template>
    <div class="min-h-screen bg-[#F5F5F5]">
      <!-- Mobile Menu Overlay -->
      <div v-if="isMobileMenuOpen" class="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden">
        <div class="bg-white w-64 h-full">
          <div class="p-4 flex justify-between items-center border-b">
            <h2 class="font-bold">카테고리</h2>
            <button @click="isMobileMenuOpen = false" class="p-2 rounded-md hover:bg-gray-100">
              <X class="h-5 w-5" />
            </button>
          </div>
          <nav class="p-4">
            <a
              v-for="category in categories"
              :key="category"
              href="#"
              class="block py-2 text-[#4A524D] hover:text-[#44AAE2]"
            >
              {{ category }}
            </a>
          </nav>
        </div>
      </div>
  
      <!-- Main Layout -->
      <div class="max-w-7xl mx-auto bg-white shadow-lg">
        <!-- Header -->
        <header class="border-b">
          <div class="p-4 flex items-center justify-between">
            <div class="flex items-center gap-4">
              <button 
                @click="isMobileMenuOpen = true"
                class="md:hidden p-2 rounded-md hover:bg-gray-100"
              >
                <Menu class="h-5 w-5" />
              </button>
              <h1 class="text-xl font-bold text-[#115583]">동네생활</h1>
            </div>
            <div class="flex items-center gap-2">
              <button class="hidden md:flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-md hover:bg-gray-100">
                <MapPin class="h-4 w-4" />
                서울특별시 광진구
              </button>
              <button class="px-4 py-2 bg-[#44AAE2] text-white rounded-md hover:bg-[#115583]">
                글쓰기
              </button>
            </div>
          </div>
          <div class="px-4 pb-4">
            <div class="relative">
              <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
              <input 
                type="search"
                placeholder="동네생활 검색"
                class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#44AAE2]"
              />
            </div>
          </div>
        </header>
  
        <!-- Main Content -->
        <div class="flex">
          <!-- Sidebar -->
          <aside class="hidden md:block w-64 p-6 border-r">
            <nav class="space-y-2">
              <a
                v-for="category in categories"
                :key="category"
                href="#"
                class="block py-2 text-[#4A524D] hover:text-[#44AAE2] transition-colors"
              >
                {{ category }}
              </a>
            </nav>
          </aside>
  
          <!-- Post List -->
          <main class="flex-1 p-6">
            <div class="flex justify-between items-center mb-4">
              <div class="flex space-x-2">
                <button 
                  v-for="tab in tabs" 
                  :key="tab.value"
                  @click="currentTab = tab.value"
                  :class="[
                    'px-3 py-2 rounded-md text-sm font-medium',
                    currentTab === tab.value 
                      ? 'bg-[#44AAE2] text-white' 
                      : 'text-[#4A524D] hover:bg-gray-100'
                  ]"
                >
                  {{ tab.label }}
                </button>
              </div>
              <button class="flex items-center text-[#4A524D] hover:text-[#44AAE2]">
                <Filter class="h-4 w-4 mr-2" />
                필터
              </button>
            </div>
            
            <div v-if="currentTab === 'all'" class="space-y-6">
              <article 
                v-for="post in posts" 
                :key="post.id"
                class="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow"
              >
                <div class="flex gap-4">
                  <img
                    v-if="post.image"
                    :src="post.image"
                    :alt="`${post.title} 이미지`"
                    class="w-24 h-24 rounded-lg object-cover flex-shrink-0"
                  />
                  <div class="flex-1">
                    <h2 class="text-lg font-bold mb-2 text-[#115583]">
                      {{ post.title }}
                    </h2>
                    <p class="text-[#4A524D] mb-2 line-clamp-2">
                      {{ post.content }}
                    </p>
                    <div class="flex items-center gap-2 text-sm text-gray-500">
                      <span class="bg-[#F0F0F0] px-2 py-1 rounded-full text-xs">
                        {{ post.category }}
                      </span>
                      <span>{{ post.author }}</span>
                      <span>•</span>
                      <span>{{ post.time }}</span>
                    </div>
                    <div class="flex items-center gap-4 mt-2">
                      <button class="flex items-center gap-1 text-gray-500 hover:text-[#44AAE2]">
                        <Heart class="h-4 w-4" />
                        <span>{{ post.likes }}</span>
                      </button>
                      <button class="flex items-center gap-1 text-gray-500 hover:text-[#44AAE2]">
                        <MessageCircle class="h-4 w-4" />
                        <span>{{ post.comments }}</span>
                      </button>
                    </div>
                  </div>
                </div>
              </article>
            </div>
            
            <div v-else-if="currentTab === 'popular'">
              <p>인기 게시물이 여기에 표시됩니다.</p>
            </div>
            
            <div v-else-if="currentTab === 'nearby'">
              <p>내 근처 게시물이 여기에 표시됩니다.</p>
            </div>
          </main>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { Menu, Search, Heart, MessageCircle, ChevronRight, X, Filter, MapPin } from 'lucide-vue-next'
  
  const isMobileMenuOpen = ref(false)
  const currentTab = ref('all')
  
  const categories = [
    '전체', '맛집', '반려동물', '운동', '생활/편의', '분실/실종', 
    '법원/약국', '고민/사연', '동네친구', '이사/시공', '주거/부동산', 
    '교육', '취미', '동네사건사고'
  ]
  
  const tabs = [
    { label: '전체', value: 'all' },
    { label: '인기', value: 'popular' },
    { label: '내 근처', value: 'nearby' },
  ]
  
  const posts = [
    {
      id: 1,
      title: '동네 맛집 추천 부탁드려요!',
      content: '이사 온 지 얼마 안 돼서 동네 맛집을 잘 모르겠어요. 추천 부탁드립니다!',
      category: '맛집',
      author: '새내기주민',
      time: '10분 전',
      likes: 5,
      comments: 3,
      image: '/placeholder.svg?height=100&width=100'
    },
    {
      id: 2,
      title: '강아지 산책 친구 구해요',
      content: '주말마다 강아지 산책하실 분 계신가요? 같이 산책하면 좋을 것 같아요.',
      category: '반려동물',
      author: '멍멍이맘',
      time: '1시간 전',
      likes: 10,
      comments: 7,
    },
    {
      id: 3,
      title: '헬스장 추천해주세요',
      content: '동네에 괜찮은 헬스장 있나요? 가격대와 시설 정보 알려주시면 감사하겠습니다.',
      category: '운동',
      author: '운동초보',
      time: '3시간 전',
      likes: 2,
      comments: 8,
      image: '/placeholder.svg?height=100&width=100'
    },
  ]
  </script>
  
  <style scoped>
  /* Add any additional styles here if needed */
  </style>