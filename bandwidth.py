import json
import os
import time
import glob

def load_stats():
    stats_files = glob.glob('/tmp/stats_dpid_*.json')
    all_stats = []
    for filepath in stats_files:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                all_stats.append(data)
        except:
            pass
    return all_stats

def render_bar(value, max_value=1000, width=30):
    filled = int((value / max_value) * width)
    filled = min(filled, width)
    bar = '#' * filled + '-' * (width - filled)
    return f'[{bar}]'

def display_stats(stats_list):
    os.system('clear')
    print('=' * 65)
    print('         NETWORK BANDWIDTH UTILIZATION MONITOR')
    print('=' * 65)
    print(f'  Last Updated: {time.strftime("%Y-%m-%d %H:%M:%S")}')
    print('=' * 65)

    if not stats_list:
        print('\n  [!] No statistics available yet.')
        print('  Make sure the Ryu controller is running and switches are connected.\n')
        return

    for switch_data in sorted(stats_list, key=lambda x: x['dpid']):
        dpid = switch_data['dpid']
        ports = switch_data.get('ports', {})
        print(f'\n  Switch DPID: {dpid}')
        print(f'  {"Port":<6} {"RX (Kbps)":<15} {"Bar":<35} {"TX (Kbps)":<15}')
        print('  ' + '-' * 63)
        for port_no, pdata in sorted(ports.items(), key=lambda x: int(x[0])):
            rx = pdata['rx_bps']
            tx = pdata['tx_bps']
            bar = render_bar(max(rx, tx))
            print(f'  {port_no:<6} {rx:<15.2f} {bar:<35} {tx:<15.2f}')
        print()

    print('=' * 65)
    print('  Legend: # = Utilized   - = Available   Max Scale = 1000 Kbps')
    print('  Press Ctrl+C to exit')
    print('=' * 65)

def main():
    print('Starting Bandwidth Display... (refreshes every 5 seconds)')
    time.sleep(1)
    try:
        while True:
            stats = load_stats()
            display_stats(stats)
            time.sleep(5)
    except KeyboardInterrupt:
        print('\n\nMonitor stopped.')

if __name__ == '__main__':
    main()
