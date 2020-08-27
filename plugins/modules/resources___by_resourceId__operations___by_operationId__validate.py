from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: resources___by_resourceId__operations___by_operationId__validate
short_description: Handle resource of type resources___by_resourceId__operations___by_operationId__validate
description: Handle resource of type resources___by_resourceId__operations___by_operationId__validate
options:
  createdAt:
    description:
    - When the operation was created
    type: str
  description:
    description:
    - Description of the operation
    type: str
  executionGroup:
    description:
    - Execution group of the operation
    type: str
  id:
    description:
    - Unique identifier for the operation
    type: str
  inputs:
    description:
    - Inputs of the operation
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  interface:
    description:
    - ID of the interface
    type: str
  method:
    choices:
    - PATCH
    - PUT
    description:
    - The HTTP method for the resource operation to be validated against
    type: str
  operationId:
    description:
    - Identifier of the operation to be changed
    type: str
  outputs:
    description:
    - Outputs of the operation
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  progress:
    description:
    - Describes any progress towards completion that the operation has made
    - 'Validate attributes are:'
    - ' - C(arr) (list): '
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  reason:
    description:
    - Reason for the operation state
    type: str
  resourceId:
    description:
    - Identifier of the resource being validated against
    type: str
  resourceStateConstraints:
    description:
    - Constraints of the resource state for this operation to execute
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  revision:
    description:
    - Strictly increasing revision number, incremented every update
    type: int
  state:
    choices:
    - post
    description: []
    type: str
  title:
    description:
    - Title of the operation
    type: str
  updatedAt:
    description:
    - When the operation was last updated
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["method"]
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
    argument_spec["updatedAt"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["title"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["revision"] = {"type": "int", "operationIds": ["post"]}
    argument_spec["resourceStateConstraints"] = {
        "type": "dict",
        "operationIds": ["post"],
    }
    argument_spec["resourceId"] = {"type": "str", "operationIds": ["post", "post"]}
    argument_spec["reason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["progress"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["outputs"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["operationId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["method"] = {
        "type": "str",
        "choices": ["PATCH", "PUT"],
        "operationIds": ["post"],
    }
    argument_spec["interface"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["inputs"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["executionGroup"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["createdAt"] = {"type": "str", "operationIds": ["post"]}
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}/validate".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "createdAt",
        "description",
        "executionGroup",
        "id",
        "inputs",
        "interface",
        "outputs",
        "progress",
        "providerData",
        "reason",
        "resourceId",
        "resourceStateConstraints",
        "revision",
        "title",
        "updatedAt",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}/validate".format(
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
