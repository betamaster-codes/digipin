# digipin
DIGIPIN (Digital Postal Index Number) is an open-source geo-coded addressing system for India. Developed by India Post with IIT-H and ISRO, it encodes precise lat/lon into 10-character alphanumeric codes and supports reverse decoding. Ideal for scalable, GIS-integrated digital infrastructure.

---

````markdown
# DIGIPIN (Digital Postal Index Number)

**DIGIPIN** is an open-source, geo-coded addressing system developed by the **Department of Posts, Ministry of Communications, Government of India** in collaboration with **IIT Hyderabad** and **ISRO (NRSC)**. It encodes geographical locations (latitude and longitude) into a **10-character alphanumeric code**, enabling a standardized, machine-readable, and privacy-preserving digital address reference.

---

## 🌍 What is DIGIPIN?

DIGIPIN divides India into a hierarchical grid of **4x4 subregions** down to ~3.8m x 3.8m precision, generating a **unique 10-digit alphanumeric code** for each grid cell.

### Example:
```text
Input Coordinates: 22.2433683° N, 73.2019148° E 
Generated DIGIPIN: 3LC-L67-647F
````

---

## 🚀 Features

* 🔁 **Bidirectional encoding**: Encode coordinates → DIGIPIN and decode DIGIPIN → coordinates
* 🔒 **Privacy-focused**: Contains no personal or address-level metadata
* 🌐 **GIS-compatible**: Ideal for digital public infrastructure, KYC, emergency response, delivery, and more
* 📦 **Offline capable**: No internet required for location encoding/decoding
* 🇮🇳 **India-specific**: Covers mainland, islands, and EEZ regions

---

## 📦 Repository Contents

| File/Folder                      | Description                             |
| -------------------------------- | --------------------------------------- |
| `digipin_encoder.py`             | Encode latitude/longitude to DIGIPIN    |
| `digipin_decoder.py`             | Decode DIGIPIN to latitude/longitude    |
| `examples/`                      | Sample code and test cases              |

---

## 🧑‍💻 How to Use

### 🔐 Encode Coordinates to DIGIPIN

```python
from digipin_encoder import get_digipin

# Example: Encode coordinates (latitude, longitude) to DIGIPIN
digipin = get_digipin(22.2433683, 73.2019148)
print("DIGIPIN:", digipin)  # Output: DIGIPIN: 3LC-L67-647F

from digipin_decoder import decode_digipin

# Example: Decode a DIGIPIN back to approximate coordinates
result = decode_digipin("3LC-L67-647F")
print("Center Coordinates:", result['center'])
print("Bounding Box:", result['bounding_box'])

```python
from digipin_encoder import get_digipin

lat = 22.2433683
lon = 73.2019148
print(get_digipin(lat, lon))  # Output: 3LC-L67-647F
```

### Decode DIGIPIN to Coordinates

```python
from digipin_decoder import get_latlng_by_digipin

code = "3LC-L67-647F"
print(get_latlng_by_digipin(code))  # Output: 22.2433683, 73.2019148
```

---

## 🏛️ Background

DIGIPIN is part of India’s initiative to build a **Digital Public Infrastructure (DPI)** for addressing under the **National Geospatial Policy 2022**. It provides a universal spatial reference for residences, institutions, and assets—critical for **last-mile delivery**, **financial inclusion**, **emergency services**, and **urban planning**.

---

## 📚 Documentation

Please refer to for:

* Code architecture
* Grid logic and bounding box
* Handling boundary conditions
* Legal and policy context

---

## ✅ Use Cases

* **Logistics and Delivery** (e.g., e-commerce, postal services)
* **Emergency Response** (e.g., ambulance/fire service location accuracy)
* **Banking & KYC** (accurate, digitized address verification)
* **Urban Governance & Planning**
* **Disaster Management**
* **Maritime & Rural Geolocation**

---

## 🤝 Contributing

We welcome contributions in the form of:

* Optimized code
* GIS tools and visualizations
* Language wrappers (Java, JS, Rust, etc.)
* Web/CLI apps

Please fork the repo and create a pull request. See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## 📜 License

DIGIPIN is released as **open-source** under a permissive [MIT License](./LICENSE).

---

## 🔍 Keywords (SEO)

```
DIGIPIN, Digital Address, Geo Coded Address, India Post, GIS, GPS Addressing, Open Location Code India, Digital Postal Index, KYC address, Indian Address Grid, National Addressing Grid, WGS84, Address as a Service (AaaS), geospatial DPI, geocoding India
```

---

## 📬 Contact & Attribution

* Pyhton Developed by: **BetaMaster**

