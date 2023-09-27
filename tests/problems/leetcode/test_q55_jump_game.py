from problems.leetcode.q55_jump_game import Solution

def test():
    sol = Solution()
    assert not sol.canJump([3, 2, 1, 0, 4]) 
    assert not sol.canJump([0,1])  
    assert not sol.canJump([1,0,1])
    assert sol.canJump([0])
    assert sol.canJump([1]) 
    assert sol.canJump([1,1]) 
    assert sol.canJump([3,2,2,0,4])
    assert sol.canJump([[2,3,1,1,4]])