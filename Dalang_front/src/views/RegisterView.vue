<template>
  <div v-if="isModalOpen" class="modal-overlay">
    <div class="register-container">
      <h1>회원가입</h1>
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="username">사용자 이름</label>
          <input
            id="username"
            type="text"
            v-model="username"
            required
            placeholder="사용자 이름"
          />
        </div>

        <div class="form-group">
          <label for="password1">비밀번호</label>
          <input
            id="password1"
            type="password"
            v-model="password1"
            required
            placeholder="비밀번호"
          />
        </div>

        <div class="form-group">
          <label for="password2">비밀번호 확인</label>
          <input
            id="password2"
            type="password"
            v-model="password2"
            required
            placeholder="비밀번호 확인"
          />
        </div>

        <div class="form-group">
          <label for="age">나이</label>
          <input
            id="age"
            type="number"
            v-model="age"
            min="0"
            required
            placeholder="나이"
          />
        </div>

        <div class="form-group">
          <label for="gender">성별 (1: 남성, 2: 여성)</label>
          <select id="gender" v-model="gender" required>
            <option value="1">남성</option>
            <option value="2">여성</option>
          </select>
        </div>

        <div class="form-group">
          <label for="salary">연봉</label>
          <input
            id="salary"
            type="number"
            v-model="salary"
            placeholder="연봉"
          />
        </div>

        <div class="form-group">
          <label for="wealth">자산</label>
          <input
            id="wealth"
            type="number"
            v-model="wealth"
            placeholder="자산"
          />
        </div>

        <div class="form-group">
          <label for="tendency">투자 성향 (1: 초고위험 - 5: 초저위험)</label>
          <select id="tendency" v-model="tendency" required>
            <option value="1">초고위험</option>
            <option value="2">고위험</option>
            <option value="3">중위험</option>
            <option value="4">저위험</option>
            <option value="5">초저위험</option>
          </select>
        </div>

        <button type="submit">회원가입</button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'RegisterComponent',
  setup() {
    // 반응형 변수 선언
    const isModalOpen = ref(true);
    const username = ref('');
    const password1 = ref('');
    const password2 = ref('');
    const age = ref(20);
    const gender = ref(1);
    const salary = ref(-1);
    const wealth = ref(-1);
    const tendency = ref(1);

    // 회원가입 메서드
    const register = function() {
      sendRegistrationRequest()
        .then(() => {
          alert('회원가입이 완료되었습니다!');
          isModalOpen.value = false;
          // 현재 모달 창 닫기!
          window.close()
        })
        .catch((error) => {
          console.error('Registration error:', error.response || error);
          alert('회원가입 중 오류가 발생했습니다. 다시 시도해 주세요.');
        });
    };

    // 회원가입 요청 메서드
    const sendRegistrationRequest = async function() {
      const form = {
        username: username.value,
        password1: password1.value,
        password2: password2.value,
        age: age.value,
        gender: gender.value,
        salary: salary.value,
        wealth: wealth.value,
        tendency: tendency.value,
      };
      const response = await axios.post(`${API_URL}/accounts/signup/`, form);
      console.log('Registration successful:', response.data);
    };
    
    // 반환 객체
    return {
      isModalOpen,
      username,
      password1,
      password2,
      age,
      gender,
      salary,
      wealth,
      tendency,
      register,
    };
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input,
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #44AAE2;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #3598c0;
}
</style>