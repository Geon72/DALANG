import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  // 로그인 기능
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(localStorage.getItem('authToken') || null)

  const isLogin = computed(() => !!token.value) // token이 존재하면 true, 없으면 false

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      // url: `${API_URL}/api/v1/articles/`,
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${token.value}` // 이건 정해진 규칙이다!
      }
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 회원가입 요청 액션
  const signUp = function (payload) {
    // const username = payload.username
    // const password1 = payload.password
    // const password2 = payload.password2
    // Django에서 받는 필드명이 password1과 password2이다

    // 구조 분해 할당
    const { 
      username, password1, password2, age, gender, salary, wealth, 
      tendency, marital_status, num_of_dependents, employment_status, 
      credit_score, monthly_expense, investment_experience 
    } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, age, gender, salary, wealth, 
        tendency, marital_status, num_of_dependents, employment_status, 
        credit_score, monthly_expense, investment_experience
      }
    })
      .then((res) => {
        console.log(res)
        console.log('success')
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    // 구조 분해 할당
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        // 단축 객체 표현 -> 키와 변수명이 같으면
        username, password
      }
    })
      .then((res) => {
        // console.log(res)
        // console.log('success')
        token.value = res.data.key
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const logOut = () => {
    token.value = null // 토큰 제거
    localStorage.removeItem('authToken') // 로컬 스토리지에서도 제거
    console.log('로그아웃 완료') // 디버깅용 로그
  }

  return { count, doubleCount, increment, logOut, articles, API_URL, getArticles, signUp, logIn, token, isLogin }
})
