import json

from redis import Redis

from flask import Flask, request, Response

from resource import setrlimit, getrlimit, RLIMIT_CPU, RLIM_INFINITY, prlimit


app = Flask(__name__)

redis = Redis(host='redis', port=6379, decode_responses=True)


@app.route('/', methods=['GET', 'POST', 'PUT']) #генерация сигнала при запросе
def index():
    data = json.loads(request.data.decode())
    print(data, type(data))
    return json.dumps({'response': 'alarm'})


@app.route('/set_value/', methods=['GET', 'POST', 'PUT']) #задает значение в redis или меняет уже существующее
def set_value():
    data: dict = json.loads(request.data.decode())
    key, value = list(data.items())[0]
    redis.set(key, value)
    return Response(status=200)


@app.route('/get_value/', methods=['GET', 'POST', 'PUT']) #получаем значение из redis
def get_value():
    data: dict = json.loads(request.data.decode())
    key: str = data.get('key')
    if key:
        value = redis.get(key)
        return json.dumps({'key': key, 'value': value})
    return Response(status=404)