from collections import defaultdict, deque
from typing import List
from enum import Enum

"""
leet code question 207. https://leetcode.com/problems/course-schedule/
Can be done two ways:
* dfs - modified to keep track status of each vertex (not_visited, processing and processed). If a status of "processing" is encountered then we are in a cycle. And the schedule is invalid
* topological sort using khan algorithm
"""

class Status(Enum):
    NOT_VISITED = 0
    PROCESSING = 1
    PROCESSED = 2


class Solution:

    def dfs(self, start, course_graph, visited) -> bool:
        # We will keep track of the status of each vertex. If we come across a processed vertex then we can exit as we don't need to reprocess it
        if visited[start] == Status.PROCESSED:
            return True
        # If we come across a vertex that is marked as "processing" then we have encountered a cycle. We are currently processing that vertex and one of its edges led back to it! So, we can return False as it is not a valid course schedule
        if visited[start] == Status.PROCESSING:
            return False
        visited[start] = Status.PROCESSING
        # defaultdict will automatically add a key if it is not found in the dict. The if statement is here to prevent a key from being added if it does not exist
        if start in course_graph:
            for node in course_graph[start]:
                if not self.dfs(node, course_graph, visited):
                    # we enountered a vertex that was in processing status. So a cycle exits. Return False as the course prerequisites are not valid.
                    return False
        # If we make it here then a cycle did not exist and the course prerequistes are valid.
        # Mark the vertex as processed so we do not prcess it again. We've determined this course has valid prerequisites.
        visited[start] = Status.PROCESSED
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a graph where the keys are the courses and the values are the prerequisites for each course
        course_graph = defaultdict(list)
        for course, prereq in prerequisites:
            course_graph[course].append(prereq)

        visited = [Status.NOT_VISITED] * numCourses

        # every key needs to be traversed because the graph may be disconnected
        for key in course_graph:
            if not self.dfs(key, course_graph, visited):
                return False

        return True


class Solution2:
    """
    solution using Kahn's topological sort algorithm
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a graph where the keys are the courses and the values are the prerequisites for each course
        course_graph = defaultdict(list)
        # this array keeps track of how many edges are incoming to a vertex (how many dependecies a course has)
        # because the course ids are 0 <= a, b <= numCourses, array index is course id 
        incoming_edges = [0] * numCourses

        # populate the incoming_edges with the number of prerequisites for each course
        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
            incoming_edges[course] += 1


        # initialize the queue with any courses that do NOT have any prerequisites
        processing_queue = deque()
        for course, prereq in enumerate(incoming_edges):
            if prereq == 0:
                processing_queue.append(course)

        # we don't need a topological ordering for this scenario. We just need to know if the schedule is valid or not
        # so just keep track of the number of classes processed. If it differs from the graph size then the schedule is
        # invalid
        num_classes_processed = 0
        while processing_queue:
            num_classes_processed += 1
            course = processing_queue.pop()
            for dependency in course_graph[course]:
                incoming_edges[dependency] -= 1
                if incoming_edges[dependency] == 0:
                    processing_queue.append(dependency)
        return num_classes_processed == numCourses

