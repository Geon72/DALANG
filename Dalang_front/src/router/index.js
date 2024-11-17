import { createRouter, createWebHistory } from 'vue-router'
import HomePageView from '@/views/HomePageView.vue'
import FindBankView from '@/views/FindBankView.vue'
import ProfileView from '@/views/ProfileView.vue'
import LoginModal from '@/components/LoginModal.vue'
import RecommendationView from '@/views/RecommendationView.vue'
import CurrencyExchangeView from '@/views/CurrencyExchangeView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePageView
  },
  {
    path: '/find-bank',
    name: 'findBank',
    component: FindBankView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginModal
  },
  {
    path: '/recommendation',
    name: 'recommendation',
    component: RecommendationView
  },
  {
    path: '/currency-exchange',
    name: 'currencyExchange',
    component: CurrencyExchangeView
  },
  // 404 페이지 라우트
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: HomePageView // 또는 별도의 404 페이지 컴포넌트
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router