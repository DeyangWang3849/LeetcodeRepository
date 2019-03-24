def findMedianSortedArrays(nums1:list,nums2:list):
    combine = sorted(nums1 + nums2)
    l = len(combine)
    if l % 2 == 0:
        return (combine[l >> 1] + combine[l >> 1 - 1]) / 2
    else:
        return combine[l >> 1]

if __name__ == '__main__':
    nums1 = [2,3,5,6,7]
    nums2 = [1,4,9,10]
    print('The median is ' + str(findMedianSortedArrays(nums1,nums2)))