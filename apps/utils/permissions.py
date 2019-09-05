from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = 'sorry,你无权限查询该数据'

    def has_permission(self, request, view):
        """
        注意：
        源码中初始化时的顺序是认证在前，权限在后，所以只要认证通过
        我们这里就可以使用request.user拿到用户信息，request.auth拿到用户对象
        """
        print(request.user)

