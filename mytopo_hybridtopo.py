from mininet.topo import Topo
from mininet.node import OVSBridge
class HybridMSTopo(Topo):
    "Mesh Topology topology example."

    def __init__(self):
        "Create custom mesh topo."
        # Initialize topology
        super().__init__()

        # Add hosts and switches
        h1 = self.addHost('h1', ip = "10.0.0.1/24")
        h2 = self.addHost('h2', ip = "10.0.0.2/24")
        h3 = self.addHost('h3', ip = "10.0.0.3/24")
        h4 = self.addHost('h4', ip = "10.0.0.4/24")
        h51 = self.addHost('h51', ip = "10.0.0.5/24")
        h61 = self.addHost('h61', ip = "10.0.0.6/24")
        h72 = self.addHost('h72', ip = "10.0.0.7/24")
        h82 = self.addHost('h82', ip = "10.0.0.8/24")
        h92 = self.addHost('h92', ip = "10.0.0.9/24")
        s1 = self.addSwitch('s1', cls = OVSBridge, stp = True)
        s2 = self.addSwitch('s2', cls = OVSBridge, stp = True)
        s3 = self.addSwitch('s3', cls = OVSBridge, stp = True)
        s4 = self.addSwitch('s4', cls = OVSBridge, stp = True)
        s11 = self.addSwitch('s11', cls = OVSBridge, stp = True)
        s12 = self.addSwitch('s12', cls = OVSBridge, stp = True)
        # Add links mesh
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s1,s4)
        self.addLink(s2,s3)
        self.addLink(s2,s4)
        self.addLink(s3,s4)

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s3)
        self.addLink(h4, s3)
        
        self.addLink(h51,s11)
        self.addLink(h61,s11)
        self.addLink(s11,s2)
        
        self.addLink(h72,s12)
        self.addLink(h82,s12)
        self.addLink(h92,s12)
        self.addLink(s12, s4)
        

topos = {'hybridmstopo': (lambda: HybridMSTopo())}
