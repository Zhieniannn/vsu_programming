def sk(i):
    opens = i.count('(')
    closes = i.count(')')
    if opens > closes:
        return 'нет ', opens - closes, ' закрытой скобки'
    elif opens < closes:
        return 'нет ', closes - opens, ' открытой скобки'
    return 'скобок нет'


print(sk(input('Example: ')))
