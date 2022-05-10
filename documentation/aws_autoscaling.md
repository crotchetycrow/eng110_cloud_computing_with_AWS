# What is AWS Autoscaling?

An AWS service that automatically adjusts the capacity of your applications. Giving you more flexibility depending on the amount of incoming traffic you have.

Autoscaling is a cloud computing feature that enables organizations to scale cloud services such as server capacities or virtual machines up or down automatically, based on defined situations such as traffic ir utilization levels.

### Benefits:

- Cost. When loads are low, auto scaling allows both companies managing their own infrastructure and businesses that rely on cloud infrastructure to send some servers to sleep. This reduces electricity costs and water costs where water is used in cooling. Cloud auto scaling also means paying for total usage instead of maximum capacity.

- Security. Auto scaling also protects against application, hardware, and network failures by detecting and replacing unhealthy instances while still providing application resiliency and availability.

- Availability. Auto scaling improves availability and uptime, especially when production workloads are less predictable.

Tools include:

- Amazon EC2 Auto Scaling which dynamically scales your Amazon EC2 instances.

## What is load balancing?

A technique used to distribute workloads uniformly across servers or other computing resources.

AWS offers their ELB (Elastic Load Balancing) service which automatically distributes incoming application traffic and scales resources to meet traffic demands.

## What are listener groups?

A listener is a process that check for connection requests using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

## What is a launch template for ASG (Auto Scaling Group)?

A launch template is a group of all the configurations that create and configure an EC2 instance.

It saves the step by step process of creating an EC2 with all the configurations and that you can easily spin up an EC2 with the same configuration.

Launch templates make use of auto scaling and allows for creating an ASG that launches both Spot and On-Demand instances.

## Launch configuration vs Launch template

Launch templates are newer and recommended by AWS over launch configuration as launch templates have more features besides auto scaling and they support multiple versions of the same instance.

Launch configurations are limited to auto scaling only, the instances are immutable and are subject to limited configuration.

## Auto scaling policy

Allow you to define the value for the upper and lower bound and scales to this defined policy.

Step scaling policies:

- Step scaling applies “step adjustments” which means you can set multiple actions to vary the scaling depending on the size of the alarm breach.

Simple scaling policies:

- Simple scaling relies on a metric as a basis for scaling. For example, you can set a CloudWatch alarm to have a CPU Utilization threshold of 80%, and then set the scaling policy to add 20% more capacity to your Auto Scaling group by launching new instances.

## Scaling out/in vs scaling up/down

Scaling out/in is horizontal scaling, increasing infrastructure to support increasing load. For example, adding more of the same functional components to spread out a load.

Scaling up/down is vertical scaling, making a component larger or faster to handle a greater load. For example, increasing storage or number of CPUs.

## Scalability

The ability of a system to take advantage of additional resources, such as database servers, processors, memory, or disk space

## High availability

The ability of a system to operate continuously without failing for a designated period of time. High Availability works to ensure a system meets an agreed-upon operational performance level.
