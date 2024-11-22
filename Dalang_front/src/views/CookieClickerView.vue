<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 to-green-900 text-white p-8">
    <h1 class="text-4xl font-bold text-center mb-8">💼 재산 증식 게임</h1>

    <div class="max-w-4xl mx-auto bg-gray-800 rounded-lg shadow-lg p-6">
      <div class="text-center mb-8">
        <p class="text-3xl font-bold">
          <span class="text-green-400">{{ formatNumber(assetValue) }}원</span> 총 자산 가치
        </p>
        <p class="text-xl">
          <span class="text-yellow-400">+{{ formatNumber(totalPerSecond) }}원</span> 초당 수익
        </p>
      </div>

      <button @click="work"
        class="w-48 h-48 mx-auto mb-8 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 rounded-full flex items-center justify-center text-2xl font-bold transition-transform duration-100 transform active:scale-95 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50"
        :class="{ 'animate-pulse': isWorking }">
        일하기
      </button>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
        <div v-for="(investment, id) in investments" :key="id"
          class="bg-gray-700 rounded-lg p-4 flex flex-col justify-between"
          :class="{ 'opacity-75': assetValue < investment.cost }">
          <div>
            <h3 class="text-xl font-bold mb-2">{{ investment.name }}</h3>
            <p class="text-sm mb-2">{{ investment.description }}</p>
            <p class="text-sm">보유: {{ investment.count }}</p>
            <p class="text-sm">수익: +{{ formatNumber(investment.return * investment.count) }}원/초</p>
          </div>
          <button @click="purchaseInvestment(id)" :disabled="assetValue < investment.cost"
            class="mt-4 bg-green-600 hover:bg-green-700 disabled:bg-gray-600 disabled:cursor-not-allowed px-4 py-2 rounded-full text-sm font-bold transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-400 focus:ring-opacity-50">
            {{ formatNumber(investment.cost) }}원 투자
          </button>
        </div>
      </div>

      <div class="bg-gray-700 rounded-lg p-4 mb-8">
        <h2 class="text-2xl font-bold mb-4">금융 이벤트</h2>
        <div v-if="currentEvent" class="mb-4">
          <h3 class="text-xl font-bold">{{ currentEvent.title }}</h3>
          <p>{{ currentEvent.description }}</p>
          <p class="text-sm text-yellow-400">영향: {{ currentEvent.impact }}</p>
        </div>
        <div v-else>현재 진행 중인 이벤트가 없습니다</div>
      </div>

      <div class="bg-gray-700 rounded-lg p-4">
        <h2 class="text-2xl font-bold mb-4">업적</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div v-for="(achievement, index) in achievements" :key="index" class="bg-gray-600 rounded-lg p-4"
            :class="{ 'opacity-50': !achievement.unlocked }">
            <h3 class="text-lg font-bold mb-2">{{ achievement.name }}</h3>
            <p class="text-sm">{{ achievement.description }}</p>
            <p v-if="achievement.unlocked" class="text-green-400 mt-2">달성!</p>
          </div>
        </div>
      </div>
    </div>

    <transition-group name="float" tag="div" class="fixed inset-0 pointer-events-none">
      <div v-for="number in floatingNumbers" :key="number.id" class="absolute text-green-400 font-bold text-5xl"
        :style="{ left: `${number.x}px`, top: `${number.y}px` }">
        +{{ formatNumber(number.value) }}원
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';

const assetValue = ref(0);
const salary = ref(10);
const isWorking = ref(false);
const floatingNumbers = ref([]);
let floatingNumberId = 0;

const addFloatingNumber = (value, x, y) => {
  const id = floatingNumberId++;
  floatingNumbers.value.push({ id, value, x, y });

  setTimeout(() => {
    floatingNumbers.value = floatingNumbers.value.filter(n => n.id !== id);
  }, 500);
};

const work = () => {
  assetValue.value += salary.value;
  isWorking.value = true;
  const button = document.querySelector('button');
  if (button) {
    const rect = button.getBoundingClientRect();
    addFloatingNumber(salary.value, rect.left + Math.random() * rect.width, rect.top);
  }
  setTimeout(() => {
    isWorking.value = false;
  }, 100);
};

