import os
import re
import pydash as _
from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/api/file', methods=['POST'])
def upload(filename='default'):
    file = request.data
    filename = request.args.get('filename')
    old_task_id = request.args.get('old_task_id')
    # 删除旧的文件

    def remove_file(f):
        if os.path.exists(os.path.join('upload', f)):
            os.remove(os.path.join('upload', f))

    if old_task_id:
        _.chain(os.listdir('upload')).filter_(lambda x: x.startswith(
            old_task_id)).for_each(lambda x: remove_file(x)).value()

    with open(os.path.join('upload', filename), 'wb') as f:
        f.write(file)
    return 'ok'


@app.route('/api/file', methods=['GET'])
def download():
    filename = request.args.get('filename', default=None)
    if not filename:
        return bad_request('filename')

    store_path = './upload/{}'.format(filename)
    if not os.path.exists(store_path):
        return Response(None, 404)

    def send_chunk():  # 流式读取
        with open(store_path, 'rb') as partial_file:
            print('===================>>> send from file server')
            yield partial_file.read(20 * 1024 * 1024)

    return Response(send_chunk(), 206, content_type='application/octet-stream')


if __name__ == '__main__':
    app.run(port=6000)
