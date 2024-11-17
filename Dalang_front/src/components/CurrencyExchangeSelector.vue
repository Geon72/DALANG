<template>
    <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
      <div class="space-y-6">
        <!-- Buy/Sell Selection -->
        <div class="flex gap-4">
          <label class="flex items-center space-x-2">
            <input type="radio" v-model="transactionType" value="buy" class="text-[#0066CC]">
            <span>외화사실때</span>
          </label>
          <label class="flex items-center space-x-2">
            <input type="radio" v-model="transactionType" value="sell" class="text-[#0066CC]">
            <span>외화파실때</span>
          </label>
        </div>
  
        <!-- Currency List -->
        <div class="space-y-2">
          <div
            v-for="currency in currencies"
            :key="currency.code"
            class="p-3 rounded-lg cursor-pointer hover:bg-gray-50 flex items-center justify-between"
            :class="{ 'bg-blue-50': selectedCurrency === currency.code }"
            @click="selectCurrency(currency.code)"
          >
            <div class="flex items-center space-x-3">
              <span class="text-2xl">{{ currency.flag }}</span>
              <span class="font-medium">{{ currency.name }}</span>
            </div>
            <span class="text-[#0066CC] font-medium">{{ currency.code }}</span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const props = defineProps(['selectedCurrency'])
  const emit = defineEmits(['update:currency'])
  
  const transactionType = ref('buy')
  
  const currencies = [
    { code: 'USD', name: '미국 달러', flag: '🇺🇸' },
    { code: 'JPY', name: '일본 엔화', flag: '🇯🇵' },
    { code: 'EUR', name: '유럽 유로', flag: '🇪🇺' },
    { code: 'AUD', name: '호주 달러', flag: '🇦🇺' },
    { code: 'BHD', name: '바레인 디나르', flag: '🇧🇭' },
    { code: 'CAD', name: '캐나다 달러', flag: '🇨🇦' },
    { code: 'CHF', name: '스위스 프랑', flag: '🇨🇭' },
    { code: 'CNY', name: '중국 위안화', flag: '🇨🇳' },
  ]
  
  const selectCurrency = (code) => {
    emit('update:currency', code)
  }
  </script>