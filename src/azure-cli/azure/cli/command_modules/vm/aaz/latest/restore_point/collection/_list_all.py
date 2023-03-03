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
    "restore-point collection list-all",
)
class ListAll(AAZCommand):
    """Get the list of restore point collections in the subscription. Use nextLink property in the response to get the next page of restore point collections. Do this till nextLink is not null to fetch all the restore point collections.

    :example: Get the list of restore point collections in a subscription.
        az restore-point collection list-all
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.compute/restorepointcollections", "2022-11-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RestorePointCollectionsListAll(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class RestorePointCollectionsListAll(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/restorePointCollections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.restore_point_collection_id = AAZStrType(
                serialized_name="restorePointCollectionId",
                flags={"read_only": True},
            )
            properties.restore_points = AAZListType(
                serialized_name="restorePoints",
                flags={"read_only": True},
            )
            properties.source = AAZObjectType()

            restore_points = cls._schema_on_200.value.Element.properties.restore_points
            restore_points.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.restore_points.Element.properties
            properties.consistency_mode = AAZStrType(
                serialized_name="consistencyMode",
            )
            properties.exclude_disks = AAZListType(
                serialized_name="excludeDisks",
            )
            properties.instance_view = AAZObjectType(
                serialized_name="instanceView",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_metadata = AAZObjectType(
                serialized_name="sourceMetadata",
            )
            properties.source_restore_point = AAZObjectType(
                serialized_name="sourceRestorePoint",
            )
            _ListAllHelper._build_schema_api_entity_reference_read(properties.source_restore_point)
            properties.time_created = AAZStrType(
                serialized_name="timeCreated",
            )

            exclude_disks = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.exclude_disks
            exclude_disks.Element = AAZObjectType()
            _ListAllHelper._build_schema_api_entity_reference_read(exclude_disks.Element)

            instance_view = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.instance_view
            instance_view.disk_restore_points = AAZListType(
                serialized_name="diskRestorePoints",
            )
            instance_view.statuses = AAZListType()

            disk_restore_points = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.instance_view.disk_restore_points
            disk_restore_points.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.instance_view.disk_restore_points.Element
            _element.id = AAZStrType()
            _element.replication_status = AAZObjectType(
                serialized_name="replicationStatus",
            )

            replication_status = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.instance_view.disk_restore_points.Element.replication_status
            replication_status.completion_percent = AAZIntType(
                serialized_name="completionPercent",
            )
            replication_status.status = AAZObjectType()
            _ListAllHelper._build_schema_instance_view_status_read(replication_status.status)

            statuses = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.instance_view.statuses
            statuses.Element = AAZObjectType()
            _ListAllHelper._build_schema_instance_view_status_read(statuses.Element)

            source_metadata = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata
            source_metadata.diagnostics_profile = AAZObjectType(
                serialized_name="diagnosticsProfile",
            )
            source_metadata.hardware_profile = AAZObjectType(
                serialized_name="hardwareProfile",
            )
            source_metadata.license_type = AAZStrType(
                serialized_name="licenseType",
            )
            source_metadata.location = AAZStrType()
            source_metadata.os_profile = AAZObjectType(
                serialized_name="osProfile",
            )
            source_metadata.security_profile = AAZObjectType(
                serialized_name="securityProfile",
            )
            source_metadata.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )
            source_metadata.user_data = AAZStrType(
                serialized_name="userData",
            )
            source_metadata.vm_id = AAZStrType(
                serialized_name="vmId",
            )

            diagnostics_profile = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.diagnostics_profile
            diagnostics_profile.boot_diagnostics = AAZObjectType(
                serialized_name="bootDiagnostics",
            )

            boot_diagnostics = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.diagnostics_profile.boot_diagnostics
            boot_diagnostics.enabled = AAZBoolType()
            boot_diagnostics.storage_uri = AAZStrType(
                serialized_name="storageUri",
            )

            hardware_profile = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.hardware_profile
            hardware_profile.vm_size = AAZStrType(
                serialized_name="vmSize",
            )
            hardware_profile.vm_size_properties = AAZObjectType(
                serialized_name="vmSizeProperties",
            )

            vm_size_properties = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.hardware_profile.vm_size_properties
            vm_size_properties.v_cp_us_available = AAZIntType(
                serialized_name="vCPUsAvailable",
            )
            vm_size_properties.v_cp_us_per_core = AAZIntType(
                serialized_name="vCPUsPerCore",
            )

            os_profile = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile
            os_profile.admin_password = AAZStrType(
                serialized_name="adminPassword",
            )
            os_profile.admin_username = AAZStrType(
                serialized_name="adminUsername",
            )
            os_profile.allow_extension_operations = AAZBoolType(
                serialized_name="allowExtensionOperations",
            )
            os_profile.computer_name = AAZStrType(
                serialized_name="computerName",
            )
            os_profile.custom_data = AAZStrType(
                serialized_name="customData",
            )
            os_profile.linux_configuration = AAZObjectType(
                serialized_name="linuxConfiguration",
            )
            os_profile.require_guest_provision_signal = AAZBoolType(
                serialized_name="requireGuestProvisionSignal",
            )
            os_profile.secrets = AAZListType()
            os_profile.windows_configuration = AAZObjectType(
                serialized_name="windowsConfiguration",
            )

            linux_configuration = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.linux_configuration
            linux_configuration.disable_password_authentication = AAZBoolType(
                serialized_name="disablePasswordAuthentication",
            )
            linux_configuration.enable_vm_agent_platform_updates = AAZBoolType(
                serialized_name="enableVMAgentPlatformUpdates",
            )
            linux_configuration.patch_settings = AAZObjectType(
                serialized_name="patchSettings",
            )
            linux_configuration.provision_vm_agent = AAZBoolType(
                serialized_name="provisionVMAgent",
            )
            linux_configuration.ssh = AAZObjectType()

            patch_settings = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.linux_configuration.patch_settings
            patch_settings.assessment_mode = AAZStrType(
                serialized_name="assessmentMode",
            )
            patch_settings.automatic_by_platform_settings = AAZObjectType(
                serialized_name="automaticByPlatformSettings",
            )
            patch_settings.patch_mode = AAZStrType(
                serialized_name="patchMode",
            )

            automatic_by_platform_settings = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.linux_configuration.patch_settings.automatic_by_platform_settings
            automatic_by_platform_settings.reboot_setting = AAZStrType(
                serialized_name="rebootSetting",
            )

            ssh = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.linux_configuration.ssh
            ssh.public_keys = AAZListType(
                serialized_name="publicKeys",
            )

            public_keys = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.linux_configuration.ssh.public_keys
            public_keys.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.linux_configuration.ssh.public_keys.Element
            _element.key_data = AAZStrType(
                serialized_name="keyData",
            )
            _element.path = AAZStrType()

            secrets = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.secrets
            secrets.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.secrets.Element
            _element.source_vault = AAZObjectType(
                serialized_name="sourceVault",
            )
            _ListAllHelper._build_schema_sub_resource_read(_element.source_vault)
            _element.vault_certificates = AAZListType(
                serialized_name="vaultCertificates",
            )

            vault_certificates = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.secrets.Element.vault_certificates
            vault_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.secrets.Element.vault_certificates.Element
            _element.certificate_store = AAZStrType(
                serialized_name="certificateStore",
            )
            _element.certificate_url = AAZStrType(
                serialized_name="certificateUrl",
            )

            windows_configuration = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration
            windows_configuration.additional_unattend_content = AAZListType(
                serialized_name="additionalUnattendContent",
            )
            windows_configuration.enable_automatic_updates = AAZBoolType(
                serialized_name="enableAutomaticUpdates",
            )
            windows_configuration.enable_vm_agent_platform_updates = AAZBoolType(
                serialized_name="enableVMAgentPlatformUpdates",
            )
            windows_configuration.patch_settings = AAZObjectType(
                serialized_name="patchSettings",
            )
            windows_configuration.provision_vm_agent = AAZBoolType(
                serialized_name="provisionVMAgent",
            )
            windows_configuration.time_zone = AAZStrType(
                serialized_name="timeZone",
            )
            windows_configuration.win_rm = AAZObjectType(
                serialized_name="winRM",
            )

            additional_unattend_content = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.additional_unattend_content
            additional_unattend_content.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.additional_unattend_content.Element
            _element.component_name = AAZStrType(
                serialized_name="componentName",
            )
            _element.content = AAZStrType()
            _element.pass_name = AAZStrType(
                serialized_name="passName",
            )
            _element.setting_name = AAZStrType(
                serialized_name="settingName",
            )

            patch_settings = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.patch_settings
            patch_settings.assessment_mode = AAZStrType(
                serialized_name="assessmentMode",
            )
            patch_settings.automatic_by_platform_settings = AAZObjectType(
                serialized_name="automaticByPlatformSettings",
            )
            patch_settings.enable_hotpatching = AAZBoolType(
                serialized_name="enableHotpatching",
            )
            patch_settings.patch_mode = AAZStrType(
                serialized_name="patchMode",
            )

            automatic_by_platform_settings = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.patch_settings.automatic_by_platform_settings
            automatic_by_platform_settings.reboot_setting = AAZStrType(
                serialized_name="rebootSetting",
            )

            win_rm = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.win_rm
            win_rm.listeners = AAZListType()

            listeners = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.win_rm.listeners
            listeners.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.os_profile.windows_configuration.win_rm.listeners.Element
            _element.certificate_url = AAZStrType(
                serialized_name="certificateUrl",
            )
            _element.protocol = AAZStrType()

            security_profile = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.security_profile
            security_profile.encryption_at_host = AAZBoolType(
                serialized_name="encryptionAtHost",
            )
            security_profile.security_type = AAZStrType(
                serialized_name="securityType",
            )
            security_profile.uefi_settings = AAZObjectType(
                serialized_name="uefiSettings",
            )

            uefi_settings = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.security_profile.uefi_settings
            uefi_settings.secure_boot_enabled = AAZBoolType(
                serialized_name="secureBootEnabled",
            )
            uefi_settings.v_tpm_enabled = AAZBoolType(
                serialized_name="vTpmEnabled",
            )

            storage_profile = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile
            storage_profile.data_disks = AAZListType(
                serialized_name="dataDisks",
            )
            storage_profile.os_disk = AAZObjectType(
                serialized_name="osDisk",
            )

            data_disks = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile.data_disks
            data_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile.data_disks.Element
            _element.caching = AAZStrType()
            _element.disk_restore_point = AAZObjectType(
                serialized_name="diskRestorePoint",
            )
            _ListAllHelper._build_schema_api_entity_reference_read(_element.disk_restore_point)
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            _element.lun = AAZIntType()
            _element.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListAllHelper._build_schema_managed_disk_parameters_read(_element.managed_disk)
            _element.name = AAZStrType()

            os_disk = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile.os_disk
            os_disk.caching = AAZStrType()
            os_disk.disk_restore_point = AAZObjectType(
                serialized_name="diskRestorePoint",
            )
            _ListAllHelper._build_schema_api_entity_reference_read(os_disk.disk_restore_point)
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            os_disk.encryption_settings = AAZObjectType(
                serialized_name="encryptionSettings",
            )
            os_disk.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListAllHelper._build_schema_managed_disk_parameters_read(os_disk.managed_disk)
            os_disk.name = AAZStrType()
            os_disk.os_type = AAZStrType(
                serialized_name="osType",
            )

            encryption_settings = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile.os_disk.encryption_settings
            encryption_settings.disk_encryption_key = AAZObjectType(
                serialized_name="diskEncryptionKey",
            )
            encryption_settings.enabled = AAZBoolType()
            encryption_settings.key_encryption_key = AAZObjectType(
                serialized_name="keyEncryptionKey",
            )

            disk_encryption_key = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile.os_disk.encryption_settings.disk_encryption_key
            disk_encryption_key.secret_url = AAZStrType(
                serialized_name="secretUrl",
                flags={"required": True},
            )
            disk_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _ListAllHelper._build_schema_sub_resource_read(disk_encryption_key.source_vault)

            key_encryption_key = cls._schema_on_200.value.Element.properties.restore_points.Element.properties.source_metadata.storage_profile.os_disk.encryption_settings.key_encryption_key
            key_encryption_key.key_url = AAZStrType(
                serialized_name="keyUrl",
                flags={"required": True},
            )
            key_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _ListAllHelper._build_schema_sub_resource_read(key_encryption_key.source_vault)

            source = cls._schema_on_200.value.Element.properties.source
            source.id = AAZStrType()
            source.location = AAZStrType(
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListAllHelper:
    """Helper class for ListAll"""

    _schema_api_entity_reference_read = None

    @classmethod
    def _build_schema_api_entity_reference_read(cls, _schema):
        if cls._schema_api_entity_reference_read is not None:
            _schema.id = cls._schema_api_entity_reference_read.id
            return

        cls._schema_api_entity_reference_read = _schema_api_entity_reference_read = AAZObjectType()

        api_entity_reference_read = _schema_api_entity_reference_read
        api_entity_reference_read.id = AAZStrType()

        _schema.id = cls._schema_api_entity_reference_read.id

    _schema_disk_encryption_set_parameters_read = None

    @classmethod
    def _build_schema_disk_encryption_set_parameters_read(cls, _schema):
        if cls._schema_disk_encryption_set_parameters_read is not None:
            _schema.id = cls._schema_disk_encryption_set_parameters_read.id
            return

        cls._schema_disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read = AAZObjectType()

        disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read
        disk_encryption_set_parameters_read.id = AAZStrType()

        _schema.id = cls._schema_disk_encryption_set_parameters_read.id

    _schema_instance_view_status_read = None

    @classmethod
    def _build_schema_instance_view_status_read(cls, _schema):
        if cls._schema_instance_view_status_read is not None:
            _schema.code = cls._schema_instance_view_status_read.code
            _schema.display_status = cls._schema_instance_view_status_read.display_status
            _schema.level = cls._schema_instance_view_status_read.level
            _schema.message = cls._schema_instance_view_status_read.message
            _schema.time = cls._schema_instance_view_status_read.time
            return

        cls._schema_instance_view_status_read = _schema_instance_view_status_read = AAZObjectType()

        instance_view_status_read = _schema_instance_view_status_read
        instance_view_status_read.code = AAZStrType()
        instance_view_status_read.display_status = AAZStrType(
            serialized_name="displayStatus",
        )
        instance_view_status_read.level = AAZStrType()
        instance_view_status_read.message = AAZStrType()
        instance_view_status_read.time = AAZStrType()

        _schema.code = cls._schema_instance_view_status_read.code
        _schema.display_status = cls._schema_instance_view_status_read.display_status
        _schema.level = cls._schema_instance_view_status_read.level
        _schema.message = cls._schema_instance_view_status_read.message
        _schema.time = cls._schema_instance_view_status_read.time

    _schema_managed_disk_parameters_read = None

    @classmethod
    def _build_schema_managed_disk_parameters_read(cls, _schema):
        if cls._schema_managed_disk_parameters_read is not None:
            _schema.disk_encryption_set = cls._schema_managed_disk_parameters_read.disk_encryption_set
            _schema.id = cls._schema_managed_disk_parameters_read.id
            _schema.security_profile = cls._schema_managed_disk_parameters_read.security_profile
            _schema.storage_account_type = cls._schema_managed_disk_parameters_read.storage_account_type
            return

        cls._schema_managed_disk_parameters_read = _schema_managed_disk_parameters_read = AAZObjectType()

        managed_disk_parameters_read = _schema_managed_disk_parameters_read
        managed_disk_parameters_read.disk_encryption_set = AAZObjectType(
            serialized_name="diskEncryptionSet",
        )
        cls._build_schema_disk_encryption_set_parameters_read(managed_disk_parameters_read.disk_encryption_set)
        managed_disk_parameters_read.id = AAZStrType()
        managed_disk_parameters_read.security_profile = AAZObjectType(
            serialized_name="securityProfile",
        )
        managed_disk_parameters_read.storage_account_type = AAZStrType(
            serialized_name="storageAccountType",
        )

        security_profile = _schema_managed_disk_parameters_read.security_profile
        security_profile.disk_encryption_set = AAZObjectType(
            serialized_name="diskEncryptionSet",
        )
        cls._build_schema_disk_encryption_set_parameters_read(security_profile.disk_encryption_set)
        security_profile.security_encryption_type = AAZStrType(
            serialized_name="securityEncryptionType",
        )

        _schema.disk_encryption_set = cls._schema_managed_disk_parameters_read.disk_encryption_set
        _schema.id = cls._schema_managed_disk_parameters_read.id
        _schema.security_profile = cls._schema_managed_disk_parameters_read.security_profile
        _schema.storage_account_type = cls._schema_managed_disk_parameters_read.storage_account_type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["ListAll"]