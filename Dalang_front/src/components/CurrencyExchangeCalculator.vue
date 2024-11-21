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

    <!-- Exchange Rate Trend Chart -->
    <div v-if="chartData" class="mt-8">
      <h2 class="text-xl font-semibold mb-4 text-center">{{ selectedCurrency }} 1년 치 환율 변동 추이</h2>
      <!-- LineChart 컴포넌트를 사용하여 차트를 렌더링 -->
      <LineChart :chart-data="chartData" :key="selectedCurrency" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'
import LineChart from './LineChart.vue' // Chart.js 기반 라인 차트 컴포넌트

const API_URL = 'http://127.0.0.1:8000'

// 반응형 데이터
const baseCurrency = ref('foreign') // '외화기준' 또는 '원화기준'
const selectedCurrency = ref('') // 선택된 외화
const amount = ref('') // 사용자가 입력한 금액
const calculatedAmount = ref(null) // 계산 결과
const currencies = ref([]) // 최신 환율 데이터를 저장
const exchangeRate = ref(0) // 현재 선택된 환율
const chartData = ref(null) // 선택된 외화의 1년 치 환율 데이터
let allData = [] // 모든 환율 데이터를 저장

// Django 서버에서 환율 데이터를 가져오는 함수
const fetchExchangeRates = async () => {
  try {
    const response = await axios.get(`${API_URL}/exchange_rate/`)
    const data = response.data
    allData = data // 모든 환율 데이터를 저장

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

    // 초기 차트 데이터 설정
    processChartData(selectedCurrency.value)
  } catch (error) {
    console.error('환율 데이터를 가져오는 중 오류 발생:', error)
  }
}

// 차트 데이터 처리 함수
const processChartData = (currencyCode) => {
  if (!currencyCode) return

  // 선택된 외화의 1년 치 데이터 필터링
  const filteredData = allData.filter(item => item.currency_unit === currencyCode)
  chartData.value = {
    labels: filteredData.map(item => item.date), // 날짜 배열
    datasets: [
      {
        label: `${currencyCode} 환율`,
        data: filteredData.map(item => item.exchange_rate), // 환율 데이터 배열
        borderColor: '#0066CC', // 라인 색상
        backgroundColor: 'rgba(0, 102, 204, 0.2)', // 라인 아래 채우기 색상
        fill: true, // 채우기 여부
        tension: 0.1, // 곡선의 부드러움
      },
    ],
  }
}

// 계산된 결과를 포맷
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
    calculatedAmount.value = parseFloat(amount.value) * exchangeRate.value
  } else if (baseCurrency.value === 'won') {
    calculatedAmount.value = parseFloat(amount.value) / exchangeRate.value
  }
}

// 외화 선택 변경 시 초기화 및 차트 업데이트
watch(selectedCurrency, (newCurrency) => {
  if (newCurrency) {
    // 계산기 초기화
    amount.value = '' // 금액 입력 초기화
    calculatedAmount.value = null // 결과 초기화

    // 차트 데이터 처리
    processChartData(newCurrency)
  }
})

// 컴포넌트 로드 시 환율 데이터 가져오기
onMounted(fetchExchangeRates)
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
