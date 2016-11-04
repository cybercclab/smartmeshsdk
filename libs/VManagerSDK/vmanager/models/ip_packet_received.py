# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class IpPacketReceived(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IpPacketReceived - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sys_time': 'datetime',
            'latency': 'int',
            'payload': 'bytearray',
            'gen_net_time': 'datetime',
            'mac_address': 'str',
            'type': 'str',
            'hops': 'int'
        }

        self.attribute_map = {
            'sys_time': 'sysTime',
            'latency': 'latency',
            'payload': 'payload',
            'gen_net_time': 'genNetTime',
            'mac_address': 'macAddress',
            'type': 'type',
            'hops': 'hops'
        }

        self._sys_time = None
        self._latency = None
        self._payload = None
        self._gen_net_time = None
        self._mac_address = None
        self._type = None
        self._hops = None

    @property
    def sys_time(self):
        """
        Gets the sys_time of this IpPacketReceived.
        Time of notification

        :return: The sys_time of this IpPacketReceived.
        :rtype: datetime
        """
        return self._sys_time

    @sys_time.setter
    def sys_time(self, sys_time):
        """
        Sets the sys_time of this IpPacketReceived.
        Time of notification

        :param sys_time: The sys_time of this IpPacketReceived.
        :type: datetime
        """
        self._sys_time = sys_time

    @property
    def latency(self):
        """
        Gets the latency of this IpPacketReceived.
        Time it took for the packet to reach the Manager, in milliseconds

        :return: The latency of this IpPacketReceived.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """
        Sets the latency of this IpPacketReceived.
        Time it took for the packet to reach the Manager, in milliseconds

        :param latency: The latency of this IpPacketReceived.
        :type: int
        """
        self._latency = latency

    @property
    def payload(self):
        """
        Gets the payload of this IpPacketReceived.
        The payload data of the packet, in base64 format

        :return: The payload of this IpPacketReceived.
        :rtype: bytearray
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this IpPacketReceived.
        The payload data of the packet, in base64 format

        :param payload: The payload of this IpPacketReceived.
        :type: bytearray
        """
        self._payload = payload

    @property
    def gen_net_time(self):
        """
        Gets the gen_net_time of this IpPacketReceived.
        Timestamp the packet was generated, in ISO 8601 format

        :return: The gen_net_time of this IpPacketReceived.
        :rtype: datetime
        """
        return self._gen_net_time

    @gen_net_time.setter
    def gen_net_time(self, gen_net_time):
        """
        Sets the gen_net_time of this IpPacketReceived.
        Timestamp the packet was generated, in ISO 8601 format

        :param gen_net_time: The gen_net_time of this IpPacketReceived.
        :type: datetime
        """
        self._gen_net_time = gen_net_time

    @property
    def mac_address(self):
        """
        Gets the mac_address of this IpPacketReceived.
        MAC address of the mote that sent this packet

        :return: The mac_address of this IpPacketReceived.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this IpPacketReceived.
        MAC address of the mote that sent this packet

        :param mac_address: The mac_address of this IpPacketReceived.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def type(self):
        """
        Gets the type of this IpPacketReceived.
        Notification type

        :return: The type of this IpPacketReceived.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IpPacketReceived.
        Notification type

        :param type: The type of this IpPacketReceived.
        :type: str
        """
        allowed_values = ["netStarted", "pathStateChanged", "pathAlert", "moteStateChanged", "joinFailed", "pingResponse", "invalidMIC", "dataPacketReceived", "ipPacketReceived", "packetSent", "cmdFinished", "configChanged", "configLoaded", "alarmOpened", "alarmClosed", "deviceHealthReport", "neighborHealthReport", "discoveryHealthReport", "rawMoteNotification", "serviceChanged", "apStateChanged", "managerStarted", "managerStopping", "optPhase", "pathAlert"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def hops(self):
        """
        Gets the hops of this IpPacketReceived.
        Number of hops the packet took from the mote to the Manager

        :return: The hops of this IpPacketReceived.
        :rtype: int
        """
        return self._hops

    @hops.setter
    def hops(self, hops):
        """
        Sets the hops of this IpPacketReceived.
        Number of hops the packet took from the mote to the Manager

        :param hops: The hops of this IpPacketReceived.
        :type: int
        """
        self._hops = hops

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

