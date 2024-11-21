<template>
  <div class="chart-container">
    <canvas ref="chart"></canvas>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue'
import { Chart, registerables } from 'chart.js'

// Chart.js 등록
Chart.register(...registerables)

// props로 전달받은 차트 데이터
const props = defineProps({
  chartData: {
    type: Object,
    required: true,
  },
})

// Chart.js 차트 참조
const chart = ref(null)
let chartInstance = null

// 차트를 렌더링하는 함수
const renderChart = () => {
  if (chartInstance) {
    chartInstance.destroy() // 기존 차트를 제거하여 메모리 누수 방지
  }
  chartInstance = new Chart(chart.value, {
    type: 'line', // 라인 차트 유형
    data: props.chartData, // 차트 데이터
    options: {
      responsive: true, // 반응형 설정
      maintainAspectRatio: false, // 반응형일 때 가로세로 비율 유지 여부
      plugins: {
        legend: {
          position: 'top', // 범례 위치
        },
      },
      scales: {
        x: {
          type: 'category', // x축 데이터 유형 (카테고리형)
          // title: {
          //   display: true,
          //   text: 'Date',
          // },
          ticks: {
            autoSkip: true,
            maxTicksLimit: 10, // x축 라벨 최대 표시 수
          },
        },
        y: {
          // title: {
          //   display: true,
          //   text: 'ExchangeRate',
          // },
          beginAtZero: false, // y축 0부터 시작 여부
        },
      },
      elements: {
        line: {
          borderWidth: 2, // 라인 두께
          tension: 0.3, // 곡선의 부드러움
        },
        point: {
          radius: 1, // 포인트 크기
          backgroundColor: '#0066CC', // 포인트 색상
        },
      },
    },
  })
}

// props가 변경될 때마다 차트를 업데이트
watch(props.chartData, renderChart)

// 컴포넌트가 마운트될 때 차트 생성
onMounted(renderChart)

// 컴포넌트가 언마운트될 때 차트 제거
onUnmounted(() => {
  if (chartInstance) {
    chartInstance.destroy()
  }
})
</script>

<style scoped>
.chart-container {
  position: relative;
  height: 400px; /* 차트 높이 */
  width: 100%; /* 차트 너비 */
}
canvas {
  display: block;
  max-width: 100%;
}
</style>