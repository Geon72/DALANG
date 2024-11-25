<script setup>
import { ref } from "vue";
import NavigationBar from "@/components/NavigationBar.vue";
import RecommendationFilterSectionDeposit from "@/components/RecommendationFilterSectionDeposit.vue";
import RecommendationResultTableDeposit from "@/components/RecommendationResultTableDeposit.vue";

const depositTableHeaders = [
  "은행",
  "상품명",
  "기본금리",
  "우대금리",
  "최고금리",
  "상세정보",
];
const depositProducts = ref([]); // API로부터 필터링된 상품 데이터 저장
const sortOrder = ref("desc");

const searchDeposits = async (filters) => {
  try {
    const response = await fetch(
      "http://127.0.0.1:8000/products/filter/deposit/",
      {
        method: "POST",
        headers: {
          Authorization: `Token ${localStorage.getItem("authToken")}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(filters),
      }
    );

    if (!response.ok) {
      const errorText = await response.text();
      console.error("API Error:", errorText);
      throw new Error(`Failed to fetch: ${response.statusText}`);
    }

    const data = await response.json();
    depositProducts.value = data.products;
  } catch (error) {
    console.error("Error fetching filtered deposits:", error);
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavigationBar />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h2 class="text-3xl font-bold mb-4">정기예금 상품 추천</h2>
      <!-- Filter Section -->
      <RecommendationFilterSectionDeposit
        :banks="[
          'KDB산업은행',
          'NH농협은행',
          '신한은행',
          '우리은행',
          'SC제일은행',
          '하나은행',
          'IBK기업은행',
          'KB국민은행',
          '한국씨티은행',
          'Sh수협은행',
          'iM뱅크(구 대구은행)',
          'BNK부산은행',
          '광주은행',
          '제주은행',
          '전북은행',
          'BNK경남은행',
          '케이뱅크',
          '카카오뱅크',
          '토스뱅크',
        ]"
        :periods="[1, 3, 6, 12, 24, 36]"
        :subscriptionMethods="[
          '전체',
          '영업점',
          '인터넷뱅킹',
          '스마트뱅킹',
          '전화',
          '기타',
        ]"
        @search="searchDeposits"
      />

      <!-- Results Table -->
      <RecommendationResultTableDeposit
        :tableHeaders="depositTableHeaders"
        :products="depositProducts"
        :sortOrder="sortOrder"
      />
    </div>
  </div>
</template>
