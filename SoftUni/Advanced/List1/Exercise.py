from _collections import deque
 
stack = deque()
 
number_of_queries = int(input())

for i in range(number_of_queries):
    query = input().split(' ')
    query_type = query[0]
    if query_type == "1":
        query_element = query[1]
        stack.appendleft(int(query_element))

    