from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions



class IsCustomerAuthenticated(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        try:
            request.session['customer_id']
        except Exception as e:
            msg = {'detail':"Authentication crediantials are required"}
            raise exceptions.AuthenticationFailed(msg)
        return view(request)