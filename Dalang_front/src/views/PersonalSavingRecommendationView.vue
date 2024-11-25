<template>
  <div class="recommendation-view">
    <!-- <h1>Recommended Saving Products</h1> -->
    <div v-if="loading" class="loading">
      <p>Loading recommendations...</p>
    </div>
    <div v-else-if="error" class="error">
      <p>Error: {{ error }}</p>
    </div>
    <div v-else class="recommendations">
      <div v-if="products.length > 0" class="product-list">
        <div v-for="product in products" :key="product.id" class="product-card">
          <h2>{{ product.name }}</h2>
          <p><strong>Company:</strong> {{ product.company }}</p>
          <p>
            <!-- 만기 후 이자율 -->
            <strong>Max Rate:</strong> {{ product.mtrt_int }}
          </p>
          <p>
            <strong>Special Conditions:</strong> {{ product.special_condition }}
          </p>
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
  name: "PersonalSavingRecommendationView",
  setup() {
    const loading = ref(true);
    const error = ref(null);
    const products = ref([]);

    const fetchRecommendations = async () => {
      try {
        loading.value = true;
        error.value = null;

        const response = await fetch(
          "http://127.0.0.1:8000/products/recommend/saving/",
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
        products.value = data.recommended_products;
      } catch (err) {
        error.value = err.message;
      } finally {
        loading.value = false;
      }
    };

    const formatCurrency = (value) => {
      if (!value) return "N/A";
      return new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
      }).format(value);
    };

    onMounted(() => {
      fetchRecommendations();
    });

    return {
      loading,
      error,
      products,
      fetchRecommendations,
      formatCurrency,
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
  background-color: rgba(0, 0, 0, 0.6); /* 배경 오버레이 */
  padding: 20px;
}

.loading,
.error {
  text-align: center;
  margin-top: 20px;
  font-size: 1.2rem;
  color: var(--text-primary);
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  width: 100%;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  background-color: #fff;
  width: calc(33.33% - 20px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 그림자 추가 */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 애니메이션 추가 */
  text-align: left;
}

.product-card:hover {
  transform: translateY(-5px); /* 호버 시 위로 살짝 이동 */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* 호버 시 그림자 강조 */
}

.product-card h2 {
  margin: 0 0 10px;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.product-card p {
  margin: 5px 0;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-primary);
}

.no-recommendations {
  font-size: 1.2rem;
  color: var(--text-secondary);
  text-align: center;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 1rem;
  color: #fff;
  background-color: var(--primary-color);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: var(--secondary-color);
}

button:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(68, 170, 226, 0.5); /* 포커스 효과 */
}
</style>
