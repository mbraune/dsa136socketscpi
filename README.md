# dsa136socketscpi
socket scpi module to drive Spectrumanalyzer Voltcraft-DSA136 / OWONXSA1000

## DSA136
Voltcraft DSA-136

identical to : OWON XSA1000TG Series Spectrum Analyzer,  https://www.owon.com.hk/list_benchtop_analyzers

## programming 

command list scpi_programming_dsa136.pdf

### restrictions
this  device supports only reduced command set, 
- does not support *OPC? or *ESR?
- does not support SYST:ERR?
- **socketscpi cannot be used (needs always \*OPC? in Init)**

### class DSA136Socket
- **DSA136Socket(host, port=5028):** constructor
- **disconnect()**   shutdown socket
- **write(cmd)**
- **query(cmd)**     return String

### example measure freq
module dsa_meas1.py
- create instance of class DSA136socket
- set freq, set span
- measure max marker position, return pos