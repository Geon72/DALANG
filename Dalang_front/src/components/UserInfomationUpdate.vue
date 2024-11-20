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
                    <label for="salary" class="block text-sl font-medium text-gray-700">연봉</label>
                    <input type="number" id="salary" v-model="formData.salary"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
                </div>
                <div>
                    <label for="wealth" class="block text-sl font-medium text-gray-700">자산</label>
                    <input type="number" id="wealth" v-model="formData.wealth"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary sm:text-sl"
                        required>
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
                <button type="submit"
                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sl font-medium text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary">
                    수정
                </button>
            </div>
        </form>
    </div>


</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const formData = ref({
  username: '',
  age: null,
  gender: '',
  salary: null,
  wealth: null,
  tendency: '',
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
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  }
};

onMounted(() => {
  fetchUserData();
});

const saveChanges = () => {
  console.log('Form data:', formData.value);
  // 여기에 API 호출 및 추가적인 처리 로직을 추가하세요!!
};
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
    border: 2px solid #cbd5e0 !important; /* 테두리 두께를 2px로 증가 */
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