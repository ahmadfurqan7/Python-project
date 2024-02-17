# Enter PIN 🏦
# KEEP SECRET YOUR PIN!!!

print('=== BANK OF CODéDEX ===')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')