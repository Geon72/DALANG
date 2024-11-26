<script setup>
import { ref } from "vue";
import NavigationBar from "@/components/NavigationBar.vue";
import RecommendationFilterSectionDeposit from "@/components/RecommendationFilterSectionDeposit.vue";
import RecommendationFilterSectionSaving from "@/components/RecommendationFilterSectionSaving.vue";
import RecommendationResultTableDeposit from "@/components/RecommendationResultTableDeposit.vue";
import RecommendationResultTableSaving from "@/components/RecommendationResultTableSaving.vue";

const activeTab = ref('deposit');
const products = ref([]);
const sortOrder = ref("desc");

const depositTableHeaders = [
  "은행", "상품명", "기본금리", "우대금리", "최고금리", "상세정보",
];

const savingTableHeaders = [
  "은행", "상품명", "기본금리", "우대금리", "최고금리", "적립방식", "상세정보",
];

const searchProducts = async (filters) => {
  try {
    const endpoint = activeTab.value === 'deposit' 
      ? "http://127.0.0.1:8000/products/filter/deposit/"
      : "http://127.0.0.1:8000/products/filter/saving/";

    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(filters),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    products.value = data.products;
  } catch (error) {
    console.error(`Error fetching filtered ${activeTab.value}s:`, error);
  }
};

const changeTab = (tab) => {
  activeTab.value = tab;
  products.value = []; // 탭 변경 시 상품 목록 초기화
};
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavigationBar />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="flex space-x-4 mb-6">
        <button 
          @click="changeTab('deposit')" 
          :class="['px-4 py-2 rounded-md', activeTab === 'deposit' ? 'bg-blue-500 text-white' : 'bg-gray-200']"
        >
          정기예금
        </button>
        <button 
          @click="changeTab('saving')" 
          :class="['px-4 py-2 rounded-md', activeTab === 'saving' ? 'bg-blue-500 text-white' : 'bg-gray-200']"
        >
          정기적금
        </button>
      </div>

      <h2 class="text-3xl font-bold mb-4">
        {{ activeTab === 'deposit' ? '정기예금' : '정기적금' }} 상품 추천
      </h2>

      <!-- Filter Section -->
      <RecommendationFilterSectionDeposit
        v-if="activeTab === 'deposit'"
        :banks="['KDB산업은행', 'NH농협은행', '신한은행', '우리은행', 'SC제일은행', '하나은행', 'IBK기업은행', 'KB국민은행', '한국씨티은행', 'Sh수협은행', 'iM뱅크(구 대구은행)', 'BNK부산은행', '광주은행', '제주은행', '전북은행', 'BNK경남은행', '케이뱅크', '카카오뱅크', '토스뱅크']"
        :periods="[1, 3, 6, 12, 24, 36]"
        :subscriptionMethods="['전체', '영업점', '인터넷뱅킹', '스마트뱅킹', '전화', '기타']"
        @search="searchProducts"
      />
      <RecommendationFilterSectionSaving
        v-else
        :banks="['KDB산업은행', 'NH농협은행', '신한은행', '우리은행', 'SC제일은행', '하나은행', 'IBK기업은행', 'KB국민은행', '한국씨티은행', 'Sh수협은행', 'iM뱅크(구 대구은행)', 'BNK부산은행', '광주은행', '제주은행', '전북은행', 'BNK경남은행', '케이뱅크', '카카오뱅크', '토스뱅크']"
        :periods="[1, 3, 6, 12, 24, 36]"
        :subscriptionMethods="['전체', '영업점', '인터넷뱅킹', '스마트뱅킹', '전화', '기타']"
        :savingMethods="['정액적립식', '자유적립식']"
        @search="searchProducts"
      />

      <!-- Results Table -->
      <RecommendationResultTableDeposit
        v-if="activeTab === 'deposit'"
        :tableHeaders="depositTableHeaders"
        :products="products"
        :sortOrder="sortOrder"
      />
      <RecommendationResultTableSaving
        v-else
        :tableHeaders="savingTableHeaders"
        :products="products"
        :sortOrder="sortOrder"
      />
    </div>
  </div>
</template>