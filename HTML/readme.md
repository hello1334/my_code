# HTML
------
## CSS
### Web site
인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
### Web pasge
HTML, CSS 등의 웹 기술을 이용하여 만들어진, "Web site"를 구성하는 하나의 요소
### Web pasge 구성요소
HTML "Structure"   CSS "Styling"   Javascript "Behavior"
### HTML
HyperText Markup Language : 웹 페이지의 의미와 구조를 정의하는 언어
### Hypertext
웹 페이지를 다른 페이지로 연결하는 링크  
참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
### Markup Language
태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어  
ex)HTML, Markdown
### <body></body>
- 페이지에 표시되는 모든 콘텐츠
### HTML Element(요소)
하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성된다.  
닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재
### HTML Attributes(속성)
1. 규칙
* 속성은 요소 이름과 속성 사이에 공백이 있어야 함  
* 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함  
* 속성 값은 열고 닫는 따옴표로 감싸야 함  
2. 목적
* 나타내고 싶진 않지만 추가적인 기능, 내용을 담고 싶을 때 사용  
* CSS에서 해당 요소를 선택하기 위한 값으로 활용된다.
### HTML Test structure
HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것
### h1 요소의 의미
h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것
### css
Cascading Style Sheet  
웹 페이지의 디자인과 레이아웃을 구성하는 언어
1. 선택자(Selector)  보통 중괄호로 구역을 설정함
2. 선언(Declaration)  선언 뒤에는 ;가 있어야함
3. 속성(Property) 
4. 값(Value)  값 뒤에서 ;가 있어야함
### CSS Selectors
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
### 자손 결합자 (""(space))
- 첫 번째 요소의 자손 요소들 선택
- 예) p span은 \<p> 안에 있는 모든 <span>를 선택 (하위 레벨 상관 없이)
### 자식 결합자 (">")
- 첫 번째 요소의 직계 자식만 선택
- 예) ul > li은 \<ul> 안에 있는 모든 \<li>를 선택 (한단계 아래 자식들만)
### !important
다른 우선순위 규칙보다 우선하여 적용하는 키워드  
* Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음
### HTML 관련 사항
1. 요소(태그) 이름은 대소문자를 구분하지 않지만 "소문자" 사용을 권장
2. 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 "큰 따옴표" 권장
3. HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 시 주의
4. CSS 인라인(inline) 스타일은 사용하지 말것
    - CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦
5. CSS의 모든 속성을 외우는 것이 아님
    - 자주 사용되는 속성은 그리 많지 않으며 주로 활용 하는 속성 위주로 사용하다 보면 자연스럽게 익히게 됨
    - 그 외 속성들은 개발하며 필요할 때마다 검색해서 학습 후 사용할 것
6. 속성은 되도록 'class'만 사용할 것
    - id, 요소 선택자 등 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
    - 문서에서 단 한번 유일하게 적용될 스타일에 경우에만 id 선택자 사용을 고려
7. 모르는것이 생기면 구글에 mdn을 검색하여 참고

## CSS Layout
### CSS Box Model
모든 HTML 요소를 사각형 박스로 표현하는 개념  
내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되는 개념  
### width & height 속성
요소의 너비와 높이를 지정  
이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함
### 박스 타입
block 타입과 inline 타입이 존재
1. block 타입
- 항상 새로운 행으로 나뉨
- 기본적으로 width속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
- 대표적인 block 타입 태그 h1~6, p, div
2. inline 타입의 특징
- 새로운 행으로 나뉘지 않음
- width와 height 속성을 사용할 수 없음
- 수직 방향. 다른 요소를 밀어낼 수 없음
- 수평 방향. 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그. a, img, span
3. inline block 타입
- inline과 block 요소 사이의 중간 지점을 제공하는 display 값
### CSS Position
요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
### Position 유형별 특징
1. static
- 기본값
- 요소를 Normal Flow에 따라 배치
2. relativ
- 요소를 Normal Flow에 따라 배치
- 자기 자신을 기준으로 이동
- 요소가 차지하는 공간은 static일 때와 같음
3. absolut
- 요소를 Normal Flow에서 제거
- 가장 가까운 relative 부모 요소를 기준으로 이동
- 문서에서 요소가 차지하는 공간이 없어짐
4. fixed
- 요소를 Normal Flow에서 제거
- 현재 화면영역(viewport)을 기준으로 이동
- 문서에서 요소가 차지하는 공간이 없어짐
5. sticky
- 요소를 Normal Flow에 따라 배치
- 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨(fixed)
- 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체  
    이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문
### z-index
요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
1. 정수 값을 사용해 z축 순서를 지정
2. 더 큰 값을 가진 요소가 작은 값의 요소를 덮음
### CSS Flexbox
요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
### Bootstrap
bootstrap 기본 사용법  
mt-5 는 margin 같은 요소의 앞자, top, -뒤의 숫자는 사이즈이다.
### 대표적인 Component
1. Alerts (경보해주기)
2. Badges
3. Buttons
4. cards
5. Navbar
### 대표적인 semantic element
div만 사용하면 개발자들이 코드를 읽을 때 힘들기 때문에 div와 기능은 같지만 이름이 구별되는 요소들을 만듬
1. header
2. nav
3. main
4. article
5. section
6. aside
7. footer
### OOCSS
object oriented css : 객체 지향적 접근법을 적용하여 css를 구성하는 방법론  
css를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인
1. 구조와 스킨을 분리
2. 컨테이너와 콘텐츠를 분리