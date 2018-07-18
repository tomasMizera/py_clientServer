
class Client:

    def __init__(self, online, origins, ip_client):
        self.online_state = online
        self.country = origins
        self.ip = ip_client

    def identify_client(self):
        print(f"I am a client from {self.country} and have ip: {self.ip} with {self.online_state} online state")

    def bind_socker(self):
        pass


a = Client(True, "Slovakia", 19216801)
a.identify_client()

if __name__ == '__main__':
    print(f'here first')
    pass

