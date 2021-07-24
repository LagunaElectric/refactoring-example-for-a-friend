class IP:
    def __init__(self, ip: str, subnet_mask: str = "255.255.0.0") -> None:
        self.ip: str = ip
        self.subnet_mask: str = subnet_mask

    def octets(self) -> list[str]:
        return self.ip.split(".")

    def octets_as_ints(self) -> list[int]:
        return [int(i) for i in self.octets()]

    def bin_octets(self) -> list[str]:
        return [bin(i).split("b")[1] for i in self.octets_as_ints()]

    def bin_mask(self) -> str:
        filled_bin_octets = []
        for octet in self.bin_octets():
            octet_to_append = octet.zfill(8) if len(octet) < 8 else octet
            filled_bin_octets.append(octet_to_append)
        return "".join(filled_bin_octets)

    def subnet_mask_octets(self) -> list[str]:
        return self.subnet_mask.split(".")

    def subnet_mask_octets_as_ints(self) -> list[int]:
        return [int(i) for i in self.subnet_mask_octets()]

    def bin_subnet_mask_octets(self) -> list[str]:
        return [bin(i).split("b")[1] for i in self.subnet_mask_octets_as_ints()]

    def bin_subnet_mask(self) -> str:
        filled_bin_submask_octets = []
        for octet in self.bin_subnet_mask_octets():
            octet_to_append = octet.zfill(8) if len(octet) < 8 else octet
            filled_bin_submask_octets.append(octet_to_append)
        return "".join(filled_bin_submask_octets)

    def bin_subnet_mask_zeros(self) -> int:
        return self.bin_subnet_mask().count("0")

    def bin_subnet_mask_ones(self) -> int:
        return 32 - self.bin_subnet_mask_zeros()

    def hosts_available(self) -> int:
        return 2 ** self.bin_subnet_mask_zeros() - 2

    def bin_network_id(self) -> str:
        return self.bin_mask()[:self.bin_subnet_mask_ones()] + "0" * self.bin_subnet_mask_zeros()

    def bin_broadcast_id(self) -> str:
        return self.bin_mask()[:self.bin_subnet_mask_ones()] + "1" * self.bin_subnet_mask_ones()

    def network_address_bin_octets(self) -> list[int]:
        return [
            i for i in [
                str(self.bin_network_id())[j:j + 8] for j in range(0, len(str(self.bin_network_id())), 8)
            ]
        ]

    def broadcast_address_bin_octets(self) -> list[int]:
        return [
            i for i in [
                str(self.bin_broadcast_id())[j:j + 8] for j in range(0, len(str(self.bin_broadcast_id())), 8)
            ]
        ]

    def network_address(self) -> str:
        return ".".join([str(int(octet, 2)) for octet in self.network_address_bin_octets()])

    def broadcast_address(self) -> str:
        return ".".join([str(int(octet, 2)) for octet in self.broadcast_address_bin_octets()])

    def __str__(self) -> str:
        out = f"ip: {self.ip}\n"
        out += f"subnet_mask: {self.subnet_mask}\n"
        out += f"octets(): {self.octets()}\n"
        out += f"octets_as_ints: {self.octets_as_ints()}\n"
        out += f"binary_octets: {self.bin_octets()}\n"
        out += f"binary_mask: {self.bin_mask()}\n"
        out += f"subnet_mask_octets: {self.subnet_mask_octets()}\n"
        out += f"subnet_mask_octets_as_ints: {self.subnet_mask_octets_as_ints()}\n"
        out += f"binary_subnet_mask_octets: {self.bin_subnet_mask_octets()}\n"
        out += f"binary_subnet_mask: {self.bin_subnet_mask()}\n"
        out += f"binary_subnet_mask_zeros: {self.bin_subnet_mask_zeros()}\n"
        out += f"binary_subnet_mask_ones: {self.bin_subnet_mask_ones()}\n"
        out += f"hosts_available: {self.hosts_available()}\n"
        out += f"net_id_bin: {self.bin_network_id()}\n"
        out += f"broadcast_id_bin: {self.bin_broadcast_id()}\n"
        out += f"network_address_bin_octets: {self.network_address_bin_octets()}\n"
        out += f"broadcast_address_binary_octets: {self.broadcast_address_bin_octets()}\n"
        out += f"network_address: {self.network_address()}\n"
        out += f"broadcast_address: {self.broadcast_address()}"
        return out


if __name__ == "__main__":
    ip: IP = IP("127.0.0.1")
    print(ip)
