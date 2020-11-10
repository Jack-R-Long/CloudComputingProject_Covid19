from django.shortcuts import render

# ------------------------------------------------------------------
# Home
# ------------------------------------------------------------------

def home(request):
	return render(request, "home/index.html")

# ------------------------------------------------------------------
# Bootstrap Template
# ------------------------------------------------------------------

def boot(request):
	return render(request, "home/formMD.html")
