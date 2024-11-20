<template>
  <section class="exchange-rate-section mt-12 px-4 sm:px-6 lg:px-8">
    <h2
      class="text-center text-2xl sm:text-3xl font-bold mb-8 bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent">
      여행갈 여행지의 환율을 알아봐요
    </h2>

    <div v-if="currencies.length" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
      <!-- 그리드 간격 조정: gap-6 -> gap-8 -->
      <div v-for="(currency, i) in currencies" :key="i"
        class="currency-card bg-white rounded-xl shadow-lg p-6 transform transition-all duration-300 hover:-translate-y-1">
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center">
            <h3 class="text-lg font-semibold text-[#115583]">{{ currency.currency_unit }}</h3>
          </div>
          <span class="text-sm font-medium text-[#44AAE2]">{{ currency.currency_unit }}</span>
        </div>
        <div class="text-center">
          <p class="text-3xl font-bold bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent mb-2">
            {{ currency.exchange_rate.toFixed(2) }}
          </p>
          <span class="text-sm text-gray-500 font-medium">{{ currency.date }}</span>
        </div>
      </div>
    </div>
    <div v-else class="text-center">
      <p class="text-gray-500">환율 데이터를 불러오는 중입니다...</p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const currencies = ref([]) // 최신 데이터만 담을 상태
const API_URL = 'http://127.0.0.1:8000'

const fetchExchangeRates = async () => {
  try {
    const response = await axios.get(`${API_URL}/exchange_rate/`) // Django API 호출
    const allData = response.data // API에서 가져온 전체 데이터

    // 가장 최신 날짜 데이터를 추출
    const latestData = {}
    allData.forEach((item) => {
      const unit = item.currency_unit
      if (
        !latestData[unit] ||
        new Date(item.date) > new Date(latestData[unit].date)
      ) {
        latestData[unit] = item // 최신 데이터로 갱신
      }
    })

    currencies.value = Object.values(latestData) // 최신 데이터만 상태에 저장
  } catch (error) {
    console.error('환율 데이터를 가져오는 중 오류 발생:', error)
  }
}

// 컴포넌트가 로드될 때 데이터 불러오기
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

.rounded-xl {
  border-radius: 1rem;
}

.shadow-lg {
  box-shadow: 0 4px 12px rgba(17, 85, 131, 0.08);
}

/* Glass morphism effect */
.bg-white {
  background: linear-gradient(145deg,
      rgba(255, 255, 255, 0.95) 0%,
      rgba(255, 255, 255, 0.85) 100%);
}

/* Responsive grid adjustments */
.grid {
  gap: 2rem; /* 기본 간격 */
}

@media (max-width: 640px) {
  .grid {
    gap: 1.5rem; /* 작은 화면에서 간격 축소 */
  }

  .currency-card {
    padding: 1rem;
  }

  .text-3xl {
    font-size: 1.5rem;
  }
}
</style>
