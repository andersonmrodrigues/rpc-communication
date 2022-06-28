from xmlrpc.server import SimpleXMLRPCServer
import numpy as np
from sklearn.preprocessing import StandardScaler

def scaler(data):
    scaler = StandardScaler()
    array = np.loadtxt(data, dtype='d', delimiter='\t', unpack=False)
    return scaler.fit_transform(array).tolist()

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("Servidor UP na porta 8000")
server.register_function(scaler, "scaler")
server.serve_forever()