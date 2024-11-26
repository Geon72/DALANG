<template>
    <div class="security-container">
        <h1 class="security-title">
            <span class="lock-icon" :class="{ 'shake-animation': isShaking }">🔐</span> Security Access
            <span class="lock-icon" :class="{ 'shake-animation': isShaking }">🔐</span>
        </h1>

        <div class="security-board">
            <div class="slots-container">
                <div v-for="(slot, index) in slots" :key="index" class="slot">
                    <button @click="rotateSlot(index)" class="slot-button" :disabled="accessGranted">
                        {{ slot.currentLetter }}
                    </button>
                </div>
            </div>

            <p class="instruction">설정된 2차 비밀번호를 입력해주세요!</p>
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
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const targetWord = 'DALANG';

const slots = ref(
    Array.from({ length: 6 }, () => ({
        currentIndex: 0,
        currentLetter: 'A'
    }))
);

const accessGranted = ref(false);
const isShaking = ref(false);

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
            alert('메인 페이지로 이동합니다.');
            router.push('/'); // 메인 페이지로 이동
        }, 3000);
    }
});

let shakeInterval;

onMounted(() => {
    shakeInterval = setInterval(() => {
        isShaking.value = true;
        setTimeout(() => {
            isShaking.value = false;
        }, 500);
    }, 2000);
});

onUnmounted(() => {
    clearInterval(shakeInterval);
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

.lock-icon {
    display: inline-block;
    transition: transform 0.5s ease;
}

.shake-animation {
    animation: shake 0.5s ease-in-out;
}

@keyframes shake {

    0%,
    100% {
        transform: rotate(0deg);
    }

    25% {
        transform: rotate(-10deg);
    }

    75% {
        transform: rotate(10deg);
    }
}
</style>
