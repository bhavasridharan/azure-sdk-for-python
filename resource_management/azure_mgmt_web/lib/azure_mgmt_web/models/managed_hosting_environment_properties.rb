# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Model object.
    #
    class ManagedHostingEnvironmentProperties

      include MsRestAzure

      # @return [String] Name of the managed hosting environment
      attr_accessor :name

      # @return [String] Location of the managed hosting environment e.g.
      # "West US"
      attr_accessor :location

      # @return [ManagedHostingEnvironmentStatus] Current status of the
      # managed hosting environment. Possible values include: 'Preparing',
      # 'Ready', 'Deleting'
      attr_accessor :status

      # @return [VirtualNetworkProfile] Description of the managed hosting
      # environment's virtual network
      attr_accessor :virtual_network

      # @return [Integer] Number of ip ssl addresses reserved for the managed
      # hosting environment
      attr_accessor :ipssl_address_count

      # @return [String] DNS suffix of the managed hosting environment
      attr_accessor :dns_suffix

      # @return [String] Subscription of the managed hosting environment (read
      # only)
      attr_accessor :subscription_id

      # @return [String] Resource group of the managed hosting environment
      # (read only)
      attr_accessor :resource_group

      # @return [Boolean] True/false indicating whether the managed hosting
      # environment is healthy
      attr_accessor :environment_is_healthy

      # @return [String] Detailed message about with results of the last check
      # of the managed hosting environment
      attr_accessor :environment_status

      # @return [Boolean] True/false indicating whether the managed hosting
      # environment is suspended. The environment can be suspended e.g. when
      # the management endpoint is no longer available
      # (most likely because NSG blocked the incoming traffic)
      attr_accessor :suspended

      # @return [String] Resource id of the api management account associated
      # with this managed hosting environment (read only)
      attr_accessor :api_management_account

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @virtual_network.validate unless @virtual_network.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.name
        output_object['name'] = serialized_property unless serialized_property.nil?

        serialized_property = object.location
        output_object['location'] = serialized_property unless serialized_property.nil?

        serialized_property = object.status
        output_object['status'] = serialized_property unless serialized_property.nil?

        serialized_property = object.virtual_network
        unless serialized_property.nil?
          serialized_property = VirtualNetworkProfile.serialize_object(serialized_property)
        end
        output_object['virtualNetwork'] = serialized_property unless serialized_property.nil?

        serialized_property = object.ipssl_address_count
        output_object['ipsslAddressCount'] = serialized_property unless serialized_property.nil?

        serialized_property = object.dns_suffix
        output_object['dnsSuffix'] = serialized_property unless serialized_property.nil?

        serialized_property = object.subscription_id
        output_object['subscriptionId'] = serialized_property unless serialized_property.nil?

        serialized_property = object.resource_group
        output_object['resourceGroup'] = serialized_property unless serialized_property.nil?

        serialized_property = object.environment_is_healthy
        output_object['environmentIsHealthy'] = serialized_property unless serialized_property.nil?

        serialized_property = object.environment_status
        output_object['environmentStatus'] = serialized_property unless serialized_property.nil?

        serialized_property = object.suspended
        output_object['suspended'] = serialized_property unless serialized_property.nil?

        serialized_property = object.api_management_account
        output_object['apiManagementAccount'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [ManagedHostingEnvironmentProperties] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = ManagedHostingEnvironmentProperties.new

        deserialized_property = object['name']
        output_object.name = deserialized_property

        deserialized_property = object['location']
        output_object.location = deserialized_property

        deserialized_property = object['status']
        if (!deserialized_property.nil? && !deserialized_property.empty?)
          enum_is_valid = ManagedHostingEnvironmentStatus.constants.any? { |e| ManagedHostingEnvironmentStatus.const_get(e).to_s.downcase == deserialized_property.downcase }
          warn 'Enum ManagedHostingEnvironmentStatus does not contain ' + deserialized_property.downcase + ', but was received from the server.' unless enum_is_valid
        end
        output_object.status = deserialized_property

        deserialized_property = object['virtualNetwork']
        unless deserialized_property.nil?
          deserialized_property = VirtualNetworkProfile.deserialize_object(deserialized_property)
        end
        output_object.virtual_network = deserialized_property

        deserialized_property = object['ipsslAddressCount']
        deserialized_property = Integer(deserialized_property) unless deserialized_property.to_s.empty?
        output_object.ipssl_address_count = deserialized_property

        deserialized_property = object['dnsSuffix']
        output_object.dns_suffix = deserialized_property

        deserialized_property = object['subscriptionId']
        output_object.subscription_id = deserialized_property

        deserialized_property = object['resourceGroup']
        output_object.resource_group = deserialized_property

        deserialized_property = object['environmentIsHealthy']
        output_object.environment_is_healthy = deserialized_property

        deserialized_property = object['environmentStatus']
        output_object.environment_status = deserialized_property

        deserialized_property = object['suspended']
        output_object.suspended = deserialized_property

        deserialized_property = object['apiManagementAccount']
        output_object.api_management_account = deserialized_property

        output_object
      end
    end
  end
end