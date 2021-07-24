from ip import IP


class SubnetCalculator:
    def __init__(self) -> None:
        self.ip: IP = None

    def get_ip_input(self) -> str:
        return input('\n\nFill in the IP address in the format www.xxx.yyy.zzz : ')

    def get_subnet_mask_input(self) -> str:
        return input("\nFill in the subnet mask in the format www.xxx.yyy.zzz: ")

    def print_results(self) -> None:
        out = f"CIDR: {self.ip.bin_subnet_mask_ones()}\n"
        out += f"NetID: {self.ip.network_address()}\n"
        out += f"Number of hosts in this subnet: {self.ip.hosts_available()}\n"
        out += f"Broadcast: {self.ip.broadcast_address()}"
        print(out)

    def prompt_to_continue(self):
        return str(input('\n\nWould you like to run the program again? (S/N): '))

    def run(self) -> None:
        running: bool = True
        yes = ['s', 'S']
        no = ['n', 'N']

        while running:
            an_ip = self.get_ip_input()
            a_subnet_mask = self.get_subnet_mask_input()
            self.ip = IP(an_ip, a_subnet_mask)
            self.print_results()
            answer = self.prompt_to_continue()
            while answer not in yes and answer not in no:
                print("Invalid choice. Please try again.")
                answer = self.prompt_to_continue()
            if answer in no:
                running = False


if __name__ == "__main__":
    print('\nSubnets Calculator (IPv4)')
    subnet_calc: SubnetCalculator = SubnetCalculator()
    subnet_calc.run()
