# What is S3 Bucket

Amazon S3 (Simple Storage Service) provides object storage, which is built for storing and recovering any amount of information or data from anywhere over the internet. It provides this storage through a web services interface.

S3 is essentially a globally available folder.

![](img/S3_diagram.png)

#### Setting up AWS CLI in EC2
- Install python `sudo apt install python3`
- Install pip `sudo apt install python3-pip -y`
- `alias python=python3` - Telling the OS explicitly which version to use
- `python --version` - Make sure version is 3.6 or above
- `sudo python3 -m pip install awscli` - Install AWS CLI
- `aws configure`
  - Access key
  - Secret access key
  - Region - eu-west-1
  - Data format - json

#### Setting up an S3 bucket via AWS CLI

- `aws s3 ls` - Sends a request to s3 and lists everything (This is how we know we've set up AWS CLI correctly)
- `aws s3 mb s3://eng110-jack` - aws 'service' 'command' (aws s3 <service> mb (make bucket) <command> s3:// (where?) eng110-jack (name))
- `sudo nano test.txt` - Create a file to send from EC2 to S3
- `aws s3 cp test.txt s3://eng110-jack/` - Copies file from EC2 to S3
- `aws s3 cp s3://eng110-jack/test.txt test.txt` - aws 'service' 'command' (aws s3 <service> cp (cp file) <command> s3:// (where from?) eng110-jack (name) (where to))
- `aws s3 rb s3://eng110-jack` - Removes the bucket (must be empty)
- `aws s3 rm s3://eng110-jack/test.txt` - Removes file `--recursive` at the end removes everything, keeps going until empty

#### Intalling boto3
- `pip3 install boto3`
- 

#### Setting permissions to access S3 files from AWS interface
- Search for S3 in search bar and select
- Select bucket
- Select file
- Select permissions tab
- Press Edit
- Change ACL and save


#### Setting up an S3 bucket from AWS interface


- Select create bucket option
- Assign a name
- Assign a region
- Enable or disable ACLs (Access control list) in object ownership
- Create bucket



`netstat -tulpn | grep PORT_NUMBER` - checks if the port is listening to X