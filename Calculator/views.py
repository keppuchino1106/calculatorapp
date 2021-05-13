from django.shortcuts import render

def caculate(request):
    return render(request, "calculator.html")

def result(request):
    userinput1 = int(request.GET['operand1'])
    useroperator = request.GET['operator']
    userinput2 = int(request.GET['operand2'])
    if useroperator == "addition":
        output = userinput1 + userinput2
    elif useroperator == "subtraction":
        output = userinput1 - userinput2
    elif useroperator == "multiplication":
        output = userinput1 * userinput2
    elif useroperator == "division" and userinput2 != 0:
        output = userinput1 / userinput2
    else:
        output = "Error: division by zero"
    return render(request, "result.html", {'output' : output})