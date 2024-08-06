def even_odd(l3):
    output_list=[]
    for num in l3:
        if num%2==0:
            output_list.append("even")
        else:
            output_list.append("odd")
    return output_list
