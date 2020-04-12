# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps
    
    # skip the last level       
    i = len(data) // 2
    currentSize = len(data)
    while i + 1 > 0:
        j = i
        while (j * 2 + 1) <= currentSize - 1:
            # get min child index
            if j*2 + 2 > currentSize - 1:
                mc = j*2 + 1
            else:
                if data[j*2 + 1] < data[j*2 + 2]:
                    mc = j * 2 + 1
                else:
                    mc = j * 2 + 2
            # if parent node larger than min child, then swap 
            if data[j] > data[mc]:
                swaps.append((j,mc))
                tmp = data[j]
                data[j] = data[mc]
                data[mc] = tmp
            j = mc      
        i = i - 1
    return swaps

# build_heap([5,4,3,2,1])          
# build_heap([1,2,3,4,5])          


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

