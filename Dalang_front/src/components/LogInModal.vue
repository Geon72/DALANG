<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 bg-white p-8 rounded-lg shadow-md">
      <div>
        <img class="mx-auto h-12 w-auto"
          src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/DALANG_FINAL-zgVATAcLguH8yROQhqFJRCjh3gdKx4.png"
          alt="DALANG Logo">
        <h2 class="mt-6 text-center text-3xl font-extrabold text-[#115583]">Sign in to your account</h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleSubmit">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="user-id" class="sr-only">ID</label>
              <input id="user-id" name="id" type="text" autocomplete="off" required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-[#44AAE2] focus:border-[#44AAE2] focus:z-10 sm:text-sm"
                placeholder="ID" v-model.trim="id">
          </div>
          <div class="relative">
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" :type="showPassword ? 'text' : 'password'"
              autocomplete="current-password" required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-[#44AAE2] focus:border-[#44AAE2] focus:z-10 sm:text-sm"
              placeholder="Password" v-model.trim="password">
            <button type="button" @click="togglePassword"
              class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
              <span v-if="!showPassword">Show</span>
              <span v-else>Hide</span>
            </button>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input id="remember-me" name="remember-me" type="checkbox" v-model="rememberMe"
              class="h-4 w-4 text-[#44AAE2] focus:ring-[#44AAE2] border-gray-300 rounded">
            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
              Remember me
            </label>
          </div>

          <div class="text-sm">
            <a href="#" class="font-medium text-[#44AAE2] hover:text-[#115583]">
              Forgot your password?
            </a>
          </div>
        </div>

        <div>
          <button type="submit" :disabled="isLoading"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#115583] hover:bg-[#44AAE2] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#44AAE2] transition duration-150 ease-in-out">
            {{ isLoading ? 'Signing in...' : 'Sign in' }}
          </button>
        </div>
      </form>

      <div class="mt-6">
        <div class="relative">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-300"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-2 bg-white text-gray-500">
              Or continue with
            </span>
          </div>
        </div>

        <div class="mt-6 grid grid-cols-2 gap-3">
          <div>
            <a href="#"
              class="w-full inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-[#FEE500] text-sm font-medium text-[#000000] hover:bg-[#FEE500]/90 transition duration-150 ease-in-out">
              Kakao
            </a>
          </div>
          <div>
            <a href="#"
              class="w-full inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 transition duration-150 ease-in-out">
              Google
            </a>
          </div>
        </div>
      </div>

      <p class="mt-2 text-center text-sm text-gray-600">
        Don't have an account?
        <a @click.prevent="goToRegister" class="font-medium text-[#44AAE2] hover:text-[#115583]" href="#">
          Sign up
        </a>
      </p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const id = ref('')
const password = ref('')
const showPassword = ref(false)
const rememberMe = ref(false)
const isLoading = ref(false)
const API_URL = 'http://127.0.0.1:8000'

const router = useRouter()

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

const handleSubmit = async () => {
  isLoading.value = true
  try {
    // Make an API call to your backend for authentication
    const response = await axios.post(`${API_URL}/accounts/login/`, {
      username: id.value,
      password: password.value
    })

    // Handle successful login
    console.log('Login successful', response.data)
    alert('로그인 성공!')
    // 현재 모달 창 닫기!
    window.close()

    // You can save tokens or handle redirection here
    // Example: localStorage.setItem('token', response.data.token)

  } catch (error) {
    // Handle login error
    console.error('Login error', error.response || error)
    alert('로그인 실패! 사용자 이름 또는 비밀번호를 확인해 주세요.')
  } finally {
    isLoading.value = false
  }
}

const goToRegister = () => {
  router.push('/register')
  console.log('fuck')
}
</script>