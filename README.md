# Documentation

This repository contains the documentation for various components revolving around the project.
For more coding-specific information, please see "Excavator" and "MotionPlatform" -repositories.

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
```

```mermaid
graph TD
    A[Raspberry Pi] --> D[ADC HAT]
    D --> C[PWM HAT]
    C --> B[OLED Screen]
    B --> E[Multiplexer]
    E --> F[IMU Sensor 1]
    E --> G[IMU Sensor 2]
    E --> H[IMU Sensor 3]
    
    K[IMU sensors can have same<br>I2C addresses if not chained]
    
    subgraph "I2C Chaining Info"
    I[I2C devices can be chained<br>if addresses differ]
    J[Devices chained: Pi -> ADC -> PWM -> OLED -> Multiplexer]
    L[Only one cable required for the entire chain]
    end
    
    style A fill:#f9d71c,stroke:#333,stroke-width:2px
    style E fill:#f9a61c,stroke:#333,stroke-width:2px
    style B fill:#85C1E9,stroke:#333,stroke-width:2px
    style C fill:#82E0AA,stroke:#333,stroke-width:2px
    style D fill:#F1948A,stroke:#333,stroke-width:2px
    style F fill:#D7BDE2,stroke:#333,stroke-width:2px
    style G fill:#D7BDE2,stroke:#333,stroke-width:2px
    style H fill:#D7BDE2,stroke:#333,stroke-width:2px
    style I fill:#F9E79F,stroke:#333,stroke-width:1px
    style J fill:#F9E79F,stroke:#333,stroke-width:1px
    style K fill:#F9E79F,stroke:#333,stroke-width:1px
    style L fill:#F9E79F,stroke:#333,stroke-width:1px
    linkStyle 0,1,2,3 stroke-width:2px,fill:none,stroke:#FF6347
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef infoText fill:#e6f2ff,stroke:#333,stroke-width:1px
    class K,I,J,L infoText
```
