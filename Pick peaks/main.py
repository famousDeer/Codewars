def pick_peaks(arr):
    pos = []
    peak = False
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            peak = i
        elif arr[i] < arr[i-1] and peak:
            pos.append(peak)
            peak = False

    return {'pos': pos, 'peaks': [arr[i] for i in pos]}

arr_num = [1,2,3,6,4,1,2,3,2,1]

print(pick_peaks(arr_num))