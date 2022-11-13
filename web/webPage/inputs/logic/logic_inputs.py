from ..models import Input
from joblib import load
from .apiMain import make_predictions

def get_inputs():
    queryset = Input.objects.all()
    return (queryset)

def create_inputs(form):
    inputs = form.save(commit=False)
    text = inputs.text
    result = make_predictions(text)["result"]
    input = Input(text=text, result=result)
    input.save()
    return ()

#Funcion para hacerlo desde la logica
def predict(text):
    model = load("modelo2.joblib")
    result = model.predict([text])
    return result[0]