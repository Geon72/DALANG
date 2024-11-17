<template>
  <div class="bg-white rounded-xl shadow-lg p-6 mb-8">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="col-span-1">
        <label class="block text-sm font-medium text-gray-700 mb-1">은행 선택</label>
        <select 
          :value="selectedBank"
          @input="$emit('update:selectedBank', $event.target.value)"
          class="w-full border-2 border-gray-200 rounded-lg px-4 py-2 focus:ring-[#44AAE2] focus:border-[#44AAE2] transition-colors"
        >
          <option value="">전체</option>
          <option value="국민은행">국민은행</option>
          <option value="신한은행">신한은행</option>
          <option value="우리은행">우리은행</option>
        </select>
      </div>
      <div class="col-span-1">
        <label class="block text-sm font-medium text-gray-700 mb-1">반경</label>
        <select 
          :value="selectedRadius"
          @input="$emit('update:selectedRadius', $event.target.value)"
          class="w-full border-2 border-gray-200 rounded-lg px-4 py-2 focus:ring-[#44AAE2] focus:border-[#44AAE2] transition-colors"
        >
          <option value="1">1km</option>
          <option value="3">3km</option>
          <option value="5">5km</option>
        </select>
      </div>
      <div class="col-span-1 flex items-end">
        <button @click="$emit('search')" class="w-full bg-gradient-to-r from-[#115583] to-[#44AAE2] text-white font-semibold py-2 px-6 rounded-lg hover:opacity-90 transition-opacity">
          검색
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  selectedBank: String,
  selectedRadius: String
})

defineEmits(['update:selectedBank', 'update:selectedRadius', 'search'])
</script>