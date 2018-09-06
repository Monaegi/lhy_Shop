# GreenWrap

## 구현목표

쇼핑몰 구동을 위한 최소기능 구현

### 기능별 

- [x] Bootstrap Template 기본 구조 설정
- [x] 카테고리 모델링
- [x] 상품, 상품옵션, 옵션별 가격/수량 모델링
- [x] 상품별 가격 변동 시 기존 가격정보 유지
- [ ] 세션기반 장바구니 기능 구현
- [ ] 주문내역 구현 및 주문내역 생성 시 주문정보(옵션명, 가격 등...) 고정값으로 저장
- [ ] 아임포트 결제 연동
- [ ] 주문 처리현황 구현
- [ ] 주문 취소기능 구현
- [ ] 회원 모델링
- [ ] 회원가입 구현

### Django Admin

- [x] 상품, 상품옵션 추가 및 변경
- [ ] 주문현황 처리
- [ ] 판매 통계
- [ ] 일정시간마다 미처리 주문 알림 기능

### 구조화

- [x] TravisCI 연동
	- [ ] TravisCI용 settings작성
	- [ ] travis.yml작성
- [ ] 상품 테스트코드 작성
- [ ] 주문내역 테스트코드 작성

## Requirements

- Python (3.6)
- pipenv

## Installation

```
pipenv install
```

## 관리자 계정

자주쓰던 아이디/비밀번호로 자동 생성 (SettingsBackend)

## 테스트

### 일반 테스트

```
py.test app
```

### 커버리지 측정하며 테스트

```
py.test app --cov=app
```