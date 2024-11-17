<template>
  <div class="bg-white shadow rounded-lg p-6 mb-8">
    <h2 class="text-2xl font-bold text-[#0088CC] mb-6">금융상품 검색</h2>
    
    <!-- 은행 선택 컴포넌트 -->
    <RecommendationBankSelection
      :banks="banks"
      v-model:selectedBanks="selectedBanks"
    />

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <!-- 이자 계산방식 -->
      <div>
        <h3 class="text-lg font-semibold text-gray-700 mb-3">이자 계산방식</h3>
        <div class="flex space-x-4">
          <label class="inline-flex items-center">
            <input type="radio" name="interest-type" value="단리" v-model="interestType" 
                   class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC]">
            <span class="ml-2 text-gray-600">단리</span>
          </label>
          <label class="inline-flex items-center">
            <input type="radio" name="interest-type" value="복리" v-model="interestType" 
                   class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC]">
            <span class="ml-2 text-gray-600">복리</span>
          </label>
        </div>
      </div>
    
    
    <!-- 만기 -->
      <div>
        <h3 class="text-lg font-semibold text-gray-700 mb-3">만기</h3>
        <div class="flex flex-wrap gap-3">
          <label v-for="period in periods" :key="period" class="inline-flex items-center">
            <input type="radio" name="period" :value="period" v-model="selectedPeriod" 
                  class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC]">
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
      
          <!-- 적립방식 -->
        <div>
        <h3 class="text-lg font-semibold text-gray-700 mb-3">적립방식</h3>
        <div class="flex space-x-4">
          <label class="inline-flex items-center">
            <input type="radio" name="saving-type" value="정액적립식" v-model="savingType" 
                   class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC]">
            <span class="ml-2 text-gray-600">정액적립식</span>
          </label>
          <label class="inline-flex items-center">
            <input type="radio" name="saving-type" value="자유적립식" v-model="savingType" 
                   class="form-radio h-5 w-5 text-[#0088CC] border-2 border-[#0088CC] focus:ring-[#0088CC]">
            <span class="ml-2 text-gray-600">자유적립식</span>
          </label>
        </div>
      </div>
    

      
    </div>

    <!-- 검색 버튼 -->
    <div class="flex justify-center">
      <button @click="handleSearch" 
              class="bg-[#0088CC] text-white px-12 py-3 rounded-lg hover:bg-[#006699] transition-colors text-lg font-semibold">
        검색
      </button>
    </div>
  </.div>
</template>

<script setup>
import { ref } from 'vue'
import RecommendationBankSelection from './RecommendationBankSelection.vue'

const props = defineProps({
  banks: Array,
  periods: Array,
  subscriptionMethods: Array
})

const emit = defineEmits(['search'])

const selectedBanks = ref([])
const interestType = ref('단리')
const selectedPeriod = ref("")
const selectedSubscriptionMethod = ref('전체')
const savingType = ref('정액적립식')
const sortOrder = ref('desc')

const handleSearch = () => {
  emit('search', {
    selectedBanks: selectedBanks.value,
    savingType: savingType.value,
    interestType: interestType.value,
    period: selectedPeriod.value,
    subscriptionMethod: selectedSubscriptionMethod.value,
    sortOrder: sortOrder.value
  })
}
</script>

<style scoped>
.form-radio:checked {
  background-color: #0088CC;
  border-color: #0088CC;
}

.form-radio:focus {
  box-shadow: 0 0 0 3px rgba(0, 136, 204, 0.5);
}

.form-select:focus {
  border-color: #0088CC;
  box-shadow: 0 0 0 3px rgba(0, 136, 204, 0.5);
}
</style>