from algoliasearch.search_client import SearchClient
import json
import configparser
import os

# 获取当前脚本的父目录
script_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

config = configparser.ConfigParser()
# 读取配置文件
config_file = os.path.join(script_dir, 'config.ini')
config.read(config_file)

application_id = config.get('algolia', 'ApplicationID')
admin_api_key = config.get('algolia', 'AdminAPIKey')
index_name = config.get('algolia', 'IndexName')

client = SearchClient.create(application_id, admin_api_key)
index = client.init_index(index_name)

# 读取数据文件
data_file = os.path.join(script_dir, 'public', 'algolia.json')
with open(data_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

response = index.save_objects(data, {'autoGenerateObjectIDIfNotExist': True})

response.wait()

print(f"上传成功！已上传 {len(data)} 个对象到 {index_name}。")
