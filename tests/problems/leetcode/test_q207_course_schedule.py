from problems.leetcode.q207_course_schedule import Solution, Solution2

class TestSolution1:
    def test_two_course_no_cycle(self):
        sol = Solution()
        assert sol.canFinish(2,   [[1,0]])

    def test_three_courses_no_cycle(self):
        sol = Solution()
        assert sol.canFinish(3, [[0,1],[1,2]])

    def test_four_courses_no_cycle(self):
        sol = Solution()
        assert sol.canFinish(4, [[0,1], [1,2], [2,3]])

    def test_three_courses_has_cycle(self):
        sol = Solution()
        assert sol.canFinish(3, [[0,1], [1,2], [2,0]]) is False

    def test_non_connected_graph_no_cycle(self):
        sol = Solution()
        assert sol.canFinish(6, [[0,1], [1,2], [2,3], [4,5]])

    def test_course_has_multiple_prereques(self):
        sol = Solution()
        assert sol.canFinish(3, [[0,1], [0,2]])

    def test_course_has_multiple_prereques_that_also_have_prereques(self):
        sol = Solution()
        assert sol.canFinish(3, [[0,1], [0,2], [1,2]])

    def test_non_connected_graph_with_cycle(self):
        sol = Solution()
        assert sol.canFinish(7, [[0,1], [0,2], [1,3], [4,5], [5,6], [6,4]]) is False

class TestSolution2:
    def test_two_course_no_cycle(self):
        sol = Solution2()
        assert sol.canFinish(2,   [[1,0]])

    def test_three_courses_no_cycle(self):
        sol = Solution2()
        assert sol.canFinish(3, [[0,1],[1,2]])

    def test_four_courses_no_cycle(self):
        sol = Solution2()
        assert sol.canFinish(4, [[0,1], [1,2], [2,3]])

    def test_three_courses_has_cycle(self):
        sol = Solution2()
        assert sol.canFinish(3, [[0,1], [1,2], [2,0]]) is False

    def test_non_connected_graph_no_cycle(self):
        sol = Solution2()
        assert sol.canFinish(6, [[0,1], [1,2], [2,3], [4,5]])

    def test_course_has_multiple_prereques(self):
        sol = Solution2()
        assert sol.canFinish(3, [[0,1], [0,2]])

    def test_course_has_multiple_prereques_that_also_have_prereques(self):
        sol = Solution2()
        assert sol.canFinish(3, [[0,1], [0,2], [1,2]])

    def test_non_connected_graph_with_cycle(self):
        sol = Solution2()
        assert sol.canFinish(7, [[0,1], [0,2], [1,3], [4,5], [5,6], [6,4]]) is False   
