from ..models import Input
from joblib import load

def get_inputs():
    queryset = Input.objects.all()
    return (queryset)

def create_inputs(form):
    inputs = form.save(commit=False)
    text = inputs.text
    print(text)
    result = predict(text)
    print(result)
    input = Input(text=text, result=result)
    input.save()
    return ()

def predict(text):
    model = load("modelo2.joblib")
    result = model.predict([text])
    return result[0]