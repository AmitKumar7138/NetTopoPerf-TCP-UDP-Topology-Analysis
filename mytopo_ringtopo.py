from mininet.topo import Topo
from mininet.node import OVSBridge
class RingTopo(Topo):
    "Linear topology example for 8 hosts."

    def __init__(self):
        "Create custom topo."
        # Initialize topology
        super().__init__()

        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        h5 = self.addHost('h5', ip='10.0.0.5/24')
        h6 = self.addHost('h6', ip='10.0.0.6/24')
        h7 = self.addHost('h7', ip='10.0.0.7/24')
        h8 = self.addHost('h8', ip='10.0.0.8/24')

        # Switch
        s1 = self.addSwitch('s1',cls=OVSBridge, stp=True)
        s2 = self.addSwitch('s2',cls=OVSBridge, stp=True)
        s3 = self.addSwitch('s3',cls=OVSBridge, stp=True)
        s4 = self.addSwitch('s4',cls=OVSBridge, stp=True)
        s5 = self.addSwitch('s5',cls=OVSBridge, stp=True)
        s6 = self.addSwitch('s6',cls=OVSBridge, stp=True)
        s7 = self.addSwitch('s7',cls=OVSBridge, stp=True)
        s8 = self.addSwitch('s8',cls=OVSBridge, stp=True)

        # Add links
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(h2, s2)
        self.addLink(s2, s3)
        self.addLink(h3, s3)
        self.addLink(s3, s4)
        self.addLink(h4, s4)
        self.addLink(s4, s5)
        self.addLink(h5, s5)
        self.addLink(s5, s6)
        self.addLink(h6, s6)
        self.addLink(s6, s7)
        self.addLink(h7, s7)
        self.addLink(s7, s8)
        self.addLink(h8, s8)
        self.addLink(s8, s1)

topos = {'ringtopo': (lambda: RingTopo())}
