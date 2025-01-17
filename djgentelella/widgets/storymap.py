from .core import TextInput, update_kwargs


class MapBasedStoryMapInput(TextInput):
    template_name = 'gentelella/widgets/storymap_mapbased.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='form-control')
        super(MapBasedStoryMapInput, self).__init__(attrs=attrs, extraskwargs=False)

    def render(self, name, value, attrs=None, renderer=None):
        self.value = value

        return super().render(name, value, attrs=attrs, renderer=renderer)

    def build_attrs(self, base_attrs, extra_attrs=None):
        """Build an attribute dictionary."""
        if extra_attrs is not None:
            if 'required' in extra_attrs:
                extra_attrs.pop('required')
            elif 'disabled' in extra_attrs:
                extra_attrs.pop('disabled')

        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        if self.value is not None:
            attrs['data-url'] = self.value

        return attrs


class GigaPixelStoryMapInput(TextInput):
    template_name = 'gentelella/widgets/storymap_gigapixel.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='form-control')
        super(GigaPixelStoryMapInput, self).__init__(attrs=attrs, extraskwargs=False)

    def render(self, name, value, attrs=None, renderer=None):
        self.value = value

        return super().render(name, value, attrs=attrs, renderer=renderer)

    def build_attrs(self, base_attrs, extra_attrs=None):
        """Build an attribute dictionary."""
        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        if self.value is not None:
            attrs['data-url'] = self.value

        return attrs
