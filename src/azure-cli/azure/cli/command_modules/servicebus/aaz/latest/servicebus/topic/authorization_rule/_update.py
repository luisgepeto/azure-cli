# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "servicebus topic authorization-rule update",
)
class Update(AAZCommand):
    """Update an authorization rule for the specified topic.

    :example: Create Authorization Rule for given Service Bus Topic.
        az servicebus topic authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name myauthorule --rights Send
    """

    _aaz_info = {
        "version": "2022-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicebus/namespaces/{}/topics/{}/authorizationrules/{}", "2022-01-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.authorization_rule_name = AAZStrArg(
            options=["-n", "--name", "--authorization-rule-name"],
            help="The authorization rule name.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=1,
            ),
        )
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The namespace name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.topic_name = AAZStrArg(
            options=["--topic-name"],
            help="The topic name.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.rights = AAZListArg(
            options=["--rights"],
            arg_group="Properties",
            help="The rights associated with the rule.",
        )

        rights = cls._args_schema.rights
        rights.Element = AAZStrArg(
            nullable=True,
            enum={"Listen": "Listen", "Manage": "Manage", "Send": "Send"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.TopicsGetAuthorizationRule(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.TopicsCreateOrUpdateAuthorizationRule(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class TopicsGetAuthorizationRule(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "authorizationRuleName", self.ctx.args.authorization_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "topicName", self.ctx.args.topic_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_sb_authorization_rule_read(cls._schema_on_200)

            return cls._schema_on_200

    class TopicsCreateOrUpdateAuthorizationRule(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "authorizationRuleName", self.ctx.args.authorization_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "topicName", self.ctx.args.topic_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_sb_authorization_rule_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("rights", AAZListType, ".rights", typ_kwargs={"flags": {"required": True}})

            rights = _builder.get(".properties.rights")
            if rights is not None:
                rights.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_sb_authorization_rule_read = None

    @classmethod
    def _build_schema_sb_authorization_rule_read(cls, _schema):
        if cls._schema_sb_authorization_rule_read is not None:
            _schema.id = cls._schema_sb_authorization_rule_read.id
            _schema.location = cls._schema_sb_authorization_rule_read.location
            _schema.name = cls._schema_sb_authorization_rule_read.name
            _schema.properties = cls._schema_sb_authorization_rule_read.properties
            _schema.system_data = cls._schema_sb_authorization_rule_read.system_data
            _schema.type = cls._schema_sb_authorization_rule_read.type
            return

        cls._schema_sb_authorization_rule_read = _schema_sb_authorization_rule_read = AAZObjectType()

        sb_authorization_rule_read = _schema_sb_authorization_rule_read
        sb_authorization_rule_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sb_authorization_rule_read.location = AAZStrType(
            flags={"read_only": True},
        )
        sb_authorization_rule_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sb_authorization_rule_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        sb_authorization_rule_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        sb_authorization_rule_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sb_authorization_rule_read.properties
        properties.rights = AAZListType(
            flags={"required": True},
        )

        rights = _schema_sb_authorization_rule_read.properties.rights
        rights.Element = AAZStrType()

        system_data = _schema_sb_authorization_rule_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_sb_authorization_rule_read.id
        _schema.location = cls._schema_sb_authorization_rule_read.location
        _schema.name = cls._schema_sb_authorization_rule_read.name
        _schema.properties = cls._schema_sb_authorization_rule_read.properties
        _schema.system_data = cls._schema_sb_authorization_rule_read.system_data
        _schema.type = cls._schema_sb_authorization_rule_read.type


__all__ = ["Update"]
