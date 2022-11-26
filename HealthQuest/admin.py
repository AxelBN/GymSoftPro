from django.contrib import admin
from .models import HealthQuests, Ailments, Joint_problems, physical_evaluation
# Register your models here.

class HealthQuestAdmin(admin.ModelAdmin):
    fields = ['name',
              'Date_of_birth',
              'address',
              'phone_number',
              'emergency_contact',
              'emergency_number',
              'ailments',
              'heart_problems',
              'allergies',
              'joint_problems',
              'specify',
              'vision_difficulties',
              'operations_surgeries',
              'skin_problems',
              ]
    search_fields = ['name',
                     'phone_number',
                     ]
    list_display = ['name',
                    'address',
                    'phone_number',
                    ]

class AilmentsModelAdmin (admin.ModelAdmin):
    fields = ['name_ailments']

class JointProblemsAdmin (admin.ModelAdmin):
    fields = ['Joint_problem']

class PhysicalEvaluationsAdmin (admin.ModelAdmin):
    fields = ['__all__']

admin.site.register(HealthQuests, HealthQuestAdmin)
admin.site.register(Ailments)
admin.site.register(Joint_problems)
admin.site.register(physical_evaluation)