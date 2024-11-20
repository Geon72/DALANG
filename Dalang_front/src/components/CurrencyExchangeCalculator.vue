<template>
  <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
    <div class="space-y-6">
      <!-- Base Currency Selection -->
      <div>
        <div class="flex gap-4">
          <label class="flex items-center space-x-2">
            <input type="radio" v-model="baseCurrency" value="foreign" class="text-[#0066CC]">
            <span>외화기준</span>
          </label>
          <label class="flex items-center space-x-2">
            <input type="radio" v-model="baseCurrency" value="won" class="text-[#0066CC]">
            <span>원화기준</span>
          </label>
        </div>
      </div>

      <!-- Exchange Rate Type -->
      <div class="flex items-center space-x-2">
        <input type="radio" checked class="text-[#0066CC]">
        <span>고시환율적용</span>
      </div>

      <!-- Date and Time Selection -->
      <div class="grid grid-cols-2 gap-4">
        <div class="relative">
          <input type="text" v-model="exchangeDate" readonly class="w-full pl-10 pr-3 py-2 border rounded-md">
          <CalendarIcon class="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-500" />
        </div>
        <select v-model="exchangeTime" class="w-full border rounded-md">
          <option value="current">고시시간(회차)</option>
        </select>
      </div>

      <!-- Amount Input -->
      <div class="space-y-4">
        <input type="number" v-model="amount" class="w-full border rounded-md px-3 py-2" placeholder="금액을 입력하세요">
        <CurrencyExchangeQuickAmountButton @select="handleQuickAmount" />
      </div>

      <!-- Calculate Button -->
      <button @click="calculate"
        class="w-full bg-[#0066CC] hover:bg-[#0055AA] text-white py-2 rounded-md transition-colors">
        계산하기
      </button>

      <!-- Result Display -->
      <div class="text-right text-xl font-semibold">
        <span>{{ calculatedAmount }}</span>
        <span class="ml-2 text-gray-600">{{ selectedCurrency }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { CalendarIcon } from 'lucide-vue-next'
import CurrencyExchangeQuickAmountButton from './CurrencyExchangeQuickAmountButton.vue'

const props = defineProps(['selectedCurrency'])
const emit = defineEmits(['update:amount'])

const baseCurrency = ref('foreign')
const exchangeDate = ref('2024.11.18')
const exchangeTime = ref('current')
const amount = ref('')
const calculatedAmount = ref(0)

const handleQuickAmount = (value) => {
  amount.value = String(value)
  emit('update:amount', amount.value)
}

const calculate = () => {
  // Implement calculation logic here
  calculatedAmount.value = parseFloat(amount.value) || 0
}
</script>