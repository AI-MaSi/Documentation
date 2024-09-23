# Documentation

This repository contains the documentation for various components revolving around the project.

```mermaid
graph TD
    subgraph Excavator System
        A[Excavator Main] --> B[Excavator]
        B -->|Control| C[PWM Controller]
        B -->|Read| D[ADC Sensors]
        B -->|Read| E[IMU Sensors]
        B -->|Read| F[GPIO Sensors]
        B --> G[Send Loop]
        B --> H[Receive Loop]
        C -->|Servo Angles| B
        D -->|Pressure Data| B
        E -->|IMU Data| B
        F -->|RPM Data| B
    end

    subgraph Motion Platform System
        M[Motion Platform Main] --> N[MotionPlatformClient]
        N --> O[NiDAQ Controller]
        N --> P[Send Loop]
        N --> Q[Receive Loop]
        N --> R[Process Received Data]
        O -->|Joystick Data| N
    end

    subgraph Server System
        I[Server Main] --> J[DataExchangeServer]
        J --> K[ThreadingHTTPServer]
        K --> L[RequestHandler]
    end

    G -->|HTTP POST Sensor Data| L
    L -->|HTTP GET Control Data| H
    P -->|HTTP POST Control Data| L
    L -->|HTTP GET Sensor Data| Q

    subgraph Excavator Components
        C
        D
        E
        F
    end
    subgraph Communication
        G
        H
        L
        P
        Q
    end