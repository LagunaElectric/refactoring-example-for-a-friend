print('\nSubnets Calculator (IPv4)')
while True:
    ip = input('\n\nFill in the IP address in the format www.xxx.yyy.zzz : ')
    octip = ip.split(".")

    int_octip = [int(i) for i in octip]

    subnet = input("\nFill in the subnet mask in the format www.xxx.yyy.zzz: ")

    octsub = subnet.split(".")
    int_octsub = [int(j) for j in octsub]
    ipbin = []
    ipbinoct = [bin(i).split("b")[1] for i in int_octip]

    for i in range(0, len(ipbinoct)):
        if len(ipbinoct[i]) < 8:
            filledbin = ipbinoct[i].zfill(8)
            ipbin.append(filledbin)
        else:
            ipbin.append(ipbinoct[i])
    ip_bin_mask = "".join(ipbin)

    subbin = []

    sub_bin_octet = [bin(i).split("b")[1] for i in int_octsub]

    for i in sub_bin_octet:
        if len(i) < 8:
            subnetfilled = i.zfill(8)
            subbin.append(subnetfilled)
        else:
            subbin.append(i)
    submask = "".join(subbin)


    zeros = submask.count("0")
    ones = 32 - zeros
    hostsavailabe = abs(2 ** zeros - 2)
    netidbin = ip_bin_mask[:ones] + "0" * zeros
    broadcastidbin = ip_bin_mask[:ones] + "1" * zeros

    networkaddbinoct = []
    broadcastbinoct = []

    [networkaddbinoct.append(i) for i in [netidbin[j:j + 8]
                                          for j in range(0, len(netidbin), 8)]]
    [broadcastbinoct.append(i) for i in [broadcastidbin[j:j + 8]
                                         for j in range(0, len(broadcastidbin), 8)]]

    networkadd = ".".join([str(int(i, 2)) for i in networkaddbinoct])
    broadcastadd = ".".join([str(int(i, 2)) for i in broadcastbinoct])

    print("CIDR:", ones)
    print("NetID:", networkadd)
    print("Number of hosts in this subnet:", hostsavailabe)
    print("Broadcast:", broadcastadd)

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
