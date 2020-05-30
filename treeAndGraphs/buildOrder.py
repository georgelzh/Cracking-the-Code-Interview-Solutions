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



The implementation follows this approach very closely.
Initialization and setup:
1. Build a graph where each project is a node and its outgoing edges represent the projects that depend
on it. That is, if A has an edge to B (A-> B), it means B has a dependency on A and therefore A must be
built before B. Each node also tracks the number of incoming edges.
2. Initialize a buildOrder array. Once we determine a project's build order, we add it to the array. We also
continue to iterate through the array, using a toBeProcessed pointer to point to the next node to be
fully processed.
CrackingTheCodinglnterview.com I 6th Edition 251
Solutions to Chapter 4 I Trees and Graphs
3. Find all the nodes with zero incoming edges and add those to a buildOrder array. Set a
toBeProcessed pointer to the beginning of the array.
Repeat until toBeProcessed is at the end of the buildOrder:
1. Read node at toBeProcessed.
» If node is null, then all remaining nodes have a dependency and we have detected a cycle.
2. For each child of node:
» Decrement child. dependencies (the number of incoming edges).
» If child. dependencies is zero, add child to end of buildOrder.
3. Increment toBeProcessed.

O(P+D) number of projects + number of dependencies
"""

def find_projects_build_order(project_name_list, dependency_list):
    graph = build_graph(project_name_list, dependency_list)
    order = order_projects(graph.projects)
    return order


def order_projects(projects):
    order = [None for i in range(len(projects))]
    to_be_processed = 0
    end_of_order_list = 0

    # first time add non dependent project to order
    end_of_order_list = add_non_dependent(order, projects, end_of_order_list)
    # start while loop to find the order
    while to_be_processed < len(projects):
        curr = order[to_be_processed]
        # return null when it's a cycle dependency
        if curr == None:
            return None
        
        # remove curr's dependency from all of its children
        else:
            children = curr.children
            for child in children:
                child.dependencies -= 1
        
        # add all projects that's non dependent now, increment end_of_order
        end_of_order_list = add_non_dependent(order, projects, end_of_order_list)
        to_be_processed += 1
    # return order if there's a valid order
    return order

def build_graph(project_name_list, project_dependency_list):
    graph = Graph()
    for project in project_name_list:
        graph.get_or_create_project(project)
    for dependency in project_dependency_list:
        # print(dependency)
        start = graph.get_or_create_project(dependency[0])
        # print(start.name)
        end = graph.get_or_create_project(dependency[1])
        # print(end.name)
        start.add_neighbor(end)
    return graph


# helper function that inserts project with 0 dependencies into order array.
# starting at offset index
def add_non_dependent(order, projects, offset):
    # return offset if offset hits the end of projects
    if offset >= len(projects):
        return offset
    for project in projects:
        # print(project.name)
        if project not in order and project.dependencies == 0:
            order[offset] = project
            offset += 1
    return offset


class Graph:
    def __init__(self):
        self.projects = []  # stores all Project Objects
        self.map = {}   # map all project_name to project
    
    def get_or_create_project(self, project_name):
        if project_name not in self.map:
            new_project = Project(project_name)
            self.map[project_name] = new_project
            self.projects.append(new_project)
        return self.map[project_name]
        
    def add_edge(self, start_project_name, end_project_name):
        start = self.get_or_create_project(start_project_name)
        end = self.get_or_create_project(end_project_name)
        start.add_neighbor(end)


class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = {}
        self.dependencies = 0
    
    # add the project that self is pointing to 
    # increment project.dependency (!not self.dependency!) by 1. 
    # since input is like (a,b), b depends on a. we can use this function like a.add_neighbor(b)
    def add_neighbor(self, project):
        if project.name not in self.map:
            self.children.append(project)
            # print(self.name, project.name)
            self.map[project.name] = project
            project.dependencies += 1

if __name__ =="__main__":

    projects = ["a", "b", "c", "d", "e", "f"]
    dependency_list = [("a","d"),("f","b"), ("b","d"), ("f","a"), ("d","c")]
    output = ["e", "f", "a", "b", "d", "c"]
    
    order = find_projects_build_order(projects, dependency_list)
    order_name = [project.name for project in order]
    # print(order_name)
    assert order_name == output, "failed"

    # a = Project("a")
    # s = Project("s")
    # a.add_neighbor(s)
    # g = build_graph(projects, dependency_list)
    # print([p.name for p in g.projects])
    
    # print(g.map)    # list of "a": project object
    # print(g.map["b"].dependencies)  #int
    # print(g.map["b"].children)  # project object
    # print(g.map["b"].children[0])  # project object

    # order_projects(g.projects)
