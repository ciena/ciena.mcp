from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: resources___by_resourceId__dependencies
short_description: Handle resource of type resources___by_resourceId__dependencies
description: Handle resource of type resources___by_resourceId__dependencies
options:
  applicationSliceId:
    description:
    - Optional query to limit resources by the application slice id.
    type: str
  domainId:
    description:
    - Optional query to limit resources by domain
    type: str
  exactTypeId:
    description:
    - Optional query to limit resources by one or more exact resource types (takes
      precedence over resourceTypeId). Use comma-separated string to specify multiple
      resource types.
    type: str
  limit:
    description:
    - The maximum number of elements to return in a single paged request
    type: int
  obfuscate:
    description:
    - If true, schema obfuscated values will be replaced with a fixed string in the
      response.
    type: bool
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
  productId:
    description:
    - Optional query to limit resources by product type
    type: str
  q:
    description:
    - Optional query parameter to define a query filter using property:value syntax
    type: str
  recursive:
    description:
    - If true, returns indirect dependencies as well, i.e., dependencies of the dependencies,
      etc.
    type: bool
  resourceId:
    description:
    - Identifies the resource for which dependency resources are searched
    type: str
  resourceProviderId:
    description:
    - Optional query to limit resources by resource provider
    type: str
  resourceTypeId:
    description:
    - Optional query to limit resources by one or more resource types. Use a comma-separated
      string to specify multiple resource types.
    type: str
  state:
    choices:
    - get
    - head
    description: []
    type: str
  subDomainId:
    description:
    - Optional query to limit resources by one or more subdomain ids. Use a comma-separated
      string to specify multiple subdomain ids.
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
    "applicationSliceId",
    "domainId",
    "exactTypeId",
    "limit",
    "obfuscate",
    "offset",
    "p",
    "pageToken",
    "productId",
    "q",
    "recursive",
    "resourceProviderId",
    "resourceTypeId",
    "subDomainId",
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
    argument_spec["tags"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["subDomainId"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "head"]}
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["resourceProviderId"] = {
        "type": "str",
        "operationIds": ["get", "head"],
    }
    argument_spec["resourceId"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["recursive"] = {"type": "bool", "operationIds": ["get", "head"]}
    argument_spec["q"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["pageToken"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["p"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["offset"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["obfuscate"] = {"type": "bool", "operationIds": ["get", "head"]}
    argument_spec["limit"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["exactTypeId"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["domainId"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["applicationSliceId"] = {
        "type": "str",
        "operationIds": ["get", "head"],
    }
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/dependencies".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/dependencies".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
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
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/dependencies".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
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


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
