# 싸피 1학기 관통 프로젝트_Dalang

## 20241118 MON
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

* 한국수출입은행 정기예금 API를 활용하여 1년 간 환율 데이터 시각화 기능 구현
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

## 20241119 TUE
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
  * 게시글, 댓글 CRUD는 Django로 구현 예정(20241120)

  ## `git add .`는 꼭!!! 주기적으로 하자^^ -> 실수로 파일 영구삭제해서 복구하느라 많이 힘들었다 ㅎㅎ