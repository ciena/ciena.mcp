from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: resource_providers___by_resourceProviderId
short_description: Handle resource of type resource_providers___by_resourceProviderId
description: Handle resource of type resource_providers___by_resourceProviderId
options:
  asyncProtocolVersion:
    description:
    - Identifies the async protocol version supported by the resource provider
    type: str
  description:
    description:
    - Description of the resource provider
    type: str
  domainSettings:
    description:
    - Domain level setting for the resource provider
    - 'Validate attributes are:'
    - ' - C(asyncDeviceTypes) (list): Specifies the Resource Type IDs that use async
      discovery strategy'
    - ' - C(connection_status) (bool): Specifies if maintenance of domain''s connection
      status is supported'
    - ' - C(initial_discovery_status) (bool): Specifies if maintenance of domain''s
      initial discovery status is supported'
    - ' - C(metaInfoDiscoveryStrategy) (dict): Specifies the Domain meta information
      polling strategy'
    - ' - C(minInterUpsertIntervalMs) (number): Specifies the minimal inter-call interval
      bpocore should honor when upserting the Domain'
    - ' - C(rpType) (dict): Specifies the RP Type'
    type: dict
  domainType:
    description:
    - Type of domain managed by the resource provider
    type: str
  id:
    description:
    - Unique identifier to address the resource provider
    type: str
  lastUpsertTime:
    description:
    - Last time the resource provider is upserted in the database
    type: str
  properties:
    description:
    - Properties of the resource provider
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  protocolVersion:
    description:
    - Identifies the protocol version supported by the resource provider
    type: str
  providerId:
    description:
    - Identifier of the resource provider in provider's context
    type: str
  relationships:
    description:
    - Settings to declare how relationships should be identified for resource types
      managed by this resource provider
    type: list
  resourceProviderId:
    description:
    - Identifier of the requested resource provider
    type: str
  resourceTypes:
    description:
    - List of resource types managed by the resource provider
    type: list
  state:
    choices:
    - delete
    - get
    - head
    - patch
    - put
    description: []
    type: str
  title:
    description:
    - Name of the resource provider
    type: str
  uri:
    description:
    - Address to contact the resource provider
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = []
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
    argument_spec["uri"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["title"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["resourceTypes"] = {"type": "list", "operationIds": ["patch", "put"]}
    argument_spec["resourceProviderId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["relationships"] = {"type": "list", "operationIds": ["patch", "put"]}
    argument_spec["providerId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["protocolVersion"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["lastUpsertTime"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["domainType"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["domainSettings"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["asyncProtocolVersion"] = {
        "type": "str",
        "operationIds": ["patch", "put"],
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/resource-providers/{resourceProviderId}".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resource-providers/{resourceProviderId}".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
    async with session.delete(_url) as resp:
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
        return await update_changed_flag(_json, resp.status, "delete")


async def _get(params, session):
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resource-providers/{resourceProviderId}".format(
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
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resource-providers/{resourceProviderId}".format(
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


async def _patch(params, session):
    accepted_fields = [
        "asyncProtocolVersion",
        "description",
        "domainSettings",
        "domainType",
        "id",
        "lastUpsertTime",
        "properties",
        "protocolVersion",
        "providerId",
        "relationships",
        "resourceTypes",
        "title",
        "uri",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resource-providers/{resourceProviderId}".format(
        **params
    )
    async with session.patch(_url, json=spec) as resp:
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
        return await update_changed_flag(_json, resp.status, "patch")


async def _put(params, session):
    accepted_fields = [
        "asyncProtocolVersion",
        "description",
        "domainSettings",
        "domainType",
        "id",
        "lastUpsertTime",
        "properties",
        "protocolVersion",
        "providerId",
        "relationships",
        "resourceTypes",
        "title",
        "uri",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resource-providers/{resourceProviderId}".format(
        **params
    )
    async with session.put(_url, json=spec) as resp:
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
        return await update_changed_flag(_json, resp.status, "put")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
