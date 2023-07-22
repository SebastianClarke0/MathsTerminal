
from matplotlib import pyplot as plt
import numpy as np

#def generate_course_graph:
    

#def generate_topic_graph:

    
def generate_subtopic_graph():
    data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.savefig('foo.png')

generate_subtopic_graph()
