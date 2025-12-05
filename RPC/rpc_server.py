from xmlrpc.server import SimpleXMLRPCServer
import base64

def get_file(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

server = SimpleXMLRPCServer(("0.0.0.0", 9000))
server.register_function(get_file, "get_file")
print("RPC server running on port 9000")
server.serve_forever()

