<template>
    <h1 class="text-2xl sm:text-3xl font-semibold text-gray-900 mb-6">회원 정보 수정</h1>
    <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">

        <form @submit.prevent="saveChanges" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label for="username" class="block text-sl font-medium text-gray-700">사용자 이름</label>
                    <input type="text" id="username" v-model="formData.username"
                        class="mt-1 block w-full border-gray-400 rounded-md shadow-sm focus:ring-primary sm:text-sl"
                        required>
                </div>
                <div>
                    <label for="age" class="block text-sl font-medium text-gray-700">나이</label>
                    <input type="number" id="age" v-model="formData.age"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                </div>
                <div>
                    <label for="gender" class="block text-sl font-medium text-gray-700">성별</label>
                    <select id="gender" v-model="formData.gender"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                        <option value="1">남성</option>
                        <option value="2">여성</option>
                    </select>
                </div>

                <div>
                    <label for="tendency" class="block text-sl font-medium text-gray-700">투자 성향</label>
                    <select id="tendency" v-model="formData.tendency"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                        <option value="1">초고위험</option>
                        <option value="2">고위험</option>
                        <option value="3">중위험</option>
                        <option value="4">저위험</option>
                        <option value="5">초저위험</option>
                    </select>
                </div>

                <div>
                    <label for="marital_status" class="block text-sl font-medium text-gray-700">결혼 여부</label>
                    <select id="marital_status" v-model="formData.marital_status"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                        <option value="0">미혼</option>
                        <option value="1">기혼</option>
                    </select>
                </div>

                <div>
                    <label for="employment_status" class="block text-sl font-medium text-gray-700">고용 상태</label>
                    <select id="employment_status" v-model="formData.employment_status"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                        <option value="0">실업</option>
                        <option value="1">고용</option>
                    </select>
                </div>

                <div>
                    <label for="investment_experience" class="block text-sl font-medium text-gray-700">투자 경험</label>
                    <select id="investment_experience" v-model="formData.investment_experience"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                        <option value="0">없음</option>
                        <option value="1">있음</option>
                    </select>
                </div>
            </div>
            <div class="space-y-4 mt-6">
                <div>
                    <label for="password1" class="block text-sl font-medium text-gray-700">새 비밀번호</label>
                    <input type="password" id="password1" v-model="formData.password1"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl">
                </div>
                <div>
                    <label for="password2" class="block text-sl font-medium text-gray-700">새 비밀번호 확인</label>
                    <input type="password" id="password2" v-model="formData.password2"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl">
                </div>
            </div>
            <div class="mt-8">
                <button type="submit" :disabled="!isFormValid"
                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sl font-medium text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary">
                    수정
                </button>
            </div>
        </form>
        <div v-if="passwordMismatch" class="text-red-500 mt-2">
            비밀번호가 일치하지 않습니다.
        </div>
        <div v-if="successMessage" class="mt-4 p-4 bg-green-100 text-green-700 rounded-md">
            {{ successMessage }}
        </div>
        <div v-if="errorMessage" class="mt-4 p-4 bg-red-100 text-red-700 rounded-md">
            {{ errorMessage }}
        </div>
    </div>


</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const successMessage = ref('');
const errorMessage = ref('');

const passwordsMatch = computed(() => {
    return formData.value.password1 === formData.value.password2;
});
const passwordMismatch = computed(() => {
    return formData.value.password1 && formData.value.password2 && !passwordsMatch.value;
});
const formData = ref({
    username: '',
    age: null,
    gender: null,
    salary: null,
    wealth: null,
    tendency: null,
    marital_status: null,
    num_of_dependents: null,
    employment_status: null,
    credit_score: null,
    monthly_expense: null,
    investment_experience: null,
});

const fetchUserData = async () => {
    const token = localStorage.getItem('authToken');
    if (token) {
        try {
            const response = await axios.get('http://127.0.0.1:8000/accounts/user/', {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            // 응답 데이터로 formData 초기화
            formData.value.username = response.data.username;
            formData.value.age = response.data.age;
            formData.value.gender = response.data.gender;
            formData.value.salary = response.data.salary;
            formData.value.wealth = response.data.wealth;
            formData.value.tendency = response.data.tendency;
            formData.value.marital_status = response.data.marital_status;
            formData.value.num_of_dependents = response.data.num_of_dependents;
            formData.value.employment_status = response.data.employment_status;
            formData.value.credit_score = response.data.credit_score;
            formData.value.monthly_expense = response.data.monthly_expense;
            formData.value.investment_experience = response.data.investment_experience;

        } catch (error) {
            console.error('Error fetching user data:', error);
        }
    }
};

onMounted(() => {
    fetchUserData();
});
const saveChanges = async () => {
    const token = localStorage.getItem('authToken');
    if (token) {
        try {
            const dataToSend = { ...formData.value };
            if (dataToSend.password1 && passwordsMatch.value) {
                dataToSend.password = dataToSend.password1;
            }
            delete dataToSend.password1;
            delete dataToSend.password2;

            const response = await axios.put('http://127.0.0.1:8000/accounts/user/', dataToSend, {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            alert('회원 정보 수정이 완료되었습니다.');
            router.push('/');
        } catch (error) {
            console.error('Error updating user data:', error.response?.data || error.message);
            errorMessage.value = '회원 정보 업데이트 중 오류가 발생했습니다: ' + (error.response?.data?.message || error.message);
        }
    }
};

const isFormValid = computed(() => {
    return formData.value.username &&
        formData.value.age &&
        formData.value.gender &&
        formData.value.salary &&
        formData.value.wealth &&
        formData.value.tendency &&
        (!formData.value.password1 || passwordsMatch.value);
});
</script>

<style>
:root {
    --color-primary: #115583;
    --color-primary-dark: #0e4669;
    --color-secondary: #44AAE2;
}

.bg-primary {
    background-color: var(--color-primary);
}

.hover\:bg-primary-dark:hover {
    background-color: var(--color-primary-dark);
}

.focus\:ring-primary:focus {
    --tw-ring-color: var(--color-primary);
}

.focus\:border-primary:focus {
    border-color: var(--color-primary);
}

.text-primary {
    color: var(--color-primary);
}

.border-primary {
    border-color: var(--color-primary);
}

@media (max-width: 640px) {
    .sm\:max-w-xl {
        max-width: 100%;
    }

    .sm\:rounded-3xl {
        border-radius: 0;
    }

    .sm\:p-20 {
        padding: 1rem;
    }
}

input,
select {
    border: 2px solid #cbd5e0 !important;
    /* 테두리 두께를 2px로 증가 */
    transition: all 0.3s ease;
}

input:focus,
select:focus {
    border-color: var(--color-primary) !important;
    box-shadow: 0 0 0 2px rgba(17, 85, 131, 0.2) !important;
    outline: none;
}

/* hover 효과 추가 */
input:hover,
select:hover {
    border-color: var(--color-secondary) !important;
}

/* placeholder 스타일 추가 */
input::placeholder {
    color: #a0aec0;
}

/* select 옵션 스타일 */
select option {
    padding: 10px;
}

/* 나머지 스타일은 그대로 유지 */
:root {
    --color-primary: #115583;
    --color-primary-dark: #0e4669;
    --color-secondary: #44AAE2;
}
</style>