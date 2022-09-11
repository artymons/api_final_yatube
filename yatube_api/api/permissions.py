from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Это переопределение сообщения,
    # если менять на MESSASGE - не работает
    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
