from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: products
short_description: Handle resource of type products
description: Handle resource of type products
options:
  active:
    description:
    - State of the product (active or inactive)
    type: bool
  constraints:
    description:
    - Additional constraints for the product
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  description:
    description:
    - Detailed description of the product
    type: str
  domainId:
    description:
    - Identifier of the domain that advertises the product
    type: str
  id:
    description:
    - Unique identifier of the product (ignored during create request)
    type: str
  includeInactive:
    description:
    - If false, returns only products that are actively offered; if true, returns
      all products
    type: bool
  limit:
    description:
    - The maximum number of elements to return in a single paged request
    type: int
  offset:
    description:
    - Requested offset within the total result set to be the first element in the
      paged response
    type: int
  p:
    description:
    - Optional query parameter to define a partial string match filter using property:value
      syntax
    type: str
  pageToken:
    description:
    - String pagination token returned from a previous query that encodes query information
      in order to optimize a
    - subsequent request for a page of results. The token includes the limit and offset
      parameters for the next page, but one or
    - both can be included to override the encoded values
    type: str
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerProductId:
    description:
    - Identifier within the provider's context or scope for the product
    type: str
  q:
    description:
    - Optional query parameter to define a query filter using property:value syntax
    type: str
  resourceTypeId:
    description:
    - The type of resource provided by the product
    type: str
  state:
    choices:
    - get
    - head
    - post
    description: []
    type: str
  title:
    description:
    - Name or title describing the product
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["includeInactive", "limit", "offset", "p", "pageToken", "q"]
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
    argument_spec["title"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "head", "post"]}
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["q"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["providerProductId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["pageToken"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["p"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["offset"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["limit"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["includeInactive"] = {"type": "bool", "operationIds": ["get", "head"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["domainId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["constraints"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["active"] = {"type": "bool", "operationIds": ["post"]}
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/products".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/products".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
    async with session.get(_url) as resp:
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
        return await update_changed_flag(_json, resp.status, "get")


async def _head(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/products".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
    async with session.head(_url) as resp:
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
        return await update_changed_flag(_json, resp.status, "head")


async def _post(params, session):
    accepted_fields = [
        "active",
        "constraints",
        "description",
        "domainId",
        "id",
        "providerData",
        "providerProductId",
        "resourceTypeId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/products".format(**params)
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
