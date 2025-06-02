# MOTION PLATFORM RAW TEST INTERFACE. KEYBOARD CONTROLLED JOG POSITIVE (FRONT PITCH) & JOG NEGATIVE (BACK PITCH)
# !!!!!USE JOG FAST COMMANDS WITH CAUTION!!!!! HAVE STOP BUTTON 'e' AVAILABLE AT ALL TIMES
# READ POSITION FEEDBACK REGISTER AFTER STOPPING BY PRESSING 'e'
# MAY REQUIRE HOMING IF ENABLING DOES NOT WORK AT BEGINNING. PERFORM HOME -COMMAND AT TRITEX EXPERT
# ~~~ ONLY TO BE USED FOR EDUCATIONAL PURPOSES ~~~

from pymodbus.client import ModbusTcpClient
import time

# Connection parameters .. 192.168.0.211 for M1, 192.168.0.212 for M2
SERVER_IP_LEFT = '192.168.0.211'  
SERVER_IP_RIGHT = '192.168.0.212'
SERVER_PORT = 502  
SLAVE_ID_1 = 1  # Slave ID for M1
SLAVE_ID_2 = 2  # Slave ID for M2

# Register address
ADDRESS = 0
ADDRESS_IEG_MODE = 4316

# Write value in DEC
VALUE = 0
VALUE_FAST = 64
VALUE_FAULT_RESET = 32768
VALUE_ENABLE = 2

# Read register
read_address = 378 # Address to read: Pfeedback
num_registers = 10 # Read 10 values of the register

# Connect to Modbus TCP server
client_left = ModbusTcpClient(SERVER_IP_LEFT, port=SERVER_PORT)
client_left.connect()
client_right = ModbusTcpClient(SERVER_IP_RIGHT, port=SERVER_PORT)
client_right.connect()

def jog_left():
    ADDRESS = 4317
    VALUE = 32
    client_left.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_1)
    client_right.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_2)
    print("2DOF M1(LEFT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("2DOF M2(RIGHT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("Press 'e' to stop")
def jog_right():
    ADDRESS = 4317
    VALUE = 16
    client_left.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_1)
    client_right.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_2)
    print("2DOF M1(LEFT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("2DOF M2(RIGHT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("Press 'e' to stop")
def stop():
    ADDRESS = 4317
    VALUE = 4
    client_left.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_1)
    client_right.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_2)
    print("2DOF M1(LEFT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("2DOF M2(RIGHT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("Stopped..")

    client_left.write_register(address=ADDRESS_IEG_MODE, value=VALUE_ENABLE, unit=SLAVE_ID_1)
    client_right.write_register(address=ADDRESS_IEG_MODE, value=VALUE_ENABLE, unit=SLAVE_ID_2)
    print("2DOF M1(LEFT):", ADDRESS_IEG_MODE, "UINT32:", VALUE_ENABLE, "-- Write successful")
    print("2DOF M2(RIGHT):", ADDRESS_IEG_MODE, "UINT32:", VALUE_ENABLE, "-- Write successful")

    print("Current position feedback registers:")
    response_left = client_left.read_holding_registers(read_address, num_registers, unit=SLAVE_ID_1)
    response_right = client_right.read_holding_registers(read_address, num_registers, unit=SLAVE_ID_2)
    print(f"Read M1 REV/S: {response_left.registers}")
    print(f"Read M2 REV/S: {response_right.registers}")
    print("Enabled..")
def fast_1():
    ADDRESS = 4317
    VALUE = 80
    client_left.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_1)
    client_right.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_2)
    print("2DOF M1(LEFT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("2DOF M2(RIGHT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
def fast_2():
    ADDRESS = 4317
    VALUE = 96
    client_left.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_1)
    client_right.write_register(address=ADDRESS, value=VALUE, unit=SLAVE_ID_2)
    print("2DOF M1(LEFT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")
    print("2DOF M2(RIGHT):", ADDRESS, "UINT32:", VALUE, "-- Write successful")

    

# Reset and enable motors
enable = input("Press 'q' to reset faults and enable drive. If it does not work, try homing the motors first")
if enable == 'q':
    try:
        client_left.write_register(address=ADDRESS_IEG_MODE, value=VALUE_FAULT_RESET, unit=SLAVE_ID_1)
        client_right.write_register(address=ADDRESS_IEG_MODE, value=VALUE_FAULT_RESET, unit=SLAVE_ID_2)
        print("2DOF M1(LEFT):", ADDRESS_IEG_MODE, "UINT32:", VALUE_FAULT_RESET, "-- Write successful")
        print("2DOF M2(RIGHT):", ADDRESS_IEG_MODE, "UINT32:", VALUE_FAULT_RESET, "-- Write successful")

        client_left.write_register(address=ADDRESS_IEG_MODE, value=VALUE_ENABLE, unit=SLAVE_ID_1)
        client_right.write_register(address=ADDRESS_IEG_MODE, value=VALUE_ENABLE, unit=SLAVE_ID_2)
        print("2DOF M1(LEFT):", ADDRESS_IEG_MODE, "UINT32:", VALUE_ENABLE, "-- Write successful")
        print("2DOF M2(RIGHT):", ADDRESS_IEG_MODE, "UINT32:", VALUE_ENABLE, "-- Write successful")

    except Exception as e:
        print("Write failed: {str(e)}")

    finally:
        # Drive enabled. Begin control 
        allow_move = True 
else: 
    print("Invalid choice. Press 'q'..")
            
while allow_move:
        print("Press 'q' to Jog Back")
        print("Press 'w' to Jog Front")
        print("Press 'e' to stop")
        print("Press 'r' to Jog Fast Back !! CAUTION !!")
        print("Press 't' to Jog Fast Front !! CAUTION !!")
        print("Press 'f' to close connection")
        choice = input("Press a button:  ")
        if choice == 'q':
            jog_left()
        elif choice == 'w':
            jog_right()
        elif choice == 'e':
            stop()
        elif choice == 'r':
            fast_1()
        elif choice == 't':
            fast_2()
        elif choice == 'f':
            # Close connection
            client_left.close()
            client_right.close()
            print ("Connection closed")
        else:
            print("Invalid choice. Please try again.")
    

