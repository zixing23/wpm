def find_closest(look_for,target_data):
    def differt(first,second):
        if first == second:
            return(0)
        elif first > second:
            return(first - second)
        else:
            return(second - first)

    max_diff = 999999
    for each_thing in target_data:
        diff = differt(each_thing,look_for)
        if diff == 0:
            found_it = each_thing
            break
        elif diff < max_diff:
            max_diff = diff
            found_it = each_thing
    return(found_it)

a = find_closest(3,[1,3,5.5,7,10,100])
print(a)



