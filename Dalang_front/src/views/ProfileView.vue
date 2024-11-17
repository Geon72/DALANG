<template>
  <div class="flex-grow bg-white">
    <NavigationBar :navItems="navItems" />
    <div class="max-w-5xl mx-auto px-4 py-8">
      <ProfileHeader :user="user" />
      <ProfilePostGrid :posts="user.posts" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProfileHeader from '@/components/ProfileHeader.vue'
import ProfilePostGrid from '@/components/ProfilePostGrid.vue'
import NavigationBar from '@/components/NavigationBar.vue'

const user = ref({
  username: 'DALANG_user',
  fullName: 'DALANG_user',
  profilePicture: '/placeholder.svg?height=160&width=160',
  bio: 'Welcome to my DALANG profile! 📸✨ Sharing moments and memories.',
  followers: 1234,
  following: 567,
  posts: [
    { id: 1, image: 'https://placeholders.dev/?width=300&height=300&text=Post1' },
    { id: 2, image: 'https://placeholders.dev/?width=300&height=300&text=Post2' },
    { id: 3, image: 'https://placeholders.dev/?width=300&height=300&text=Post3' },
    { id: 4, image: 'https://placeholders.dev/?width=300&height=300&text=Post4' },
    { id: 5, image: 'https://placeholders.dev/?width=300&height=300&text=Post5' },
    { id: 6, image: 'https://placeholders.dev/?width=300&height=300&text=Post6' },
    { id: 7, image: 'https://placeholders.dev/?width=300&height=300&text=Post7' },
    { id: 8, image: 'https://placeholders.dev/?width=300&height=300&text=Post8' },
    { id: 9, image: 'https://placeholders.dev/?width=300&height=300&text=Post9' },
  ]
})

const navItems = [
  { name: '홈', route: '/' },
  { name: '예/적금 추천', route: '/recommendations' },
  { name: '근처 은행', route: '/find-bank' },
  { name: '환율 계산기', route: '/currency-calculator' },
  { name: '커뮤니티', route: '/community' },
]
</script>