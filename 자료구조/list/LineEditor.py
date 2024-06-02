from arraylist import ArrayList


list = ArrayList()
while True:
    command = input(["메뉴 선택 i-입력, d-삭제, r-변경, p-출력, l-읽기, s-저장, q-종료: "])

    if command == 'i':
        pos = int(input("입력행 번호: "))
        e = input("입력값 내용: ")
        list.insert(pos, e)

    elif command == 'd':
        pos = int(input("입력행 번호: "))
        list.delete(pos)

    elif command == 'r':
        pos = int(input("입력행 번호: "))
        e = input("입력값 내용: ")
        list.replace(pos, e)

    elif command == 'p':
        print("Line Editor")
        for line in range(list.size):
            print("[%d] " %line, end = '')
            print(list.getEntry(line))
        print()


    elif command == 'l':
        filename = "text.txt"
        innerfile = open(filename , 'r')
        lines = innerfile.readlines()
        for line in lines:
            list.insert(list.size, line.rstrip("\n"))
        innerfile.close()


    elif command == 's':
        filename = "text.txt"
        outerfile = open(filename, "w")
        list_size = list.size
        for line in range(list_size):
            outerfile.write(list.getEntry(line) + "\n")
        outerfile.close()
    elif command == "q":
        exit()