from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields`and 'read_only_fields argument.
    controls which fields should be displayed what fields should be set as read_only
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields or exludes' kwarg up to the superclass
        fields = kwargs.pop("fields", None)
        exclude = kwargs.pop("exclude", None)

        read_only_fields = kwargs.pop("read_only_fields", None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if exclude is not None and fields is not None:
            # maybe an Assertion error?
            raise AttributeError(
                f"{self.__class__.__name__} cannot have both a fields and exludes attribut set "
                " please declear only one of these"
            )

        if fields is not None:
            allowed = set(fields)
            exisiting = set(self.fields)

            for field_name in exisiting - allowed:
                # remove items from dict like obj
                self.fields.pop(field_name)

        if exclude is not None:
            # can't set fields and excules property on model
            exclude = set(exclude)

            for field_name in exclude:
                # remove items from dict like obj
                self.fields.pop(field_name)

        if read_only_fields is not None:

            try:
                self.Meta.read_only_fields

            except AttributeError:
                # serializer meta class must posses this attribute for this to work
                raise AttributeError(
                    f"{self.__class__.__name__} does not have an "
                    "attribute read_only_fields, create an empty list in Meta class to resolve this "
                    "Class Meta: read_only_fields=[ ]"
                )

            else:
                # using a set to prevent repetition of fields appended to
                # read_only_frields due to user refreshing page
                model_read_only_fields = set()

                for field in read_only_fields:
                    model_read_only_fields.add(field)

                self.Meta.read_only_fields = list(model_read_only_fields)

    def get_url(self, obj):
        """
            takes the absolute url of a view, 
            and appends a full path to it
            absolute_url = question/<int:pk>
            full path = https://<domain_name>/<absolute_url>
            """
        return self.context["request"].build_absolute_uri(obj.get_absolute_url())
