# DesignPattern

## Command Pattern
- 커맨드 패턴은 객체가 특정 기능을 바로 수행하거나 나중에 트리거할 때, 필요한 모든 정보를 캡슐화하는 행동 패턴이다.
    - 메소드명
    - 메소드를 소유하는 객체
    - 메소드 인자
- Command, Receiver, Invoker, Client 클래스로 구성된다.
    - command객체는 Receiver 객체에 대해 알고 있으며, Receiver객체의 함수를 호출한다.
    - Receiver 함수의 인자는 Command 객체에 저장되어 있다.
    - Invoker는 명령을 수행한다.
    - Client는 Command 객체를 생성하고 Receiver를 정한다.
- Command Pattern은 다음의 3가지 상황에 적합하게 사용된다.
    - 수행할 명령에 따라 객체를 변수화 할 때
    - 요청을 큐에 저장하고 각기 다른 시점에 수행해야 하는 경우
    - 작은 단위의 연산을 기반으로 하는 상위 연산을 만들 때
- Command Pattern 실제 활용 사례
    - 증권거래소를 보면, 증권거래소를 통해서 고객은 주식을 매수 또는 매도한다.
    - 일반적으로 고객이 주식을 직접 사거나 팔지 않고, 에이전트나 브로커가 고객과 거래소 사이에서 중개역할을 한다.
    - 월요일 오전에 주식시장이 개장하면 주식을 매매하려는 경우
        - 주식시장이 휴장한 일요일 밤에도 중개사에게 매매를 요청할 수 있다.
        - 중개사는 요청을 월요일 아침까지 큐에 넣어둔다.
- Command Pattern 장점
    - 작업을 요청하는 클래스와 실제로 작업을 수행하는 클래스를 분리한다.
    - 큐에 커맨드를 순서대로 저장한다.
    - 기존 코드를 수정하지 않고, 새로운 커맨드를 쉽게 추가할 수 있다.
    - 커맨드 패턴으로 롤백 시스템을 구현할 수 있다.
- Command Pattern 단점
    - 클래스와 객체가 많으므로, 신중하게 클래스를 작성해야 한다. 
    - 모든 작업이 독립적인 Command 클래스이므로 구현, 유지보수해야 하는 클래스가 많다.

## Proxy Pattern
- 프록시(Proxy)란?
    - 요청자와 공급자 사이의 중재자를 의미한다.
    - 요청자는 요청을 하고, 공급자는 요청에 맞는 리소스(Resource)를 전달한다.
    - 웹 서비스 관점에서는 Proxy Server가 해당된다.
        - 클라이언트가 특정 웹사이트에 접속하면 우선 프록시 서버에 웹 페이지 등의 리소스를 요청한다.
        - 프록시 서버는 내부적으로 요청을 분석해, 알맞은 서버로 요청을 보내고 결과를 받아 클라이언트에게 전달한다.
- 디자인 패턴 관점에서 Proxy 클래스는 객체의 인터페이스 역할을 한다.
    - 여기서 객체란? 네트워크 연결 또는 메모리, 파일에 저장된 객체 등의 다양한 종류에 해당된다.
    - 정리하면, Proxy 클래스는 반환해 사용할 객체를 감싸는 포장지 또는 에이전트 객체이다.
- Proxy는 객체 클래스의 구현과 상관없이 감싸려는 객체에 대한 기능을 제공한다.
- Proxy Pattern의 예시
    - 배우(Actor), 에이전트(Agent)의 관계를 비유한다.
    - 배우 모집을 할 때, 보통 직접 배우에게 연락하기보다 에이전트를 통해 모집한다.
    - 배우의 스케줄과 상황에 따라 에이전트는 출연할 의사가 있는지 전달한다.
    - 제작사는 배우에게 직접 접근하지 않고, 에이전트가 배우를 대신해 스케줄과 출연료를 조율하는 Proxy의 역할을 한다.
