# 플레이페어 암호

# J를 제외한 대문자로 주어짐
inp = input()
cipherkey = input()

alphabet = [chr(i) for i in range(65, 91) if chr(i) != "J"]
panel = []

for k in cipherkey:
    if k in alphabet:
        alphabet.remove(k)
        panel.append(k)

for i in alphabet:
    panel.append(i)

# inp를 두글자씩 나누어서 같은건 X 추가, X가 같으면 Q 추가하기, 마지막 Padding은 X
twice = 0
inp_set = []

while twice < len(inp):
    a = inp[twice]
    if twice + 1 == len(inp):
        # 마지막 한 글자가 남으면 무조건 X 패딩 (XX가 되어도 그대로)
        inp_set.append(a + 'X')
        twice += 1
    else:
        b = inp[twice + 1]
        if a != b:
            inp_set.append(a + b)
            twice += 2
        else:
            filler = 'Q' if a == 'X' else 'X'
            inp_set.append(a + filler)
            twice += 1

answer = []

for k in inp_set:
    p, q = panel.index(k[0]) // 5, panel.index(k[0]) % 5
    r, s = panel.index(k[1]) // 5, panel.index(k[1]) % 5

    # 같은행 -> shift >1
    if p == r:
        answer.append(panel[p*5 + (q+1)%5])
        answer.append(panel[r*5 + (s+1)%5])
    
    # 같은열 -> shift v1
    elif q == s:
        answer.append(panel[((p+1)*5)%25 + q])
        answer.append(panel[((r+1)*5)%25 + s])

    # 다른행 다른열 -> 위치 swap
    else:
        answer.append(panel[p*5 + s])
        answer.append(panel[r*5 + q])

print("".join(answer))