const investments = ref({
  savings: {
    name: '저축 계좌',
    description: '안전하지만 낮은 수익률의 투자',
    count: 0,
    return: 0.1,
    cost: 10,
    costIncrease: 5,
  },
  portfolio: {
    name: '투자 포트폴리오',
    description: '높은 수익률이지만 약간의 위험이 있음',
    count: 0,
    return: 1,
    cost: 100,
    costMultiplier: 1.15,
  },
  realEstate: {
    name: '부동산',
    description: '안정적인 장기 수익',
    count: 0,
    return: 10,
    cost: 1000,
    costMultiplier: 1.3,
  },
  business: {
    name: '사업 벤처',
    description: '높은 위험, 높은 잠재적 수익',
    count: 0,
    return: 100,
    cost: 10000,
    costMultiplier: 1.5,
  },
});

const achievements = ref([
  { name: '첫 걸음', description: '첫 100원 벌기', unlocked: false, threshold: 100 },
  { name: '소액 투자자', description: '자산 1,000원 달성하기', unlocked: false, threshold: 1000 },
  { name: '중급 투자자', description: '자산 10,000원 달성하기', unlocked: false, threshold: 10000 },
  { name: '대형 투자자', description: '자산 100,000원 달성하기', unlocked: false, threshold: 100000 },
  { name: '백만장자', description: '자산 1,000,000원 달성하기', unlocked: false, threshold: 1000000 },
  { name: '다각화된 포트폴리오', description: '모든 종류의 투자 상품 최소 1개씩 보유하기', unlocked: false },
]);

const events = [
  { title: '시장 호황', description: '주식 시장이 호황입니다!', impact: '30초 동안 투자 수익이 1.5배로 증가합니다' },
  { title: '경제 불황', description: '경제가 침체기에 접어들었습니다', impact: '30초 동안 투자 수익이 0.75배로 감소합니다' },
  { title: '예상치 못한 지출', description: '예상치 못한 청구서가 도착했습니다', impact: '현재 자산의 5%를 잃습니다' },
  { title: '행운의 날', description: '오늘은 운이 좋은 날입니다!', impact: '일회성으로 현재 자산의 10%를 얻습니다' },
];

const currentEvent = ref(null);

const totalPerSecond = computed(() => {
  return Object.values(investments.value).reduce((total, investment) => {
    return total + investment.return * investment.count;
  }, 0);
});

const purchaseInvestment = (id) => {
  const investment = investments.value[id];
  if (assetValue.value >= investment.cost) {
    assetValue.value -= investment.cost;
    investment.count++;
    if (investment.costIncrease) {
      investment.cost += investment.costIncrease;
    } else if (investment.costMultiplier) {
      investment.cost = Math.floor(investment.cost * investment.costMultiplier);
    }
  }
};

const formatNumber = (num) => {
  if (num === null || num === undefined || isNaN(num)) {
    return '0.00';
  }
  num = Number(num);
  if (num >= 1e9) return (num / 1e9).toFixed(2) + 'B';
  if (num >= 1e6) return (num / 1e6).toFixed(2) + 'M';
  if (num >= 1e3) return (num / 1e3).toFixed(2) + 'K';
  return num.toFixed(2);
};

const checkAchievements = () => {
  achievements.value.forEach(achievement => {
    if (!achievement.unlocked) {
      if (achievement.threshold && assetValue.value >= achievement.threshold) {
        achievement.unlocked = true;
        alert(`업적 달성: ${achievement.name}`);
      } else if (achievement.name === '다각화된 포트폴리오') {
        const allInvestmentsOwned = Object.values(investments.value).every(investment => investment.count > 0);
        if (allInvestmentsOwned) {
          achievement.unlocked = true;
          alert(`업적 달성: ${achievement.name}`);
        }
      }
    }
  });
};

