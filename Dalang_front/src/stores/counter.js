import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  // 로그인 관련 상태 및 함수
  const token = ref(localStorage.getItem('authToken') || null)
  const isLogin = computed(() => !!token.value) // token이 존재하면 true, 없으면 false
  const userId = ref(localStorage.getItem('userId') || null) // 사용자 ID 상태 추가
  const API_URL = 'http://127.0.0.1:8000'

  // 게시글 관련 상태 및 함수
  const articles = ref([])
  const myPosts = ref([])
  const likedPosts = ref([])

  // 내가 쓴 글 가져오기
  const getMyPosts = async (userId) => {
    try {
      const response = await axios.get(`${API_URL}/articles/user/${userId}/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      myPosts.value = response.data.map(post => ({
        id: post.id,
        title: post.title,
        content: post.content,
        date: new Date(post.created_at).toLocaleDateString(),
        likes: post.like_count,
        comments: post.comment_count
      }))
    } catch (error) {
      console.error('Failed to fetch my posts:', error)
    }
  }

  // 내가 좋아요한 글 가져오기
  const getLikedPosts = async () => {
    try {
      const response = await axios.get(`${API_URL}/articles/liked/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      likedPosts.value = response.data.map(post => ({
        id: post.id,
        title: post.title,
        content: post.content,
        date: new Date(post.created_at).toLocaleDateString(),
        likes: post.like_count,
        comments: post.comment_count
      }))
    } catch (error) {
      console.error('Failed to fetch liked posts:', error)
    }
  }

  // 전체 게시글 가져오기
  const getArticles = async () => {
    try {
      const response = await axios.get(`${API_URL}/articles/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      articles.value = response.data
    } catch (error) {
      console.error('Failed to fetch articles:', error)
    }
  }

  // 로그인 요청 액션
  const logIn = async (payload) => {
    try {
      const { username, password } = payload
      // 로그인 요청
      const response = await axios.post(`${API_URL}/accounts/login/`, { username, password })
      token.value = response.data.key
      localStorage.setItem('authToken', token.value)
  
      // 로그인 성공 후 사용자 정보 요청
      const userResponse = await axios.get(`${API_URL}/accounts/user/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      userId.value = userResponse.data.id
      localStorage.setItem('userId', userId.value)
    } catch (error) {
      console.error('Login failed:', error)
    }
  }

  // 로그아웃 액션
  const logOut = () => {
    token.value = null // 토큰 제거
    localStorage.removeItem('authToken') // 로컬 스토리지에서도 제거
    userId.value = null // 로그아웃 시 사용자 ID 제거
    console.log('로그아웃 완료') // 디버깅용 로그
  }

  return {
    userId,
    count,
    doubleCount,
    increment,
    logOut,
    articles,
    API_URL,
    getArticles,
    logIn,
    token,
    isLogin,
    myPosts,
    likedPosts,
    getMyPosts,
    getLikedPosts
  }
})