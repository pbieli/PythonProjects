import concurrent.futures
import argparse
import socket

def portscan_worker(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f'Port {port} is open.')
            else:
                print(f'Port {port} is closed.')
    except socket.timeout:
        print(f'Port {port} timed out.')
    except Exception as e:
        print(f'An error occurred while scanning port {port}: {e}')

def portscan(target, start_port, end_port, num_threads):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for port in range(start_port, end_port + 1):
            futures.append(executor.submit(portscan_worker, target, port))
        for future in concurrent.futures.as_completed(futures):
            future.result()

def main():
    parser = argparse.ArgumentParser(description='Multi-threaded port scanner.')
    parser.add_argument('target', help='Target IP address')
    parser.add_argument('start_port', type=int, help='Start port')
    parser.add_argument('end_port', type=int, help='End port')
    parser.add_argument('--threads', type=int, default=10, help='Number of threads (default: 10)')
    args = parser.parse_args()

    if args.start_port < 1 or args.end_port > 65535 or args.start_port > args.end_port:
        print('Invalid port range.')
        return

    portscan(args.target, args.start_port, args.end_port, args.threads)

if __name__ == '__main__':
    main()

