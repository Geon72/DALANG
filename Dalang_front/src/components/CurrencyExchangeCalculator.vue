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
        <label class="flex items-center space-x-2" v-for="currency in currencies" :key="currency.code">
          <input type="radio" v-model="selectedCurrency" :value="currency.code" class="text-[#0066CC]">
          <span>{{ currency.code }}</span>
        </label>
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
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const baseCurrency = ref('foreign') // '외화기준' 또는 '원화기준'
const selectedCurrency = ref('') // 선택한 외화
const amount = ref('') // 입력된 금액
const calculatedAmount = ref(null) // 계산 결과
const currencies = ref([]) // 최신 환율 데이터를 저장
const exchangeRate = ref(0) // 현재 선택된 환율

// Django 서버에서 최신 환율 데이터를 가져오는 함수
const fetchLatestExchangeRates = async () => {
  try {
    const response = await axios.get(`${API_URL}/exchange_rate/`)
    const data = response.data

    // 최신 날짜의 'USD', 'EUR', 'JPY(100)', 'CNH'만 필터링
    const priorityOrder = ['USD', 'EUR', 'JPY(100)', 'CNH']
    const latestData = {}

    data.forEach((item) => {
      const unit = item.currency_unit
      const itemDate = new Date(item.date)

      if (
        priorityOrder.includes(unit) &&
        (!latestData[unit] || itemDate > new Date(latestData[unit].date))
      ) {
        latestData[unit] = {
          code: unit,
          exchangeRate: item.exchange_rate,
          date: item.date, // 최신 날짜 저장
        }
      }
    })

    // 필터링된 최신 데이터 정렬
    currencies.value = Object.values(latestData)
      .sort((a, b) => priorityOrder.indexOf(a.code) - priorityOrder.indexOf(b.code))

    // 기본 선택된 외화 설정
    if (currencies.value.length > 0) {
      selectedCurrency.value = currencies.value[0].code
    }
  } catch (error) {
    console.error('환율 데이터를 가져오는 중 오류 발생:', error)
  }
}

// 계산된 결과 포맷
const formattedResult = computed(() => {
  if (calculatedAmount.value !== null) {
    return calculatedAmount.value.toLocaleString(undefined, { minimumFractionDigits: 2 })
  }
  return ''
})

// 계산 함수
const calculate = () => {
  if (!selectedCurrency.value || !amount.value) {
    alert('외화 종류와 금액을 모두 입력하세요.')
    return
  }

  // 선택된 외화의 환율 찾기
  const selectedCurrencyData = currencies.value.find((item) => item.code === selectedCurrency.value)
  if (!selectedCurrencyData) {
    alert('선택한 외화에 대한 환율을 찾을 수 없습니다.')
    return
  }

  exchangeRate.value = selectedCurrencyData.exchangeRate

  // 외화기준 또는 원화기준에 따른 계산
  if (baseCurrency.value === 'foreign') {
    // 외화 기준: 입력값(외화) * 환율 = 원화
    calculatedAmount.value = parseFloat(amount.value) * exchangeRate.value
  } else if (baseCurrency.value === 'won') {
    // 원화 기준: 입력값(원화) / 환율 = 외화
    calculatedAmount.value = parseFloat(amount.value) / exchangeRate.value
  }
}

// 계산기 초기화 함수
const resetCalculator = () => {
  amount.value = ''
  calculatedAmount.value = null
}

// baseCurrency 또는 selectedCurrency 변경 시 초기화
watch([baseCurrency, selectedCurrency], resetCalculator)

// 컴포넌트 로드 시 최신 환율 데이터 가져오기
onMounted(fetchLatestExchangeRates)
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
