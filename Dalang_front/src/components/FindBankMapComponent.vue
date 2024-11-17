<template>
  <div class="bg-white rounded-xl shadow-lg p-6 mb-8 relative">
    <div class="aspect-w-16 aspect-h-9 bg-gray-200 rounded-lg">
      <!-- This div would be replaced with an actual map component -->
      <div class="flex items-center justify-center text-gray-500">
        Map would be displayed here
      </div>
    </div>
    <button @click="$emit('get-my-location')" class="absolute top-4 right-4 bg-white text-[#115583] border-2 border-[#115583] px-4 py-2 rounded-lg hover:bg-[#115583] hover:text-white transition-colors flex items-center">
      <CrosshairIcon class="w-5 h-5 mr-2" />
      내 위치
    </button>
  </div>
</template>

<script setup>
import { CrosshairIcon } from 'lucide-vue-next'

defineEmits(['get-my-location'])
</script>