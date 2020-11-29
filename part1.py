from main import *
import sys

conn = socket(AF_PACKET, SOCK_RAW, ntohs(3))
file = pcap('saveFile.pcap')
i = 1
print("\n\t* Start Capturing!\n")
while True:
    try:
        raw_data, addr = conn.recvfrom(65535)
        file.write(raw_data)
        tmp = Ethernet(raw_data)
        print("\nCaptured Frame No.", i, ":")
        i += 1
        tmp.show()
    except (KeyboardInterrupt, SystemExit):
        file.close()
        print("\n\n\t\t* End of Capturing!\n\n")
        sys.exit(0)
    # except:
    #     print("\n\n\t\tSomething Happened!\n\n")

