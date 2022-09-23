n = int(input())

def func2(arr, n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if(arr[i] + arr[j] == 100):
                print("1")
                return 1
    print("0")       
    return 0

func2([50, 42], n)