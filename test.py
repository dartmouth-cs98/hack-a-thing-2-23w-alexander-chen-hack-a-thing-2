import requests

with open('/Users/alex/sources/hack-a-thing-2-23w-alexander-chen-hack-a-thing-2/server/files/example.mp4', 'rb') as f:
    files = [
        ('file', ('example.mp4', f, 'application/octet-stream')),
    ]

    print(requests.post("http://127.0.0.1:5000", files=files).json())
    print(requests.Request('POST', 'http://127.0.0.1:5000',
          files=files).prepare().body.decode('ascii'))
