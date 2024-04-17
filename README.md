# Instagram Clone Coding
## 과제 목표

1. DRF 적용하기 (BE)
2. REST API 구성하기
3. git 커밋 / PR에 신경써서 작업하기

## 개발 멤버 소개
<table> 
<tr> <td align="center">Front-End<br/>
<td align="center">Back-End<br/>
</tr>
<tr> <td height="0px" align="center"> <a href="https://github.com/"> <br> 윤성현 </a> <br></td> <td height="0px" align="center"> <a href="https://github.com/kim-caron"> <br> 김성현 </a> <br></td></tr> 
 </table>

## 프로젝트 기간
### 24.04.16 ~ 24.04.21
- 기획 및 설계 : 
- 프로젝트 구현 : 
- 버그 수정 및 산출물 정리 : 
 
## 개발 환경
#### Front
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white" style="height : auto; margin-left : 10px; margin-right : 10px;"/>
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white" style="height : auto; margin-left : 10px; margin-right : 10px;"/>

#### Back
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white" style="height : auto; margin-left : 10px; margin-right : 10px;"/>
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" style="height : auto; margin-left : 10px; margin-right : 10px;"/>

#### 협업 툴
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white" style="height : auto; margin-left : 10px; margin-right : 10px;"/>
<img src="https://img.shields.io/badge/Mattermost-0058CC?style=for-the-badge&logo=Mattermost&logoColor=white" style="height : auto; margin-left : 10px; margin-right : 10px;"/>


## 프로젝트 요구사항

### FE

- django가 아닌 독립적인 폴더에 프로젝트를 구성해 주세요.
- 게시물 / 릴스 / 태그됨 탭 중 **게시물** 탭만 구현해 주세요.
- NavBar: 좌측, 인스타그램이 제공하는 다양한 기능을 버튼을 통해 사용할 수 있습니다.
    - NavBar를 아이콘과 함께 구현해주세요. 단 본 과제에선 홈, 프로필 페이지만 구현하기 때문에 그 외의 버튼에 대해서는 별도의 링크 연결은 하지 않으셔도 괜찮습니다.
    - 아이콘은 다음의 링크를 통해 쉽게 구할 수 있습니다. https://fonts.google.com/icons
- StoryContainer: 팔로잉 중인 인물의 스토리 존재 여부를 확인할 수 있습니다.
    - 기본값은 해당 인물의 스토리를 확인하지 않은 상태(테두리에 빛이 들어온 상태)입니다.
    - 해당 인물의 사진을 클릭할 경우 별도의 모달창을 표시하지 않고 해당 인물을 확인한 상태(테두리에 빛이 꺼진 상태)로 변경해주세요.
- Post: 인스타그램 게시물입니다.
    - BE와 합치기 전에는 더미데이터로 진행해 주세요.
        - ex ) { id : 1, author : ‘홍길동’, post : ‘내용입니다’, liked : [ ‘홍길동’, … ], comments : [ { comment_author : ‘전우치’, comment : ‘댓글’ } , … ] }
    - 하트 버튼을 누르면 빨간색 하트로 토글됩니다.
        - (선택) 좋아요 개수가 표시됩니다.
    - 댓글 달기에서 댓글을 달 수 있으며, 게시글에 댓글이 존재한다면 최대 3개까지 보여줍니다.
- Profile: 유저 디테일 페이지입니다.
    - 작성한 게시글을 확인 할 수 있습니다.
        - (선택) 왼쪽부터 쌓이며, 한 줄에 최대 3개까지 보여줍니다.
    - 게시물, 팔로잉, 팔로우 수를 확인할 수 있습니다.

### BE

- FE와 합치기 전에는 간단한 Templates 내에서 DTL을 활용하여 테스트 해보세요.
    - 또는 Postman과 같은 API 플랫폼을 이용하셔도 좋습니다.
