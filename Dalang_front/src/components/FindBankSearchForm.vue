<template>
    <div class="search-form bg-white p-4 rounded-lg shadow-md mb-6">
        <div class="grid grid-cols-3 gap-4">
            <div class="col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-1">은행/ATM 선택</label>
                <select v-model="localSelectedType"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    @change="emitSearchParams">
                    <option value="ALL">전체</option>
                    <option value="BANK">은행</option>
                    <option value="ATM">ATM</option>
                </select>
            </div>

            <div class="col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-1">검색 반경</label>
                <select v-model="localSelectedRadius"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    @change="emitSearchParams">
                    <option value="500">500m</option>
                    <option value="1000">1km</option>
                </select>
            </div>

            <div class="col-span-1 flex items-end">
                <button @click="handleSearch"
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md transition duration-200">
                    검색
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
    selectedType: String,
    selectedRadius: String
})

const emit = defineEmits(['search', 'update:selectedType', 'update:selectedRadius'])

const localSelectedType = ref(props.selectedType || 'ALL')
const localSelectedRadius = ref(props.selectedRadius || '1000')

const emitSearchParams = () => {
    emit('update:selectedType', localSelectedType.value)
    emit('update:selectedRadius', localSelectedRadius.value)
}

const handleSearch = () => {
  emit('update:selectedType', localSelectedType.value)
  emit('update:selectedRadius', localSelectedRadius.value)
  
  emit('search', {
    type: localSelectedType.value,
    radius: parseInt(localSelectedRadius.value)
  })
}
</script>