class Search:
    """
    In Progress
    """

    def __init__(self) -> None:
        pass

    def binarySearch(nums,target):
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return None
        
            