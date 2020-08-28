

# Ciena MCP Collection

The Ansible Ciena MCP collection includes a variety of Ansible content to help automate the management of Ciena MCP network management system.

This collection has been tested against MCP 4.2

## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10,<2.11**.

## Included content

<!--start collection content-->

### Modules
Name | Description
--- | ---
[ciena.saos10.saos10_command](https://github.com/ciena/ciena.saos10/blob/main/docs/saos10_command.md)|Run commands on remote devices running Ciena SAOS 10
[ciena.saos10.saos10_facts](https://github.com/ciena/ciena.saos10/blob/main/docs/saos10_facts.md)|Collect facts from remote devices running Ciena SAOS 10

<!--end collection content-->
## Installing this collection

Install the Ciena MCP collection with the Ansible Galaxy CLI:

```bash
ansible-galaxy collection install ciena.mcp
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ciena.mcp
```

## Using this collection

### Using modules from the Ciena MCP collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `ciena.mcp.resources`.

```yaml
---
- name: playbook get vars for lab localhost facts
  import_playbook: lab_get_vars.yml
  when: hostvars['localhost'].lab_vars is not defined
- hosts:
  - localhost
  vars:
    devices:
    - 10.20.10.1
    - 10.20.10.2
    - 10.20.10.3
    - 10.20.10.4
    mcp_creds: &mcp_creds
      mcp_hostname: 10.10.10.10
      mcp_username: admin
      mcp_password: adminpw
  name: Enroll Devices in MCP
  collections:
  - ciena.mcp
  gather_facts: false
  tasks:
  - name: list getNEConnectionProfiles
    discovery_api_neprofiles:
      <<: *mcp_creds
      state: get
  - name: createNEConnectionProfile
    discovery_api_neprofiles:
      <<: *mcp_creds
      state: post
      data:
        type: neConnectionProfile
        attributes:
          name: saos10
          profileDescription: saos10
          typeGroup: "/typeGroups/PN10x"
          isEnabled: true
          isDefault: false
          protocolEndpoints:
            cli:
              connection:
                hostport: 22
              authentication:
                username: diag
                password: ciena123
            netconf:
              connection:
                hostport: 830
              authentication:
                username: diag
                password: ciena123
    register: connectionProfile
  - name: debug
    debug:
      var: connectionProfile
  - name: Create Management Session
    loop: "{{ devices }}"
    discovery_api_managementsessions:
      <<: *mcp_creds
      state: post
      data:
        attributes:
          ipAddress: "{{ devices }}"
          profile: "{{ connectionProfile.data.id }}"
          resourcePartitionInfo: []
          additionalIpAddresses: []
        type: managementSessions
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Ciena MCP collection repository](https://github.com/ciena/ciena.mcp).

Release is done automatically use Github Actions as part of merging to master.

## Changelogs

[CHANGELOG](CHANGELOG.md)

## Roadmap

* build a roadmap

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

See [LICENSE](LICENSE) to see the full text.

