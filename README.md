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