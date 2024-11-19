<template>
  <div class="min-h-screen bg-gray-50">
    <NavigationBar />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 class="text-3xl font-bold mb-2">내 주변 은행 찾기</h1>
      <p class="text-gray-600 mb-6">현재 위치에서 가까운 은행을 찾아보세요</p>

      <FindBankSearchForm v-model:selectedType="selectedType" v-model:selectedRadius="selectedRadius"
        @search="handleSearch" />

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2">
          <FindBankMapComponent ref="mapComponent" :selectedType="selectedType" :selectedRadius="selectedRadius"
            @update:banks="updateBanks" />
        </div>
        <div class="lg:col-span-1">
          <FindBankBankList :banks="banks" @show-on-map="showOnMap" />
        </div>

      </div>
    </main>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'
import FindBankSearchForm from '@/components/FindBankSearchForm.vue'
import FindBankMapComponent from '@/components/FindBankMapComponent.vue'
import FindBankBankList from '@/components/FindBankBankList.vue'

// 상태 관리
const selectedType = ref('ALL')
const selectedRadius = ref('1000')
const banks = ref([])
const mapComponent = ref(null)

// 메서드
const handleSearch = () => {
  if (mapComponent.value) {
    mapComponent.value.findCurrentLocation()
  }
}

const updateBanks = (newBanks) => {
  banks.value = newBanks
}

const showOnMap = (bank) => {
  if (mapComponent.value) {
    mapComponent.value.focusOnBank(bank)
  }
}
</script>