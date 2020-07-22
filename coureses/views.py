from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView , \
                                      DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,\
                                        PermissionRequiredMixin                                     
from .models import Course

class OwnerMixin(object):
    def get_queryset(self):
        qs= super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ['subject','title','slug','overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin,OwnerEditMixin):
    template_name = 'coureses/manage/course/list.html'

class ManageCourseListView(OwnerCourseMixin, ListView):
    
    template_name = 'coureses\manage\course\list.html'
    permission_required = 'coureses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
   # template_name = 'coureses\manage\course\form.html'
    permission_required = 'coureses.add_course'

class CourseUpdateView(OwnerCourseEditMixin, UpdateView ):
    permission_required = 'coureses.change_course'

class CourseDeleteView(OwnerCourseMixin , DeleteView):
    template_name = 'coureses\manage\course\delete.html'
    
    """ def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)"""
