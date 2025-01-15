# Motion Platform Modbus Controller

A huge thank you to **Teemu Leppänen** for creating this awesome documentation and codebase for controlling a 2DOF motion platform!

## What's This?
This project lets you control a simulator motion platform using Modbus TCP. It includes both documentation and example code to get you started with Tritex II 90-115 series motors.

## Quick Setup
1. Network settings:
   - Left Motor (M1): 192.168.0.211
   - Right Motor (M2): 192.168.0.212
   - Port: 502

2. Basic controls available:
   - Direct control (Jog, Home)
   - Analog control (Position, Velocity)
   - Host control (for custom movement)

## Safety First!
Remember to check the emergency stop buttons:
- One on the pre-control unit
- One on the right side of operator cabin

## Want to Learn More?
Check out the detailed documentation that Teemu created - it covers everything from initial setup to advanced controls. The example Python code shows how to get started with basic movements.

Katja's Extended implementation using FluentModbus can be found here (thank you as well!): [Kapa77i/Tritex_ModBus: My Thesis work on Tritex Modbus connection](https://github.com/Kapa77i/Tritex_ModBus).