input_file = open("input2.txt", 'r')
output_file = open("output2.txt", 'w')

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        change = 0  
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                change = 1  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if change == 0:  
            break


t = int(input_file.readline())
array = list(map(int, input_file.readline().split()))

bubbleSort(array)

print(" ".join(map(str, array)), file=output_file)

input_file.close()
output_file.close()