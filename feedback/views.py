from django.shortcuts import render
from forms import FeedbackForm
from content.views import index
from portal_3dex.views import do_login
# Create your views here.
def send_form(request):
    try:
        if request.user.first_name:
            if request.method == 'POST':
                form = FeedbackForm(request.POST)

                # Have we been provided with a valid form?
                if form.is_valid():
                    # Save the new category to the database.
                    form.save(commit=True)

                    # Now call the index() view.
                    # The user will be shown the homepage.
                    return index(request)
                else:
                    # The supplied form contained errors - just print them to the terminal.
                    print form.errors
            else:
                # If the request was not a POST, display the form to enter details.
                form = FeedbackForm()

            # Bad form (or form details), no form supplied...
            # Render the form with error messages (if any).
            context={'form': form}
            return render(request,'feedback.html',context)
    except AttributeError:
        return do_login(request)