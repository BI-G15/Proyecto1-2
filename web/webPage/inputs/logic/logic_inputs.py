from ..models import Input

def get_inputs():
    queryset = Input.objects.all()
    return (queryset)

def create_inputs(form):
    inputs = form.save()
    inputs.save()
    return ()