class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        write_pos = len(nums1) - 1
        source1_pos = m - 1
        source2_pos = len(nums2) - 1

        while write_pos >= 0:
            #print(f"{write_pos},{source1_pos},{source2_pos}")
            if source1_pos >= 0 and source2_pos >= 0:
                # pick the largest, or the first in case of a tie:
                if nums1[source1_pos] >= nums2[source2_pos]:
                    nums1[write_pos] = nums1[source1_pos]
                    source1_pos -= 1
                else:
                    nums1[write_pos] = nums2[source2_pos]
                    source2_pos -= 1
            
            elif source1_pos >= 0:
                nums1[write_pos] = nums1[source1_pos]
                source1_pos -= 1
            else:
                nums1[write_pos] = nums2[source2_pos]
                source2_pos -= 1

            write_pos -= 1
