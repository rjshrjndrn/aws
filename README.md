### AWS ec2 Instance create

**Options**
```
usage: aws_ec2.py [-h] [--create] [--start START] [--stop STOP]
                  [--terminate TERMINATE] [--status [STATUS]] [--size SIZE]
                  [--count COUNT] [--profile PROFILE] [--type TYPE]
                  [--image IMAGE] [--region REGION]
                  [--security_group SECURITY_GROUP]
                  [--assosiate_public_ip ASSOSIATE_PUBLIC_IP]
                  [--subnet_id SUBNET_ID] [--key_name KEY_NAME] [--tag TAG]
                  [--dryrun]

optional arguments:
  -h, --help            show this help message and exit
  --profile PROFILE     Profile of your AWS cli credentials, eg: for
                        [organization1] type --profile organization1 (default:
                        default)

Main Options:
  --create              Create instance with supplied args (default: False)
  --start START         comma seperated instance ids to start eg: --start
                        i-0ee0682f2112069bf,i-0ee0682f2112069ff (default:
                        None)
  --stop STOP           comma seperated instance ids to stop eg: --stop
                        i-0ee0682f2112069bf,i-0ee0682f2112069ff (default:
                        None)
  --terminate TERMINATE
                        comma seperated instance ids to terminate eg:
                        --terminate i-0ee0682f2112069bf,i-0ee0682f2112069ff
                        (default: None)
  --status [STATUS]     show status of all instances except terminated. use
                        comma seperated ids for a specific group instance
                        (default: )

EC2 create args:
  --size SIZE           size of the EBS disc in GB (default: 8)
  --count COUNT         number of instances you want (default: 1)
  --type TYPE           Instance type (default: t2.micro)
  --image IMAGE         os image id (default: ami-bec974d8)
  --region REGION       Region to use (default: None)
  --security_group SECURITY_GROUP
                        Security Group Name (default: )
  --assosiate_public_ip ASSOSIATE_PUBLIC_IP
                        assosiate public ip address ? True/False (default:
                        True)
  --subnet_id SUBNET_ID
                        subnet id, if you want to launch instance in a
                        specific vpc or subnet (default: )
  --key_name KEY_NAME   Key pair to login to the instance if not exist, then
                        create and save .pem in current working directory
                        (default: rajesh_test_key)
  --tag TAG             Name tag for the instance (default: test_rajesh)
  --dryrun

```
**Examples**

```
./aws_ec2.py --profile my_profile --count 2 --type t2.medium
