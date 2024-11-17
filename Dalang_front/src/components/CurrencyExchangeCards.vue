<template>
    <section class="exchange-rate-section mt-12 px-4 sm:px-6 lg:px-8">
      <h2 class="text-center text-2xl sm:text-3xl font-bold mb-8 bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent">
        여행갈 여행지의 환율을 알아봐요
      </h2>
      
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
        <div 
          v-for="currency in currencies" 
          :key="currency.code"
          class="currency-card bg-white rounded-xl shadow-lg p-6 transform transition-all duration-300 hover:-translate-y-1"
        >
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center">
              <img :src="currency.flag" :alt="currency.name" class="w-8 h-8 mr-3">
              <h3 class="text-lg font-semibold text-[#115583]">{{ currency.name }}</h3>
            </div>
            <span class="text-sm font-medium text-[#44AAE2]">{{ currency.code }}</span>
          </div>
          <div class="text-center">
            <p class="text-3xl font-bold bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent mb-2">
              {{ currency.rate }}
            </p>
            <span class="text-sm text-gray-500 font-medium">1,000 KRW 기준</span>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const currencies = ref([
    {
      name: '미국 외화',
      code: 'USD',
      rate: '0.75',
      flag: '/flags/us.svg'
    },
    {
      name: '일본 외화',
      code: 'JPY',
      rate: '112.50',
      flag: '/flags/jp.svg'
    },
    {
      name: '베트남 외화',
      code: 'VND',
      rate: '18,150',
      flag: '/flags/vn.svg'
    },
    {
      name: '중국 외화',
      code: 'CNY',
      rate: '5.40',
      flag: '/flags/cn.svg'
    },
    {
      name: '유럽 외화',
      code: 'EUR',
      rate: '0.69',
      flag: '/flags/eu.svg'
    }
  ])
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
      rgba(255, 255, 255, 0.85) 100%
    );
  }
  
  /* Responsive adjustments */
  @media (max-width: 640px) {
    .currency-card {
      padding: 1rem;
    }
    
    .text-3xl {
      font-size: 1.5rem;
    }
  }
  </style>