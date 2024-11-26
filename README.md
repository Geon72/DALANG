# SSAFY 12기 비전공 1학기 관통(금융) 프로젝트: DALANG 💼

## 1. 팀원 정보 및 업무 분담 내역 👥

| Name | 허건👑 | 서석주 |
|------|-------|--------|
| Position | Design/Front/Backend Develop | Backend Develop |
| Git | [@Geon72](https://github.com/Geon72) | [@seokkjjoo](https://github.com/seokkjjoo) |
| E-mail | ssgeonu@gmail.com | redbucker@gmail.com |

## 2. 목표 서비스 구현 및 실제 구현 정도 🎯

### 구현 목표
- 금융 상품 추천 및 비교 기능
- 사용자 맞춤형 금융 상품 제안
- 실시간 금융 정보 제공
- 사용자들의 검색 비겓이터를 통한 핫이슈 추천기능
- MAU 확보를 위한 게이미피케이션
- 배포

### 실제 구현 수준
- **MAU 확보를 위한 게이미피케이션** ✅
- 금융 상품 기본 정보 조회 및 비교 기능 구현 ✅
- 사용자 프로필 기반 간단한 추천 알고리즘 적용 ✅
- 커뮤니티 구현 ✅

## 3. 데이터베이스 모델링(ERD) 📊

![ERD1](https://github.com/user-attachments/assets/987c9bac-e342-4e9e-8ee8-6e913030d5c6)
![erd2](https://github.com/user-attachments/assets/b2fbae1e-3d0c-494e-9361-5d4d66b8400e)

## 4. 금융 상품 추천 알고리즘에 대한 기술적 설명 🧮

우리 팀의 금융 상품 추천 알고리즘은 다음과 같은 요소를 고려하여 설계되었습니다:

1. 사용자 프로필 분석 👤
2. 금융 목표 매칭 🎯
3. 위험 선호도 평가 📊
4. 과거 거래 이력 활용 📜
5. 시장 동향 반영 📈

이러한 요소들을 종합적으로 고려하여 가중치 기반의 점수 시스템을 적용, 최종 추천 목록을 생성합니다.

## 5. 핵심 기능에 대한 설명 🔑

### 1. 맞춤형 금융 상품 추천 💰

![homepage](https://github.com/user-attachments/assets/7fb937d3-2fa1-4387-968b-2f3d1198c0f6)

#### 주요 역할 및 기능
- NavigationBar를 통한 상단 네비게이션 제공
- HomePageBannerImage로 배너 이미지 표시
- HomePageServiceSection을 통해 주요 서비스 소개 (예/적금추천, 근처 은행, 환율 계산기)
- HomePageFriendsSection으로 친구들의 최근 금융 활동 표시
- HomePageReviewBoard를 통한 사용자 리뷰와 댓글 기능
- 리뷰 신고, 좋아요, 댓글 토글, 댓글 추가 기능
- 로그인 성공 시 해당 라우트로 이동 및 페이지 새로고침

### 2. 예적금 추천 💳

![image](https://github.com/user-attachments/assets/f97b9e6f-be4d-42a3-a4d5-e8eaa7c8f986)

#### 주요 기능 및 구조
- 정기예금과 정기적금 탭 제공
- RecommendationFilterSection을 통한 필터링 옵션
- searchProducts 함수를 통한 상품 검색
- RecommendationResultTable을 통한 결과 표시
- ref를 사용한 반응형 데이터 관리
- fetch를 사용한 백엔드 API 통신 (인증 토큰 사용)

### 3. 근처 은행 🏦

![image2](https://github.com/user-attachments/assets/c14f2ac6-4342-4818-bfac-85ec50f48dab)

#### 주요 기능 및 구조
- FindBankSearchForm을 통한 은행 유형과 검색 반경 설정
- FindBankMapComponent를 사용한 지도 표시
- FindBankBankList를 통한 검색된 은행 목록 표시
- 반응형 그리드 시스템을 활용한 레이아웃

### 4. 환율 계산기 💱

![image3](https://github.com/user-attachments/assets/fa8e20be-7f54-478e-ad5a-af7a4c7b227f)

#### 주요 기능 및 구조
- CurrencyExchangeCards를 통한 주요 환율 정보 표시
- CurrencyExchangeCalculator를 사용한 환전 계산
- CurrencyExchangeSelector를 통한 통화 선택
- 반응형 디자인 및 시각적 효과 적용

### 5. 커뮤니티 💬

![image4](https://github.com/user-attachments/assets/938e5fbf-0ee0-44b9-ac1a-d0aa11d97ab1)
![image5](https://github.com/user-attachments/assets/44f55282-f1c7-4818-9805-f948a227867d)

#### 주요 기능 및 구조
- 게시글 작성 및 조회 기능
- 댓글 시스템을 통한 사용자 간 상호작용
- 좋아요 기능으로 인기 게시글 파악
- 카테고리별 게시글 분류 시스템

### 6. 프로필 👤

![image6](https://github.com/user-attachments/assets/96cf67f3-ec4e-476e-a052-ad49331eac00)

#### 주요 기능 및 구조
- ProfileHeader와 ProfilePostGrid 컴포넌트 사용
- axios를 사용한 백엔드 API 통신
- 사용자 정보, 작성 게시물, 좋아요한 게시물, 댓글 단 게시물 데이터 로드

### 7. Gamification 🎮

#### a. 클릭커 기반

![image7](https://github.com/user-attachments/assets/32a12c1e-3e3c-433a-b5ed-526efc45c637)
#### 주요 기능 및 구조
- 자산 증식 시뮬레이션 게임
- 다양한 투자 옵션 제공
- 업적 시스템을 통한 목표 달성 유도
#### b. 룰렛 기반

![image8](https://github.com/user-attachments/assets/da2d2804-0a8a-4643-9613-5f7db0bcf16e)
#### 주요 기능 및 구조
- "DALANG" 단어 맞추기 게임
- 슬롯 머신 스타일의 인터페이스
- 승리/패배에 따른 애니메이션 효과
#### c. 이차 보안

![image9](https://github.com/user-attachments/assets/61a8277d-67ac-46dc-b01f-dc3f2a2bf748)
#### 주요 기능 및 구조
- 2차 비밀번호 입력을 통한 보안 강화
- 인터랙티브한 슬롯 회전 메커니즘
- 성공적인 인증 시 메인 페이지로 리다이렉션
#### d. 당신은 로봇인가요?

![image10](https://github.com/user-attachments/assets/0e408f1f-f78d-426d-8629-eb78595d0da1)
#### 주요 기능 및 구조
- 이미지 기반 CAPTCHA 시스템
- 사용자 검증을 위한 개 이미지 선택 과제
- 단계별 회원가입 프로세스의 일부로 통합
#### e. 상품추천 애니메이션

![image11](https://github.com/user-attachments/assets/3d740d41-fdbf-471d-967e-ea920db05c2e)
#### 주요 기능 및 구조
- 개인화된 금융 상품 추천 시각화
- 플립 카드 효과를 통한 상품 정보 표시
- 로딩 애니메이션으로 사용자 경험 향상
- 
## 6. 생성형 AI를 활용한 부분 🤖

1. 기본 아이디어 구상
2. FRONTEND 구현 기능
3. 시나리오 기반 투자 전략 아이디어
4. PPT 제작
5. 그 외 기타 디버깅

## 7. 기타 (느낀점, 후기 등) 💭

### 허건
정말 많은 일이 있었습니다. 싸피에서 배운 내용에 더해 FIGMA를 통한 디자인, 까먹어버린 html, css, bootstrap 공부, front에서 애니메이션 및 다양한 기능구현을 위한 고뇌로 3주간 알차게 보냈습니다. 비록 배포까지는 도달하지 못했으나, 처음 프로젝트이니만큼 남는 것이 많은 기회였으며, 특히 필수 프로젝트라는 틀에 갇혀 구현하는 것이 아닌 점유율, 경쟁성 나아나 MAU 확보라는 주제로 폭넓게 기획하여 풍성한 프로젝트 제작을 하는 데에 발을 도달하지 않았나 싶습니다. 계절학기 동안 부족한 점을 보완하여 다음 프로젝트에 밑거름이 될 수 있게 하겠습니다. 다양한 사고 구현에 함께 해준 팀원에게 고마움을 표합니다.

### 서석주
짧은 프로젝트 기간 동안 취업 준비를 병행하느라 프로젝트에 온전히 집중하지 못한 점이 아쉬웠습니다. 12월 계절 학기 동안 미흡한 프로젝트 기능은 보완하고, 더 나아가 클라우드 서비스를 통한 배포를 직접 해볼 예정입니다. 소통이 원활했고, 함께 했던 팀원인 허건 교육생에게 큰 감사함을 느낍니다. 특히 소통이 원활해서 서로의 니즈 파악이 원활했고, 기능 구현에도 어려움이 없었던 것 같습니다. 커뮤니케이션 역량이 개발자로서 중요함을 알 수 있었습니다. 12월 동안 부족한 CI/CD 역량과 Java, Spring Framework 공부가 필요함을 느꼈습니다. 힘들었지만 행복했던 프로젝트였습니다.

### 기술 스택
- Frontend: Vue.js, Vuex, Vue Router
- Backend: Django, Django REST Framework
- Database: SQLIte
- 기타: Figma

### 향후 개선 계획
1. 머신러닝 모델 고도화를 통한 추천 정확도 향상
2. 배포 공부
3. 게임을 통한 마일리지 확보, 상용성 구상

### 프로젝트 타임라인
- 기획 및 요구사항 분석: 1주차
- 디자인 및 프로토타입 개발: 1주차
- 핵심 기능 구현: 2주차
- 테스트 및 디버깅: 3주차
- 최종 발표 준비: 3주차

본 프로젝트를 통해 우리 팀은 실제 금융 서비스 개발 과정을 경험하며, 기술적 역량뿐만 아니라 팀워크와 프로젝트 관리 능력도 크게 향상시킬 수 있었습니다. 특히 MAU에 집중하는 전략으로, 자신만의 특색을 보일 수 있는 방안으로 게이미피케이션을 이용, FRONT에서 다양한 기능 및 애니메이션을 구현하는 법을 배웠습니다.
`;
