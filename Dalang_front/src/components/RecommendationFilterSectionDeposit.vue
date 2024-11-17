<template>
    <div class="bg-white shadow rounded-lg p-6 mb-8">
      <h2 class="text-2xl font-bold text-[#0088CC] mb-6">금융상품 검색</h2>
      
         <!-- 은행 선택 컴포넌트 -->
      <RecommendationBankSelection
        :banks="banks"
        v-model:selectedBanks="selectedBanks"
      />
  
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <!-- Interest Calculation Method -->
        <div>
          <h3 class="text-lg font-semibold text-gray-700 mb-3">이자 계산방식</h3>
          <div class="flex space-x-4">
            <label class="inline-flex items-center">
              <input type="radio" name="interest-type" value="simple" v-model="interestType" class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC] transition duration-300 ease-in-out">
              <span class="ml-2 text-gray-600">단리</span>
            </label>
            <label class="inline-flex items-center">
              <input type="radio" name="interest-type" value="compound" v-model="interestType" class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC] transition duration-300 ease-in-out">
              <span class="ml-2 text-gray-600">복리</span>
            </label>
          </div>
        </div>
  
        <!-- Maturity Period -->
        <div>
          <h3 class="text-lg font-semibold text-gray-700 mb-3">만기</h3>
          <div class="flex flex-wrap gap-3">
            <label v-for="period in periods" :key="period" class="inline-flex items-center">
              <input type="radio" name="period" :value="period" v-model="selectedPeriod" class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC] transition duration-300 ease-in-out">
              <span class="ml-2 text-gray-600">{{ period }}개월</span>
            </label>
          </div>
        </div>
      </div>
  
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <!-- Subscription Method -->
        <div>
          <h3 class="text-lg font-semibold text-gray-700 mb-3">가입방식</h3>
          <div class="flex flex-wrap gap-3">
            <label v-for="method in subscriptionMethods" :key="method" class="inline-flex items-center">
              <input type="radio" name="subscription" :value="method" v-model="selectedSubscriptionMethod" class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC] transition duration-300 ease-in-out">
              <span class="ml-2 text-gray-600">{{ method }}</span>
            </label>
          </div>
        </div>
  
        <!-- Sort Method -->
        <div>
          <h3 class="text-lg font-semibold text-gray-700 mb-3">정렬방식</h3>
          <div class="flex flex-col sm:flex-row gap-3">
            <select v-model="sortOrder" class="form-select border-2 border-[#0088CC] rounded-md w-full focus:ring-[#0088CC] focus:border-[#0088CC] text-gray-600">
              <option value="asc">오름차순으로 정렬</option>
              <option value="desc">내림차순으로 정렬</option>
            </select>
          </div>
        </div>
      </div>
  
      <!-- Search Button -->
      <div class="flex justify-center">
        <button @click="$emit('search')" class="bg-[#0088CC] text-white px-12 py-3 rounded-lg hover:bg-[#006699] transition-colors text-lg font-semibold shadow-md hover:shadow-lg">
          검색
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import RecommendationBankSelection from './RecommendationBankSelection.vue'
  const props = defineProps({
    banks: Array,
    periods: Array,
    subscriptionMethods: Array
  })
  
  defineEmits(['search'])
  
  const selectAll = ref(false)
  const selectedBanks = ref([])
  const interestType = ref('simple')
  const selectedPeriod = ref('')
  const selectedSubscriptionMethod = ref('전체')
  const sortOrder = ref('desc')
  
  const toggleAllBanks = () => {
    if (selectAll.value) {
      selectedBanks.value = [...props.banks]
    } else {
      selectedBanks.value = []
    }
  }
  
  const updateSelectAllState = () => {
    selectAll.value = selectedBanks.value.length === props.banks.length
  }
  
  watch(selectedBanks, updateSelectAllState)
  </script>
  
  <style scoped>
  .form-checkbox:checked, .form-radio:checked {
    background-color: #0088CC;
    border-color: #0088CC;
  }
  
  .form-checkbox:checked {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
  }
  
  .form-radio:checked {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='8' cy='8' r='3'/%3e%3c/svg%3e");
  }
  
  .form-checkbox:checked:hover, .form-radio:checked:hover {
    background-color: #006699;
    border-color: #006699;
  }
  
  .form-checkbox:focus, .form-radio:focus {
    box-shadow: 0 0 0 3px rgba(0, 136, 204, 0.5);
  }
  
  .select-all-checkbox input[type="checkbox"] {
    transform: scale(1.2);
  }
  
  @keyframes checkboxPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }
  
  .form-checkbox:checked, .form-radio:checked {
    animation: checkboxPulse 0.3s ease-in-out;
  }
  </style>