def print_sequence(sequence):
    result = ""
    cnt = 0
    for el in sequence:
        if cnt == 0:
            cnt+=int(el)-1
            result+=el
        else:
            cnt-=1
    return result

if __name__ == "__main__":
    print_sequence(input('введите последовательность'))
