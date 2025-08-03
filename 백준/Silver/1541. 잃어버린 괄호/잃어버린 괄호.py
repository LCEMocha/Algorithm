expr = input()

tokens = []
num = ''
for ch in expr:
    if ch in '+-':
        if num:
            tokens.append(str(int(num)))  # 선행 0 제거
        tokens.append(ch)
        num = ''
    else:
        num += ch
if num:
    tokens.append(str(int(num)))  # 마지막 숫자 처리

result_expr = []
i = 0
while i < len(tokens):
    if tokens[i] == '-':
        result_expr.append('-(')
        i += 1
        result_expr.append(tokens[i])
        i += 1
        while i < len(tokens) and tokens[i] != '-':
            result_expr.append(tokens[i])
            i += 1
            if i < len(tokens):
                result_expr.append(tokens[i])
                i += 1
        result_expr.append(')')
    else:
        result_expr.append(tokens[i])
        i += 1

final_expr = ''.join(result_expr)
print(eval(final_expr))