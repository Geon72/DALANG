<template>
  <nav class="bg-white">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center py-4">
        <div class="flex items-center">
          <a href="/" class="flex items-center no-hover-effect">
            <img src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/DALANG_FINAL-zgVATAcLguH8yROQhqFJRCjh3gdKx4.png" alt="DALANG Logo" class="h-10 w-auto mr-4">
            <span class="text-[#115583] font-bold text-xl">DALANG</span>
          </a>
        </div>
        <div class="hidden lg:flex space-x-4 items-center">
          <a v-for="item in navItems.slice(1)" :key="item.name" @click.prevent="handleNavClick(item.route)" href="#" class="text-[#4A524D] hover:text-[#44AAE2] transition-colors font-bold">
            {{ item.name }}
          </a>
        </div>
        <div class="flex items-center space-x-4">
          <div class="relative">
            <button @mouseenter="showSearch = true" @mouseleave="hideSearchIfNotFocused" class="text-[#4A524D] hover:text-[#44AAE2] focus:outline-none">
              <SearchIcon />
            </button>
            <div v-show="showSearch" 
                 @mouseenter="showSearch = true" 
                 @mouseleave="hideSearchIfNotFocused"
                 class="absolute right-0 mt-2 w-64 bg-white rounded-md shadow-lg py-1 z-10">
              <input ref="searchInput" 
                     type="text" 
                     placeholder="검색어를 입력하세요" 
                     class="w-full p-2 border-b focus:outline-none focus:border-[#44AAE2]"
                     @focus="showSearch = true"
                     @blur="hideSearchIfNotFocused">
            </div>
          </div>
          <div class="relative">
            <button @click="toggleProfileMenu" class="profile-button text-[#4A524D] hover:text-[#44AAE2]">
              <UserIcon />
            </button>
            <div v-if="isProfileMenuOpen" class="profile-menu absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-10">
              <a href="#" @click.prevent="handleProfileItemClick('profile')" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">내 프로필</a>
              <a href="#" @click.prevent="handleProfileItemClick('settings')" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">설정</a>
            </div>
          </div>
          <button @click="handleAuthClick" class="text-[#4A524D] hover:text-[#44AAE2]">
            {{ isLoggedIn ? '로그아웃' : '로그인' }}
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
      <a v-for="item in navItems.slice(1)" :key="item.name" @click.prevent="handleNavClick(item.route)" href="#" class="block py-2 text-[#4A524D] hover:text-[#44AAE2] transition-colors font-bold">
        {{ item.name }}
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { SearchIcon, UserIcon, MenuIcon } from 'lucide-vue-next'

const isMenuOpen = ref(false)
const isProfileMenuOpen = ref(false)
const isLoggedIn = ref(false)
const showSearch = ref(false)
const searchInput = ref(null)

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
  { name: '예/적금 추천', route: '/recommendations' },
  { name: '근처 은행', route: '/find-bank' },
  { name: '환율 계산기', route: '/currency-calculator' },
  { name: '커뮤니티', route: '/community' },
]

const openLoginWindow = () => {
  const loginWindow = window.open('/login', 'LoginWindow', 'width=500,height=800')
  
  const checkWindowClosed = setInterval(() => {
    if (loginWindow.closed) {
      clearInterval(checkWindowClosed)
      checkLoginStatus()
    }
  }, 1000)
}

const checkLoginStatus = () => {
  // 여기에 로그인 상태를 확인하는 로직을 구현
  // 예: API 호출을 통해 세션 상태 확인
  // 성공적으로 로그인했다면 isLoggedIn.value = true로 설정
}

const handleNavClick = (route) => {
  if (!isLoggedIn.value) {
    openLoginWindow()
  } else {
    window.location.href = route
  }
}

const handleAuthClick = () => {
  if (isLoggedIn.value) {
    // 로그아웃 로직 구현
    isLoggedIn.value = false
    console.log('Logged out')
  } else {
    openLoginWindow()
  }
}

const handleProfileItemClick = (item) => {
  if (!isLoggedIn.value) {
    openLoginWindow()
  } else {
    switch(item) {
      case 'profile':
        console.log('Navigate to profile page')
        // 프로필 페이지로 이동하는 로직 추가
        break
      case 'settings':
        console.log('Navigate to settings page')
        // 설정 페이지로 이동하는 로직 추가
        break
    }
  }
  closeProfileMenu()
}

const handleOutsideClick = (event) => {
  const profileMenu = document.querySelector('.profile-menu')
  const profileButton = document.querySelector('.profile-button')
  if (isProfileMenuOpen.value && profileMenu && !profileMenu.contains(event.target) && !profileButton.contains(event.target)) {
    closeProfileMenu()
  }
}

onMounted(() => {
  document.addEventListener('click', handleOutsideClick)
})

onUnmounted(() => {
  document.removeEventListener('click', handleOutsideClick)
})
</script>

<style scoped>
.no-hover-effect {
  @apply hover:bg-transparent;
}
</style>