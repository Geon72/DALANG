import { createRouter, createWebHistory } from "vue-router";
import HomePageView from "@/views/HomePageView.vue";
import FindBankView from "@/views/FindBankView.vue";
import ProfileView from "@/views/ProfileView.vue";
import LogInModal from "@/components/LogInModal.vue";
import RecommendationView from "@/views/RecommendationView.vue";
import CurrencyExchangeView from "@/views/CurrencyExchangeView.vue";
import CommunityView from "@/views/CommunityView.vue";
import PachinkoView from "@/views/PachinkoView.vue";
import CookieClickerView from "@/views/CookieClickerView.vue";
import RegisterView from "@/views/RegisterView.vue";
import UserInfomationUpdateView from "@/views/UserInfomationUpdateView.vue";
import CreatePostView from "@/views/CreatePostView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import PersonalDepositRecommendationView from "@/views/PersonalDepositRecommendationView.vue";
import PersonalSavingRecommendationView from "@/views/PersonalSavingRecommendationView.vue";
import PachinkoGameView from "@/views/PachinkoGameView.vue";
import SecondarySecurityView from "@/views/SecondarySecurityView.vue";
// 회원가입 연습

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePageView,
  },
  {
    path: "/find-bank",
    name: "findBank",
    component: FindBankView,
  },
  {
    path: "/profile/:id?",
    name: "profile",
    component: ProfileView,
    props: true,
  },
  {
    path: "/login",
    name: "login",
    component: LogInModal,
  },
  {
    path: "/recommendation",
    name: "recommendation",
    component: RecommendationView,
  },
  {
    path: "/currency-exchange",
    name: "currencyExchange",
    component: CurrencyExchangeView,
  },
  {
    path: "/community",
    name: "community",
    component: CommunityView,
  },
  // 404 페이지 라우트
  {
    path: "/:pathMatch(.*)*",
    name: "notFound",
    component: HomePageView, // 또는 별도의 404 페이지 컴포넌트
  },
  // 회원가입 연습
  // 파칭코
  {
    path: "/pachinko",
    name: "pachinko",
    component: PachinkoView, // Pachinko View 등록
  },
  {
    path: "/cookieClicker",
    name: "cookieClicker",
    component: CookieClickerView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/user/edit",
    name: "UserInfomationUpdate",
    component: UserInfomationUpdateView,
  },
  {
    path: "/user/createPost",
    name: "createPost",
    component: CreatePostView,
  },
  {
    path: "/articles/:id",
    name: "ArticleDetail",
    component: ArticleDetailView,
    props: true,
  },
  {
    path: "/personal-deposit-recommendation",
    name: "PersonalDepositRecommendationView",
    component: PersonalDepositRecommendationView,
  },
  {
    path: "/personal-saving-recommendation",
    name: "PersonalSavingRecommendationView",
    component: PersonalSavingRecommendationView,
  },
  {
    path: "/secondary-security",
    name: "SecondarySecurityView",
    component: SecondarySecurityView,
  },
  {
    path: "/pachinkogame",
    name: "PachinkoGameView",
    component: PachinkoGameView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
