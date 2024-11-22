<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <!-- 헤더 섹션 -->
      <header class="text-center mb-12">
        <h1 class="text-4xl font-bold text-gray-600 mb-2">회원가입</h1>
        <p class="text-lg text-gray-600">DALANG과 친구 되는 중...</p>
      </header>

      <!-- 메인 컨텐츠 영역 -->
      <div class="bg-white shadow-lg rounded-lg overflow-hidden">
        <div class="p-6 sm:p-8">
          <!-- 진행 상태 표시기 -->
          <ol class="flex items-center justify-center mb-8">
            <li v-for="(step, index) in steps" :key="index" class="flex items-center"
              :class="{ 'text-blue-600 font-semibold': currentStep === index + 1, 'text-gray-400': currentStep !== index + 1 }">
              <span class="w-8 h-8 flex items-center justify-center border-2 rounded-full mr-2"
                :class="{ 'border-blue-600 bg-blue-600 text-white': currentStep === index + 1, 'border-gray-300': currentStep !== index + 1 }">
                {{ index + 1 }}
              </span>
              {{ step }}
              <svg v-if="index < steps.length - 1" class="w-5 h-5 mx-2" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clip-rule="evenodd" />
              </svg>
            </li>
          </ol>

          <!-- 단계 1: 사용자 정보 입력 폼 -->
          <div v-if="currentStep === 1" key="user-info">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">필수 정보를 기입해주세요!</h2>
            <form @submit.prevent="nextStep" class="space-y-6">
              <div v-for="field in formFields.slice(0, 7)" :key="field.id">
                <label :for="field.id" class="block text-sm font-medium text-gray-700">{{ field.label }}</label>
                <input v-if="field.type !== 'select'" :type="field.type" :id="field.id" v-model="formData[field.id]"
                  required
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
                <select v-else :id="field.id" v-model="formData[field.id]" required
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                  <option v-for="option in field.options" :key="option.value" :value="option.value">
                    {{ option.label }}
                  </option>
                </select>
              </div>
              <div>
                <button type="submit"
                  class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                  Next
                </button>
              </div>
            </form>
          </div>

          <!-- 단계 2: 추가 사용자 정보 입력 -->
          <div v-else-if="currentStep === 2" key="additional-info">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">추가 정보도 기입해주세요!</h2>
            <form @submit.prevent="register" class="space-y-6">
              <div v-for="field in formFields.slice(7)" :key="field.id">
                <label :for="field.id" class="block text-sm font-medium text-gray-700">{{ field.label }}</label>
                <input v-if="field.type !== 'select'" :type="field.type" :id="field.id" v-model="formData[field.id]"
                  required
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
                <select v-else :id="field.id" v-model="formData[field.id]" required
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                  <option v-for="option in field.options" :key="option.value" :value="option.value">
                    {{ option.label }}
                  </option>
                </select>
              </div>
              <div class="flex justify-between">
                <button @click="previousStep"
                  class="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                  Back
                </button>
                <button type="submit"
                  class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                  Register
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterComponent',
  data() {
    return {
      currentStep: 1,
      steps: ['Your Information', 'Additional Information'],
      formData: {
        username: '',
        password1: '',
        password2: '',
        age: 20,
        gender: 1,
        salary: -1,
        wealth: -1,
        tendency: 1,
        marital_status: 0,
        num_of_dependents: 0,
        employment_status: 0,
        credit_score: 0,
        monthly_expense: 0,
        investment_experience: 0
      },
      formFields: [
        { id: 'username', label: 'Username', type: 'text' },
        { id: 'password1', label: 'Password', type: 'password' },
        { id: 'password2', label: 'Confirm Password', type: 'password' },
        { id: 'age', label: 'Age', type: 'number' },
        {
          id: 'gender', label: 'Gender', type: 'select', options: [
            { value: 1, label: '남성' },
            { value: 2, label: '여성' }
          ]
        },
        { id: 'salary', label: 'Annual Salary', type: 'number' },
        { id: 'wealth', label: 'Total Wealth', type: 'number' },
        {
          id: 'tendency', label: 'Risk Tendency', type: 'select', options: [
            { value: 1, label: '초고위험' },
            { value: 2, label: '고위험' },
            { value: 3, label: '중위험' },
            { value: 4, label: '저위험' },
            { value: 5, label: '초저위험' }
          ]
        },
        {
          id: 'marital_status', label: 'Marital Status', type: 'select', options: [
            { value: 0, label: '미혼' },
            { value: 1, label: '기혼' }
          ]
        },
        { id: 'num_of_dependents', label: 'Number of Dependents', type: 'number' },
        {
          id: 'employment_status', label: 'Employment Status', type: 'select', options: [
            { value: 0, label: '실업' },
            { value: 1, label: '고용' }
          ]
        },
        { id: 'credit_score', label: 'Credit Score', type: 'number' },
        { id: 'monthly_expense', label: 'Monthly Expense', type: 'number' },
        {
          id: 'investment_experience', label: 'Investment Experience', type: 'select', options: [
            { value: 0, label: '없음' },
            { value: 1, label: '있음' }
          ]
        }
      ]
    };
  },
  methods: {
    nextStep() {
      if (this.currentStep < 2) {
        this.currentStep++;
      }
    },
    previousStep() {
      if (this.currentStep > 1) {
        this.currentStep--;
      }
    },
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/accounts/signup/', this.formData);
        console.log('Registration successful:', response.data);
        alert('회원가입이 완료되었습니다!');
        this.$emit('registration-complete');
        this.$router.push('/login');
      } catch (error) {
        console.error('Registration error:', error.response || error);
        alert('회원가입 중 오류가 발생했습니다. 다시 시도해 주세요.');
      }
    }
  }
};
</script>