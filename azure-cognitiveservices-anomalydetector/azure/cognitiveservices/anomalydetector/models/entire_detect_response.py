# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EntireDetectResponse(Model):
    """EntireDetectResponse.

    :param period: Frequency extracted from the series, zero means no
     recurrent pattern has been found.
    :type period: int
    :param expected_values: ExpectedValues contain expected value for each
     input point. The index of the array is consistent with the input series.
    :type expected_values: list[float]
    :param upper_margins: UpperMargins contain upper margin of each input
     point. UpperMargin is used to calculate upperBoundary, which equals to
     expectedValue + (100 - marginScale)*upperMargin. Anomalies in response can
     be filtered by upperBoundary and lowerBoundary. By adjusting marginScale
     value, less significant anomalies can be filtered in client side. The
     index of the array is consistent with the input series.
    :type upper_margins: list[float]
    :param lower_margins: LowerMargins contain lower margin of each input
     point. LowerMargin is used to calculate lowerBoundary, which equals to
     expectedValue - (100 - marginScale)*lowerMargin. Points between the
     boundary can be marked as normal ones in client side. The index of the
     array is consistent with the input series.
    :type lower_margins: list[float]
    :param is_anomaly: IsAnomaly contains anomaly properties for each input
     point. True means an anomaly either negative or positive has been
     detected. The index of the array is consistent with the input series.
    :type is_anomaly: list[bool]
    :param is_negative_anomaly: IsNegativeAnomaly contains anomaly status in
     negative direction for each input point. True means a negative anomaly has
     been detected. A negative anomaly means the point is detected as an
     anomaly and its real value is smaller than the expected one. The index of
     the array is consistent with the input series.
    :type is_negative_anomaly: list[bool]
    :param is_positive_anomaly: IsPositiveAnomaly contain anomaly status in
     positive direction for each input point. True means a positive anomaly has
     been detected. A positive anomaly means the point is detected as an
     anomaly and its real value is larger than the expected one. The index of
     the array is consistent with the input series.
    :type is_positive_anomaly: list[bool]
    """

    _validation = {
        'period': {'required': True},
        'expected_values': {'required': True},
        'upper_margins': {'required': True},
        'lower_margins': {'required': True},
        'is_anomaly': {'required': True},
        'is_negative_anomaly': {'required': True},
        'is_positive_anomaly': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'expected_values': {'key': 'expectedValues', 'type': '[float]'},
        'upper_margins': {'key': 'upperMargins', 'type': '[float]'},
        'lower_margins': {'key': 'lowerMargins', 'type': '[float]'},
        'is_anomaly': {'key': 'isAnomaly', 'type': '[bool]'},
        'is_negative_anomaly': {'key': 'isNegativeAnomaly', 'type': '[bool]'},
        'is_positive_anomaly': {'key': 'isPositiveAnomaly', 'type': '[bool]'},
    }

    def __init__(self, period, expected_values, upper_margins, lower_margins, is_anomaly, is_negative_anomaly, is_positive_anomaly):
        super(EntireDetectResponse, self).__init__()
        self.period = period
        self.expected_values = expected_values
        self.upper_margins = upper_margins
        self.lower_margins = lower_margins
        self.is_anomaly = is_anomaly
        self.is_negative_anomaly = is_negative_anomaly
        self.is_positive_anomaly = is_positive_anomaly
