# network-utilization-monitor
# SDN Network Utilization Monitor

## Tools Used
- Mininet
- Ryu Controller
- Python

## Run Steps

### Start Controller
ryu-manager monitor.py

### Start Topology
sudo mn --custom topology.py --topo mytopo --controller remote

### Test
pingall
iperf
