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
            <form @submit.prevent="nextStep" class="space-y-6">
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
                <button @click="nextStep"
                  class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                  Next
                </button>
              </div>
            </form>
          </div>
          <!-- 단계 3: Human Verification -->
          <div v-else-if="currentStep === 3" key="human-verification" class="max-w-md mx-auto">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Human Verification</h2>
            <p class="mb-4 text-center">Please select all images containing a dog.</p>
            <div class="grid grid-cols-3 gap-4 mb-6">
              <div v-for="(image, index) in displayedImages" :key="index" class="relative">
                <img :src="image.src" :alt="`Image ${index + 1}`" class="w-full h-auto rounded-lg cursor-pointer"
                  :class="{ 'ring-2 ring-blue-500': selectedImages.includes(index) }" @click="toggleSelection(index)" />
                <div v-if="selectedImages.includes(index)" class="absolute top-2 left-2 bg-blue-500 rounded-full p-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white" viewBox="0 0 20 20"
                    fill="currentColor">
                    <path fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd" />
                  </svg>
                </div>
              </div>
            </div>
            <div class="flex flex-col items-center justify-between mt-6">
              <div class="flex justify-between w-full mb-4">
                <button @click="previousStep"
                  class="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                  Back
                </button>
                <button v-if="!verificationSuccess" @click="verifyCaptcha"
                  class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                  Verify
                </button>
                <button v-else @click="register"
                  class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                  Register
                </button>
              </div>
              <p :class="['text-center w-full', resultClass]">
                {{ resultMessage }}
              </p>
            </div>
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
      steps: ['Your Information', 'Additional Information', 'Human Verification'],
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
      ],
      verificationSuccess: false,
      attemptCount: 0,
      maxAttempts: 3,
      displayedImages: [],
      selectedImages: [],
      verificationResult: null,
      allImages: Array.from({ length: 24 }, (_, i) => ({
        src: `src/assets/verifyingimages/cropped_image_${i + 1}.jpg`,
        number: i + 1
      })),
      humanImages: [2, 4, 5, 7, 9, 11, 14, 16, 18, 20, 21, 23]
    };
  },
  computed: {
  resultClass() {
    if (this.verificationResult === null) return '';
    if (this.verificationResult === 'success') return 'text-green-600';
    if (this.verificationResult === 'partial') return 'text-yellow-600';
    return 'text-red-600';
  },
  resultMessage() {
    if (this.verificationResult === null) return null;
    if (this.verificationResult === 'success') return 'Verification successful! You can now register.';
    if (this.verificationResult === 'partial') return '정답을 모두 맞추지 못했습니다. 다시 시도해보세요.';
    return '흠.. 그건 개인데요, human이 아니신가봐요';
  }
},
  methods: {
    nextStep(event) {
      if (event) {
        event.preventDefault();
      }
      if (this.currentStep < this.steps.length) {
        this.$nextTick(() => {
          this.currentStep++;
          if (this.currentStep === 3) {
            this.generateCaptcha();
          }
        });
      }
    },
    previousStep() {
      if (this.currentStep > 1) {
        this.currentStep--;
      }
    },
    generateCaptcha() {
      this.displayedImages = this.shuffleArray([...this.allImages]).slice(0, 9);
      this.selectedImages = [];
      this.verificationResult = null;
    },
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    },
    toggleSelection(index) {
      const i = this.selectedImages.indexOf(index);
      if (i === -1) {
        this.selectedImages.push(index);
      } else {
        this.selectedImages.splice(i, 1);
      }
    },
    verifyCaptcha() {
      const selectedNumbers = this.selectedImages.map(index => this.displayedImages[index].number);
      const correctAnswers = this.displayedImages.filter(img => this.humanImages.includes(img.number));

      if (selectedNumbers.length === correctAnswers.length &&
        selectedNumbers.every(num => this.humanImages.includes(num))) {
        this.verificationResult = 'success';
        this.verificationSuccess = true;
      } else if (selectedNumbers.every(num => this.humanImages.includes(num))) {
        this.verificationResult = 'partial';
      } else {
        this.verificationResult = 'wrong';
        this.attemptCount++;
      }

      if (this.attemptCount >= this.maxAttempts) {
        alert("나가주세요");
        window.close();
      } else if (!this.verificationSuccess) {
        this.generateCaptcha();
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
  },
  mounted() {
    this.$nextTick(() => {
      const form = this.$el.querySelector('form');
      if (form) {
        console.log('Form is connected to DOM');
      }
    });
  }
};
</script>