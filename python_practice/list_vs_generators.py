import random
import time

names = ['sunny', 'bunny', 'chinny', 'vinny']
subjects = ['python', 'java', 'blockchain']

def people_list(num):
    results = []
    for i in range(num):
        person = {
            "id": i,
            "name": random.choice(names),
            "subjects": random.choice(subjects)
        }
        results.append(person)
    return results

def people_generator(num):
    for i in range(num):
        person = {
            "id": i,
            "name": random.choice(names),
            "subjects": random.choice(subjects)
        }
        yield person


t1 = time.time()
res_list = people_list(10000)
t2 = time.time()
print("List method, Time taken:", t2-t1)

t1 = time.time()
res_list = people_list(10000)
t2 = time.time()
print("Generator method, Time taken:", t2-t1)