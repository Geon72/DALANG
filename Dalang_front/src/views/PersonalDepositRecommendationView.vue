<template>
  <div class="recommendation-view">
    <h1 class="main-title">Recommended Deposit Products</h1>
    <div v-if="isLoading" class="loading-container">
      <transition name="fade" mode="out-in">
        <div :key="loadingStep" class="loading-step">
          <div class="loading-spinner"></div>
          <p>{{ loadingMessages[loadingStep] }}</p>
        </div>
      </transition>
    </div>
    <div v-else-if="error" class="error">
      <p>Error: {{ error }}</p>
    </div>
    <div v-else class="recommendations">
      <div v-if="products.length > 0" class="product-list">
        <div 
          v-for="(product, index) in products" 
          :key="product.id" 
          class="product-card-container"
          :style="{ animationDelay: `${index * 0.2}s` }"
        >
          <div class="product-card" :class="{ 'is-flipped': product.isFlipped }" @click="flipCard(product)">
            <div class="product-card-front">
              <h2>{{ product.name }}</h2>
              <p><strong>Company:</strong> {{ product.company }}</p>
              <p><strong>Click to see details</strong></p>
            </div>
            <div class="product-card-back">
              <h2>{{ product.name }}</h2>
              <p><strong>Company:</strong> {{ product.company }}</p>
              <p><strong>Max Rate:</strong> {{ product.mtrt_int }}</p>
              <p><strong>Special Conditions:</strong> {{ product.special_condition }}</p>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>No recommendations available.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "PersonalDepositRecommendationView",
  setup() {
    const isLoading = ref(true);
    const loadingStep = ref(0);
    const error = ref(null);
    const products = ref([]);

    const loadingMessages = [
      "투자성향을 분석하고 있어요...",
      "신용점수를 분석하고 있어요...",
      "연봉을 분석하고 있어요...",
      "거의 다 왔어요! 당신에게 추천드릴 상품은...!"
    ];

    const simulateLoading = () => {
      isLoading.value = true;
      loadingStep.value = 0;

      const interval = setInterval(() => {
        loadingStep.value++;
        if (loadingStep.value >= loadingMessages.length) {
          clearInterval(interval);
          fetchRecommendations();
        }
      }, 2000); // Change message every 2 seconds
    };

    const fetchRecommendations = async () => {
      try {
        error.value = null;

        const response = await fetch(
          "http://127.0.0.1:8000/products/recommend/deposit/",
          {
            method: "GET",
            headers: {
              Authorization: `Token ${localStorage.getItem("authToken")}`,
              "Content-Type": "application/json",
            },
          }
        );

        if (!response.ok) {
          const errorText = await response.text();
          console.error("API Error:", errorText);
          throw new Error(`Failed to fetch: ${response.statusText}`);
        }

        const data = await response.json();
        products.value = data.recommended_products.map(product => ({
          ...product,
          isFlipped: false
        }));

        // Simulate a delay before showing results
        setTimeout(() => {
          isLoading.value = false;
        }, 1000);
      } catch (err) {
        error.value = err.message;
        isLoading.value = false;
      }
    };

    const flipCard = (product) => {
      product.isFlipped = !product.isFlipped;
    };

    onMounted(() => {
      simulateLoading();
    });

    return {
      isLoading,
      loadingStep,
      loadingMessages,
      error,
      products,
      flipCard,
    };
  },
};
</script>

<style scoped>
.recommendation-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f0f4f8;
  padding: 40px 20px;
}

.main-title {
  font-size: 3rem;
  color: #00008B;
  margin-bottom: 40px;
  text-align: center;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  animation: fadeInDown 0.8s ease-out;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 200px;
}

.loading-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.loading-spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.loading,
.error {
  text-align: center;
  margin-top: 20px;
  font-size: 1.2rem;
  color: #333;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  width: 100%;
  max-width: 1200px;
}

.product-card-container {
  perspective: 1000px;
  width: calc(33.33% - 20px);
  min-width: 300px;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.8s ease-out forwards;
}

.product-card {
  position: relative;
  width: 100%;
  height: 250px;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  cursor: pointer;
}

.product-card.is-flipped {
  transform: rotateY(180deg);
}

.product-card-front,
.product-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 15px;
  padding: 20px;
  background-color: #ffffff;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow: hidden;
}

.product-card-back {
  transform: rotateY(180deg);
  background-color: #e8f4fd;
}

.product-card h2 {
  margin: 0 0 15px;
  color: #2c3e50;
  font-size: 1.3rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.product-card p {
  margin: 8px 0;
  font-size: 0.9rem;
  line-height: 1.4;
  color: #34495e;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-card-front p:last-child {
  margin-top: auto;
  font-weight: 500;
  color: #3498db;
}

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

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .product-card-container {
    width: 100%;
  }
}
</style>

