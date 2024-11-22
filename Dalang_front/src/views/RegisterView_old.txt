<template>
    <!-- 전체 페이지 컨테이너 -->
    <div class="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mx-auto">
            <!-- 헤더 섹션 -->
            <header class="text-center mb-12">
                <h1 class="text-3xl font-bold text-gray-900 mb-2">FinanceWise</h1>
                <p class="text-lg text-gray-600">Personalized financial product recommendations tailored just for you
                </p>
            </header>

            <!-- 메인 컨텐츠 영역 -->
            <div class="bg-white shadow-lg rounded-lg overflow-hidden">
                <div class="p-6 sm:p-8">
                    <!-- 진행 상태 표시기 -->
                    <ol class="flex items-center justify-center mb-8">
                        <!-- 각 단계를 나타내는 동적 리스트 아이템 -->
                        <li v-for="(step, index) in steps" :key="index" class="flex items-center"
                            :class="{ 'text-blue-600 font-semibold': currentStep === index + 1, 'text-gray-400': currentStep !== index + 1 }">
                            <!-- 단계 번호 원 -->
                            <span class="w-8 h-8 flex items-center justify-center border-2 rounded-full mr-2"
                                :class="{ 'border-blue-600 bg-blue-600 text-white': currentStep === index + 1, 'border-gray-300': currentStep !== index + 1 }">
                                {{ index + 1 }}
                            </span>
                            {{ step }}
                            <!-- 단계 사이의 화살표 (마지막 단계 제외) -->
                            <svg v-if="index < steps.length - 1" class="w-5 h-5 mx-2" fill="currentColor"
                                viewBox="0 0 20 20">
                                <path fill-rule="evenodd"
                                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                    clip-rule="evenodd" />
                            </svg>
                        </li>
                    </ol>

                    <!-- 단계 1: 사용자 정보 입력 폼 -->
                    <div v-if="currentStep === 1" key="user-info">
                        <h2 class="text-2xl font-semibold text-gray-900 mb-6">Your Information</h2>
                        <form @submit.prevent="nextStep" class="space-y-6">
                            <!-- 나이 입력 필드 -->
                            <div>
                                <label for="age" class="block text-sm font-medium text-gray-700">Age</label>
                                <input type="number" id="age" v-model="userInfo.age" required
                                    class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                            </div>
                            <!-- 연간 수입 입력 필드 -->
                            <div>
                                <label for="income" class="block text-sm font-medium text-gray-700">Annual
                                    Income</label>
                                <input type="number" id="income" v-model="userInfo.income" required
                                    class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                            </div>
                            <!-- 위험 감수성 선택 필드 -->
                            <div>
                                <label for="riskTolerance" class="block text-sm font-medium text-gray-700">Risk
                                    Tolerance</label>
                                <select id="riskTolerance" v-model="userInfo.riskTolerance" required
                                    class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                                    <option value="">Select...</option>
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                            </div>
                            <!-- 투자 목표 입력 필드 -->
                            <div>
                                <label for="investmentGoal" class="block text-sm font-medium text-gray-700">Investment
                                    Goal</label>
                                <input type="text" id="investmentGoal" v-model="userInfo.investmentGoal" required
                                    class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                            </div>
                            <!-- 다음 단계로 이동하는 버튼 -->
                            <div>
                                <button type="submit"
                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                                    Next
                                </button>
                            </div>
                        </form>
                    </div>

                    <!-- 단계 2: 사용자 선호도 선택 -->
                    <div v-else-if="currentStep === 2" key="preferences">
                        <h2 class="text-2xl font-semibold text-gray-900 mb-6">Your Preferences</h2>
                        <div class="space-y-6">
                            <!-- 각 선호도 옵션에 대한 토글 스위치 -->
                            <div v-for="(preference, index) in preferences" :key="index"
                                class="flex items-center justify-between">
                                <span class="text-sm font-medium text-gray-700">{{ preference.label }}</span>
                                <label class="switch">
                                    <input type="checkbox" v-model="preference.value">
                                    <span class="slider round"></span>
                                </label>
                            </div>
                            <!-- 추천 받기 버튼 -->
                            <div>
                                <button @click="nextStep"
                                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                                    Get Recommendations
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- 단계 3: 추천 결과 표시 -->
                    <div v-else key="results">
                        <h2 class="text-2xl font-semibold text-gray-900 mb-6">Your Recommendations</h2>
                        <!-- 추천 상품 그리드 -->
                        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                            <!-- 각 추천 상품 카드 -->
                            <div v-for="(product, index) in recommendedProducts" :key="index"
                                class="bg-white overflow-hidden shadow rounded-lg border border-gray-200 transition-all duration-300 hover:shadow-xl">
                                <div class="p-5">
                                    <!-- 상품 아이콘 -->
                                    <div
                                        class="flex items-center justify-center w-12 h-12 rounded-md bg-blue-500 text-white mb-4">
                                        <component :is="product.icon" class="w-6 h-6" />
                                    </div>
                                    <!-- 상품 이름 -->
                                    <h3 class="text-lg font-medium text-gray-900">{{ product.name }}</h3>
                                    <!-- 상품 설명 -->
                                    <p class="mt-2 text-sm text-gray-500">{{ product.description }}</p>
                                    <!-- 상품 유형 태그 -->
                                    <div class="mt-4">
                                        <span
                                            class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blue-600 bg-blue-200">
                                            {{ product.type }}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- 다시 시작 버튼 -->
                        <div class="mt-8">
                            <button @click="resetForm"
                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                                Start Over
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { CreditCard, Banknote, BarChart } from 'lucide-vue-next';

