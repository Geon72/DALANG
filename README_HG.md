# 241116 기본 틀 제작

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

# 241117-241118
# DALANG 금융 서비스 웹 애플리케이션 개발 문서

## 프로젝트 개요

DALANG은 SSAFY 관통프로젝트의 일환으로 개발된 금융상품추천 및 비교 웹 애플리케이션입니다. 주요 기능으로는 은행 찾기, 정기예금/적금 상품 비교, 그리고 사용자 프로필 관리 등이 있습니다. 이 프로젝트는 Django와 Vue.js를 활용하여 구현되었으며, 카카오맵 API를 통합하여 위치 기반 서비스를 제공합니다.

## 시간을 많이 소요한 요소들

### 주요 문제 상황과 해결 과정

1. 카카오맵 API 초기화 문제

**문제 상황:**
Vue 컴포넌트 생명주기와 카카오맵 API 로딩 타이밍이 맞지 않아 지도 초기화 실패

**해결 과정:**
- 동적 스크립트 로딩 방식 도입
- API 로드 완료 후 초기화 로직 실행하도록 변경
- onMounted 훅 내에서 비동기 함수를 사용하여 API 로딩 대기

```javascript
onMounted(async () => {
  await loadKakaoMapScript();
  initMap();
});
```

2. 위치 정보 접근 거부 처리

**문제 상황:**
사용자가 위치 정보 제공을 거부할 경우 서비스 작동 불가

**해결 과정:**
- 위치 정보 접근 실패 시 기본 위치(예: 서울시청) 사용 로직 추가
- 사용자에게 위치 정보 필요성 안내 메시지 표시
- 수동으로 위치 입력할 수 있는 대체 UI 제공

```javascript
const getMyLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      successCallback,
      (error) => {
        console.error("위치 정보를 가져오는데 실패했습니다:", error);
        useDefaultLocation();
        showLocationErrorMessage();
      }
    );
  } else {
    console.error("Geolocation이 지원되지 않습니다.");
    useDefaultLocation();
    showLocationErrorMessage();
  }
};
```

3. 컴포넌트 간 데이터 전달 문제

**문제 상황:**
지도 컴포넌트에서 검색된 은행 데이터를 목록 컴포넌트로 효과적으로 전달하기 어려움

**해결 과정:**
- 부모 컴포넌트(FindBankView.vue)에서 상태 관리
- Props와 Emit을 활용한 데이터 흐름 개선
- 필요한 경우 Pinia 상태 관리 라이브러리 도입 검토

```vue
<!-- FindBankView.vue -->
<template>
  <FindBankMapComponent @search-results="updateSearchResults" />
  <FindBankBankList :banks="searchResults" />
</template>

<script setup>
import { ref } from 'vue';
import FindBankMapComponent from './FindBankMapComponent.vue';
import FindBankBankList from './FindBankBankList.vue';

const searchResults = ref([]);

const updateSearchResults = (results) => {
  searchResults.value = results;
};
</script>
```

4. 성능 최적화 문제

**문제 상황:**
많은 수의 은행 마커를 표시할 때 성능 저하 발생

**해결 과정:**
- 마커 클러스터링 기능 구현
- 뷰포트 내의 마커만 렌더링하는 최적화 적용
- 데이터 페이지네이션 구현으로 초기 로딩 데이터 양 감소

```javascript
const clusterer = new kakao.maps.MarkerClusterer({
  map: map,
  averageCenter: true,
  minLevel: 5
});

clusterer.addMarkers(markers);
```

이러한 문제들을 해결하는 과정에서 비동기 프로그래밍, 상태 관리, 성능 최적화 등 다양한 웹 개발 기술을 심도 있게 학습하고 적용할 수 있었습니다. 특히 사용자 경험을 고려한 에러 처리와 대체 UI 제공의 중요성을 깨달았습니다.


## 주요 기능

### 1. 홈페이지
- 서비스 소개
- 친구 활동 표시
- 리뷰 시스템

### 2. 은행 찾기 (FindBank)
FindBank 기능은 카카오맵 API를 활용하여 사용자 주변의 은행을 검색하고 지도에 표시하는 서비스입니다.

#### 주요 컴포넌트
- FindBankView.vue (메인 뷰)
- FindBankMapComponent.vue (지도 컴포넌트)
- FindBankBankList.vue (은행 목록 컴포넌트)
- FindBankSearchForm.vue (검색 폼 컴포넌트)

#### 구현 기능
- 현재 위치 기반 지도 초기화
- 키워드 기반 은행 검색
- 검색 결과의 지도 마커 표시
- 검색 결과 목록 별도 컴포넌트로 표시
- 페이지네이션 기능
- 반응형 디자인

#### 개발 과정 및 해결한 문제
1. 카카오맵 API 통합
   - API 키 및 도메인 설정 관련 이슈 해결
   - 스크립트 로딩 방식 개선 (동적 로딩에서 정적 로딩으로 변경)
