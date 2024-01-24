from django.core.mail import send_mail 
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Post
from django.db.models import  Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, Http404


# def home(request):
#     queryset = Post.objects.all()
#     model = Post
#     fields = ['last_name', 'first_name', 'preferred_date', 'procedure', 'exam_type', 'radiologist_name', 'radtech_name']
#     context = {
#         #'posts': Post.objects.all()
#         "fields": fields,
#         "queryset": queryset
#     }
#     if request.method == 'POST':
#         queryset = Post.objects.filter(Post_icontains=model[''].value())

#         context = {
#             "fields": fields,
#             "model": model,
#             "queryset": queryset
#         }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search', '')
        if search_term:
            queryset = queryset.filter(Q(last_name__icontains=search_term) | Q(first_name__icontains=search_term) |
            Q(procedure__icontains=search_term) | Q(preferred_date__icontains=search_term) | 
            Q(exam_type__icontains=search_term) | Q(radiologist_name__icontains=search_term) | 
            Q(radtech_name__icontains=search_term))
        return queryset

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['last_name', 'first_name', 'middle_name', 'sex', 'date_of_birth', 
    'email_address', 'contact_number', 'requesting_physician', 'hospital_site', 
    'preferred_date', 'doctors_request', 
    'exam_type', 'procedure', 'status']

    def form_valid(self, form):
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        email = [form.cleaned_data['email_address']]
        
        hospital_site = form.cleaned_data['hospital_site']
        exam_type = form.cleaned_data['exam_type']
        preferred_date = form.cleaned_data['preferred_date']

        procedure = form.cleaned_data['procedure']
        status = form.cleaned_data['status']

        email_from = settings.EMAIL_HOST_USER

        html = render_to_string('blog/email_template.html', {
            'last_name': last_name,
            'first_name': first_name,
           
            'hospital_site': hospital_site,
            'exam_type': exam_type,
            'procedure': procedure,
            'preferred_date': preferred_date,
            'status': status
        })

        send_mail('Appointment Details', 'This is the message', email_from, email, html_message=html)
        
        return super().form_valid(form)
    

    # def form_valid(self, form):
        # form.instance.author = self.request.user # sets the author to be equal to the current logged in user
        # return super().form_valid(form) # this runs the form_valid method in our parent class

class PostUpdateView(LoginRequiredMixin, UpdateView): 
    model = Post
    fields = ['last_name', 'first_name', 'middle_name', 'sex', 'date_of_birth', 
    'email_address', 'contact_number', 'requesting_physician', 'hospital_site', 
    'preferred_date', 'doctors_request', 'radiologist_name', 'radtech_name',
    'exam_type', 'procedure', 'status']

    def form_valid(self, form):
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        email = [form.cleaned_data['email_address']]
       
        hospital_site = form.cleaned_data['hospital_site']
        exam_type = form.cleaned_data['exam_type']
        preferred_date = form.cleaned_data['preferred_date']
        procedure = form.cleaned_data['procedure']
        status = form.cleaned_data['status']

        email_from = settings.EMAIL_HOST_USER

        html = render_to_string('blog/email_template.html', {
            'last_name': last_name,
            'first_name': first_name,
          
            'hospital_site': hospital_site,
            'exam_type': exam_type,
            'procedure': procedure,
            'preferred_date': preferred_date,
            'status': status
        })
        send_mail('Appointment Details', 'This is the message', email_from, email, html_message=html)
        
        form.instance.author = self.request.user 
        return super().form_valid(form)

    #def test_func(self): # function to check if the author is actually the one updating the post
        #post = self.get_object()
        #if self.request.user == post.author:
            #return True
        #return False

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    #def test_func(self):
        #post = self.get_object()
        #if self.request.user == post.author:
            #return True
        #return False
        

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# def booking(request):
#    return render(request, 'blog/booking.html')