// 현재 단계를 추적하는 반응형 변수
const currentStep = ref(1);

// 단계 이름 배열
const steps = ['Your Information', 'Preferences', 'Recommendations'];

// 사용자 정보를 저장하는 반응형 객체
const userInfo = reactive({
    age: '',
    income: '',
    riskTolerance: '',
    investmentGoal: ''
});

// 사용자 선호도를 저장하는 반응형 배열
const preferences = reactive([
    { label: 'High Returns', value: false },
    { label: 'Low Risk', value: false },
    { label: 'Short-term Goals', value: false },
    { label: 'Long-term Growth', value: false },
    { label: 'Regular Income', value: false }
]);

// 추천 상품 목록 (실제 애플리케이션에서는 API 호출 결과로 대체될 수 있음)
const recommendedProducts = [
    {
        name: 'High-Yield Savings Account',
        description: 'Safe and liquid savings with competitive interest rates.',
        type: 'Savings',
        icon: Banknote
    },
    {
        name: 'Balanced Mutual Fund',
        description: 'Diversified investment for moderate growth and income.',
        type: 'Investment',
        icon: BarChart
    },
    {
        name: 'Rewards Credit Card',
        description: 'Earn cashback or points on your everyday spending.',
        type: 'Credit',
        icon: CreditCard
    }
];

// 다음 단계로 이동하는 함수
const nextStep = () => {
    if (currentStep.value < 3) {
        currentStep.value++;
    }
};

// 폼을 초기 상태로 리셋하는 함수
const resetForm = () => {
    currentStep.value = 1;
    Object.keys(userInfo).forEach(key => userInfo[key] = '');
    preferences.forEach(pref => pref.value = false);
};
</script>

<style scoped>
/* 토글 스위치 스타일링 */
.switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: .4s;
}

.slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: .4s;
}

input:checked+.slider {
    background-color: #2196F3;
}

input:focus+.slider {
    box-shadow: 0 0 1px #2196F3;
}

input:checked+.slider:before {
    transform: translateX(26px);
}

.slider.round {
    border-radius: 34px;
}

.slider.round:before {
    border-radius: 50%;
}
</style>