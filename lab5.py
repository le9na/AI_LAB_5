from collections import deque


class BFS:
    def __init__(self, size=12):
        self.N = size  # number of vertices in the graph
        self.G = [[False] * self.N for _ in range(self.N)]  # adjacency matrix
        self.Acc = [False] * self.N  # visited nodes
        self.Q = deque()  # queue for BFS
        self.setup_graph(size)
        print("+--------------------------------------+")
        print()

    def setup_graph(self, size):
        self.G = [[False] * self.N for _ in range(self.N)]
        edges = [
            (0, 1),
            (0, 8),
            (0, 4),
            (1, 2),
            (1, 3),
            (2, 6),
            (3, 4),
            (3, 5),
            (6, 7),
            (8, 9),
            (9, 10),
            (10, 11)
        ]
        for u, v in edges:
            self.G[u][v] = self.G[v][u] = True

    def bfs(self, start, goal):
        self.Q.append(start)
        self.Acc[start] = True
        print("The queue:\n")
        print(f"[ {self.ret_city(self.Q[0])} ]")

        while self.Q:
            at = self.Q.popleft()  # get the head of the queue
            if goal == at:
                print("+--------------------------------------+")
                print(f"\nThe goal {self.ret_city(goal)} is reached\n\n")
                print("+--------------------------------------+")
                return

            print("+--------------------------------------+")
            print(f"\nNow in {self.ret_city(at)}")
            print("+--------------------------------------+")
            add_to_queue = f"{self.ret_city(at)} is not the goal, cities [ "

            for i in range(self.N):
                if self.G[at][i] and not self.Acc[i]:
                    self.Q.append(i)
                    add_to_queue += f"{self.ret_city(i)} "
                    self.Acc[i] = True

            add_to_queue += "] are added to the queue"
            print(add_to_queue)

            print("Queue: ", end="")
            for i in self.Q:
                print(f" {self.ret_city(i)} ", end="")
            print()

    @staticmethod
    def ret_city(i):
        cities = [
            "Buraydah", "Unayzah", "AlZulfi", "Al-Badai",
            "Riyadh-Alkhabra", "AlRass", "UmSedrah", "Shakra",
            "Al-Bukayriyah", "Sheehyah", "Dhalfa", "Mulida"]
        return cities[i]


if __name__ == "__main__":
    print("\nChoose a city number to start: \n")
    for i in range(12):
        print(f"{BFS.ret_city(i)} city[{i}]")
    print("\nInput: ", end="")
    choosen_city = int(input())

    print("\nChoose a city number for the goal: ")
    print("\nInput: ", end="")
    goal = int(input())

    choice = BFS()  # Size
    choice.bfs(choosen_city, goal)
