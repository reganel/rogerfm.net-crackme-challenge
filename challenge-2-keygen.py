def pg(login):
    v5=45
    answer = 0
    for i in login:
        answer+=v5*ord(i)
        v5+=1
    return answer
