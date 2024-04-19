from django.contrib import admin
from .models import Project, Task, BugReport, FeatureRequest

# Inline класс для модели Task
class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    fields = ('name', 'description', 'assignee', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

# Класс администратора для модели Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    # Подключение inline для Task
    inlines = [TaskInline, BugReportInline, FeatureRequestInline]

# Класс администратора для модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assignee', 'project')
    search_fields = ('name', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')

    inlines = [BugReportInline, FeatureRequestInline]

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'task', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status',)

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'task', 'project')
    search_fields = ('title', 'description')

