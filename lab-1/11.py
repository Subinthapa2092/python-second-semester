# Program to implement bytes and bytearrays.

b = bytes([65, 66, 67])
print("Bytes:", b)

ba = bytearray([65, 66, 67])
print("Bytearray before change:", ba)

ba[0] = 70
print("Bytearray after change:", ba)