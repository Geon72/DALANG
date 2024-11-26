<template>
  <div class="bg-white shadow rounded-lg overflow-hidden">
    <div class="flex justify-between items-center p-4 border-b">
      <div class="text-sm text-gray-600">
        검색결과: <span class="font-semibold">{{ products.length }}건</span>
      </div>
      <RecommendationExcelExport :data="exportData" :headers="exportHeaders" />
    </div>

    <div class="overflow-x-auto">
      <div class="inline-block min-w-full align-middle">
        <div class="overflow-hidden border-b border-gray-200 shadow sm:rounded-lg">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th v-for="(header, index) in tableHeaders" :key="header"
                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider sticky top-0 bg-gray-50 z-10"
                    :class="{ 'hidden sm:table-cell': index > 3 && index < tableHeaders.length - 1 }">
                  {{ header }}
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="(product, index) in visibleProducts" :key="product.id"
                  :class="index % 2 === 0 ? 'bg-white' : 'bg-gray-50'">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">{{ product.kor_co_nm }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ product.fin_prdt_nm }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900" :title="product.mtrt_int">
                    {{ abbreviateInterestRate(product.mtrt_int) }}
                  </div>
                </td>
                <td class="px-6 py-4">
                  <div class="text-sm text-gray-900 max-w-xs overflow-hidden text-ellipsis" :title="product.spcl_cnd">
                    {{ truncateText(product.spcl_cnd, 30) }}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap hidden sm:table-cell">
                  <div class="text-sm text-gray-900">{{ product.join_way }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap hidden sm:table-cell">
                  <div class="text-sm text-gray-900">{{ product.join_member }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                  <button class="text-[#0088CC] hover:text-[#006699] font-medium" @click="showDetails(product)">
                    상세보기
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="flex justify-center p-4" v-if="hasMoreItems">
      <button @click="loadMore" class="bg-[#0088CC] hover:bg-[#006699] text-white font-bold py-2 px-4 rounded">
        더보기
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import RecommendationExcelExport from "./RecommendationExcelExport.vue";
import depositProducts from '@/assets/depositProducts.json';

const products = ref(JSON.parse(JSON.stringify(depositProducts)));
const visibleItemCount = ref(5);

const tableHeaders = ["은행명", "상품명", "기본금리", "우대조건", "가입방법", "가입대상", "상세정보"];

const sortOrder = ref("desc");

const sortedProducts = computed(() => {
  return [...products.value].sort((a, b) => {
    const compareValue = sortOrder.value === "asc" ?
      a.mtrt_int.localeCompare(b.mtrt_int) :
      b.mtrt_int.localeCompare(a.mtrt_int);
    return compareValue;
  });
});

const visibleProducts = computed(() => {
  return sortedProducts.value.slice(0, visibleItemCount.value);
});

const hasMoreItems = computed(() => {
  return visibleItemCount.value < sortedProducts.value.length;
});

const loadMore = () => {
  visibleItemCount.value += 5;
};

const exportHeaders = [
  "은행명",
  "상품명",
  "기본금리",
  "우대조건",
  "가입방법",
  "가입대상",
];

const exportData = computed(() => {
  return sortedProducts.value.map((product) => ({
    은행명: product.kor_co_nm,
    상품명: product.fin_prdt_nm,
    기본금리: product.mtrt_int,
    우대조건: product.spcl_cnd,
    가입방법: product.join_way,
    가입대상: product.join_member,
  }));
});

const showDetails = (product) => {
  console.log("Show details for:", product);
};

const abbreviateInterestRate = (rate) => {
  const matches = rate.match(/(\d+(\.\d+)?%)/g);
  if (matches && matches.length > 0) {
    return matches[0];
  }
  return '상세보기';
};

const truncateText = (text, maxLength) => {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength) + '...';
};
</script>

<style scoped>
.overflow-x-auto {
  scrollbar-width: thin;
  scrollbar-color: #CBD5E0 #EDF2F7;
}

.overflow-x-auto::-webkit-scrollbar {
  height: 8px;
}

.overflow-x-auto::-webkit-scrollbar-track {
  background: #EDF2F7;
}

.overflow-x-auto::-webkit-scrollbar-thumb {
  background-color: #CBD5E0;
  border-radius: 20px;
  border: 3px solid #EDF2F7;
}
</style>