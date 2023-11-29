from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI

net = Mininet(controller=Controller)

s1 = net.addSwitch('s1')

h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')

net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s1)
net.addLink(h4, s1)

net.start()

CLI(net)

net.stop()
