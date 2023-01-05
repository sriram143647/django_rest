from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class custom_throttle_rate(AnonRateThrottle,UserRateThrottle):
    scope = 'custom_throttle'