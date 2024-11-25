<template>
  <div class="banner-wrapper w-full">
    <div class="mx-auto mb-9">
      <!-- Splide 캐러셀 -->
      <Splide :options="splideOptions" aria-label="Home Page Banner Carousel">
        <!-- 슬라이드 반복 렌더링 -->
        <SplideSlide v-for="(slide, index) in slides" :key="index">
          <div
            class="relative h-96 overflow-hidden rounded-lg"
            :style="{ backgroundColor: slide.color }"
          >
            <!-- 어두운 배경 오버레이 -->
            <div
              class="absolute inset-0 bg-black bg-opacity-40 transition-opacity"
            ></div>
            <!-- 슬라이드 콘텐츠 -->
            <div
              class="absolute inset-0 flex flex-col items-center justify-center text-center space-y-4"
            >
              <h2
                class="text-white font-bold text-2xl sm:text-3xl lg:text-4xl tracking-wide drop-shadow-lg"
              >
                {{ slide.title }}
              </h2>
              <button
                v-if="slide.buttonText === 'Click!'"
                @click="openCookieClickerView"
                class="bg-white font-bold py-3 px-6 sm:py-4 sm:px-8 lg:py-5 lg:px-10 rounded-full text-lg sm:text-xl lg:text-2xl shadow-xl transform transition-transform hover:scale-105 hover:bg-opacity-95"
                :style="{ color: slide.color }"
                :aria-label="'Go to ' + slide.buttonText"
              >
                {{ slide.buttonText }}
              </button>
              <button
                v-else-if="slide.buttonText === 'Explore!'"
                @click="openPachinkoView"
                class="bg-white font-bold py-3 px-6 sm:py-4 sm:px-8 lg:py-5 lg:px-10 rounded-full text-lg sm:text-xl lg:text-2xl shadow-xl transform transition-transform hover:scale-105 hover:bg-opacity-95"
                :style="{ color: slide.color }"
                :aria-label="'Go to ' + slide.buttonText"
              >
                {{ slide.buttonText }}
              </button>
              <button
                v-else-if="slide.buttonText === 'Deposit More!'"
                @click="openPersonalDepositRecommendationView"
                class="bg-white font-bold py-3 px-6 sm:py-4 sm:px-8 lg:py-5 lg:px-10 rounded-full text-lg sm:text-xl lg:text-2xl shadow-xl transform transition-transform hover:scale-105 hover:bg-opacity-95"
                :style="{ color: slide.color }"
                :aria-label="'Go to ' + slide.buttonText"
              >
                {{ slide.buttonText }}
              </button>
              <button
                v-else-if="slide.buttonText === 'Saving More!'"
                @click="openPersonalSavingRecommendationView"
                class="bg-white font-bold py-3 px-6 sm:py-4 sm:px-8 lg:py-5 lg:px-10 rounded-full text-lg sm:text-xl lg:text-2xl shadow-xl transform transition-transform hover:scale-105 hover:bg-opacity-95"
                :style="{ color: slide.color }"
                :aria-label="'Go to ' + slide.buttonText"
              >
                {{ slide.buttonText }}
              </button>
            </div>
          </div>
        </SplideSlide>
      </Splide>
    </div>
  </div>
</template>

<script setup>
import { Splide, SplideSlide } from "@splidejs/vue-splide";
import "@splidejs/splide/dist/css/splide.min.css";
import { useRouter } from "vue-router";

const router = useRouter();

// 슬라이드 데이터
const slides = [
  { color: "#44AAE2", buttonText: "Click!", title: "쿠키클릭커" },
  { color: "#E24444", buttonText: "Explore!", title: "DALANG 미니게임" },
  {
    color: "#44E250",
    buttonText: "Deposit More!",
    title: "당신만을 위한 예금상품추천",
  },
  {
    color: "#F6BB43",
    buttonText: "Saving More!",
    title: "당신만을 위한 적금상품추천",
  },
];

// Splide 옵션
const splideOptions = {
  type: "loop",
  perPage: 1,
  autoplay: true,
  pauseOnHover: true,
  interval: 4000, // 전환 간격
  speed: 800, // 전환 애니메이션 속도
  arrows: true,
  pagination: true,
};

// Explore 버튼 클릭 시 새 창 열기
const openPachinkoView = () => {
  const newWindow = window.open("/pachinko", "_blank", "width=800,height=600");
};
const openCookieClickerView = () => {
  const newWindow = window.open(
    "/cookieClicker",
    "_blank",
    "width=800,height=600"
  );
};
const openPersonalDepositRecommendationView = () => {
  const newWindow = window.open(
    "/personal-deposit-recommendation",
    "_blank",
    "width=800,height=600"
  );
};
const openPersonalSavingRecommendationView = () => {
  const newWindow = window.open(
    "/personal-saving-recommendation",
    "_blank",
    "width=800,height=600"
  );
};
</script>

<style scoped>
/* 기존 규격 유지 */
.banner-wrapper {
  max-width: 1200px;
  /* 너비를 고정 */
  margin: auto;
  /* 가운데 정렬 */
}

button {
  transition: all 0.3s ease-in-out;
}

button:hover {
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
}

h2 {
  animation: fadeInDown 1s ease-in-out;
}

/* 애니메이션 정의 */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
