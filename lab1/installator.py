import wmi
import hashlib
import os.path

def hash_key():
    c = wmi.WMI().Win32_PhysicalMedia()[0]
    serial_number = c.SerialNumber
    return hashlib.sha512(serial_number.encode('utf-8')).hexdigest()


def check_keys(filename):
    if not os.path.isfile(filename):
        return False
    with open(filename, "r") as license:
        if license.readline() == hash_key():
            return True
        else:
            return False


def create_license(filename):
    with open(filename, "w") as license:
        license.write(hash_key())


if __name__ == "__main__":
    create_license("license.key")
    with open("license.key", "r") as license:
        print(license.readline())