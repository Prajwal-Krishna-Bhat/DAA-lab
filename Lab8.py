#Design an application to schedule an exam. Given a list of different subjets and students who are enrolled in many subjects, many subjects would have common students of the same batch, some backlogged students, etc.
#Find the solution to the following:
#a.Obtain the schedule for the exam so that no 2 exams with a common student are scheduled at the same time.
#b.How many minimum time slots are required to schedule all exams?
from collections import defaultdict
class Graph:
    def __init__(self,subjects):
        self.subjects=subjects
        self.graph=defaultdict(list)
    def add_edge(self, subject1, subject2):
        self.graph[subject2].append(subject2)
        self.graph[subject1].append(subject1)
    def graph_coloring(self):
        color_map={}
        available_colors=set(range(1,len(self.subjects)+1))
        for subject in self.subjects:
            used_colors=set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])
            available_color=available_colors-used_colors
            if available_color:
                color_map[subject]=min(available_color)
            else:
                color_map[subject]=len(available_colors)+1
                available_colors.add(color_map[subject])
        return color_map
    def get_minimum_time_slots(self):
        color_map=self.graph_coloring()
        return max(color_map.values())
subjects=['Math','Physics','Chemistry','Biology']
students={
    'Math':['Alice','Bob','Charlie'],
    'Physics':['Alice','Charlie','David'],
    'Chemistry':['Bob','Charlie','Eve'],
    'Biology':['Alice','David','Eve']
}
graph=Graph(subjects)
graph.add_edge('Math','Physics')
graph.add_edge('Math','chemistry')
graph.add_edge('Chemistry','Physics')
graph.add_edge('Biology','Physics')
minimum_time_slots=graph.get_minimum_time_slots()
print(f"Minimum time slots needed:{minimum_time_slots}")