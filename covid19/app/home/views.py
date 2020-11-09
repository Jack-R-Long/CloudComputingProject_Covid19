from django.shortcuts import render

# ------------------------------------------------------------------
# Home
# ------------------------------------------------------------------

def home(request):
	return render(request, "home/index.html")
