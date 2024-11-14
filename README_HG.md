## 라우팅 설정 및 컴포넌트 구조 조정

### 초기 라우팅 문제

1\. **HomeView 컴포넌트 누락**
   - 라우터 설정에서 `HomeView` 참조, 실제로는 `HomePage` 컴포넌트 존재
   - 애플리케이션 렌더링 실패

2\. **App.vue 구조 문제**
   - `App.vue`가 `HomePage` 컴포넌트 직접 임포트, 라우팅 시스템과 충돌

### 해결 과정

1\. **라우터 설정 수정**
   - `router/index.js` 파일에서 `HomeView` 대신 `HomePage` 임포트

<pre>
<code class="language-javascript">
import HomePage from '../components/HomePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    // ... 기타 라우트
  ],
})
</code>
</pre>

2\. **App.vue 수정**
   - 라우터 뷰 사용하도록 변경

<pre>
<code class="language-vue">
<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>
</code>
</pre>

3\. **컴포넌트 위치 조정**
   - `HomePage.vue`를 `components` 폴더에 유지

## 최종 구조 및 확인 사항

1\. **프로젝트 구조**
   <pre>
   src/
   ├── App.vue
   ├── components/
   │   └── HomePage.vue
   ├── router/
   │   └── index.js
   └── views/
       └── AboutView.vue
   </pre>

2\. **main.js 확인**
   - 라우터 올바르게 사용 확인

<pre>
<code class="language-javascript">
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
</code>
</pre>

3\. **빌드 및 실행**
   - 변경사항 적용 후 프로젝트 재빌드 및 실행
   <pre>
   npm run build
   npm run serve
   </pre>

## 결과

- Vue 애플리케이션 성공적 렌더링
- `HomePage` 컴포넌트가 루트 경로('/')에서 올바르게 표시
- CSS 기반 플레이스홀더가 이미지 대신 사용되어 레이아웃 의도대로 표시

이러한 과정을 통해 초기 설정 문제를 해결하고, Vue.js 프로젝트의 기본 구조를 올바르게 설정할 수 있었습니다. 앞으로의 개발 과정에서도 이러한 경험을 바탕으로 효율적인 문제 해결과 구조 개선이 가능할 것입니다.
