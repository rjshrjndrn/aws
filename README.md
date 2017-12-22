### AWS ec2 Instance create

*Main options*
```
➜  aws git:(master) ✗ ./aws_ec2.py -h
usage: aws_ec2.py [-h] [--create] [--start START] [--stop STOP]
                  [--terminate TERMINATE] [--status [STATUS]] [--count COUNT]
                  [--profile PROFILE] [--type TYPE] [--image IMAGE]
                  [--security_group SECURITY_GROUP]
                  [--assosiate_public_ip ASSOSIATE_PUBLIC_IP]
                  [--subnet_id SUBNET_ID] [--keyname KEYNAME] [--tag TAG]
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
  --count COUNT         number of instances you want (default: 1)
  --type TYPE           Instance type (default: t2.micro)
  --image IMAGE         os image id (default: ami-bec974d8)
  --security_group SECURITY_GROUP
                        Security Group Name (default: )
  --assosiate_public_ip ASSOSIATE_PUBLIC_IP
                        assosiate public ip address ? True/False (default:
                        True)
  --subnet_id SUBNET_ID
                        subnet id, if you want to launch instance in a
                        specific vpc or subnet (default: )
  --keyname KEYNAME     Key pair to login to the instance (default:
                        rajesh_test_key)
  --tag TAG             Name tag for the instance (default: test_rajesh)
  --dryrun
```
