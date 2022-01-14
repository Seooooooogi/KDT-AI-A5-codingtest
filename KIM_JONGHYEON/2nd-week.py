def solution(s):
    answer = ""
    tmp1=""
    tmp2=""
    count = 1
    min = len(s)
    for i in range(1,len(s)+1,1):
        answer = ""
        if len(s) % i == 0:
            for j in range(len(s)//i):
                for l in range(i):
                    tmp2 += s[j*i+l]
                if tmp1 == '':
                    tmp1 = tmp2
                elif tmp1 == tmp2:
                    count += 1
                else:
                    if count != 1:
                        answer += str(count) + tmp1
                        count = 1
                    else:
                        answer += tmp1
                    if j == len(s)//i - 1:
                        answer += tmp2
        if min > len(answer):
            min = len(answer)
            answer = ''
                
    return answer