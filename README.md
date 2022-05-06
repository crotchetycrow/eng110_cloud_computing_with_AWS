# What is cloud computing?

Cloud computing is the delivery of computing services such as software, databases, servers and networking, over the internet. This means end users are able to access software and applications from wherever they are.

- Benefits?
  - Optimized costs: CapEx vs OpEx
  - Flexibility and scalability:
    - Only pay for what you use, no need concern yourself with IT solutions/management
    - When demand spikes or need for more powerful resources, these can be altered on demand
    - Easily maintainable global presence, focus on performance on where their userbase is
  - Mobility:
    - Setting up VMs or other services is quick and simple
  - Disaster recovery:
    - Paired regions (Azure) 500km apart leads to backups in data centres that won't be affected by power outages
  - Easy management and monitoring of product health services
  - Security
    - Data security from creation to destruction
    - Protected through encryption, MFA and backups
    - Internal data centre security
      - GovCloud (AWS) or Azure Government (Azure)
        - Used for sensitive data
        - Exclusive to Government staff (with access)

## Intro to AWS

#### Regions:
  - Physical locations for data centres around the globe for Amazon/Microsoft/Google to store their servers 
    - Low latency means that your users have improved connectivity
#### Availability zones:
  - Isolated locations within regions which contains the power and network connectivity
  - Multiple AZs are created so that in the instance of data centre failures there are backups for disaster recovery
  - The high availability nature of AZs means that there is reliable performance and minimal downtime
#### Types of cloud
  - Public cloud:
    - Cloud services offered by a third party (Amazon/Microsoft/Google) to multiple tenants
    - Data centres are owned by third party
  - Private cloud:
    - Cloud services offered by a third party (Amazon/Microsoft/Google) to specific tenants
    - Data centres might be owned by organisations
    - Organisations might have their own infrastructure
  - Hybrid cloud:
    - Cloud services offered by a third party (Amazon/Microsoft/Google) to multiple tenants
    - Data centres might be owned by organisations and services would be provided by third party (or vice versa)
#### Services
  - IaaS
    - A third party provides clients pay-as-you-go access to:
    - Storage, networking, servers, and other computing resources in the cloud.
  - PaaS
    - A service provider offers access to:
    - A cloud-based environment in which users can build and deliver applications
    - The provider supplies underlying infrastructure
  - SaaS
    - A service provider:
    - Delivers software and applications through the internet
    - Users subscribe to the software and access it via the web or vendor APIs
#### Microservices
  - An architectural approach to creating cloud applications
    - Each application is built as a set of services, and each service runs in its own processes and communicates through APIs
      - Benefits:
        - Update code at any time using continuous integration/continuous delivery (CI/CD)
        - Development teams can work in parallel. Small teams can move faster than large teams
        - Because the components of microservices architectures are granular, it’s easier to improve and maintain code
      - Disadvantages:
        - Difficult to manage a large number of services
        - Complex testing over a distributed environment
        - Harder to maintain the network as it has less fault tolerance, needs more load balancing

## What is an AMI?

An Amazon Machine Image is a master image for the creation of virtual servers (EC2).

The machine images are like templates that are configured with an operating system and other software that determine the user's operating environment.

- Benefits
  - Pre-configured templates that allow you to quickly deploy one or more instances
  - Quickly and efficiently determine what computing power, memory, storage and other factors you need for apps
  - Low cost
  - Flexibility
    - Run various different OS
    - Can include many AWS services
  - Scale and experiment with instances without worrying about infrastructure
- Use cases
  - Preparing a template for multiple EC2s that might need a base configuration but might have different functionality (think inheritance/polymorphism)

## AWS Best Practices

- Naming conventions
  - eng110_jack (for any files)
- AWS services:
  - Switch off at the end of the day (PAYG)
  - Ask if you want to use beyond 1800
    - Latest 2000
  - Terminating loses data but costs nothing
  - Stopping saves data but costs
- Use Ireland region EU-WEST1/A/B/C
- AWS KEYS MUST NOT BE SHARED
  - SAVE LOCAL
- file.pem - Move to .ssh folder in your machine

