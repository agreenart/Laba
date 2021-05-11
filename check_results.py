from data import HashTable,Hashes
from generator import generate
from sort import Merge_sort
import random
from timesub import check_time
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


def load_and_find_results(db_file_name, count, schema, schema_data):
    key = 'fio'
    generate(db_file_name, count, schema, schema_data)
    fp_list = load_fp_from_file(db_file_name)
    query_obj = random.choice(fp_list)
    query = getattr(query_obj,key)
    fp_map = defaultdict(list)
    fp_custom_map_good = HashTable()
    for el in fp_list:
        el.set_hash_type('good')
        fp_map[getattr(el, key)].append(el)
        fp_custom_map_good.add(el)
    print(linear_search(fp_list, key, query))
    print(sort_and_binary_seach(fp_list, key, query))
    print(binary_search(fp_list, key, query))
    print(check_time(fp_map.__getitem__)(query))
    print(check_time(fp_custom_map_good.get)(Hashes.good_hash(query)))
    fp_custom_map_bad = HashTable()
    for el in fp_list:
        el.set_hash_type('bad')
        fp_custom_map_bad.add(el)
    query_obj.set_hash_type('bad')
    print(check_time(fp_custom_map_bad.get)(Hashes.bad_hash(query)))

#load_and_find_results(DATABASE_FILE_NAME, 100, schema_office_worker, data_office_worker)