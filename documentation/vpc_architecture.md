# Networking - VPC Architecture

## What is VPC?

A virtual private cloud is a secure, isolated private cloud hosted within a public cloud. VPC customers can run code, store data, host websites, and do anything else they could do in an ordinary private cloud, but the private cloud is hosted remotely by a public cloud provider.

It should be noted that not all private clouds are hosted in this way.

VPCs combine the scalability and convenience of public cloud computing with the data isolation of private cloud computing.

Amazon VPC is a AWS service used for creating a VPC

Benefits:

- Agility:
  - A VPC gives users full control over the network size along with automation to scale resources up or down whenever required. These resources can be scaled dynamically in real-time.
- Security:
  - It is isolated so a user’s data and space don’t mix with a cloud provider’s other customers. Users have full control of how resources and workloads are accessed and by whom.
  - Responsibility for cloud security is shared between the cloud provider and the user and users must take steps to secure their data and apps in the cloud.
- Ease of use:
  - Easy to connect a VPC to a public cloud or to on-prem cloud architectures.

## What are subnets?

Subnet is a logical subdivision of an IP network. The practice of dividing a network into two or more networks is called subnetting.AWS provides two types of subnetting one is Public which allow the internet to access the machine and another is private which is hidden from the internet.

"Containers" within a VPC that segment off a slice of range of IP addresses you have defined. Subnets allow you to give different access rules and place resources in different containers where those rules should apply.

Think VPC is an apartment and subnets are different rooms in your apartment. You wouldn't have a big open window in your bathroom on the shower wall, much like you wouldn't put a database with sensitive information in a public subnet.

## What is a CIDR (Classless Inter-Domain Routing) block?

CIDR blocks are used for specifying a range of IP addresses in IPv4 or IPv6 format. A way of allocating IP addresses and IP routing. Meaning that only IP addresses within that range are allowed access - CIDR work in conjunction with subnets to define access.

Think CIDR is the access code to get into your locked highly secure bedroom (subnet).

## What is a sub-mask?

A subnet is like an IP address but for only internal usage within a network. Routers use subnet masks to route data packets to the right place.

Subnet masks are not indicated within data packets traversing the internet - those packets only indicate the destination IP address, which a router will match with a subnet.

Bob sends a letter to Alice, but he sends it to Alice's place of employment rather than her home. Alice's office is quite large with many different departments. To ensure employees receive their correspondence quickly, the administrative team at Alice's workplace sorts mail by department rather than by individual employee. After receiving Bob's letter, they look up Alice's department and see she works in Customer Support. They send the letter to the Customer Support department instead of to Alice, and the customer support department gives it to Alice.

In this analogy, "Alice" is like an IP address and "Customer Support" is like a subnet mask.

Subnet masks are the messenger for the packet between IP addresses and the destination device.

## What is IP (internet protocol) networking?

IP networks allow devices to communicate using IP addresses. An IP is essentially a set of predetermined rules that structure and format the data we send over internet networks.

IP is fundamental to allowing our devices to communicate with each other. It is the IP address that acts as the identifier and differentiates each individual device connected to a network.

Each computer, smartphone, tablet, laptop or router has its own unique IP address. This is a unique string of numbers separated by decimals. Each decimal number is called an Octet.

An IP network refers to any group of devices, each with their own unique IP addresses, connected under the same network topology. Devices connected to a shared IP network can send and receive information.

A private IP network allows data to be shared between connected devices securely, by enforcing password protected connectivity that allows only those devices in your office or home to access the IP network.

## What is a routing table?

A routing table is a type of data file that acts as a map and is often installed on a router, networked computer or other hardware. The routing table contains information about various routes between devices in order to present the most efficient paths for data packets.

A routing table uses static and dynamic Internet protocol or IP addresses to identify devices, and works with an ARP (Address resolution protocol) cache that holds these addresses. The routing table is commonly referred to as a resource for finding the next hop, or subsequent route for a data packet.

Traffic light, routing table determines where traffic goes

## What is an NACL (Network Access Control List)?

NACL is a security layer for your VPC that controls the traffic in and out of one or more subnets. The NACL is made up of several components:

- Rule number: This is a number associated with every rule. Rules are evaluated starting with the lowest numbered rule. As soon as the rule matches traffic, the rule is applied regardless of whether the highest-numbered rule contradicts to it.
- Protocol: You can specify any protocol that has a standard protocol number. For example, Http, Https, ICMP, SSH, etc.
- Inbound rules: It specifies the source of the traffic and the destination port.
- Outbound rules: It specifies the destination traffic and the destination port.

The default NACL allows all the traffic to flow in or out of the subnet which is associated with it. Each NACL also includes a rule whose rule number is asterisk which determines if traffic does not match any of the numbered rules, then it is denied. This rule cannot be modified or removed.

Custom NACL is a user-defined NACL, and by default, it denies all the inbound and outbound traffic until you add rules.

NACL can be understood as the firewall or protection for the subnet. Security group can be understood as a firewall to protect EC2 instances.

Think the security guard checking a guest list (rules), if your name (rule number) flags then you are denied access to the bar (subnet).
