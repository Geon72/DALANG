<template>
  <div class="bg-white shadow rounded-lg overflow-hidden">
    <div class="flex justify-between items-center p-4">
      <div class="text-sm text-gray-600">
        검색결과: <span class="font-semibold">{{ products.length }}건</span>
      </div>
      <RecommendationExcelExport :data="exportData" :headers="exportHeaders" />
    </div>

    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th
            v-for="header in tableHeaders"
            :key="header"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            {{ header }}
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr
          v-for="(product, index) in sortedProducts"
          :key="product.id"
          :class="index % 2 === 0 ? 'bg-white' : 'bg-gray-50'"
        >
          <!-- 은행 -->
          <td class="px-6 py-4">
            <div class="flex items-center">
              <div class="flex-shrink-0 h-10 w-10">
                <img
                  class="h-10 w-10"
                  :src="product.bankLogo"
                  :alt="product.bankName"
                />
              </div>
              <div class="ml-4">
                <div class="text-sm font-medium text-gray-900">
                  {{ product.bankName }}
                </div>
              </div>
            </div>
          </td>
          <!-- 상품명 -->
          <td class="px-6 py-4">
            <div class="text-sm font-medium text-gray-900">
              {{ product.productName }}
            </div>
          </td>
          <!-- 기본금리 -->
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.baseRate }}%</div>
          </td>
          <!-- 우대금리 -->
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.primeRate }}%</div>
          </td>
          <!-- 최고금리 -->
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.maxRate }}%</div>
          </td>
          <!-- 상세정보 -->
          <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
            <button
              class="text-[#0088CC] hover:text-[#006699] font-medium"
              @click="showDetails(product)"
            >
              상세보기
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { computed } from "vue";
import RecommendationExcelExport from "./RecommendationExcelExport.vue";

const props = defineProps({
  tableHeaders: {
    type: Array,
    required: true,
  },
  products: {
    type: Array,
    required: true,
  },
  sortOrder: {
    type: String,
    default: "desc",
  },
});

// 정렬된 상품 목록
const sortedProducts = computed(() => {
  return [...props.products].sort((a, b) => {
    const compareValue =
      props.sortOrder === "asc" ? a.maxRate - b.maxRate : b.maxRate - a.maxRate;
    return compareValue;
  });
});

// 엑셀 내보내기용 헤더
const exportHeaders = [
  "은행명",
  "상품명",
  "기본금리(%)",
  "우대금리(%)",
  "최고금리(%)",
  "우대조건",
];

// 엑셀 내보내기 데이터
const exportData = computed(() => {
  return sortedProducts.value.map((product) => ({
    은행명: product.bankName,
    상품명: product.productName,
    "기본금리(%)": product.baseRate,
    "우대금리(%)": product.primeRate,
    "최고금리(%)": product.maxRate,
    우대조건: product.maxRateCondition,
  }));
});

// 상세 정보 보기 핸들러
const showDetails = (product) => {
  console.log("Show details for:", product);
};
</script>
