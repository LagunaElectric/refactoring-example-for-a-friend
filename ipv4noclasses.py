print('\nSubnets Calculator (IPv4)')
while True:
    ip: str = input('\n\nFill in the IP address in the format www.xxx.yyy.zzz : ')  # declaration
    ip_octets = ip.split(".")

    # we've just identified the class

    ip_octets_as_ints = [int(i) for i in ip_octets]

    subnet_mask = input("\nFill in the subnet mask in the format www.xxx.yyy.zzz: ")

    subnet_mask_octets = subnet_mask.split(".")
    subnet_mask_octets_ints = [int(j) for j in subnet_mask_octets]
    binary_ip_octets = [bin(i).split("b")[1] for i in ip_octets_as_ints]

    filled_bin_octets = []
    for octet in range(0, len(binary_ip_octets)):
        if len(binary_ip_octets[octet]) < 8:
            filledbin = binary_ip_octets[octet].zfill(8)
            filled_bin_octets.append(filledbin)
        else:
            filled_bin_octets.append(binary_ip_octets[octet])
    ip_bin_mask = "".join(filled_bin_octets)

    binary_subnet_mask_octets = [bin(i).split("b")[1] for i in subnet_mask_octets_ints]

    filled_bin_submask_octets = []
    for octet in binary_subnet_mask_octets:
        if len(octet) < 8:
            subnet_filled = octet.zfill(8)
            filled_bin_submask_octets.append(subnet_filled)
        else:
            filled_bin_submask_octets.append(octet)
    binary_subnet_mask = "".join(filled_bin_submask_octets)

    bin_subnet_mask_zeros = binary_subnet_mask.count("0")
    bin_subnet_mask_ones = 32 - bin_subnet_mask_zeros
    hosts_available = abs(2 ** bin_subnet_mask_zeros - 2)
    bin_network_id = ip_bin_mask[:bin_subnet_mask_ones] + "0" * bin_subnet_mask_zeros
    bin_broadcast_id = ip_bin_mask[:bin_subnet_mask_ones] + "1" * bin_subnet_mask_zeros

    network_address_bin_octets = []
    broadcast_address_bin_octets = []

    [network_address_bin_octets.append(i) for i in [bin_network_id[j:j + 8]
                                                    for j in range(0, len(bin_network_id), 8)]]
    [broadcast_address_bin_octets.append(i) for i in [bin_broadcast_id[j:j + 8]
                                                      for j in range(0, len(bin_broadcast_id), 8)]]

    network_address = ".".join([str(int(octet, 2)) for octet in network_address_bin_octets])
    broadcast_address = ".".join([str(int(octet, 2)) for octet in broadcast_address_bin_octets])

    print("CIDR:", bin_subnet_mask_ones)
    print("NetID:", network_address)
    print("Number of hosts in this subnet:", hosts_available)
    print("Broadcast:", broadcast_address)

    while True:
        yes = ['s', 'S']
        no = ['n', 'N']
        answer = str(input('\n\nWould you like to run the program again? (S/N): '))
        if answer in yes or no:
            break
        print("Invalid choice. Please try again.")
    if answer in yes:
        continue
    elif answer in no:
        print("See you a next time!")
        break
    else:
        break
