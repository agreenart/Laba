from data import data_office_worker, schema_office_worker,HashTable,Hashes
from generator import generate
from sort import heap_sort, bubble_sort, Merge_sort
import random
from matplotlib import pylab as plt
from timesub import check_time
from multimap import MultiMap
from progress.bar import IncrementalBar
from collections import defaultdict
from load_from_file import load_fp_from_file

def linear_search(items, key, query):
    result = []
    for pos, element in enumerate(items):
        if getattr(element, key) == query:
            result.append(pos)
    return result

def binary_search(items, key, query):
    result = []
    left = 0
    right = len(items) - 1
    middle = int(right // 2)
    while getattr(items[middle], key) != query and left <= right:
        if query > getattr(items[middle], key):
            left = middle + 1
        else:
            right = middle - 1
        middle = int((left + right) // 2)

    if left <= right:
        result.append(middle)
        bound = middle + 1
        while bound < len(items) and getattr(items[bound], key) == query:
            result.append(bound)
            bound += 1
        bound = middle - 1
        while bound >= 0 and getattr(items[bound], key) == query:
            result.append(bound)
            bound -= 1
    return result

def sort_and_binary_seach(arr, key, query):
    Merge_sort(arr)
    return binary_search(arr, key, query)

def mm_search(items,key):
    keys = [getattr(el,key) for el in items]
    multi = MultiMap([(key,value) for key, value in zip(keys, items)])
    result = multi.getall(key)
    return result

def laba3(db_file_name, count_range, schema, schema_data):
    results = {'linear': [],
               'binary': [],
               'binary+sort': [],
               'multimap': [],
               'hashtable_map_good': [],
               'hashtable_map_bad': [],
               'bad_collisions': [],
               'good_collisions': []
               }
    key = 'fio'
    max_count_iterations = 2
    iterations = len(count_range)
    bar = IncrementalBar('Countdown', max=iterations)
    bar.start()

    for count in count_range:
        bar.next()
        print ('\n')

        for count_iterations in range(max_count_iterations):
            generate(db_file_name, count, schema, schema_data)
            fp_map = defaultdict(list)
            fp_list = load_fp_from_file(db_file_name)
            query_obj = random.choice(fp_list)
            query = getattr(query_obj, key)


            print('check lin')
            linear = check_time(linear_search)(fp_list, key, query)
            print('check sort+bin')
            sort_and_bin_search = check_time(sort_and_binary_seach)(fp_list,key, query)
            print('check bin')
            bin_search = check_time(binary_search)(fp_list, key, query)
            print('check multimap')
            map_search = check_time(fp_map.__getitem__)(query)

            print('check hashtable good')
            fp_custom_map_good = HashTable()
            for el in fp_list:
                el.set_hash_type('good')
                fp_map[getattr(el, key)].append(el)
                fp_custom_map_good.add(el)
            query_obj.set_hash_type('good')
            custom_map_good_search = check_time(fp_custom_map_good.get)(Hashes.good_hash(query))

            print('check hashtable bad')
            fp_custom_map_bad = HashTable()
            for el in fp_list:
                el.set_hash_type('bad')
                fp_custom_map_bad.add(el)
            query_obj.set_hash_type('bad')
            custom_map_bad_search = check_time(fp_custom_map_bad.get)(Hashes.bad_hash(query))

            results['linear'].append((count, linear))
            results['binary'].append((count, bin_search))
            results['binary+sort'].append((count, sort_and_bin_search))
            results['multimap'].append((count, map_search))
            results['hashtable_map_good'].append((count, custom_map_good_search))
            results['hashtable_map_bad'].append((count, custom_map_bad_search))
            results['bad_collisions'].append((count, fp_custom_map_bad.collision_count))
            results['good_collisions'].append((count, fp_custom_map_good.collision_count))

    plot_graph(results, count_range, max_count_iterations)
    print('bad_collisions: ',results['bad_collisions'])
    print('good_collisions: ',results['good_collisions'])
    bar.finish()
    return results

def plot_graph(results, count_range, max_count_iterations):

    print(results.items())
    x = count_range
    y1 = {'linear': [], 'binary': [], 'binary+sort': [], 'multimap': [], 'hashtable_map_good': [], 'hashtable_map_bad': [] }
    y2 = {'bad_collisions': [], 'good_collisions': [] }
    for type_search, value in results.items():
        acc = 0
        if type_search in y1.keys():
            y = y1
        else:
            y = y2
        for i in range(len(value) + 1):
            if i > 0 and i % max_count_iterations == 0:
                y[type_search].append(acc / max_count_iterations)
                acc = 0
            else:
                acc += value[i][1]

    plt.title('Comparison speeds of search in array')
    plt.yscale('log')
    plt.xlabel('Amount of objects')
    plt.subplot(2, 1, 1)
    plt.yscale('log')
    for count, item in enumerate(y1.items()):
        plt.plot(x,item[1],label=item[0])
        plt.legend(title='Legend')
    plt.subplot(2,1,2)
    for count, item in enumerate(y2.items()):
        plt.plot(x,item[1],label=item[0])
        plt.legend(title='Legend')
    plt.show()
    print(x)
    print(y1, y2)

if __name__ == '__main__':
    COUNT_ELEMENTS = [5000, 10000, 25000, 50000, 100000]
    DATABASE_FILE_NAME = 'workers.txt'
    laba3(DATABASE_FILE_NAME, COUNT_ELEMENTS, schema_office_worker, data_office_worker)