2. 위치 정보 처리
   - 사용자 현재 위치 찾기 기능 구현
   - 위치 정보 접근 거부 시 기본 위치(서울시청) 사용 로직 추가
3. 데이터 흐름 최적화
   - 컴포넌트 간 데이터 전달 방식 개선 (emit 활용)
   - 부모 컴포넌트(FindBankView.vue)에서 상태 관리
4. UI/UX 개선
   - 지도 컨테이너 크기 조정 문제 해결
   - 검색 결과 표시 방식 변경 (인포윈도우에서 별도 컴포넌트로)
   - 현재 위치 마커 디자인 개선

### 3. 정기예금/적금 상품 비교

#### 주요 컴포넌트
- RecommendationView.vue (메인 컴포넌트)
- RecommendationFilterSectionDeposit.vue (예금 필터)
- RecommendationFilterSectionSaving.vue (적금 필터)
- RecommendationResultTableDeposit.vue (예금 결과 테이블)
- RecommendationResultTableSaving.vue (적금 결과 테이블)
- RecommendationBankSelection.vue (은행 선택 공통 컴포넌트)
- RecommendationExcelExport.vue (엑셀 내보내기 공통 컴포넌트)

#### 주요 기능
- 탭 전환 기능 (정기예금/정기적금)
- 필터링 기능 (은행 선택, 적립방식, 이자 계산방식, 만기 기간, 가입방식)
- 정렬 기능
- 엑셀 내보내기 기능

### 4. 사용자 프로필 관리
- 사용자 정보 표시
- 활동 내역
- 설정 관리

## 기술 스택

- Frontend: Vue.js 3, Tailwind CSS
- Backend: Django
- API: 카카오맵 API
- 상태 관리: Pinia
- 기타 라이브러리: ExcelJS, Heroicons, lucide-vue-next

## 프로젝트 구조

```
project-root/
├── src/
│   ├── assets/
│   │   └── images/
│   ├── components/
│   │   ├── NavigationBar.vue
│   │   ├── MobileMenu.vue
│   │   ├── FindBank/
│   │   │   ├── FindBankMapComponent.vue
│   │   │   ├── FindBankBankList.vue
│   │   │   └── FindBankSearchForm.vue
│   │   └── Recommendation/
│   │       ├── RecommendationFilterSectionDeposit.vue
│   │       ├── RecommendationFilterSectionSaving.vue
│   │       ├── RecommendationResultTableDeposit.vue
│   │       └── RecommendationResultTableSaving.vue
│   ├── views/
│   │   ├── HomePageView.vue
│   │   ├── FindBankView.vue
│   │   ├── RecommendationView.vue
│   │   └── ProfileView.vue
│   ├── router/
│   ├── store/
│   ├── App.vue
│   └── main.js
├── public/
│   └── index.html
├── .env
├── package.json
├── tailwind.config.js
└── vite.config.js
```

## 개발 과정

1. 초기 컴포넌트 구조 설계
2. 레이아웃 및 반응형 디자인 구현
3. 카카오맵 API 통합
4. 정기예금/적금 상품 비교 기능 구현
5. 사용자 인증 및 프로필 관리 기능 추가

## 주요 해결 과제

1. 레이아웃 및 반응형 디자인 문제
   - 해결: Tailwind CSS를 활용한 그리드 시스템 및 미디어 쿼리 적용
2. 카카오맵 API 통합 이슈
   - 해결: 동적 스크립트 로딩 및 API 키 관리 최적화
3. 컴포넌트 간 데이터 전달
   - 해결: Pinia를 활용한 상태 관리 및 이벤트 버스 구현
4. 성능 최적화
   - 해결: 컴포넌트 지연 로딩 및 가상 스크롤링 적용

## 스타일링

```css
:root {
  --primary-color: #115583;
  --secondary-color: #44AAE2;
  --text-primary: #4A524D;
  --text-secondary: #92B3B5;
}
```

## 향후 개선사항

1. 실제 API 연동 및 데이터 관리 강화
2. 사용자 경험 개선 (로딩 상태, 에러 처리 등)
3. 접근성 향상 (ARIA 속성 추가)
4. 테스트 코드 작성 및 CI/CD 파이프라인 구축
5. 국제화(i18n) 지원
6. 검색 필터 기능 강화
7. 사용자 위치 기반 실시간 업데이트

이 README는 DALANG 프로젝트의 전반적인 개발 과정과 주요 기능, 기술 스택, 그리고 향후 개선 방향을 요약하고 있습니다. 프로젝트의 구조와 해결한 주요 과제들을 포함하여 개발자들이 프로젝트의 전체적인 흐름을 이해하는 데 도움을 줄 수 있도록 작성되었습니다.
`;
