# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from course.models import Course, CourseClass, CourseSort, Lesson, Teacher, Buy
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "learn_time", "nums", "image", "describe"]
    list_filter = ["name", "price", "learn_time", "nums", "image", "describe"]
    search_fields = ["name", "price", "learn_time", "nums", "image", "describe"]

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseClassAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        verbose_name = u"第一分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseSortAdmin(admin.ModelAdmin):
    list_display = ["classes", "name"]
    list_filter = ["classes", "name"]
    search_fields = ["classes", "name"]

    class Meta:
        verbose_name = u"第二分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class LessonAdmin(admin.ModelAdmin):
    list_display = ["name", "lesson_course"]
    list_filter = ["name", "lesson_course"]
    search_fields = ["name", "lesson_course"]

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["teacher_course", "teacher_name", "teacher_des"]
    list_filter = ["teacher_course", "teacher_name", "teacher_des"]
    search_fields = ["teacher_course", "teacher_name", "teacher_des"]

    class Meta:
        verbose_name = u"老师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseClass,CourseClassAdmin)
admin.site.register(CourseSort, CourseSortAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Teacher,TeacherAdmin)