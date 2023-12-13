from mininet.topo import Topo


class CustomStarTopo(Topo):
    "Star topology with 4 switches and 12 hosts."

    def __init__(self):
        "Create custom topo."
        # Initialize topology
        super().__init__()

        # Add switches
        centralSwitch = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')

        # Add hosts and connect them to their respective switches
        # Switch 2 hosts
        for h in range(1, 4):
            host = self.addHost('h%s' % h, ip='10.0.0.%s/24' % h)
            self.addLink(host, switch2)

        # Switch 3 hosts
        for h in range(4, 7):
            host = self.addHost('h%s' % h, ip='10.0.0.%s/24' % h)
            self.addLink(host, switch3)

        # Switch 4 hosts
        for h in range(7, 10):
            host = self.addHost('h%s' % h, ip='10.0.0.%s/24' % h)
            self.addLink(host, switch4)

        # Additional hosts connected to central switch
        for h in range(10, 13):
            host = self.addHost('h%s' % h, ip='10.0.0.%s/24' % h)
            self.addLink(host, centralSwitch)

        # Connect switches to the central switch
        self.addLink(switch2, centralSwitch)
        self.addLink(switch3, centralSwitch)
        self.addLink(switch4, centralSwitch)


topos = {'customstartopo': (lambda: CustomStarTopo())}
