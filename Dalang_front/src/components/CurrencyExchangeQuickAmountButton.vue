<template>
    <div class="flex gap-2">
      <button
        v-for="amount in quickAmounts"
        :key="amount"
        @click="$emit('select', amount)"
        class="flex-1 border border-gray-300 rounded-md py-2 hover:bg-gray-50 transition-colors"
      >
        {{ amount }}
      </button>
    </div>
  </template>
  
  <script setup>
  const quickAmounts = [10, 100, 500, 1000]
  
  defineEmits(['select'])
  </script>