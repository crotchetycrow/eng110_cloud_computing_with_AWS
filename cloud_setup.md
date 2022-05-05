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

## Connecting to EC2
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


#### Diagram of set up process:
![](img/EC2_diagram.png)


## Adding files from local host to EC2

- `scp -i location/file.pem -r destination/dir ec2@ip.com:source/file/or/folder`
  - SCP is secure file proxy
  - -i is identifier
  - pem location
  - -r receive
  - destination
  - Public DNS/ec2 id
  - source file or folder
  
#### Reverse proxy with NGINX

- In Security Groups, edit inbound rules
  - Custom TCP, set port range to 3000
- In /etc/nginx/sites-available/default:
  - `nano default` and add the following:
    - server_name your-ip;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
                proxy_pass http://localhost:3000;
        }

        location /fibonacci/ {
                proxy_pass http://localhost:3000/fibonacci/;
        }
- `npm start` - Tada!

#### Setting up MongoDB

- `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4`
- `sudo add-apt-repository 'deb [arch=amd64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse'`
- `sudo apt update -y`
- `sudo apt install mongodb-org -y`
- `sudo systemctl start mongod`
- `sudo systemctl enable mongod`
- `mongo --eval 'db.runCommand({ connectionStatus: 1 })'` - Verify
  - or `sudo systemctl status mongod`

`netstat -tulpn | grep PORT_NUMBER` - checks if the port is listening to X

