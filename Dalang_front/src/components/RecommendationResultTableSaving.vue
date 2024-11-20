<template>
  <div class="bg-white shadow rounded-lg overflow-hidden">
    <div class="flex justify-between items-center p-4">
      <div class="text-sm text-gray-600">
        검색결과: <span class="font-semibold">{{ products.length }}건</span>
      </div>
      <RecommendationExcelExport :data="exportData" :headers="exportHeaders" :tabType="currentTab" />
    </div>

    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            은행
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            상품명
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            기본금리(단리정액 %)
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            최고금리(우대금리 포함, 단리정액 %)
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            상세정보
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            전월적금 평균금리(만기12개월 기준)
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="(product, index) in sortedProducts" :key="product.id"
          :class="index % 2 === 0 ? 'bg-white' : 'bg-gray-50'">
          <td class="px-6 py-4">
            <div class="flex items-center">
              <div class="flex-shrink-0 h-10 w-10">
                <img class="h-10 w-10" :src="product.bankLogo" :alt="product.bankName">
              </div>
              <div class="ml-4">
                <div class="text-sm font-medium text-gray-900">{{ product.bankName }}</div>
                <div class="flex space-x-1">
                  <span v-if="product.isOnline" class="px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded">재</span>
                  <span v-if="product.isSpecial"
                    class="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 rounded">소</span>
                  <span v-if="product.isConfirmed"
                    class="px-2 py-1 text-xs bg-green-100 text-green-800 rounded">확</span>
                </div>
              </div>
            </div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.productName }}</div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.baseRate }}%</div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.maxRate }}%</div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm">
            <button class="text-[#0088CC] hover:text-[#006699] font-medium" @click="showDetails(product)">
              보기
            </button>
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.averageRate }}%</div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import RecommendationExcelExport from './RecommendationExcelExport.vue'

const props = defineProps({
  products: {
    type: Array,
    required: true
  },
  sortOrder: {
    type: String,
    default: 'desc'
  }
})

const sortedProducts = computed(() => {
  return [...props.products].sort((a, b) => {
    const compareValue = props.sortOrder === 'asc'
      ? a.maxRate - b.maxRate
      : b.maxRate - a.maxRate
    return compareValue
  })
})

const exportHeaders = [
  '은행명',
  '상품명',
  '기본금리(단리정액 %)',
  '최고금리(우대금리 포함, 단리정액 %)',
  '전월적금 평균금리(만기12개월 기준)'
]

const exportData = computed(() => {
  return sortedProducts.value.map(product => ({
    은행명: product.bankName,
    상품명: product.productName,
    '기본금리(단리정액 %)': product.baseRate,
    '최고금리(우대금리 포함, 단리정액 %)': product.maxRate,
    '전월적금 평균금리(만기12개월 기준)': product.averageRate
  }))
})

const showDetails = (product) => {
  console.log('Show details for:', product)
}
</script>