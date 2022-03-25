
def get_yellow_num(width, height):
    return (width-2)*(height-2)

def solution(brown, yellow):
    width = brown // 2
    height = 2

    while width >= height:
        if get_yellow_num(width, height) == yellow:
            break
        width -= 1
        height += 1
    answer = [width, height]
    return answer


print(solution(24, 24))