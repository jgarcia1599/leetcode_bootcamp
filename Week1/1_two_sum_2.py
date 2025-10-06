# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# d

def twoSum(numbers, target):
    pointer_1,pointer_2 = 0, len(numbers)-1
    while pointer_1 < pointer_2: 
        current_sum = numbers[pointer_1] + numbers[pointer_2]
        if current_sum == target: 
            return [pointer_1+1,pointer_2+1]
        elif current_sum < target: 
            pointer_1+=1
        else: 
            pointer_2-=1
    return []