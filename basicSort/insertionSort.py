def insertionSort(input_array,array_length):
    for i in range(2, array_length+1):
        val, idx=input_array[i],i
        while input_array[idx-1]>val:
            input_array[idx]=input_array[idx-1]
            idx-=1
        input_array[idx]=val



