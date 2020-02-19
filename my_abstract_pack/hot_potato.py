import my_abstract_pack.abstract_pack as absytact_type


def hot_potato(player_list, num):
    queue = absytact_type.Queue()

    for i in player_list:
        queue.enqueue(i)

    while queue.size() > 1:
        for i in  range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()

if __name__ =='__main__':
    print (hot_potato(['arun','kiruthika', 'tanvi', 'kamaraj', 'punitha'], 6))
