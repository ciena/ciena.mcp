# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Ciena
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment(object):
    # Parameters for MCP REST Client based modules
    DOCUMENTATION = r"""
options:
  hostname:
    description:
    - The hostname or IP address of the MCP server.
    - If the value is not specified in the task, the value of environment variable C(MCP_HOST) will be used instead.
    type: str
  username:
    description:
    - The username of the MCP server.
    - If the value is not specified in the task, the value of environment variable C(MCP_USER) will be used instead.
    type: str
    aliases: [ admin, user ]
  password:
    description:
    - The password of the MCP server.
    - If the value is not specified in the task, the value of environment variable C(MCP_PASSWORD) will be used instead.
    type: str
    aliases: [ pass, pwd ]
  validate_certs:
    description:
    - Allows connection when SSL certificates are not valid.
    - Set to C(no) when certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable C(MCP_VALIDATE_CERTS) will be used instead.
    type: bool
    default: yes
  protocol:
    description:
    - The connection to protocol.
    type: str
    choices: [ http, https ]
    default: https
"""
