# 싸피 1학기 관통 프로젝트_Dalang

## 20241118 월
* 카카오맵 API를 활용하여 은행 검색 기능 구현
  * 기존에 없던 목록과 마커에 마우스를 올리면 해당 목록과 마커가 가르켜 편리성을 확대함
  ```
  // 지도의 확대 레벨을 5로 고정합니다 - seokzzoo
    map.setLevel(5);

    // 인포윈도우가 표시될 때 지도의 중심을 마커 위치로 설정합니다 - seokzzoo
    map.setCenter(marker.getPosition());
    ```
  * Django에서 카카오맵 API를 통한 은행 검색 기능 구현 완료
  * 지도 기능은 Backend에서 관리하기 보다는 Frontend에서 관리하는 것이 더 낫다고 판단
  * Vue.js에서 같은 기능을 어떻게 구현해야 할지 고민해야 할 것!!

* 한국수출입은행 환율 API를 활용하여 1년 간 환율 데이터 시각화 기능 구현
  * 실시간 환율 데이터 시각화 기능을 구현하고자 했으나 유료 API를 활용해야 가능해서 일단은 보류
  * 최근 1년 간 달러, 엔, 유로, 위안화 환율 데이터를 바탕으로 저렴한 신혼여행을 원하는 고객에게 추천 가능!
  * 환율 데이터 시각화 기능도 Backend에서 관리하기 보다는 Frontend에서 관리하는 것이 더 낫다고 판단
  * Vue.js에서 같은 기능을 어떻게 구현해야 할지 고민해야 할 것!!

* 금융감독원 정기예금 API를 활용하여 예금 상품 서버에 저장 완료!
  * 필요한 데이터만 선택함
    * kor_co_nm : 은행명
    * fin_prdt_nm : 상품명
    * intr_rate_type : 저축 금리 유형 / 이자 계산방식
    * save_trm : 저축 기간 [단위: 개월]
    * intr_rate : 일반 금리
    * intr_rate2 : 우대 금리
    * join_way : 가입 방법
    * spcl_cnd : 특별 조건
    * join_deny : 가입 제한 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    * join_member : 가입 대상
    * etc_note : 기타 사항
    * created_at : 생성 날짜
  * 추후 금융감독원 정기적금 API를 활용하여 적금 상품도 서버에 저장 해야 함!!!(~~20241119 예정~~ 20241119완료!)

* db.sqlite3는 유지해야 하기 때문에 .gitignore에서 sql관련 파일명 주석처리 완료!
* 파일을 수정하다 예상치 못하게 파일을 지워 프로젝트가 구동되지 않을 수 있으니 하나의 기능이 구현 완료 되면 GIT에 저장하며 관리하는 것이 좋을 것 같다!!!

## 20241119 화
* 로그인 기능 구현
  * User 모델
    * username : 유저네임(Front에서 ID)
    * age : 나이
    * gender : 성별 - Gender must be 1 (남성) or 2 (여성)
    * salary : 연봉
    * wealth : 자산
    * tendency : 투자성향 - Tendency must be between 1 (초고위험) and 5 (초저위험)
  * Serializer 개념 완벽 이해 -> .py to .json for Client
    * Serializer -> '직렬화'뿐만 아니라 '역직렬화'의 개념도 포함
      * CustomRegisterSerializer 참고!
    * PJT10번 PDF파일 참고!
  * 회원가입, 로그인, 로그아웃 기능은 JS로 구현!(익숙했다..) / 회원정보 수정(20241120 예정)

* 게시판 기능 구현(미완) -> hashtag 아이디어 포함
  * Article 모델 -> User 모델과 어떻게 연결해야 할까...
    * title : 게시글 제목
    * content : 게시글 내용
    * hashtag1 : 해쉬태그1
    * hashtag2 : 해쉬태그2
    * hashtag2 : 해쉬태그2
    * created_at : 게시글 생성 시점
    * updated_at : 게시글 수정 시점
  * Comment 모델
    * article : Foreign Key of Article
    * author : 댓글 작성자
    * content : 댓글 내용
    * created_at : 게시글 생성 시점
  * 게시글, 댓글 CRUD는 Django로 구현 예정(~~20241120~~ 20241120완료!)

  ## `git add .`는 꼭!!! 주기적으로 하자^^ -> 실수로 파일 영구삭제해서 복구하느라 많이 힘들었다 ㅎㅎ

