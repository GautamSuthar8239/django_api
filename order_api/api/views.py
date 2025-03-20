from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Order
from .serializers import OrderSerializer, UserSerializer

# 🔹 USER AUTHENTICATION VIEWS

@api_view(["POST"])
@permission_classes([AllowAny])  # ✅ This allows unauthenticated access
def register_user(request):
    """Register a new user."""
    try:
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(email=email).exists():
            return Response({"error": "User already exists"}, status=400)

        user = User.objects.create(
            username=email, email=email, password=make_password(password)
        )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                # "uid": user.id,
                # "email": user.email,
                "message": "User registered successfully",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            },
            status=201,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["POST"])
@permission_classes([AllowAny])  # ✅ This allows unauthenticated access
def login_user(request):
    """Authenticate a user and return JWT tokens."""
    try:
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)

        if user is None:
            return Response({"error": "Invalid email or password"}, status=401)

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                # "uid": user.id,
                # "email": user.email,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            },
            status=200,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """Get user profile details."""
    return Response({"uid": request.user.id, "email": request.user.email})

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_user(request, user_id):
    """Admin can delete users."""
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({"message": "User deleted"}, status=204)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


# 🔹 ORDER MANAGEMENT VIEWS

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_orders(request):
    """Get all orders."""
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request):
    """Create a new order."""
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_order(request, order_id):
    """Update an order."""
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_order(request, order_id):
    """Admin can delete an order."""
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({"message": "Order deleted"}, status=204)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
