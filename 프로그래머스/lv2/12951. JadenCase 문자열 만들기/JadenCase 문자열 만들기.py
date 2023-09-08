def solution(s):

    s = s.lower()
    convert_next = True

    result = []

    for char in s:
        # 현재 문자가 알파벳이면서, 단어의 첫 문자라면
        if char.isalpha() and convert_next:
            result.append(char.upper())
            convert_next = False
        # 현재 문자가 공백일 경우
        elif char == ' ':
            result.append(char)
            convert_next = True
        # 그 외의 경우
        else:
            result.append(char)
            convert_next = False

    return ''.join(result)
