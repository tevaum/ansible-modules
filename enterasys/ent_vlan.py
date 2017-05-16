#!/usr/bin/python

from ansible.module_utils.network import NetworkModule, NetworkError
from ansible.module_utils.netcli import CommandRunner

def main():
    spec = dict(
        host=dict(required=False),
        vlan_id=dict(required=True, type='str'),
        name=dict(required=False),
        state=dict(choices=['present', 'absent'], default='present', required=False)
    )

    module = NetworkModule(argument_spec=spec)

    module.exit_json({changed: False, "huvs": "nivs"})

if __name__ == '__main__':
    main()
