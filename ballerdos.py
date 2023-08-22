import time
import scapy.all as scapy

def packets(ip, packetss, persec):
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
    ip = input("Enter target IP: ")
    packetss = int(input("Enter number of packets: "))
    persec = 0.1 

    try:
        packets(ip, packets, persec)
    except KeyboardInterrupt:
        print("Tool interrupted.")

if __name__ == "__main__":
    main()                                                                           
