# Simple ATM Controller

클래스와 메서드로만 이루어진 간단한 ATM.
MVC 패턴 구성 및 테스트 코드 포함.

## 설치
1. 터미널 창 띄우기
2. `git clone` 입력
3. `pip install argon2_cffi` 입력
  (Argon2: 암호화를 위한 해쉬 라이브러리)

## 테스트
Python 내장 라이브러리인 unittest를 이용합니다.
터미널에 `python -m unittest` 입력

패키지별로 테스트하고 싶은 경우, `python -m unittest 패키지명/test/*.py` 입력
예) service 폴더만 테스트하고 싶은 경우,  `python -m unittest service/test/*.py`

주의: 각 폴더에 __init__.py를 추가해야 합니다.
그래야 unittest가 파일들을 찾을 수 있습니다.


## 구조
Django 없이 클래스와 메서드로만 구성되어 있습니다.

Spring 프레임워크의 구조와 유사하게 MVC 패턴을 적용했습니다.
이는 요구사항에서 은행 API나 ATM 기기랑 연동될 수도 있다고 했기에,
확장성을 고려했습니다.

크게 Controller - Service - Repository로 구성되어 있습니다.
역순으로 보자면,
Repository: DB에 저장하거나, DB에서 데이터를 받아오는 역할

Service: 핵심 비즈니스 로직을 다루는 역할. 
유저가 입력한 값을 체크해 repository에 저장하거나,
repository에서 받아온 값을 처리해서 반환합니다.

Controller: 유저에게 받은 입력을 서비스에 넘겨 처리한 후, 다시 유저에게 돌려줍니다.
각각의 서비스들을 묶어서 일련의 순서를 따르게 할 수 있습니다.

### Repository
DB와 연동되는 부분.

Java의 Interface와 유사하게 Python에서 추상 클래스(abstract class)를 이용하여 구현.
이를 통해 기존 코드 수정 없이 DB 종류에 따라 확장할 수 있음.

현재는 가장 간단하게 메모리를 저장 장치로 사용 중.
차후 DB를 쓰게 될 경우, 추상 클래스를 상속하여 기존 메서드들을 오버라이딩 해야 함.

