class JabberThread(Thread):
    """Class for Jabber connection thread"""

    def __init__(self, client):
        """Constructor for JabberThread Class

        @type client: Client
        @param client: instace of xmpp.Client class
        """
        Thread.__init__(self)
        self.client = client
        self.connected = True

    def process(self):
        """Starts the xmpp client process"""
        try:
            self.client.Process(1)
        except:
            return False
        return True

    def run(self):
        """When xmpp client is connected runs the client process """
        time.sleep(5)
        while self.client.Process(1) and self.connected:
            pass
        self.client.disconnect()
        self.connected = False
