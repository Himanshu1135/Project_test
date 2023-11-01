from django.shortcuts import render
from .sms_spam_main import sms_spam_predict,SpamModel,Vectorizer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def spam_classifier(request):
    if request.method == "POST":
        try:
            # -------------------------- Data input
            text = request.POST['input']
            # print(text)
            # data = request.body.decode('utf-8')
            # data = json.loads(data)
            # text = data.get('sms')
            #---------------------------- predication   
            results = sms_spam_predict(text,SpamModel,Vectorizer)
            # print(results)
            ml_response = {"result": results}
        except KeyError as e:
            ml_response = {"result": e}

        return render(request,'spam.html',ml_response)
    return render(request,'spam.html')
