<template>
    <div class="pachinko-container">
        <h1 class="game-title">🎰 DALANG으로 맞춰라! 🎰</h1>

        <div class="game-board">
            <div class="slots-container">
                <div v-for="(slot, index) in slots" :key="index" class="slot">
                    <div class="slot-wheel" :style="{ transform: `translateY(${slot.offset}px)` }">
                        <div v-for="(letter, letterIndex) in alphabet" :key="letterIndex" class="slot-letter">
                            {{ letter }}
                        </div>
                    </div>
                </div>
            </div>

            <div class="controls">
                <button @click="startGame" :disabled="isRunning" class="game-button start-button">
                    <span class="button-emoji">🎲</span> Start
                </button>
                <button @click="stopSlot" :disabled="!isRunning || currentSlot >= 6" class="game-button stop-button">
                    <span class="button-emoji">🛑</span> Stop
                </button>
            </div>
        </div>

        <transition name="fade">
            <div v-if="result === 'win'" class="result win-animation">
                <h2>🎉🎊 축하합니다! 🎊🎉</h2>
                <p>D, A, L, A, N, G 조합 성공!</p>
                <div class="fireworks">
                    <div class="firework" v-for="n in 3" :key="n"></div>
                </div>
            </div>
        </transition>

        <!-- LOSE 애니메이션 -->
        <transition name="fade">
            <div v-if="result === 'lose'" class="result lose-animation shake-animation">
                <h2>😢 허접이시네요! 😢</h2>
                <p>다시 도전해보세요!</p>
                <!-- 조롱하는 이모지 -->
                <div class="taunting-emojis">
                    🤡 💩 🤡 💩 🤡
                </div>
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const slots = ref(
    Array.from({ length: 6 }, () => ({
        offset: 0,
        interval: null,
    }))
);
const isRunning = ref(false);
const currentSlot = ref(0);
const result = ref(null);

const targetCombination = ['D', 'A', 'L', 'A', 'N', 'G'];

const startGame = () => {
    isRunning.value = true;
    result.value = null;
    currentSlot.value = 0;

    slots.value.forEach((slot, index) => {
        slot.interval = setInterval(() => {
            slot.offset -= 60;
            if (slot.offset <= -60 * alphabet.length) {
                slot.offset = 0;
            }
        }, 500 + index * 25);
    });
    startBackgroundEffect(); // 배경 색상 변화 시작
};

const stopSlot = () => {
    if (currentSlot.value < slots.value.length) {
        const slot = slots.value[currentSlot.value];
        clearInterval(slot.interval);

        const finalIndex = Math.abs(slot.offset / -60) % alphabet.length;
        slot.offset = -60 * finalIndex;

        currentSlot.value++;

        checkIntermediateResult(); // 중간 결과 확인

        if (currentSlot.value === slots.value.length) {
            setTimeout(checkResult, 500);
        }
    }
};

const checkIntermediateResult = () => {
    const currentCombination = slots.value
        .slice(0, currentSlot.value)
        .map((slot) => alphabet[Math.abs(slot.offset / -60) % alphabet.length]);

    const targetPartialCombination = targetCombination.slice(0, currentSlot.value);

    if (JSON.stringify(currentCombination) !== JSON.stringify(targetPartialCombination)) {
        result.value = 'lose';
        isRunning.value = false;
        stopBackgroundEffect(); // 배경 색상 변화 중단
    }
};

const checkResult = () => {
    const finalCombination = slots.value.map(
        (slot) => alphabet[Math.abs(slot.offset / -60) % alphabet.length]
    );

    if (JSON.stringify(finalCombination) === JSON.stringify(targetCombination)) {
        result.value = 'win';
    } else {
        result.value = 'lose';
    }

    isRunning.value = false;
};

onMounted(() => {
    document.body.classList.add('game-background');
});

onUnmounted(() => {
    document.body.classList.remove('game-background');
});
</script>

<style scoped>
/* 전체 컨테이너 */
.pachinko-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 2rem;
    background-color: #ffffff;
    /* 메인 배경색 */
}

.game-title {
    font-size: 3rem;
    font-weight: bold;
    color: #115583;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    margin-bottom: 2rem;
}

.game-board {
    background-color: #e5e7eb;
    border-radius: 20px;
    padding: 2rem;
}

.slots-container {
    display: flex;
    gap: 15px;
    margin-bottom: 2rem;
}

.slot {
    width: 80px;
    height: 80px;
    overflow: hidden;
    border-radius: 10px;
    background-color: #2C3E50;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}

.slot-wheel {
  transition: transform 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.slot-letter {
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    font-weight: bold;
    color: #44AAE2;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.controls {
    display: flex;
    justify-content: center;
    gap: 1rem;
}

.game-button {
    font-size: 1.2rem;
    font-weight: bold;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.button-emoji {
    margin-right: 0.5rem;
    font-size: 1.4rem;
}

.start-button {
    background-color: #2ecc71;
    color: white;
}

.start-button:hover:not(:disabled) {
    background-color: #27ae60;
}

.stop-button {
    background-color: #e74c3c;
    color: white;
}

.stop-button:hover:not(:disabled) {
    background-color: #c0392b;
}

.reset-button {
    background-color: #3498db;
    color: white;
}


.game-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.result {
    margin-top: 2rem;
    text-align: center;
    padding: 1rem;
    border-radius: 10px;
    animation: popIn 0.5s ease-out;
}

.win-animation {
    background-color: rgba(46, 204, 113, 0.2);
    color: #2ecc71;
}

.lose-animation {
    background-color: rgba(231, 76, 60, 0.2);
    color: #e74c3c;
}

.result h2 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.result p {
    font-size: 1.2rem;
}

.fireworks {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}

.firework {
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    animation: explode 1s ease-out infinite;
}

.firework:nth-child(1) {
    background-color: #ff0;
    left: 20%;
    top: 40%;
}

.firework:nth-child(2) {
    background-color: #f0f;
    left: 50%;
    top: 20%;
    animation-delay: 0.2s;
}

.firework:nth-child(3) {
    background-color: #0ff;
    left: 80%;
    top: 60%;
    animation-delay: 0.4s;
}

@keyframes explode {
    0% {
        transform: scale(0);
        opacity: 1;
    }

    100% {
        transform: scale(20);
        opacity: 0;
    }
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

:global(.game-background) {
    background: white;
    background-size: 400% 400%;
}

@keyframes gradientBG {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}
</style>