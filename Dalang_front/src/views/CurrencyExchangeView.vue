<template>
  <div class="min-h-screen bg-gray-50">
    <NavigationBar :navItems="navItems" />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <!-- Header Section -->
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold mb-4 bg-gradient-to-r from-[#115583] to-[#44AAE2] bg-clip-text text-transparent">
          외화환전
        </h1>
        <p class="text-xl text-gray-600 mb-8">
          외화 환전금액을 계산하여 드립니다.
        </p>

        <!-- Currency Exchange Cards -->
        <CurrencyExchangeCards />
      </div>

      <!-- Main Exchange Calculator Section -->
      <div class="grid md:grid-cols-2 gap-12">
        <!-- Left Section - Exchange Calculator -->
        <div class="bg-white rounded-xl shadow-lg p-8 border border-gray-100">
          <CurrencyExchangeCalculator :selected-currency="selectedCurrency" :amount="amount"
            @update:amount="updateAmount" />
        </div>

        <!-- Right Section - Currency Selection -->
        <div class="bg-white rounded-xl shadow-lg p-8 border border-gray-100">
          <CurrencyExchangeSelector :selected-currency="selectedCurrency" @update:currency="updateCurrency" />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'
import CurrencyExchangeCalculator from '@/components/CurrencyExchangeCalculator.vue'
import CurrencyExchangeSelector from '@/components/CurrencyExchangeSelector.vue'
import CurrencyExchangeCards from '@/components/CurrencyExchangeCards.vue'

// State management
const selectedCurrency = ref('USD')
const amount = ref('')

// Navigation items
const navItems = ref([
  { name: '환율계산기', path: '/' },
  { name: '환율정보', path: '/rates' },
  { name: '고객센터', path: '/support' },
])

// Event handlers
const updateCurrency = (currency) => {
  selectedCurrency.value = currency
}

const updateAmount = (newAmount) => {
  amount.value = newAmount
}
</script>

<style scoped>
.rounded-xl {
  border-radius: 1rem;
}

.shadow-lg {
  box-shadow: 0 10px 15px -3px rgba(17, 85, 131, 0.1),
    0 4px 6px -2px rgba(17, 85, 131, 0.05);
}

/* Hover effects */
.bg-white {
  transition: transform 0.3s ease;
}

.bg-white:hover {
  transform: translateY(-2px);
}

/* Glass morphism effect */
.bg-white {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .p-8 {
    padding: 1.5rem;
  }

  .text-5xl {
    font-size: 2.5rem;
  }

  .text-xl {
    font-size: 1.125rem;
  }
}
</style>