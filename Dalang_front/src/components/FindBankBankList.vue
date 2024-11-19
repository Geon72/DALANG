<template>
    <div class="bank-list bg-white rounded-lg shadow-md p-4">
      <h2 class="text-xl font-bold mb-4">주변 은행/ATM 목록</h2>
      <div v-if="banks.length > 0" class="space-y-4">
        <div 
          v-for="bank in banks" 
          :key="bank.id"
          class="bank-item p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors duration-200 cursor-pointer"
          @click="$emit('show-on-map', bank)"
        >
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-semibold">{{ bank.name }}</h3>
            <span 
              :class="[
                'px-2 py-1 rounded-full text-sm font-medium',
                bank.type === 'ATM' ? 'bg-red-100 text-red-800' : 'bg-blue-100 text-blue-800'
              ]"
            >
              {{ bank.type }}
            </span>
          </div>
          <div class="mt-2 space-y-1 text-sm text-gray-600">
            <p class="flex items-center gap-1">
              <span class="font-medium">주소:</span> {{ bank.address }}
            </p>
            <p class="flex items-center gap-1">
              <span class="font-medium">거리:</span> {{ bank.distance }}m
            </p>
            <p class="flex items-center gap-1">
              <span class="font-medium">영업시간:</span> {{ bank.hours }}
            </p>
            <p class="flex items-center gap-1">
              <span 
                :class="[
                  'inline-flex items-center px-2 py-1 rounded-full text-xs font-medium',
                  bank.isOpen ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                ]"
              >
                {{ bank.isOpen ? '영업중' : '영업종료' }}
              </span>
            </p>
          </div>
        </div>
      </div>
      <p v-else class="text-center text-gray-500 py-4">
        검색된 은행/ATM이 없습니다.
      </p>
    </div>
  </template>
  
  <script setup>
  defineProps({
    banks: {
      type: Array,
      default: () => []
    }
  })
  
  defineEmits(['show-on-map'])
  </script>
  
  <style scoped>
  .bank-list {
    max-height: 500px;
    overflow-y: auto;
  }
  
  .bank-list::-webkit-scrollbar {
    width: 6px;
  }
  
  .bank-list::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  
  .bank-list::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 3px;
  }
  
  .bank-list::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
  </style>