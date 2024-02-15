def solution(phone_book):
    phone_book_hash = set(phone_book)  # 전화번호부를 해시 테이블에 저장
    for phone_number in phone_book:
        temp = ""
        for number in phone_number[:-1]:  # 마지막 숫자를 제외한 모든 숫자에 대해
            temp += number
            if temp in phone_book_hash:  # 현재 접두사가 해시 테이블에 있는지 확인
                return False
    return True