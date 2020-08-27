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
module: nsi__api__tpes___by_tpeId
short_description: Handle resource of type nsi__api__tpes___by_tpeId
description: Handle resource of type nsi__api__tpes___by_tpeId
options:
  data:
    description:
    - 'Validate attributes are:'
    - ' - C(attributes) (dict): '
    - ' - C(id) (str): The unique identifier for the TPE resource'
    - ' - C(meta) (dict): A metadata object that contains non-standard meta information'
    - ' - C(relationships) (dict): '
    - ' - C(type) (str): The TPE resource type'
    type: dict
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    type: str
  include:
    description:
    - '(Optional) List of comma separated resources to be side-loaded.  The allowed
      values are: expectations, tpePlanned, tpeDiscovered'
    type: str
  included:
    description:
    - Referenced sub-resources
    type: list
  meta:
    description:
    - A metadata object that contains non-standard meta information
    - 'Validate attributes are:'
    - ' - C(absoluteTotal) (int): The unfiltered total number of entities in the data'
    - ' - C(aggregations) (list): The aggregated data based on a requested aggregation
      name and criteria'
    - ' - C(filtered) (bool): Flags whether the current object is filtered using `fields`
      query param or not'
    - ' - C(missingReferenceIds) (list): The list of missing resource IDs'
    - ' - C(missingReferences) (bool): boolean detailing if the GET FRE tree has any
      missing references'
    - ' - C(total) (int): The total number of entities in the data'
    type: dict
  state:
    choices:
    - delete
    - get
    - put
    description: []
    type: str
  tpeId:
    description:
    - TPEResource identifier
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["fields", "include"]
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
    argument_spec["tpeId"] = {"type": "str", "operationIds": ["delete", "get", "put"]}
    argument_spec["state"] = {"type": "str", "choices": ["delete", "get", "put"]}
    argument_spec["meta"] = {"type": "dict", "operationIds": ["put"]}
    argument_spec["included"] = {"type": "list", "operationIds": ["put"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["data"] = {"type": "dict", "operationIds": ["put"]}
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
    return "https://{mcp_hostname}/nsi/api/tpes/{tpeId}".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{mcp_hostname}/nsi/api/tpes/{tpeId}".format(**params) + gen_args(
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
    _url = "https://{mcp_hostname}/nsi/api/tpes/{tpeId}".format(**params) + gen_args(
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


async def _put(params, session):
    accepted_fields = ["data", "included", "meta"]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/nsi/api/tpes/{tpeId}".format(**params)
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
