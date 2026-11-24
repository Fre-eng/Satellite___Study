# PART 1: Create Housekeeping class

class Housekeeping:

    def __init__(self, battery_voltage, temperature, mode):
        self.battery_voltage = battery_voltage
        self.temperature = temperature
        self.mode = mode

    def display(self):
        print("####### Housekeeping Data #######")
        print("Battery Voltage: ", self.battery_voltage)
        print("Temperature: ", self.temperature)
        print("Mode: ", self.mode)


# PART 2: Create an object

satellite = Housekeeping(3.7, 25, "Normal")

satellite.display()


# PART 3: Create a binary packet

packet = bytes([0x01, 0x19, 0x07, 0x4A])


# PART 4: Save the packet

with open("packet.bin", "wb") as file:
    file.write(packet)


# PART 5: Read the saved packet

with open("packet.bin", "rb") as file:
    received_packet = file.read()


# PART 6: Display received data

print("\n+++++++ RECEIVED HOUSEKEEPING DATA +++++++")

for byte in received_packet:
    print(byte)
    print("Packet length:", len(received_packet), "bytes")