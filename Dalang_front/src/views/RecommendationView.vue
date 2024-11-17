<template>
  <div class="min-h-screen bg-gray-50">
    <NavigationBar :navItems="navItems" />
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- 상단 탭 네비게이션 -->
      <div class="mb-6">
        <h2 class="text-2xl font-bold text-[#0088CC] mb-4">예금상품금리비교</h2>
        <div class="border-b border-gray-200">
          <nav class="-mb-px flex space-x-8">
            <a
              v-for="tab in tabs"
              :key="tab.id"
              :href="tab.href"
              :class="[
                tab.active
                  ? 'border-[#0088CC] text-[#0088CC]'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
                'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm'
              ]"
              @click.prevent="activateTab(tab)"
            >
              {{ tab.name }}
            </a>
          </nav>
        </div>
      </div>

      <!-- 정기예금 컴포넌트들 -->
      <template v-if="currentTab === '정기예금'">
        <RecommendationFilterSectionDeposit
          :banks="banks"
          :periods="periods"
          :subscriptionMethods="subscriptionMethods"
          @search="searchDeposits"
        />
        <RecommendationResultTableDeposit 
          :tableHeaders="depositTableHeaders"
          :products="depositProducts"
          :sortOrder="sortOrder"
        />
      </template>

      <!-- 정기적금 컴포넌트들 -->
      <template v-else>
        <RecommendationFilterSectionSaving
          :banks="banks"
          :periods="periods"
          :subscriptionMethods="subscriptionMethods"
          @search="searchSavings"
        />
        <RecommendationResultTableSaving
          :tableHeaders="savingTableHeaders"
          :products="savingProducts"
          :sortOrder="sortOrder"
        />
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'
import RecommendationFilterSectionDeposit from '@/components/RecommendationFilterSectionDeposit.vue'
import RecommendationResultTableDeposit from '@/components/RecommendationResultTableDeposit.vue'
import RecommendationFilterSectionSaving from '@/components/RecommendationFilterSectionSaving.vue'
import RecommendationResultTableSaving from '@/components/RecommendationResultTableSaving.vue'

const tabs = ref([
  { id: 1, name: '정기예금', href: '#', active: true },
  { id: 2, name: '정기적금', href: '#', active: false },
])

const currentTab = computed(() => {
  const activeTab = tabs.value.find(tab => tab.active)
  return activeTab?.name || '정기예금'
})

const activateTab = (selectedTab) => {
  tabs.value = tabs.value.map(tab => ({
    ...tab,
    active: tab.id === selectedTab.id
  }))
}

const banks = [
  'KDB산업은행', 'NH농협은행', '신한은행', '우리은행', 'SC제일은행', '하나은행',
  'IBK기업은행', 'KB국민은행', '한국씨티은행', 'Sh수협은행', 'iM뱅크(구 대구은행)', 'BNK부산은행',
  '광주은행', '제주은행', '전북은행', 'BNK경남은행', '케이뱅크', '카카오뱅크', '토스뱅크'
]

const periods = [1, 3, 6, 12, 24, 36]
const subscriptionMethods = ['전체', '영업점', '인터넷뱅킹', '스마트뱅킹', '전화', '기타']
const sortOrder = ref('desc')

// 정기예금 관련 데이터
const depositTableHeaders = ['은행/상품명', '기본금리', '우대금리', '최고금리', '상세정보']
const depositProducts = ref([
  {
    id: 1,
    bankName: '국민은행',
    productName: 'KB 스마트 정기예금',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 3.05,
    primeRate: 0.3,
    maxRate: 3.35,
    maxRateCondition: '온라인 신규 및 자동이체 조건 충족 시'
  }
])

// 정기적금 관련 데이터
const savingTableHeaders = ['은행/상품명', '기본금리', '우대금리', '최고금리', '상세정보']
const savingProducts = ref([
  {
    id: 1,
    bankName: 'KDB산업은행',
    productName: 'KDB 기업정기적금',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 2.45,
    primeRate: 0.00,
    maxRate: 2.45,
    maxRateCondition: '기본금리'
  },
  {
    id: 2,
    bankName: '우리은행',
    productName: '우리SUPER주거래적금',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 2.80,
    primeRate: 1.40,
    maxRate: 4.20,
    maxRateCondition: '주거래 실적 충족 시'
  },
  {
    id: 3,
    bankName: '우리은행',
    productName: 'WON적금',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 3.70,
    primeRate: 0.20,
    maxRate: 3.90,
    maxRateCondition: '우리카드 이용실적 충족 시'
  },
  {
    id: 4,
    bankName: 'SC제일은행',
    productName: '퍼스트가계적금',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 3.30,
    primeRate: 0.00,
    maxRate: 3.30,
    maxRateCondition: '기본금리'
  },
  {
    id: 5,
    bankName: '하나은행',
    productName: '내맘적금',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 2.60,
    primeRate: 0.50,
    maxRate: 3.10,
    maxRateCondition: '하나카드 실적 충족 시'
  },
  {
    id: 6,
    bankName: 'KB국민은행',
    productName: 'KB국민프리미엄적금(정액)',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 2.50,
    primeRate: 0.90,
    maxRate: 3.40,
    maxRateCondition: 'KB카드 실적 충족 시'
  },
  {
    id: 7,
    bankName: 'Sh수협은행',
    productName: 'Sh해양플라스틱Zero!적금 (정액적립식)',
    bankLogo: '/placeholder.svg?height=40&width=40',
    baseRate: 3.50,
    primeRate: 0.50,
    maxRate: 4.00,
    maxRateCondition: '친환경 실천 조건 충족 시'
  }
])

const searchDeposits = (filters) => {
  console.log('Searching deposits with filters:', filters)
}

const searchSavings = (filters) => {
  console.log('Searching savings with filters:', filters)
}

const navItems = [
  { name: '홈', route: '/' },
  { name: '예/적금 추천', route: '/recommendations' },
  { name: '근처 은행', route: '/find-bank' },
  { name: '환율 계산기', route: '/currency-calculator' },
  { name: '커뮤니티', route: '/community' },
]
</script>