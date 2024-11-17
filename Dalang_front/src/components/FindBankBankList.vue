<template>
  <div class="space-y-4">
    <div v-for="bank in banks" :key="bank.id" class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow p-6">
      <div class="flex items-start justify-between">
        <div class="flex items-center">
          <div :class="['w-12 h-12 rounded-lg flex items-center justify-center text-white font-bold mr-4', {'bg-[#115583]': bank.name === '국민은행', 'bg-[#44AAE2]': bank.name === '신한은행'}]">
            {{ bank.name.slice(0, 2) }}
          </div>
          <div>
            <h3 class="text-lg font-semibold text-[#115583]">{{ bank.name }} {{ bank.branch }}</h3>
            <p class="text-sm text-gray-500">{{ bank.distance }}m</p>
            <p class="text-sm text-gray-600 mt-1">{{ bank.address }}</p>
            <div class="mt-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
              {{ bank.isOpen ? '영업중' : '영업종료' }} · {{ bank.hours }}
            </div>
          </div>
        </div>
        <button @click="$emit('show-on-map', bank)" class="text-[#44AAE2] hover:text-[#115583] font-medium transition-colors flex items-center">
          <MapPinIcon class="w-5 h-5 mr-1" />
          지도에서 보기
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { MapPinIcon } from 'lucide-vue-next'

defineProps({
  banks: {
    type: Array,
    required: true
  }
})

defineEmits(['show-on-map'])
</script>