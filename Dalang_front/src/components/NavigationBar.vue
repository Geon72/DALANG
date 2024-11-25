<template>
  <nav class="bg-white">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center py-4">
        <div class="flex items-center">
          <a href="/" class="flex items-center no-hover-effect">
            <img :src="DALANG_LOGO" alt="DALANG Logo" class="h-10 w-auto mr-4">
            <span class="text-[#115583] font-bold text-3xl">DALANG</span>
          </a>
        </div>
        <div class="hidden lg:flex space-x-4 items-center">
          <a v-for="item in navItems.slice(1)" :key="item.name" :href="item.route"
            class="text-[#4A524D] hover:text-[#44AAE2] transition-colors font-bold text-xl pt-2">
            {{ item.name }}
          </a>
        </div>
        <div class="flex items-center space-x-4 pt-2">
          <div class="relative">
            <button @mouseenter="showSearch = true" @mouseleave="hideSearchIfNotFocused"
              class="text-[#4A524D] hover:text-[#44AAE2] focus:outline-none">
              <SearchIcon />
            </button>
            <div v-show="showSearch" @mouseenter="showSearch = true" @mouseleave="hideSearchIfNotFocused"
              class="absolute right-0 mt-2 w-64 bg-white rounded-md shadow-lg py-1 z-10">
              <input ref="searchInput" type="text" placeholder="검색어를 입력하세요"
                class="w-full p-2 border-b focus:outline-none focus:border-[#44AAE2]" @focus="showSearch = true"
                @blur="hideSearchIfNotFocused">
            </div>
          </div>
          <!-- 프로필 메뉴는 로그인 상태일 때만 표시 -->
          <div v-if="store.isLogin" class="relative">
            <button @click="toggleProfileMenu" class="profile-button text-[#4A524D] hover:text-[#44AAE2]">
              <UserIcon />
            </button>
            <div v-if="isProfileMenuOpen"
              class="profile-menu absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-10">
              <router-link :to="{ name: 'profile', params: { id: store.userId } }"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                내 프로필
              </router-link>
              <a href="/user/edit" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">설정</a>
            </div>
          </div>
          <!-- 로그인/회원가입 또는 로그아웃 버튼 -->
          <div v-if="!store.isLogin" class="flex space-x-2">
            <button @click="openLoginWindow" class="text-[#4A524D] hover:text-[#44AAE2] font-bold">
              로그인
            </button>
            <button @click="openRegisterWindow" class="text-[#4A524D] hover:text-[#44AAE2] font-bold">
              회원가입
            </button>
          </div>
          <!-- 로그아웃 버튼 -->
          <button v-else @click="handleLogout" class="text-[#4A524D] hover:text-[#44AAE2] font-bold">
            로그아웃
          </button>
          <button @click="toggleMenu" class="lg:hidden">
            <MenuIcon class="text-[#115583]" />
          </button>
        </div>
      </div>
    </div>
  </nav>

  <!-- Mobile menu -->
  <div v-if="isMenuOpen" class="lg:hidden bg-white shadow-md">
    <div class="container mx-auto px-4 py-2">
      <a v-for="item in navItems.slice(1)" :key="item.name" :href="item.route"
        class="block py-2 text-[#4A524D] hover:text-[#44AAE2] transition-colors font-bold">
        {{ item.name }}
      </a>
    </div>
  </div>
</template>

<script setup>
// Vue와 Pinia 가져오기
import { ref, onMounted, onUnmounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { SearchIcon, UserIcon, MenuIcon } from 'lucide-vue-next'
import DALANG_LOGO from '@/assets/DALANG_LOGO.png'

const store = useCounterStore() // Pinia 스토어 사용!!
const showSearch = ref(false)
const searchInput = ref(null)
const isMenuOpen = ref(false)
const isProfileMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const toggleProfileMenu = (event) => {
  event.stopPropagation()
  isProfileMenuOpen.value = !isProfileMenuOpen.value
}

const closeProfileMenu = () => {
  isProfileMenuOpen.value = false
}

const hideSearchIfNotFocused = () => {
  setTimeout(() => {
    if (document.activeElement !== searchInput.value) {
      showSearch.value = false
    }
  }, 200)
}

const navItems = [
  { name: '홈', route: '/' },
  { name: '예/적금 추천', route: '/recommendation' },
  { name: '근처 은행', route: '/find-bank' },
  { name: '환율 계산기', route: '/currency-exchange' },
  { name: '커뮤니티', route: '/community' },
]

// 로그인 창 열기 함수
const openLoginWindow = () => {
  const loginWindow = window.open('/login', 'LoginWindow', 'width=500,height=800')
}

// 회원가입 창 열기 함수
const openRegisterWindow = () => {
  const registerWindow = window.open('/register', 'RegisterWindow', 'width=500,height=800')
}

// 로그아웃 처리 함수
const handleLogout = () => {
  store.logOut() // Pinia의 token 값을 null로 설정!!
}
</script>

<style scoped>
.no-hover-effect {
  @apply hover:bg-transparent;
}
</style>