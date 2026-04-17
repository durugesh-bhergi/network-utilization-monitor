# Network Utilization Monitor

## Overview

An SDN-based Network Utilization Monitor built using **Mininet** and **Ryu Controller**. The system collects byte counters from OpenFlow switches, estimates bandwidth usage on each port, and displays real-time utilization in the terminal — updated every 5 seconds.

---

## Project Structure

```
network-utilization-monitor/
├── topology.py             # Mininet network topology
├── monitor_controller.py   # Ryu SDN controller with stats collection
├── bandwidth_display.py    # Terminal-based bandwidth visualizer
└── README.md
```

---

## Requirements

- Python 3.x
- Mininet (`sudo apt install mininet`)
- Ryu SDN Framework (`pip install ryu`)
- Open vSwitch (`sudo apt install openvswitch-switch`)

---

## Setup

```bash
git clone https://github.com/<your-username>/network-utilization-monitor.git
cd network-utilization-monitor
pip install ryu
```

---

## Execution

### Step 1 — Start the Ryu Controller
```bash
ryu-manager monitor_controller.py
```

### Step 2 — Launch the Mininet Topology (new terminal)
```bash
sudo python3 topology.py
```

### Step 3 — Run the Bandwidth Display (new terminal)
```bash
python3 bandwidth_display.py
```

---

## Topology

```
h1 ─┐              ┌─ h3
     ├── s1 ── s2 ──┤
h2 ─┘              └── s3 ── h4
```

- 4 hosts (h1–h4), 3 switches (s1–s3)
- Host-to-switch links: 10 Mbps
- Switch-to-switch links: 100 Mbps
- Remote controller on 127.0.0.1:6653

---

## How It Works

1. `topology.py` creates the virtual network using Mininet with a remote Ryu controller.
2. `monitor_controller.py` installs default flow rules, handles packet forwarding, and polls port statistics every 5 seconds via OpenFlow `OFPPortStatsRequest`.
3. Byte counter deltas are used to compute RX/TX bandwidth in Kbps and saved to `/tmp/stats_dpid_<id>.json`.
4. `bandwidth_display.py` reads these JSON files and renders a live ASCII bar-chart of utilization.

---

## Testing Traffic

Inside the Mininet CLI:
```bash
mininet> h1 iperf -s &
mininet> h2 iperf -c 10.0.0.1 -t 30
mininet> pingall
```

---

## License

MIT License