- 데코레이터(@decorator)와 프록시(Proxy) 차이점?
    - 데코레이터는 런타임에 객체에 대한 추가적인 행위를 한다.
    - 프록시는 객체에 대한 접근을 제어한다. 즉, 프록시와 연결된 object들은 동적이지 않다.

## Observer Pattern
- 행위 패턴으로서 이름 그대로 객체의 역할(행동)에 초점을 둔다.
- 더 큰 기능을 구현하기 위한 객체 간의 상호 작용을 중요시하며, 가장 단순한 행위 패턴이다.
    - 옵서버 패턴에서 객체는 자식의 목록을 유지하며 객체가 옵서버에 정의된 메소드를 호출할 때마다 옵서버에 이를 알린다.
- 분산형 애플리케이션에는 사용자가 요청한 작업을 수행하는 다수의 서비스가 엮여 있다.
    - 사용자 가입 절차를 진행한다.
    - 사용자의 계정 상태를 확인하고, 이메일을 발송한다.
    - 사용자가 가입을 하면 유저 서비스는 이메일 서비스의 메소드를 호출 해, 계정 인증 이메일을 발송한다.
    - 계증은 인증됐지만, 포인트가 부족한 경우 사용자에게 이를 알리는 이메일을 전송한다.
- 브로드캐스트 혹은 pub/sub 시스템에서 옵서버 패턴이 자주 등장한다.
    - 만약 특정 블로그의 최신글을 즐겨 읽는 기술 애호가가 있다.
        - 블로그는 구독자 또는 옵서버의 목록을 유지하는 객체이다.
    - 특정 기술 블로그를 구독하였다. 특정 기술 블로그는 이미 많은 구독자를 보유하고 있다.
    - 블로그에 새로운 글이 등록되거나 기존 글이 수정되면 구독자들은 알림을 받는다.
- 옵서버 패턴은 다음과 같은 상황에 적합하다.
    - 분산 시스템의 이벤트 서비스를 구현
    - 뉴스 에이전시 프레임워크
    - 주식 시장 모델

## Adapter Pattern
- 클라이언트의 요구에 따라 특정 인터페이스를 다른 인터페이스에 맞춘다.
- 서로 다른 클래스의 인터페이스를 목적에 맞춰 변환한다.

## Bridge Pattern
- 객체의 인터페이스와 구현을 분리해 독립적으로 동작할 수 있게 한다.

## Decorator Pattern
- 런타임에 객체의 책임을 덧붙인다. 인터페이스를 통해 객체에 속성을 추가한다.

## Facade Pattern
- 복잡한 내부 시스템 로직을 감추고 클라이언트가 쉽게 시스템에 접근할 수 있는 인터페이스를 제공한다.
    - 상점의 구조를 전혀 모르는 고객이 물품을 구입하러 상점을 방문했다.
    - 일반적으로 상점에 대해 잘 알고 있는 주인에게 먼저 다가간다.
    - 주인은 고객이 요청한 물품을 찾아 고객에게 전달한다.
- 서브시스템의 인터페이스를 통합시킨 단일 인터페이스를 제공해 클라이언트가 쉽게 서브시스템에 접근할 수 있게 한다.
- 단일 인터페이스 객체로 복잡한 서브시스템을 대체한다.
- 클라이언트와 내부 구현을 분리한다.
- Facade: 외부에서 보기에 깔끔하도록 복잡한 서브시스템을 감싸는 역할을 한다.
    - 어떤 서브시스템이 요청에 알맞는지 알고 있는 인터페이스이다.
    - 텀포지션을 통해 클라이언트의 요청을 적합한 서브시스템 객체에 전달한다.
- System: 전체 시스템을 하나의 복잡한 복합체로 만드는 여러 서브시스템의 집합이다.
    - 서브시스템의 기능을 구현하는 클래스이다. 
    - Facade 객체가 지시한 일을 담당하지만 Facade의 존재도 모르며 참조하지도 않는다.
- Client: Facade를 통해 서브시스템과 통신한다.
    - 클라이언트는 Facade를 인스턴스화하는 클래스이다.
    - Facade에 서브시스템을 통해 작업을 수행하도록 요청한다.