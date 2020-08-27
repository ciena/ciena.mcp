

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

This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the Ciena MCP collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `ciena.mcp.saos10_command`.
The following example task replaces configuration changes in the existing configuration on a Ciena SAOS 10 network device, using the FQCN:

```yaml
---
  - name: Execute SAOS 10 commands
    ciena.saos10.saos10_command:
      commands:
      - software show
  - name: Set port config
    ciena.saos10.saos10_command:
      commands:
      - config
      - oc-if:interfaces interface 2 config name 2 description myport
      - exit
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