- (이호준) FE/BE 공통 → 개발에 앞서 기능명세서를 간단하게라도 작성해보세요.
- (이호준) App을 어떻게 나눌지(설계), model/view/serializer와 기타 class 및 function/method의 이름을 어떻게 지을지(네이밍)에 대해서도 고민해보세요.
- (이호준) branch를 분리하는 기준을 고민해보고 해당 branch에서 구현을 완료했으면 main(master) branch로 PR을 자주 날리세요.

        
- API 명세서를 작성해 보세요.
- 요청받을 데이터는 아래와 같습니다.
    - 로그인
        - createsuperuser로 진행해 보세요.
    - 게시글 작성
        - 이미지 ( 최대 1개 )
        - 내용
    - 게시글 정보
        - 이미지
        - 내용
        - 좋아요
        - 댓글
        - …
    - 프로필
        - 게시글 []
            - 게시글
                - 이미지
                - 내용
                - 좋아요
                - 댓글
                - …
        - 팔로워
        - 팔로잉

## API 명세서

### 👨‍👩‍👧‍👦회원 기능
<table> 
<tr>
<td align="center">기능<br/>
<td align="center">URL<br/>
<td align="center">method<br/>
<td align="center">return<br/>
</tr>
<tr>
<td align="center">로그인<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
</tr>
<tr>
<td align="center">팔로우<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
</tr>
</table>

### 📝게시글 기능
<table> 
<tr>
<td align="center">기능<br/>
<td align="center">URL<br/>
<td align="center">method<br/>
<td align="center">return<br/>
</tr>
<tr>
<td align="center">댓글<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
</tr>
<tr>
<td align="center">좋아요<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
</tr>
<tr>
<td align="center">상세정보<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
</tr>
<tr>
<td align="center">스토리<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
<td align="center">기능<br/>
</tr>
</table>


## 기능 명세서
<table> 
<tr>
<td align="center">
페이지 이름<br/>
<td align="center">
기능<br/>
</tr>
<tr>
<td align="center">
로그인 화면<br/>
<td align="left">
1. 로그인/ 로그아웃<br/>
</tr>
<tr>
<td align="center">
홈 화면<br/>
<td align="left">
1. 게시물 나열(이미지, 내용, 좋아요, 댓글)<br/>
2. 팔로잉 중인 인물의 스토리 존재 여부<br/>
3. 댓글 달기<br/>
</tr>
<tr>
<td align="center">
프로필 화면<br/>
<td align="left">
1. 팔로우 기능<br/>
2. 팔로우, 팔로잉 정보<br/>
3. 해당 유저의 게시글 목록(이미지, 내용, 좋아요, 댓글)<br/>
4. 해당 유저의 스토리<br/>
</tr>
</table>

## ERD

## Commit Template
```
# 제목은 최대 50글자까지 아래에 작성: ex) Feat: Add Key mapping  

# 본문은 아래에 작성  

# 꼬릿말은 아래에 작성: ex) Github issue #23  

# --- COMMIT END ---  
#   <타입> 리스트  
#   feat        : 기능 (새로운 기능)  
#   fix         : 버그 (버그 수정)  
#   refactor    : 리팩토링  
#   design      : CSS 등 사용자 UI 디자인 변경  
#   comment     : 필요한 주석 추가 및 변경  
#   style       : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)  
#   docs        : 문서 수정 (문서 추가, 수정, 삭제, README)  
#   test        : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)  
#   chore       : 기타 변경사항 (빌드 스크립트 수정, assets, 패키지 매니저 등)  
#   init        : 초기 생성  
#   rename      : 파일 혹은 폴더명을 수정하거나 옮기는 작업만 한 경우  
#   remove      : 파일을 삭제하는 작업만 수행한 경우  
# ------------------  
#   제목 첫 글자를 대문자로  
#   제목은 명령문으로  
#   제목 끝에 마침표(.) 금지  
#   제목과 본문을 한 줄 띄워 분리하기  
#   본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.  
#   본문에 여러줄의 메시지를 작성할 땐 "-"로 구분  
# ------------------  
#   <꼬리말>  
#   필수가 아닌 optioanl  
#   Fixes        :이슈 수정중 (아직 해결되지 않은 경우)  
#   Resolves     : 이슈 해결했을 때 사용  
#   Ref          : 참고할 이슈가 있을 때 사용  
#   Related to   : 해당 커밋에 관련된 이슈번호 (아직 해결되지 않은 경우)  
#   ex) Fixes: #47 Related to: #32, #21  
```