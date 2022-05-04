# What is cloud computing?

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

- Regions?
  - Latency
- Availability zones?
  - Why multiple availability zones (DR)?
  - High availability?
- Types of cloud?
  - Public
  - Private
  - Hybrid
- Services?
  - IaaS
  - PaaS
  - SaaS
- Microservices?
  - Benefit?

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
- eng110.pem - Move to .ssh folder in your machine

