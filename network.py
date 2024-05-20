from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info

class NetworkSlicingTopo(Topo):
    def __init__(self):

        info( '*** Create an empty network and add nodes to it. ***\n' )
        Topo.__init__(self)

        # 
        info( '*** Create template host, switch, and link ***\n' )
        host_config = dict(inNamespace=True)
        #http_link_config = dict(bw=1)
        #video_link_config = dict(bw=10)
        #host_link_config = dict()

        info( '*** Adding controller ***\n' )

        info("*** Adding Hosts _ Pink Slice ***\n")
        self.addHost('H1', **host_config)
        self.addHost('H2', **host_config)
        self.addHost('H5', **host_config)
        self.addHost('H6', **host_config)

        info("*** Adding Switches _ Pink Slice ***\n")
        self.addSwitch('S1', **{"dpid": "%016x" % (1)})
        self.addSwitch('S3', **{"dpid": "%016x" % (3)})
        self.addSwitch('S6', **{"dpid": "%016x" % (6)})
        self.addSwitch('S4', **{"dpid": "%016x" % (4)})

        info("*** Creating Links With Specified Ports _ Pink Slice ***\n")
        self.addLink("H1" , "S1")
        self.addLink("H2" , "S1")
        self.addLink("S1" , "S3")
        self.addLink("S1" , "S4")
        self.addLink("S3" , "S6")
        self.addLink("S4" , "S6")
        self.addLink("S6" , "H5")
        self.addLink("S6" , 'H6')

        info("*** Adding Hosts _ Blue Slice ***\n")
        self.addHost('H3', **host_config)
        self.addHost('H4', **host_config)
        self.addHost('H7', **host_config)
        self.addHost('H8', **host_config)

        info("*** Adding Switches _ Blue Slice ***\n")
        self.addSwitch('S2', **{"dpid": "%016x" % (2)})
        self.addSwitch('S5', **{"dpid": "%016x" % (5)})
        self.addSwitch('S7', **{"dpid": "%016x" % (7)})

        info("*** Creating Links With Specified Ports _ Blue Slice ***\n")

        self.addLink("H3" , "S2")
        self.addLink("H4" , "S2")
        self.addLink("S2" , "S4")
        self.addLink("S2" , 'S5')
        self.addLink('S4' , 'S7')
        self.addLink('S5' , 'S7')
        self.addLink('S7' , 'H7')
        self.addLink('S7' , 'H8')


topos = {"networkslicingtopo": (lambda: NetworkSlicingTopo())}

if __name__ == "__main__":
    topo = NetworkSlicingTopo()
    net = Mininet(
        topo=topo,
        switch=OVSKernelSwitch,
        build=False,
        autoSetMacs=True,
        autoStaticArp=True,
        link=TCLink,
    )
    controller = RemoteController("c1", ip="127.0.0.1", port=6633)
    net.addController(controller)
    net.build()
    net.start()
    CLI(net)
    net.stop()