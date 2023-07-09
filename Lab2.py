class Job:
    def __init__(self,Id,dl,p):
        self.taskid=Id
        self.deadline=dl
        self.profit=p
def schedulejobs(jobs,T):
    profit=0
    slot=[-1]*T
    jobs.sort(key=lambda x: x.profit, reverse=True)
    for jobs in jobs:
        for j in reversed(range(min(T,jobs.deadline))):
            if slot[j]==-1:
                slot[j]=jobs.taskid
                profit +=jobs.profit
                break
    print("The scheduled jobs are",list(filter(lambda x:x!=-1,slot)))
    print("the total profit earned is",profit)
if __name__=='__main__':
    n=int(input("enter the no of jobs:"))
    jobs=[]
    for i in range(n):
        taskid=input("Enter task ID for job{}:".format(i+1))
        deadline=int(input("Enter deadline for job{}:".format(i+1)))
        profit=int(input("Enter profit for job{}:".format(i+1)))
        jobs.append(Job(taskid,deadline,profit))
    T=int(input("Enter the total time:"))
    schedulejobs(jobs,T)
