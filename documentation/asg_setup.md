- Launch template
- Create launch template
- Name, decsription, tag
- Tick provide guidance
- Quick start > ubuntu > 18.04
- Instance type > t2 micro
- Key pair eng119
- subnet devopsstudent default 1a
- security group eng110_jack_app
- Storage = fine
- Advanced options:

  - User data = provision.sh
    `#!/bin/bash sudo apt-get update -y sudo apt-get upgrade -y sudo apt-get install nginx -y sudo systemctl restart nginx sudo systemctl enable nginx`

- EC2 > AUTO SCALING GROUP >
