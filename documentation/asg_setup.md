## Setting up an Auto Scaling Group launch template with AWS

- From AWSManager select/search EC2
- On the left side navbar select 'Launch template' from instance tab
- Select 'Create launch template'
- Name, description, tag as per usual naming conventions ('eng110-jack-')
- Tick 'provide guidance'
- Selecting AMI choose: Quick start > ubuntu > 18.04
- Instance type select 't2 micro'
- Key pair select 'eng119'
- ~~subnet DevOpsStudent default 1a~~
- Select existing security group: 'eng110_jack_app'
- No need to change storage configuration
- Advanced options:

  - User data = provision.sh
    ```
      #!/bin/bash
      sudo apt-get update -y
      sudo apt-get upgrade -y
      sudo apt-get install nginx -y
      sudo systemctl restart nginx
      sudo systemctl enable nginx
    ```

#### Setting up an ASG with AWS

- EC2 > AUTO SCALING GROUPs > CREATE AUTO SCALING GROUPS > NAME > LAUNCH TEMPLATE/CREATE > NEXT
- AZ AND SUBNETS : 1A,1B,1C > NEXT
- ATTACH NEW LOAD BALANCE :
  - ALB(HTTP/S)
  - Internet facing
  - Create a target group/select
- Next Group size and scaling policies:
  - Desired: 2
  - Minimum: 2
  - Maximum: 3
  - target tracking scaling policy (metric to be discussed with business owner)
- Tags

- Terminate to test it will spin up a new EC2
- Increase usage to cause a crash

#### Creating an alarm

- AWSManager > EC2 > AGS > your ASG
- Monitoring > CloudWatch > Alarms
- Select 'create a new alarm'
- Select 'metric'
- EC2 > By Auto Scaling Group
- eng110-jack-ASG-app 'CPUUtilization'
- Select period
- Define value (e.g. 50)
- Create/Select SNS topic

  - Create a new topic (name)
  - Enter email

- Add name and description

- Create dynamic scaling policies
- From the dropdown menu select 'Step scaling'
- Name the policy
- Select CloudWatch alarm from dropdown menu
- Select an action from dropdown menu
- Define the value of capacity units
- Define time the instance needs to spin up
- Hit create - Tada!
