# Define constants to make code more readable
c_CLIENT = 1
c_SERVER = 2


class Client:

    def __init__(self, online, origins, ip_client):
        self.online_state = online
        self.country = origins
        self.ip = ip_client

        self.identify_client()

    def identify_client(self):
        print(f"I am a client from {self.country} and have ip: {self.ip} with {self.online_state} online state")

    def bind_socket(self):
        pass


if __name__ == '__main__':

    # app_side = either client or server
    app_side = int(input('Choose your side:\n\t1 - client\n\t2 - server\n'))

    if app_side == c_CLIENT:
        Client(True, "Slovakia", "192.168.0.1")

    elif app_side == c_SERVER:
        # not implemented yet
        pass
    else:
        pass
    pass
