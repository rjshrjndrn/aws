#!/usr/bin/python3

from boto3 import Session
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from getpass import getuser
from time import sleep

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

main_opts = parser.add_argument_group('Main Options')
ec2_group = parser.add_argument_group('EC2 create args')

main_opts.add_argument('--create',
        action='store_true',
        help='Create instance with supplied args')

main_opts.add_argument('--start',
        type=str,
        help='comma seperated instance ids to start \
                eg: --start i-0ee0682f2112069bf,i-0ee0682f2112069ff')

main_opts.add_argument('--stop',
        type=str,
        help='comma seperated instance ids to stop \
                eg: --stop i-0ee0682f2112069bf,i-0ee0682f2112069ff')

main_opts.add_argument('--terminate',
        type=str,
        help='comma seperated instance ids to terminate \
                eg: --terminate i-0ee0682f2112069bf,i-0ee0682f2112069ff')

main_opts.add_argument('--status',
        type=str,
        default='',
        const='all',
        action='store',
        nargs='?',
        help='show status of all instances except terminated. \
                use comma seperated ids for a specific group instance')

ec2_group.add_argument('--count',
        default=1,
        type=int,
        help='number of instances you want')

parser.add_argument('--profile',
        default='default',
        type=str,
        help='Profile of your AWS cli credentials, \
        eg: for [organization1] type --profile organization1')

# Arguments related to ec2
ec2_group.add_argument('--type',
        default='t2.micro',
        type=str,
        help='Instance type')

ec2_group.add_argument('--image',
        default='ami-bec974d8', # Ubuntu16.04 Instance ID
        type=str,
        help='os image id')

ec2_group.add_argument('--region',
        type=str,
        help='Region to use')

ec2_group.add_argument('--security_group',
        default='',
        type=str,
        help='Security Group Name')

ec2_group.add_argument('--assosiate_public_ip',
        default=True,
        type=bool,
        help='assosiate public ip address ? True/False')

ec2_group.add_argument('--subnet_id',
        default='',
        type=str,
        help='subnet id, if you want to launch instance in a specific vpc or subnet')

ec2_group.add_argument('--key_name',
        default='rajesh_test_key', # My test key
        type=str,
        help='Key pair to login to the instance \
                if not exist, then create and save .pem in current working directory')

ec2_group.add_argument('--tag',
        default='test_'+getuser(), # My user name
        type=str,
        help='Name tag for the instance')

ec2_group.add_argument('--dryrun',
        action='store_true')

args = parser.parse_args()
s = Session(profile_name=args.profile)
if not args.region:
    ec2 = s.resource('ec2')
else:
    ec2 = s.resource('ec2',region_name=args.region)

# Dynamic network config
# If you don't care about subnets and vpcs and want to use all by default
if not args.subnet_id and not args.security_group:
    network_interfaces ={ 'AssociatePublicIpAddress': args.assosiate_public_ip,
                            'DeviceIndex': 0,
                        }
else:
    network_interfaces = { 'AssociatePublicIpAddress': args.assosiate_public_ip,
                            'DeviceIndex': 0,
                            'SubnetId': args.subnet_id,
                            'Groups': [
                                args.security_group,    
                            ],
                        }

# Creating key pair
if args.key_name:
    try:
        key_pair = ec2.create_key_pair(KeyName=args.key_name)
        with open(args.key_name+'.pem','a') as key:
            key.write(key_pair.key_material)
        print(args.key_name+'created and .pem saved in current working directory')
    except Exception as e:
        print("Key: {} exists".format(args.key_name))

# status of Instances
def status(instance_id):
    if not instance_id:
        pass
    elif instance_id=='all':
        for i in ec2.instances.all():
            # skipping all terminated instances
            if i.private_ip_address:
                print('\n{}\n{}\nName: {}\nStatus: {}\npublic ip: {}\nprivate ip: {}'.format(i.id, '*'*len(i.id),
                    i.tags[0]['Value'], i.state['Name'], i.public_ip_address, i.private_ip_address))
    else:
        instances = instance_id.split(',')
        for inst in instances:
            i = ec2.Instance(id=inst)
            print('\n{}\n{}\nName: {}\nStatus: {}\npublic ip: {}\nprivate ip: {}'.format(i.id, '*'*len(i.id),
                i.tags[0]['Value'], i.state['Name'], i.public_ip_address, i.private_ip_address))

# Creating instances
if args.create:
    print('Creating {} Instances of {} with {}.Please use {} key' \
        .format(args.count, args.type,args.image,args.key_name))
    try:
        instance = ec2.create_instances(ImageId=args.image,
                    InstanceType=args.type,
                    KeyName=args.key_name,
                    MinCount=1, MaxCount=args.count,
                    TagSpecifications=[{
                        'ResourceType': 'instance',
                        'Tags':[{
                            'Key': 'Name',
                            'Value': args.tag
                            },
                        ]
                        },
                    ],
                    NetworkInterfaces=[network_interfaces],
                    DryRun=args.dryrun,
                )
        sleep(5)
        for i in instance:
            status(i.id)
    except Exception as e:
        print(e)

# Checking status
if args.status:
    status(args.status)

# Changing ec2 to client for low level access
# ie, start/stop/terminate
if not args.region:
    ec2 = s.client('ec2')
else:
    ec2 = s.client('ec2', region_name=args.region)

if args.start:
    instances = args.start.split(',')
    ec2.start_instances(InstanceIds=instances)
    
if args.stop:
    instances = args.stop.split(',')
    ec2.stop_instances(InstanceIds=instances)

if args.terminate:
    instances = args.terminate.split(',')
    ec2.terminate_instances(InstanceIds=instances)
