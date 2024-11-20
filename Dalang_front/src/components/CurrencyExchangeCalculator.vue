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

      <!-- Foreign Currency Selection -->
      <div class="flex items-center space-x-4">
        <span class="font-semibold text-gray-600">외화 종류</span>
        <label class="flex items-center space-x-2" v-for="currency in availableCurrencies" :key="currency">
          <input type="radio" v-model="selectedCurrency" :value="currency" class="text-[#0066CC]">
          <span>{{ currency }}</span>
        </label>
      </div>

      <!-- Date Selection -->
      <div class="relative">
        <input type="date" v-model="exchangeDate" class="w-full pl-3 pr-3 py-2 border rounded-md">
      </div>

      <!-- Amount Input -->
      <div>
        <input type="number" v-model="amount" class="w-full border rounded-md px-3 py-2" placeholder="금액을 입력하세요">
      </div>

      <!-- Calculate Button -->
      <button @click="calculate"
        class="w-full bg-[#0066CC] hover:bg-[#0055AA] text-white py-2 rounded-md transition-colors">
        계산하기
      </button>

      <!-- Result Display -->
      <div v-if="calculatedAmount" class="text-right text-xl font-semibold mt-4">
        <span>{{ formattedResult }}</span>
        <span class="ml-2 text-gray-600">{{ baseCurrency === 'foreign' ? 'KRW' : selectedCurrency }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

const baseCurrency = ref('foreign') // '외화기준' 또는 '원화기준'
const exchangeDate = ref('')
const selectedCurrency = ref('')
const amount = ref('')
const calculatedAmount = ref(null)
const availableCurrencies = ref(['USD', 'EUR', 'JPY', 'CNH']) // 외화 종류
const exchangeRate = ref(0) // API로부터 가져올 환율 값

// 데이터를 가져오는 함수
const fetchExchangeRate = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/exchange_rate/detail/', {
      params: {
        date: exchangeDate.value,
        currency_unit: selectedCurrency.value
      }
    })
    exchangeRate.value = response.data.exchange_rate || 0
    console.log('Fetched exchange rate:', exchangeRate.value)
  } catch (error) {
    console.error('환율 데이터를 가져오는 중 오류 발생:', error)
    exchangeRate.value = 0
  }
}

// 계산된 결과 포맷
const formattedResult = computed(() => {
  if (calculatedAmount.value !== null) {
    // selectedCurrency가 비어있거나 null일 때 기본값 처리
    const currency = selectedCurrency.value || '외화'
    return baseCurrency.value === 'foreign'
      ? `${calculatedAmount.value.toLocaleString()}`
      : `${calculatedAmount.value.toFixed(2)}`
  }
  return ''
})


// 계산 함수
const calculate = async () => {
  if (!exchangeDate.value || !selectedCurrency.value || !amount.value) {
    alert('날짜, 외화 종류, 금액을 모두 입력하세요.')
    return
  }

  // 환율 데이터 가져오기
  await fetchExchangeRate()

  // 외화기준 또는 원화기준에 따른 계산
  if (baseCurrency.value === 'foreign') {
    // 외화 기준: 입력값(외화) * 환율 = 원화
    calculatedAmount.value = parseFloat(amount.value) * exchangeRate.value
  } else if (baseCurrency.value === 'won') {
    // 원화 기준: 입력값(원화) / 환율 = 외화
    calculatedAmount.value = parseFloat(amount.value) / exchangeRate.value
  }
}
</script>

<style scoped>
/* 기본 스타일 */
.bg-white {
  background-color: #fff;
}
.border {
  border-color: #ddd;
}
.w-full {
  width: 100%;
}
</style>
