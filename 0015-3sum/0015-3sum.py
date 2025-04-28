# inspired by NeetCode

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
  
        # ! reduce this to n "two sum on sorted input" problems:
        nums.sort()
        #print(nums)
        list_of_triplets = []
        
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, len(nums) - 1
            while j<k:
                #print(f"{i},{j},{k}\t{nums[i]},{nums[j]},{nums[k]}")
                target = -nums[i]
                cur_pair_sum = nums[j]+nums[k]
                if  cur_pair_sum < target:
                    j += 1
                    while j<=k and nums[j] == nums[j-1]:
                        j += 1
                elif cur_pair_sum > target:
                    k -= 1
                    while k>=j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    # found a triplet:
                    #print(f"accepted {i},{j},{k}\t{nums[i]},{nums[j]},{nums[k]}")
                    list_of_triplets.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    while k>=j and nums[k] == nums[k+1]:
                        k -= 1

        return list_of_triplets
    