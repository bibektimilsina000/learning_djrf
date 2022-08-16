from rest_framework import serializers
from api.models import Student


def start_with_r(value):
    if value[0].lower() != "p":
        raise serializers.ValidationError("must be start with r")
    return value


class StudentSerilizers(serializers.Serializer):
    class Meta:
        model = Student
        field = "__all__"

        def create(self, validated_data):
            return Student.objects.create(**validated_data)

        def update(self, instance, validated_data):

            instance.name = validated_data.get("name", instance.name)

            instance.roll = validated_data.get("roll", instance.roll)

            instance.city = validated_data.get("city", instance.city)
            instance.save()
            return instance

        # field level validation
        def validate_roll(self, value):
            if value >= 200:
                raise serializers.ValidationError("Seat full")
            return value

            # object level validation

        def validate(self, data):
            name = data.get("name")
            city = data.get("city")

            if name.lower() == "prashamsha" and city.lower() == "bhaktapur":
                raise serializers.ValidationError("i still miss you")
            return data
