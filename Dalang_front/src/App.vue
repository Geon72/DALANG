<template>
  <div class="app-wrapper">
    <!-- Router View -->
    <router-view />
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

const handleNavClick = (route) => {
  if (!isLoggedIn.value) {
    alert('로그인하세요')
    window.location.href = '/login'
  } else {
    window.location.href = route
  }
}

const handleAuthClick = () => {
  if (isLoggedIn.value) {
    isLoggedIn.value = false
    console.log('Logged out')
  } else {
    window.location.href = '/login'
  }
}

const handleProfileItemClick = (item) => {
  if (!isLoggedIn.value) {
    alert('로그인하세요')
    window.location.href = '/login'
  } else {
    switch (item) {
      case 'profile':
        console.log('Navigate to profile page')
        break
      case 'settings':
        console.log('Navigate to settings page')
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

<style>
/* 전역 스타일 */
:root {
  --primary-color: #115583;
  --secondary-color: #44AAE2;
  --text-primary: #4A524D;
  --text-secondary: #92B3B5;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  width: 100%;
  min-height: 100vh;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-primary);
  background-color: #f8f9fa;
  line-height: 1.5;
}

.app-wrapper {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
}

/* 컨테이너 스타일 */
.container {
  width: 100%;
  margin: 0 auto;
  padding: 0 1rem;
}

/* 반응형 컨테이너 */
@media (min-width: 640px) {
  .container {
    max-width: 640px;
    padding: 0 1.5rem;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
    padding: 0 2rem;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
    padding: 0 2rem;
  }
}

@media (min-width: 1280px) {
  .container {
    width: 1024px;
    padding: 0 2rem;
    margin: 0 auto;
  }
}

.no-hover-effect {
  @apply hover:bg-transparent;
}
</style>