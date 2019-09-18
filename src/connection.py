class Connection:
    broker_address = ""
    port = 0
    user = ""
    password = ""

    def __init__(self, broker_address,port,user,password):
        self.broker_address = broker_address
        self.port = port
        self.user = user
        self.password = password
