from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from .models import User, Train, Booking
from .serializers import UserSerializer, TrainSerializer, BookingSerializer

# 1. User Registration
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])  # Encrypt the password
            user.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. User Login
class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# 3. Add Train (Admin Only)
class AddTrain(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Train added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 4. Check Seat Availability
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def check_seat_availability(request):
    source = request.query_params.get('source')
    destination = request.query_params.get('destination')
    trains = Train.objects.filter(source=source, destination=destination)
    serializer = TrainSerializer(trains, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 5. Book Seat
class BookSeat(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        train_id = request.data.get('train_id')
        seat_number = request.data.get('seat_number')

        try:
            train = Train.objects.get(id=train_id)
            if train.available_seats <= 0:
                return Response({"error": "No seats available"}, status=status.HTTP_400_BAD_REQUEST)

            # Lock the operation to avoid race conditions
            with transaction.atomic():
                train.available_seats -= 1
                train.save()
                booking = Booking.objects.create(
                    user=request.user,
                    train=train,
                    seat_number=seat_number
                )
            return Response({"message": "Seat booked successfully!", "booking_id": booking.id}, status=status.HTTP_201_CREATED)
        except Train.DoesNotExist:
            return Response({"error": "Train not found"}, status=status.HTTP_404_NOT_FOUND)

# 6. Get Booking Details
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_booking_details(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
