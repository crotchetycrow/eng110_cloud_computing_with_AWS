## Setting up an Auto Scaling Group with AWS

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

- EC2 > AUTO SCALING GROUP >
