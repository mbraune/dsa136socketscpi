"""
based on https://github.com/morgan-at-keysight/socketscpi/blob/master/socketscpi/socketscpi.py
---
Author Martin Braune
class for SpectrumAnalyzer DSA136  (Voltcraft/OWON)
this  device supports only reduced command set, 
    (e.g.   does not support *OPC? or *ESR?, 
            does not support SYST:ERR? )
--> socketscpi cannot be used here , since*OPC? in Init
"""
import socket

class DSA136Socket:
    def __init__(self, host, port=5028, timeout=10):
        """Open socket connection with settings for instrument control."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(False)
        self.socket.settimeout(timeout)
        self.socket.connect((host, port))
        self.write('*rst')
        self.instId = self.query('*idn?')

    def disconnect(self):
        """Gracefully close connection."""
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def write(self, cmd):
        """Write a command string to instrument."""
        msg = f'{cmd}\n'
        self.socket.send(msg.encode('latin_1'))

    def query(self, cmd):
        """Sends query to instrument and returns reply as string."""
        msg = f'{cmd}\n'
        self.socket.send(msg.encode('latin_1'))

        # Read continuously until termination character is found.
        response = b''
        while response[-1:] != b'\n':
            response += self.socket.recv(1024)
        # Strip out whitespace and return.
        return response.decode('latin_1').strip()

