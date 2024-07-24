from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import NutritionPersonalDetails, ValuesConsumedPerDay, ValuesRecommendedPerDay
from .serializers import NutritionPersonalDetailsSerializer, ValuesConsumedPerDaySerializer, ValuesRecommendedPerDaySerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# Create your views here.


class NutritionPersonalDetailsViewSet(ModelViewSet):
    queryset = NutritionPersonalDetails.objects.all()
    serializer_class = NutritionPersonalDetailsSerializer
    permission_classes = [IsAuthenticated]

    # sobreescribo para filtrar por id_user
    def get_queryset(self):
        queryset = super().get_queryset()
        id_user = self.request.query_params.get('id_user')
        if id_user is not None:
            queryset = queryset.filter(id_user=id_user)
        return queryset

    # sobreescribo para crear o actualizar un registro segun el id_user
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('id_user')

        # Verifica si ya existe un registro con ese user_id
        detail_instance = NutritionPersonalDetails.objects.filter(
            id_user=user_id).first()

        if detail_instance:
            # Si existe, actualiza el registro existente
            serializer = self.get_serializer(
                detail_instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Si no existe, crea un nuevo registro
            return super(NutritionPersonalDetailsViewSet, self).create(request, *args, **kwargs)


class ValuesConsumedPerDayViewSet(ModelViewSet):
    queryset = ValuesConsumedPerDay.objects.all()
    serializer_class = ValuesConsumedPerDaySerializer
    permission_classes = [IsAuthenticated]

    # sobreescribo para filtrar por id_user
    def get_queryset(self):
        queryset = super().get_queryset()
        id_user = self.request.query_params.get('id_user')
        today = timezone.now().date()
        if id_user is not None:
            queryset = queryset.filter(
                id_user=id_user).filter(created_at__date=today)
        return queryset

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('id_user')
        value_consumed = ValuesConsumedPerDay.objects.filter(id_user=user_id)
        today = timezone.localdate()
        mutable_data = request.data.copy()
        if value_consumed:
            detail_instance = ValuesConsumedPerDay.objects.filter(created_at__date=today).first()
            if detail_instance:
                # Si existe, actualiza el registro existente
                mutable_data.update({
                    'id_user': user_id,
                    'total_carbs': (detail_instance.total_carbs or 0) + request.data.get('carbs', 0),
                    'total_protein': (detail_instance.total_protein or 0) + request.data.get('protein', 0),
                    'total_fat': (detail_instance.total_fat or 0) + request.data.get('fat', 0),
                    'total_cals': (detail_instance.total_cals or 0) + request.data.get('cal', 0),
                    'total_water': (detail_instance.total_water or 0) + request.data.get('water', 0),
                })
                serializer = self.get_serializer(detail_instance, data=mutable_data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
        mutable_data.update({
            'id_user': user_id,
            'total_carbs': mutable_data.get('carbs', 0),
            'total_protein': mutable_data.get('protein', 0),
            'total_fat': mutable_data.get('fat', 0),
            'total_cals': mutable_data.get('cal', 0),
            'total_water': mutable_data.get('water', 0),
        })
        # Instead of calling super().create with mutable_data, handle the creation manually
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ValuesRecommendedPerDayViewSet(ModelViewSet):
    queryset = ValuesRecommendedPerDay.objects.all()
    serializer_class = ValuesRecommendedPerDaySerializer
    permission_classes = [IsAuthenticated]

    # sobreescribo para filtrar por id_user
    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        if id_user is not None:
            nutrition_detail = NutritionPersonalDetails.objects.filter(
                id_user=id_user).first()
            if nutrition_detail:
                return ValuesRecommendedPerDay.objects.filter(id_nutrition_personal_details=nutrition_detail.id)
        return ValuesRecommendedPerDay.objects.none()

    # sobreescribo para crear o actualizar un registro segun el id_user
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('id_user')
        nutrition_detail = NutritionPersonalDetails.objects.filter(
            id_user=user_id).first().id

        if nutrition_detail:
            detail_instance = ValuesRecommendedPerDay.objects.filter(
                id_nutrition_personal_details=nutrition_detail).first()

            if detail_instance:
                # Si existe, actualiza el registro existente
                serializer = self.get_serializer(
                    detail_instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                request.data["id_nutrition_personal_details"] = nutrition_detail
                return super(ValuesRecommendedPerDayViewSet, self).create(request, *args, **kwargs)
