#!/usr/bin/env python
# Info module template

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by
#   https://git.blueplanet.com/Ciena/nate/swagger_ansible_code_generator
#
# Do not edit this file manually.
#
# Changes should be made in the swagger used to
#   generate this file or in the generator
#
#############################################

from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: resources__validate
short_description: Handle resource of type resources__validate
description: Handle resource of type resources__validate
options:
  autoClean:
    description:
    - Free up any resources automatically upon any activation failure
    type: bool
  custom:
    description:
    - Whether to perform custom validation in addition to built-in schema and accessor
      validations
    type: bool
  description:
    description:
    - Detailed description of this resource
    type: str
  desiredOrchState:
    description:
    - Desired orchestration state
    type: str
  discovered:
    description:
    - Is this resource discovered
    type: bool
  full:
    description:
    - Whether the request body represents a full resource
    type: bool
  label:
    description:
    - Textual label
    type: str
  nativeState:
    description:
    - Native (type specific) state
    type: str
  orchState:
    description:
    - Current state of the resource in the orchestrator
    type: str
  orderId:
    description:
    - If applicable, the order containing this resource
    type: str
  productId:
    description:
    - The type of product for this resource
    type: str
  properties:
    description:
    - Properties
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerResourceId:
    description:
    - Identifier of the resource in provider's context
    type: str
  reason:
    description:
    - Reason for the orchestration state
    type: str
  shared:
    description:
    - Is resource shared?
    type: bool
  sharingPermissionId:
    description:
    - The sharing permission of the resource
    type: str
  state:
    choices:
    - post
    description: []
    type: str
  subDomainId:
    description:
    - Sub-domain ID
    type: str
  tags:
    description:
    - Tags
    type: dict
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["custom", "full"]
from ansible.module_utils.basic import env_fallback

try:
    from ansible_module.turbo.module import AnsibleTurboModule as AnsibleModule
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.mcp.plugins.module_utils.mcp import (
    gen_args,
    open_session,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "mcp_hostname": dict(
            type="str", required=False, fallback=(env_fallback, ["MCP_HOST"])
        ),
        "mcp_username": dict(
            type="str", required=False, fallback=(env_fallback, ["MCP_USER"])
        ),
        "mcp_password": dict(
            type="str",
            required=False,
            no_log=True,
            fallback=(env_fallback, ["MCP_PASSWORD"]),
        ),
    }
    argument_spec["tags"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["subDomainId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["sharingPermissionId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["shared"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["reason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerResourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orderId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["nativeState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["label"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["full"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["discovered"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["desiredOrchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["custom"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["autoClean"] = {"type": "bool", "operationIds": ["post"]}
    return argument_spec


async def get_device_info(params, session, _url, _key):
    async with session.get(((_url + "/") + _key)) as resp:
        _json = await resp.json()
        entry = _json["value"]
        entry["_key"] = _key
        return entry


async def list_devices(params, session):
    existing_entries = []
    _url = url(params)
    async with session.get(_url) as resp:
        _json = await resp.json()
        devices = _json["value"]
    for device in devices:
        _id = list(device.values())[0]
        existing_entries.append((await get_device_info(params, session, _url, _id)))
    return existing_entries


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        mcp_hostname=module.params["mcp_hostname"],
        mcp_username=module.params["mcp_username"],
        mcp_password=module.params["mcp_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):
    return "https://{mcp_hostname}/bpocore/market/api/v1/resources/validate".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "autoClean",
        "description",
        "desiredOrchState",
        "discovered",
        "label",
        "nativeState",
        "orchState",
        "orderId",
        "productId",
        "properties",
        "providerData",
        "providerResourceId",
        "reason",
        "shared",
        "sharingPermissionId",
        "subDomainId",
        "tags",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resources/validate".format(
        **params
    )
    async with session.post(_url, json=spec) as resp:
        content_types = [
            "application/json-patch+json",
            "application/vnd.api+json",
            "application/json",
        ]
        try:
            if resp.headers["Content-Type"] in content_types:
                _json = await resp.json()
            else:
                print("response Content-Type not supported")
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "post")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
