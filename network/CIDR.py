class CIDR:
    def __init__(self, cidr):
        self.octets, self.prefix_len = self.validate_cidr(cidr)

    @staticmethod
    def validate_cidr(cidr):
        """
        Validate input CIDR notation

        :param cidr: CIDR notation for representing subnets
        :type: String

        :return: List of decimal octets, prefix length
        :type: List[int], int
        """
        # Check proper cidr notation
        split1 = cidr.split("/")
        if len(split1) != 2:
            raise ValueError("CIDR notation invalid.")

        # Check for prefix length characters
        try:
            prefix_len = int(split1[1])
        except ValueError:
            raise ValueError("Illegal value for prefix length. Integer expected.")

        # Check for prefix length range
        if prefix_len < 0 or prefix_len > 32:
            raise ValueError("Illegal value for prefix length. Should be within range [0, 32].")

        # Check for octet count
        octets = split1[0].split(".")
        if len(octets) != 4:
            raise ValueError("Illegal format for IP address. Should contain 4 octets.")

        # Check for octet values
        int_octets = []
        for octet in octets:
            try:
                int_octet = int(octet)
            except ValueError:
                raise ValueError("Illegal value for IP address. Octet values cannot contain non-numeric characters.")
            else:
                if int_octet < 0 or int_octet > 255:
                    raise ValueError("Illegal value for IP address. Octet value should be an integer within [0, 255].")
                int_octets.append(int_octet)

        return int_octets, prefix_len

    def to_string(self):
        """
        Convert octet list and prefix length to string of CIDR notation

        :return: CIDR notation
        :type: String
        """
        return ".".join([str(o) for o in self.octets]) + "/" + str(self.prefix_len)

    def display(self):
        """
        Print the string representation of octet list and prefix length

        :return: CIDR notation
        :type: String
        """
        print(self.to_string())
