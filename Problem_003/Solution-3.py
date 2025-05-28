
tamim = int(input('tamims age:'))
hamim = int(input('hamims age:'))

def GetElderBrother(tamim, hamim):
    if tamim > hamim:
        return f"Elder is: tamim, Age: {tamim}"
    elif hamim > tamim:
        return f"Elder is: hamim, Age: {hamim}"
    else:
        return "Same Age"

print(GetElderBrother(tamim, hamim))