const triggerRandomEvent = () => {
  if (Math.random() < 0.1) { // 10% chance of event occurring
    currentEvent.value = events[Math.floor(Math.random() * events.length)];

    if (currentEvent.value.title === '시장 호황') {
      Object.values(investments.value).forEach(investment => investment.return *= 1.5);
      setTimeout(() => {
        Object.values(investments.value).forEach(investment => investment.return /= 1.5);
        currentEvent.value = null;
      }, 30000);
    } else if (currentEvent.value.title === '경제 불황') {
      Object.values(investments.value).forEach(investment => investment.return *= 0.75);
      setTimeout(() => {
        Object.values(investments.value).forEach(investment => investment.return /= 0.75);
        currentEvent.value = null;
      }, 30000);
    } else if (currentEvent.value.title === '예상치 못한 지출') {
      assetValue.value *= 0.95;
      setTimeout(() => {
        currentEvent.value = null;
      }, 5000);
    } else if (currentEvent.value.title === '행운의 날') {
      assetValue.value *= 1.1;
      setTimeout(() => {
        currentEvent.value = null;
      }, 5000);
    }
  }
};

const resetGame = () => {
  assetValue.value = 0;
  salary.value = 10;
  investments.value = {
    savings: {
      name: '저축 계좌',
      description: '안전하지만 낮은 수익률의 투자',
      count: 0,
      return: 1,
      cost: 100,
      costIncrease: 50,
    },
    portfolio: {
      name: '투자 포트폴리오',
      description: '높은 수익률이지만 약간의 위험이 있음',
      count: 0,
      return: 10,
      cost: 1000,
      costMultiplier: 1.5,
    },
    realEstate: {
      name: '부동산',
      description: '안정적인 장기 수익',
      count: 0,
      return: 100,
      cost: 10000,
      costMultiplier: 2,
    },
    business: {
      name: '사업 벤처',
      description: '높은 위험, 높은 잠재적 수익',
      count: 0,
      return: 1000,
      cost: 100000,
      costMultiplier: 3,
    },
  };
  achievements.value = [
    { name: '첫 걸음', description: '첫 1,000월 벌기', unlocked: false, threshold: 1000 },
    { name: '중급 투자자', description: '자산 10,000원 달성하기', unlocked: false, threshold: 10000 },
    { name: '대형 투자자', description: '자산 100,000원 달성하기', unlocked: false, threshold: 100000 },
    { name: '백만장자', description: '자산 1,000,000원 달성하기', unlocked: false, threshold: 1000000 },
    { name: '다각화된 포트폴리오', description: '모든 종류의 투자 상품 최소 1개씩 보유하기', unlocked: false },
  ];
  currentEvent.value = null;
  localStorage.removeItem('financialFortuneBuilder');
};

let productionInterval;
let saveInterval;
let eventInterval;

onMounted(() => {
  const savedGame = localStorage.getItem('financialFortuneBuilder');
  if (savedGame) {
    const gameState = JSON.parse(savedGame);
    assetValue.value = gameState.assetValue;
    investments.value = gameState.investments;
    achievements.value = gameState.achievements;
  }

  productionInterval = setInterval(() => {
    assetValue.value += totalPerSecond.value / 10;
    checkAchievements();
  }, 100);

  saveInterval = setInterval(() => {
    localStorage.setItem('financialFortuneBuilder', JSON.stringify({
      assetValue: assetValue.value,
      investments: investments.value,
      achievements: achievements.value,
    }));
  }, 10000);

  eventInterval = setInterval(triggerRandomEvent, 60000);
});

onMounted(() => {
  resetGame();
  productionInterval = setInterval(() => {
    assetValue.value += totalPerSecond.value / 10;
    checkAchievements();
  }, 100);
  saveInterval = setInterval(() => {
    localStorage.setItem('financialFortuneBuilder', JSON.stringify({
      assetValue: assetValue.value,
      investments: investments.value,
      achievements: achievements.value,
    }));
  }, 10000);
  eventInterval = setInterval(triggerRandomEvent, 60000);
});
</script>

<style scoped>
.float-enter-active,
.float-leave-active {
  transition: all 0.5s ease-out;
}

.float-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.8);
}

.float-leave-to {
  opacity: 0;
  transform: translateY(-50px) scale(1.2);
}

.float-enter-to,
.float-leave-from {
  opacity: 1;
  transform: translateY(0) scale(1);
}
</style>