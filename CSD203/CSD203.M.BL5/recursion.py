def move(n,a,b,c):
    if n == 1:
        print(f"{a} -> {b}")
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,c,b,a)
        
move(10,"a","b","c")