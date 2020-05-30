"""
4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
Hints: #26, #47, #60, #85, #125, #133

Alternatively, we can use depth-first search (DFS) to find the build path.
"""
from enum import Enum
import unittest
from collections import deque

def find_projects_build_order(project_name_list, project_dependency_list):
    graph = build_graph(project_name_list, project_dependency_list)
    return order_project(graph.get_projects())


def order_project(projects):
    # new stack to store the order
    stack = deque()
    # for all project, we do dfs search
    for project in projects:
        if project.state == Project.State.BLANK:
            if do_dfs(project, stack) == False:
                return None
    return stack


def do_dfs(project, stack):
    # if we meet a project with state partial, then we return false, it's a cycle
    if project.state == Project.State.PARIAL:
        return False
    
    # update current project state
    if project.state == Project.State.BLANK:
        project.state == Project.State.PARIAL

        # do dfs search for the child project 
        # only when the current project has blank state
        children = project.children
        for child in children:
            if do_dfs(child, stack) == False:
                return False
        # push curr to the stack when it's done pushiing all the children to the stack
        # this way we maintain the order or the stack correctlt. 
        project.set_state(Project.State.COMPLETE)
        stack.appendleft(project)

    # return true when it's finished a dfs search for a project
    return True

def build_graph(project_name_list, project_dependency_list):
    graph = Graph()

    # build project
    for project in project_name_list:
        graph.get_or_create_project(project)
    
    # build dependency relationships within each project
    for start, end in project_dependency_list:
        start = graph.map[start]
        end = graph.map[end]
        start.add_neighbor(end)
    return graph

class Graph:
    def __init__(self):
        self.projects = []
        self.map = {}

    def get_or_create_project(self, project_name):
        if project_name not in self.map:
            new_project = Project(project_name)
            self.map[project_name] = new_project
            self.projects.append(project_name)
        return self.map[project_name]
    
    def add_edge(self, start_project_name, end_project_name):
        start = self.get_or_create_project(start_project_name)
        end = self.get_or_create_project(end_project_name)
        start.add_neighbor(end)

    def get_projects(self):
        projects = []
        for project in self.projects:
            projects.append(self.map[project])
        return projects

class Project:
    class State(Enum):
        PARIAL = "partial"
        COMPLETE = "COMPLETE"
        BLANK = "BLANK"
    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = {}
        self.state = Project.State.BLANK
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def add_neighbor(self, project):
        if project.name not in self.map:
            self.map[project.name] = project
            self.children.append(project)


if __name__ =="__main__":

    project_name_list = ["a", "b", "c", "d", "e", "f"]
    dependency_list = [("a","d"),("f","b"), ("b","d"), ("f","a"), ("d","c")]
    output = ["e", "f", "a", "b", "d", "c"]
    
    order = find_projects_build_order(project_name_list, dependency_list)
    order_name = [project.name for project in order]
    print(order_name)