## 20241120 수
* 게시판 기능 구현 완료
  * 게시판, 댓글 CRUD, LIKE 기능 구현 완료
    * serializer의 read_only option
      => 쉽게 말해 'POST'요청(클라이언트가 해당 필드를 수정하거나 생성 요청 등)을 할 수 없다. 하지만 'GET'요청시에는 직렬화하여 클라이언트에게 반환한다.
    * Postman
      => API 설계, 개발, 테스트, 디버깅, 문서화하는 데 유용한 API 클라이언트 도구이다. Postman의 'My Workspace'의 'Collections'에 미리 엔드포인트를 저장하여 쉽게 테스트 및 디버깅을 할 수 있다!(수아야 고마워^^)
    * Django의 class View에 대한 공부가 필요하다!!!(예정)

* 환율 계산기 기능 구현 완료
  * Django에서 한국수출입은행 환율 API 활용하여 데이터를 수집하고 DB에 저장 완료
  * 계산 기능은 Vue에서 구현
    * Vue에서 'CurrencyExchangeCards', 'CurrencyExchangeCalculator' 컴포넌트를 수정하며 프론트엔드를 살짝 경험해보았다.
    * 전체적으로 JavaScript에 대한 이해도가 낮아 코드 리뷰에 chatgpt를 많이 활용했다. => `추후 보완할 사항`
    * 결과적으로 구현했으나, 'CurrencyExchangeSelector'에 대한 논의 및 API를 활용하여 추가 데이터 수집 작업 소요가 필요할 것으로 생각된다.(~~20241121 토의 예정~~ 토의 완료!)

## 20241121 목
* User 모델 수정(필드 추가)
  * 추천 서비스 구현 시 고려해야 할 요소(필드)가 부족하다 판단하여 추가
    * marital_status : 기혼 여부(0 : 미혼, 1 : 기혼)
    * num_of_dependents : 부양가족 수
    * employment_status : 고용 여부(0 : 실업, 1 : 고용)
    * credit_score : 신용점수
    * monthly_expense : 월평균 지출
    * investment_experience : 투자 경험 여부(0 : 없음, 1 : 있음)

* exchangerate 모델 수정(추가 데이터 수집)
  * CurrencyExchangeSelector에 다양한 국가의 금일 환율 정보를 표시하면 좋을 것 같다는 의견이 있었음
  * 호주 달러, 바레인 디나르, 캐나다 달러, 스위스 프랑, 영국 파운드, 아랍에미리트 디르함의 과거 1년 치 환율 데이터 수집
  ```
  # 국가 코드
  target_currencies = ["USD", "JPY(100)", "EUR", "CNH", "AUD", "BHD", "CAD", "CHF", "GBP", "AED"]
  # 달러, 엔화, 유로, 위안화, 호주 달러, 바레인 디나르, 캐나다 달러, 스위스 프랑, 영국 파운드, 아랍에미리트 디르함
  ```

* 환율 계산기 기능 구현 수정 & 완료
  * CurrencyExchangeView 내에 있는 CurrencyExchangeCards, CurrencyExchangeCalculator, CurrencyExchangeSelector 컴포넌트 수정 완료
    * CurrencyExchangeCalculator는 오늘의 환율 데이터만 사용하여 구현
    * CurrencyExchangeCalculator 내에 지난 1년 간 달러, 유로, 엔, 위안화의 환율 변동 추이를 보여주는 꺾은선 그래프 구현 완료 -> `Chart.js`사용 -> 추후 공부하자 ^^
    * CurrencyExchangeSelector 컴포넌트 내에 오늘 기준 화폐들을 살 때 가격과 팔 때 가격을 라디오 버튼으로 구현했고, 수수료는 1%로 가정했다.
      * 수수료 계산 기능은 Vue에서 구현
        * 살 때 단위화폐 당 환율 => 환율 * 1.01
        * 팔 때 단위화폐 당 환율 => 환율 * 0.99

* 추후 금융 상품 추천 서비스 알고리즘 작성해야 함!!!
  * 금융 상품은 세 개 추천할 계획
  * 아직 구상ing...