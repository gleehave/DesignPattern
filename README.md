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