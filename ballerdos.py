import time
import scapy.all as scapy

def packet_sender(target_ip, packet_count, interval):
    for _ in range(packet_count):
        packet = scapy.IP(dst=target_ip)/scapy.ICMP()
        scapy.send(packet, verbose=False)
        print("Sent packet to", target_ip)
        time.sleep(interval)

def main():
    print("""
    
$$$$$$$\            $$\ $$\                           $$\                     
$$  __$$\           $$ |$$ |                          $$ |                    
$$ |  $$ | $$$$$$\  $$ |$$ | $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$$\ 
$$$$$$$\ | \____$$\ $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  _____|
$$  __$$\  $$$$$$$ |$$ |$$ |$$$$$$$$ |$$ |  \__|$$ /  $$ |$$ /  $$ |\$$$$$$\  
$$ |  $$ |$$  __$$ |$$ |$$ |$$   ____|$$ |      $$ |  $$ |$$ |  $$ | \____$$\ 
$$$$$$$  |\$$$$$$$ |$$ |$$ |\$$$$$$$\ $$ |      \$$$$$$$ |\$$$$$$  |$$$$$$$  |
\_______/  \_______|\__|\__| \_______|\__|       \_______| \______/ \_______/ 
                                  
    """)
    target_ip = input("Enter target IP: ")
    packet_count = int(input("Enter number of packets: "))
    interval = 0.1 

    try:
        send_packets(target_ip, packet_count, interval)
    except KeyboardInterrupt:
        print("Tool interrupted.")

if __name__ == "__main__":
    main()                                                                           
