<template>
  <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
    <div class="space-y-6">
      <!-- Buy/Sell Selection -->
      <div class="flex gap-4">
        <label class="flex items-center space-x-2">
          <input type="radio" v-model="transactionType" value="buy" class="text-[#0066CC]">
          <span>외화사실때</span>
        </label>
        <label class="flex items-center space-x-2">
          <input type="radio" v-model="transactionType" value="sell" class="text-[#0066CC]">
          <span>외화파실때</span>
        </label>
      </div>

      <!-- Currency List -->
      <div class="space-y-2">
        <div v-for="currency in currencies" :key="currency.code"
          class="p-3 rounded-lg cursor-pointer hover:bg-gray-50 flex items-center justify-between"
          :class="{ 'bg-blue-50': selectedCurrency === currency.code }" @click="selectCurrency(currency.code)">
          <div class="flex items-center space-x-3">
            <!-- 환전 수수료 1% 가정 -->
            <div>
              <span class="font-medium">
                <!-- <i :class="getFlagClass(currency.code)" class="mr-2"></i> -->
                
                {{ currency.code }} ({{ getCurrencyName(currency.code) }})
              </span>
              <div v-if="transactionType === 'buy'" class="text-sm text-gray-500">
                살 때: {{ (currency.exchangeRate * 1.01).toFixed(2) }} 원
              </div>
              <div v-else class="text-sm text-gray-500">
                팔 때: {{ (currency.exchangeRate * 0.99).toFixed(2) }} 원
              </div>
            </div>
          </div>
          <span class="text-[#0066CC] font-medium">
            {{ currency.code }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
// import '@fortawesome/fontawesome-free/css/all.min.css'

const props = defineProps(['selectedCurrency'])
const emit = defineEmits(['update:currency'])

const transactionType = ref('buy') // 기본값: 외화 사실 때
const currencies = ref([]) // 환율 데이터를 저장할 상태

const API_URL = 'http://127.0.0.1:8000'

// 통화 코드와 이름 매핑
const currencyNames = {
  USD: '달러',
  EUR: '유로',
  JPY: '엔화',
  CNY: '위안화',
  GBP: '영국 파운드',
  CHF: '스위스 프랑',
  AUD: '호주 달러',
  AED: '아랍에미리트 디르함',
  BHD: '바레인 디나르',
}


// 통화 코드로 이름 반환
const getCurrencyName = (code) => currencyNames[code] || '알 수 없음'

// Django 서버에서 최신 환율 데이터를 가져오는 함수
const fetchExchangeRates = async () => {
  try {
    const response = await axios.get(`${API_URL}/exchange_rate/`)
    const data = response.data

    // 최신 데이터만 필터링
    const latestData = {}
    data.forEach((item) => {
      const unit = item.currency_unit
      const itemDate = new Date(item.date)

      // 가장 최신 날짜의 데이터를 저장
      if (!latestData[unit] || itemDate > new Date(latestData[unit].date)) {
        latestData[unit] = {
          code: unit,
          exchangeRate: item.exchange_rate,
          date: item.date, // 최신 날짜 저장
        }
      }
    })

    // 통화 순서에 따라 정렬된 데이터
    const priorityOrder = [
      'USD', 'EUR', 'JPY', 'CNY', 'GBP', 'CHF', 'AUD', 'AED', 'BHD'
    ]
    currencies.value = Object.values(latestData)
      .filter((item) => priorityOrder.includes(item.code)) // 우선순위에 있는 코드만 포함
      .sort((a, b) => priorityOrder.indexOf(a.code) - priorityOrder.indexOf(b.code)) // 우선순위대로 정렬
  } catch (error) {
    console.error('환율 데이터를 가져오는 중 오류 발생:', error)
  }
}

// 선택된 통화를 부모 컴포넌트로 전달
const selectCurrency = (code) => {
  emit('update:currency', code)
}

// 컴포넌트가 로드될 때 환율 데이터를 가져옴
onMounted(fetchExchangeRates)
</script>

<style scoped>
.currency-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(68, 170, 226, 0.1);
}

.currency-card:hover {
  border-color: rgba(68, 170, 226, 0.3);
  box-shadow: 0 8px 24px rgba(17, 85, 131, 0.1);
}

.rounded-lg {
  border-radius: 0.5rem;
}

.shadow-sm {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.text-[#0066CC] {
  color: #0066cc;
}
</style>
