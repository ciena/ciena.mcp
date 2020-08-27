from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: domains
short_description: Handle resource of type domains
description: Handle resource of type domains
options:
  accessUrl:
    description:
    - Access URL to the domain
    type: str
  address:
    description:
    - Address of the domain
    - 'Validate attributes are:'
    - ' - C(city) (str): City'
    - ' - C(country) (str): Country'
    - ' - C(latitude) (number): Latitude'
    - ' - C(longitude) (number): Longitude'
    - ' - C(state) (str): State/province'
    - ' - C(street) (str): Street'
    - ' - C(zip) (str): Postal/zip code'
    type: dict
  description:
    description:
    - Detailed description
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
  onlyEnableTypes:
    description:
    - When non-empty, only enable these resource types in the domain
    type: list
  operationMode:
    description:
    - Operation mode of this domain
    type: str
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
  properties:
    description:
    - Properties the domain
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  q:
    description:
    - Optional query parameter to define a query filter using property:value syntax
    type: str
  rpId:
    description:
    - Resource provider managing this domain
    type: str
  state:
    choices:
    - get
    - head
    - post
    description: []
    type: str
  tenantId:
    description:
    - Orchestrator tenant ID for the domain owner (if unspecified defaults to requester)
    type: str
  title:
    description:
    - Descriptive name/title of domain
    type: str
  validate:
    description:
    - Whether to use a custom validator
    type: bool
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["limit", "obfuscate", "offset", "p", "pageToken", "q", "validate"]
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
    argument_spec["validate"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["title"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["tenantId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "head", "post"]}
    argument_spec["rpId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["q"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["pageToken"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["p"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["operationMode"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["onlyEnableTypes"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["offset"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["obfuscate"] = {
        "type": "bool",
        "operationIds": ["get", "head", "post"],
    }
    argument_spec["limit"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["address"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["accessUrl"] = {"type": "str", "operationIds": ["post"]}
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/domains".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/domains".format(
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
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/domains".format(
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
        "accessUrl",
        "address",
        "description",
        "onlyEnableTypes",
        "operationMode",
        "properties",
        "rpId",
        "tenantId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/domains".format(**params)
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
