<template>
  <div class="min-h-screen bg-gradient-to-b from-blue-50 to-white">
    <NavigationBar :navItems="navItems" />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Header Section -->
      <div class="mb-8">
        <h1 class="text-4xl font-bold bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent">
          내 주변 은행 찾기
        </h1>
        <p class="mt-2 text-gray-600 text-lg">
          현재 위치에서 가까운 은행을 찾아보세요
        </p>
      </div>

      <FindBankSearchForm 
        @search="searchBanks" 
        :selectedBank="selectedBank"
        :selectedRadius="selectedRadius"
        @update:selectedBank="selectedBank = $event"
        @update:selectedRadius="selectedRadius = $event"
      />

      <FindBankMapComponent 
        @get-my-location="getMyLocation"
      />

      <FindBankBankList 
        :banks="banks" 
        @show-on-map="showOnMap"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'

import FindBankSearchForm from '@/components/FindBankSearchForm.vue'
import FindBankMapComponent from '@/components/FindBankMapComponent.vue'
import FindBankBankList from '@/components/FindBankBankList.vue'

const selectedBank = ref('')
const selectedRadius = ref('1')
const banks = ref([
  {
    id: 1,
    name: '국민은행',
    branch: '강남지점',
    distance: 250,
    address: '서울특별시 강남구 테헤란로 152',
    isOpen: true,
    hours: '09:00 - 16:00'
  },
  {
    id: 2,
    name: '신한은행',
    branch: '역삼지점',
    distance: 450,
    address: '서울특별시 강남구 강남대로 390',
    isOpen: true,
    hours: '09:00 - 16:00'
  }
])

const searchBanks = () => {
  console.log('Searching banks:', selectedBank.value, selectedRadius.value)
  // Implement bank search logic here
}

const getMyLocation = () => {
  console.log('Getting current location')
  // Implement geolocation logic here
}

const showOnMap = (bank) => {
  console.log('Showing bank on map:', bank)
  // Implement map centering and marker highlighting logic here
}
</script>