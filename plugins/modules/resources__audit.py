from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: resources__audit
short_description: Handle resource of type resources__audit
description: Handle resource of type resources__audit
options:
  domainId:
    description:
    - Identifier of the domain whose resources should be audited
    type: str
  exactTypeId:
    description:
    - Option to limit the audit to one or more resource types specified (takes precedence
      over resourceTypeId). Use a comma-separated string to specify multiple resource
      types.
    type: str
  p:
    description:
    - Optional query parameter to define a partial string match filter using property:value
      syntax
    type: str
  productId:
    description:
    - Identifier of the product whose resources should be audited
    type: str
  q:
    description:
    - Optional query parameter to define a query filter using property:value syntax
    type: str
  resourceProviderId:
    description:
    - Identifier of the provider whose resources should be audited
    type: str
  resourceTypeId:
    description:
    - Option to limit the audit to one or more resource types specified and their
      derived types. Use a comma-separated string to specify multiple resource types.
    type: str
  state:
    choices:
    - post
    description: []
    type: str
  tags:
    description:
    - Optional query parameter to define a tag filter using tagKey:tagValue syntax
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "domainId",
    "exactTypeId",
    "p",
    "productId",
    "q",
    "resourceProviderId",
    "resourceTypeId",
    "tags",
]
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
    argument_spec["tags"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["resourceProviderId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["q"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["p"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["exactTypeId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["domainId"] = {"type": "str", "operationIds": ["post"]}
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/resources/audit".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resources/audit".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
    async with session.post(_url) as resp:
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
