from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def create_network():
    net = Mininet(link=TCLink, switch=OVSKernelSwitch)

    #info("*** Adding controller ***\n")
    #net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    info("*** Adding Hosts _ Pink Slice ***\n")
    H1 = net.addHost('H1', ip='10.0.0.1/24')
    H2 = net.addHost('H2', ip='10.0.0.2/24')
    H5 = net.addHost('H5', ip='10.0.0.5/24')
    H6 = net.addHost('H6', ip='10.0.0.6/24')

    info("*** Adding Switches _ Pink Slice ***\n")
    S1 = net.addSwitch('S1')
    S3 = net.addSwitch('S3')
    S6 = net.addSwitch('S6')
    S4 = net.addSwitch('S4')

    info("*** Creating Links With Specified Ports _ Pink Slice ***\n")
    net.addLink(H1 , S1)
    net.addLink(H2 , S1)
    net.addLink(S1 , S3)
    net.addLink(S1 , S4)
    net.addLink(S3 , S6)
    net.addLink(S4 , S6)
    net.addLink(S6 , H5)
    net.addLink(S6 , H6)

    info("*** Adding Hosts _ Blue Slice ***\n")
    H3 = net.addHost('H3', ip='10.0.0.3/24')
    H4 = net.addHost('H4', ip='10.0.0.4/24')
    H7 = net.addHost('H7', ip='10.0.0.7/24')
    H8 = net.addHost('H8', ip='10.0.0.8/24')

    info("*** Adding Switches _ Blue Slice ***\n")
    S2 = net.addSwitch('S2')
    S5 = net.addSwitch('S5')
    S7 = net.addSwitch('S7')

    info("*** Creating Links With Specified Ports _ Blue Slice ***\n")

    net.addLink(H3 , S2)
    net.addLink(H4 , S2)
    net.addLink(S2 , S4)
    net.addLink(S2 , S5)
    net.addLink(S4 , S7)
    net.addLink(S5 , S7)
    net.addLink(S7 , H7)
    net.addLink(S7 , H8)
  
    info("*** Starting Network ***\n")
    net.start()

    info("*** Adding flow rules to Swith 4 to block traffic between pink slice and blue slice ***\n")

    info("*** Running CLI ***\n")
    CLI(net)

    info("*** Stopping Network ***\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()

