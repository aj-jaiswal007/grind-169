from queue import Queue


q = Queue()
for i in range(10):
    q.put((i, i))

new = q.get()
q.put(new)



for i in range(10):
    print(q.get())