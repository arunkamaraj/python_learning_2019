import my_abstract_pack.abstract_pack as ap
possible_input_word = ['TOON','POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
start = 'TOON'
target = 'PLEA'

def word_ladder_problem():
    bucket_dict = {}
    g = ap.Graphs()

    for word in possible_input_word:
        for i in range(len(word)):
            key = word[:i] + '_' + word[i+1:]
            if key in bucket_dict.keys():
                bucket_dict[key].append(word)
            else:
                bucket_dict[key]= [word]

    # print(bucket_dict, len(bucket_dict.keys()))

    # create graph
    for key in bucket_dict.keys():
        for word1 in bucket_dict[key]:
            for word2 in bucket_dict[key]:
                if word1 != word2:
                    g.add_edges(word1, word2)

    # print(g)
    bfs_traversal(g, start)
    traverse_to(g,  'PLEA')


def bfs_traversal(g, start_node):
    que = ap.Queue()
    output = []
    node = g.get_vertex(start_node)
    que.enqueue(node)
    # node.length += 1
    node.color ='grey'

    while not que.is_empty():
        data = que.dequeue()
        data.color = 'black'
        output.append(data.id)
        for i in data.get_connections():
            if i.color == 'white':
                que.enqueue(i)
                i.predecessor = data
                i.length = data.length + 1
                i.color = "grey"

    # print(output)
    # print('length', data.length)

def traverse_to(g, item):
    node = g.get_vertex(item)

    while node.predecessor:
        print (node.id)
        node = node.predecessor
    print(node.id)

if __name__ == "__main__":
    word_ladder_problem()
    # traverse_to('PLEA')




