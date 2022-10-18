class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1]*len(nums1)
        nummap = {}
        for i,j in enumerate(nums1):
            nummap[j] = i
        for i in range(len(nums2)):
            if nums2[i] in nummap:
                j=i+1
                while j < len(nums2):
                    if  nums2[j] > nums2[i]:
                        x = nummap[nums2[i]]
                        output[x] = nums2[j]
                        break
                    j+=1
            
        return output
