s = input()

def create(start_num, total_len):
    set = ''
    start = str(start_num)
    end =''
    for n in range(start_num,1000):
        if len(set) >= total_len:
            break
        set += str(n)
        end = str(n)
    return set,start,end
def solve():
    case=[]
    case.append(create(int(s[0]),len(s))) #한자리
    if len(s) >= 2:
        case.append(create(int(s[0:2]),len(s))) #두자리
    if len(s) >= 3:
        case.append(create(int(s[0:3]),len(s))) #세자리

    for i in range(3):
        if s == case[i][0]:
            print(case[i][1], case[i][2])
            break

solve()
