from ipaddress import IPv4Network


def calculate_network_ip(gateway_ip, subnet_mask):
    # Check if the subnet mask is in CIDR notation
    if '/' in subnet_mask:
        # The subnet mask is in CIDR notation
        subnet_mask_cidr = int(subnet_mask.split('/')[1])
        subnet_mask_decimal = str(IPv4Network(f"0.0.0.0/{subnet_mask_cidr}", strict=False).netmask)
    else:
        # The subnet mask is in dotted decimal notation
        subnet_mask_decimal = subnet_mask

    # Calculate the network IP based on the gateway IP and subnet mask in dotted decimal notation
    gateway_network = IPv4Network(f"{gateway_ip}/{subnet_mask_decimal}", strict=False)
    return gateway_network.network_address
