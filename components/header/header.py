from django_components import component

@component.register("navbar")
class navbar(component.Component):
    template_name = "navbar.html"

