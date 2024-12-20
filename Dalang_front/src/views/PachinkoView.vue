<template>
    <div class="security-container">
      <h1 class="security-title">🔐 Security Access 🔐</h1>
  
      <div class="security-board">
        <div class="slots-container">
          <div v-for="(slot, index) in slots" :key="index" class="slot">
            <button @click="rotateSlot(index)" class="slot-button" :disabled="accessGranted">
              {{ slot.currentLetter }}
            </button>
          </div>
        </div>
  
        <p class="instruction">Click each letter to rotate. Spell "DALANG" to gain access.</p>
      </div>
  
      <transition name="fade">
        <div v-if="accessGranted" class="result success-animation">
          <h2>🎉 CONGRATULATIONS! 🎉</h2>
          <p>Access granted. Redirecting to main page...</p>
        </div>
      </transition>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, watch } from 'vue';
  
  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  const targetWord = 'DALANG';
  
  const slots = ref(
    Array.from({ length: 6 }, () => ({
      currentIndex: 0,
      currentLetter: 'A'
    }))
  );
  
  const accessGranted = ref(false);
  
  const currentWord = computed(() => {
    return slots.value.map(slot => slot.currentLetter).join('');
  });
  
  const rotateSlot = (index) => {
    const slot = slots.value[index];
    slot.currentIndex = (slot.currentIndex + 1) % alphabet.length;
    slot.currentLetter = alphabet[slot.currentIndex];
  };
  
  watch(currentWord, (newWord) => {
    if (newWord === targetWord) {
      accessGranted.value = true;
      setTimeout(() => {
        // Redirect to main page or perform any other action
        alert('Redirecting to main page...');
      }, 3000);
    }
  });
  </script>
  
  <style scoped>
  .security-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 2rem;
    background-color: #f0f4f8;
  }
  
  .security-title {
    font-size: 2.5rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 2rem;
  }
  
  .security-board {
    background-color: #ffffff;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  }
  
  .slots-container {
    display: flex;
    gap: 15px;
    margin-bottom: 1rem;
  }
  
  .slot {
    width: 60px;
    height: 60px;
  }
  
  .slot-button {
    width: 100%;
    height: 100%;
    font-size: 2rem;
    font-weight: bold;
    color: #ffffff;
    background-color: #3498db;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .slot-button:hover:not(:disabled) {
    background-color: #2980b9;
  }
  
  .slot-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  
  .instruction {
    text-align: center;
    color: #7f8c8d;
    margin-top: 1rem;
  }
  
  .result {
    margin-top: 2rem;
    text-align: center;
    padding: 1rem;
    border-radius: 10px;
    animation: popIn 0.5s ease-out;
  }
  
  .success-animation {
    background-color: rgba(46, 204, 113, 0.2);
    color: #27ae60;
  }
  
  .result h2 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }
  
  .result p {
    font-size: 1.2rem;
  }
  
  @keyframes popIn {
    0% {
      transform: scale(0.8);
      opacity: 0;
    }
    100% {
      transform: scale(1);
      opacity: 1;
    }
  }
  
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }
  
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>