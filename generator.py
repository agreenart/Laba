import random

def get_element(element, schema_data, str_data):
    if element[0] == 'schema_data':
        return random.choice(schema_data[element[1]])
    else :
        return random.choice(element[1])


def generate(file_name, count, schema, schema_data):
    file = open(file_name, 'w')
    for i in range(count):
        str_data = []
        for element in schema[0]:
            str_data.append(get_element(element, schema_data, str_data))
        file.write(schema[1].format(*tuple(str_data)))
    file.close()