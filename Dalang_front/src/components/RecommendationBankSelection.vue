<template>
    <div class="mb-8">
      <h3 class="text-lg font-semibold text-gray-700 mb-3">은행 선택</h3>
      <div class="space-y-4">
        <label class="inline-flex items-center select-all-checkbox">
          <input 
            type="checkbox" 
            v-model="selectAll" 
            @change="toggleAllBanks" 
            class="form-checkbox h-5 w-5 text-[#0088CC] rounded-sm border-2 border-[#0088CC] focus:ring-[#0088CC] transition duration-300 ease-in-out"
          >
          <span class="ml-2 text-lg font-medium text-gray-700">전체</span>
        </label>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
          <label v-for="bank in banks" :key="bank" class="inline-flex items-center">
            <input 
              type="checkbox" 
              v-model="selectedBanks" 
              :value="bank" 
              @change="updateSelectAllState"
              class="form-checkbox h-5 w-5 text-[#0088CC] rounded-sm border-2 border-[#0088CC] focus:ring-[#0088CC] transition duration-300 ease-in-out"
            >
            <span class="ml-2 text-sm text-gray-600">{{ bank }}</span>
          </label>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  
  const props = defineProps({
    banks: {
      type: Array,
      required: true
    }
  })
  
  const emit = defineEmits(['update:selectedBanks'])
  
  const selectAll = ref(false)
  const selectedBanks = ref([])
  
  const toggleAllBanks = () => {
    if (selectAll.value) {
      selectedBanks.value = [...props.banks]
    } else {
      selectedBanks.value = []
    }
    emit('update:selectedBanks', selectedBanks.value)
  }
  
  const updateSelectAllState = () => {
    selectAll.value = selectedBanks.value.length === props.banks.length
    emit('update:selectedBanks', selectedBanks.value)
  }
  
  watch(selectedBanks, updateSelectAllState)
  </script>