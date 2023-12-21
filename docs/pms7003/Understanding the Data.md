# **Understanding the Data**

This system collects environmental data, including temperature, humidity, and particulate matter concentrations in the air. This section provides a detailed breakdown of the data output:

### 1. Temperature (`temp_f`)

- **Unit**: Degrees Fahrenheit (°F)
- **Description**: 
  - Represents the ambient temperature where the DHT sensor is placed.

### 2. Humidity (`humidity`)

- **Unit**: Percentage (%)
- **Description**: 
  - Measures the relative humidity of the environment. This value represents the amount of moisture in the air compared to the maximum it can hold at the same temperature.

### 3. Particulate Matter (from PMS sensor)

The PMS7003 sensor quantifies particulate matter (PM) concentrations for distinct particle sizes. Particulate matter consists of tiny liquid droplets and solid particles in the air, such as dust, pollen, soot, and smoke. 

- **Categories**:
  - **PM1.0 (`pm1_0` and `pm1_0_2` for the second sensor)**
  - **PM2.5 (`pm2_5` and `pm2_5_2` for the second sensor)**
  - **PM10 (`pm10` and `pm10_2` for the second sensor)**
  
- **Unit**: µg/m³ (micrograms per cubic meter)
- **Description**:
  - These metrics represent the concentration of particulates in the air for particles with diameters less than or equal to 1.0, 2.5, and 10 micrometers, respectively. For example, PM2.5 pertains to particles that are 2.5 micrometers or smaller, which are especially relevant for health due to their capability to penetrate deep into the lungs.

### 4. Number of Particles

The system measures the particle count for various sizes per 0.1 liter of air:

- **Fields**: 
  - Examples include `n0_3`, `n0_5`, `n1_0`, `n2_5`, `n5_0`, and `n10` (with `_2` variants for the second sensor).

- **Unit**: Count per 0.1L of air.
- **Description**:
  - Indicates how many particles of a specific size (e.g., 0.3 micrometers) are found in every 0.1 liter of air.

