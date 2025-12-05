import xmlrpc.client
import base64

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:9000")

remote_path = "test.txt"     # file to download from server
save_as = "received.txt"     # where to save locally

data = proxy.get_file(remote_path)
if data:
    with open(save_as, "wb") as f:
        f.write(base64.b64decode(data))
    print("File downloaded!")
else:
    print("File not found on server.")

