from unittest.mock import Mock

json = Mock()
json.loads('{"k","v"}')
print(f'mock json object: {json}')

json.loads('{"k2","v2"}')

count_calls = json.loads.call_count
print(f'count calls: {count_calls}')

print(f'Last call arg info: {json.loads.call_args}')
print(f'List of calls: {json.loads.call_args_list}')
print(f'Last of calls to json method: {json.method_calls}')