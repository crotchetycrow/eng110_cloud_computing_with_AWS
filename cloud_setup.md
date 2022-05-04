# Setting up access to a AWS VM (EC2)

- Move file.pem into .ssh folder
  - Located in home dir
- Type chmod 400 file.pem in bash terminal
  - Chmod 400 (chmod a+rwx,u-wx,g-rwx,o-rwx) sets permissions so that:
    - (U)ser / owner can read, can't write and can't execute
    - (G)roup can't read, can't write and can't execute
    - (O)thers can't read, can't write and can't execute.

## Setting up an EC2 (VM) on AWS

- Select EC2
- Select launch instance
  - Choose the launch instance option
- Select Ubuntu 18.04 (free tier)
- Select t2 micro, it's a 3 page app doesn't need much.
#### In configuring instance details select the following:
  - Number of Instance: 1
  - Default network
  - Select subnet default DevOpsStudent - default euw ending in 1a
  - Auto-assign public IP: Enable
#### No changes to Storage -  More than enough
- Add tag eng110_jack (So we know that it belongs to me)
#### Security Group:
  - Create a new Security Group
  - Name it "eng110_jack"
  - Give description
  - Two rules:
    - SSH with the source being 'My IP'
      - Give description (Office ip)
    - HTTP with source being 'Anywhere'
      - Give description "NGINX"
  - Review
#### Launch:
    - Choose existing key pair:
      - eng119 | RSA

#### Connecting to EC2
- Click on instance
- Connect (top right)
- Click on SSH CLIENT
  - Copy the command example
- Open your git bash terminal:
  - cd into .ssh
  - paste command
  - sudo apt-get update -y
  - sudo apt-get upgrade -y
  - sudo apt-get install nginx -y
- Go to your public IP (found on EC2 Instance connect)
- Post in url bar - Tada!