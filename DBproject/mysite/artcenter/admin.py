from django.contrib import admin
from  . import models
from artcenter.models import Program
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime, timedelta


class CostListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Cost')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'cost'

    def lookups(self, request, model_admin):
        return (
            ('1', _('10000元以下')),
            ('2', _('10001~20000元')),
            ('3', _('20001~30000元')),
            ('4', _('30001~40000元')),
            ('5', _('40001~50000元')),
            ('6', _('超過50000元')),

        )

    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(cost__gte=0,
                                    cost__lte=10000)
        if self.value() == '2':
            return queryset.filter(cost__gte=10001,
                                    cost__lte=20000)
        if self.value() == '3':
            return queryset.filter(cost__gte=20001,
                                    cost__lte=30000)
        if self.value() == '4':
            return queryset.filter(cost__gte=30001,
                                    cost__lte=40000)
        if self.value() == '5':
            return queryset.filter(cost__gte=40001,
                                    cost__lte=50000)
        if self.value() == '6':
            return queryset.filter(cost__gte=50001)

class ProgramtypeListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Type of Program')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'program_type'
    def lookups(self, request, model_admin):
        return (
            ('1', _('Music')),
            ('2', _('Speech')),
            ('3', _('Photo')),
            ('4', _('Drama')),
        )
    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(program_type__exact = 'Music')
        if self.value() == '2':
            return queryset.filter(program_type__exact = 'Speech')
        if self.value() == '3':
            return queryset.filter(program_type__exact = 'Photo')
        if self.value() == '4':
            return queryset.filter(program_type__exact = 'Drama')

class AudienceListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Audience')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'audience_number'
    def lookups(self, request, model_admin):
        return (
            ('1', _('100人以下')),
            ('2', _('101~150人')),
            ('3', _('151~200人')),
            ('4', _('超過200人')),
        )
    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(audience_number__gte=0,
                                    audience_number__lte=100)
        if self.value() == '2':
            return queryset.filter(audience_number__gte=101,
                                    audience_number__lte=150)
        if self.value() == '3':
            return queryset.filter(audience_number__gte=151,
                                    audience_number__lte=200)
        if self.value() == '4':
            return queryset.filter(audience_number__gte=201)

class AgeListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Age')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'age'

    def lookups(self, request, model_admin):

        return (
            ('1', _('19歲以下')),
            ('2', _('20~22')),
            ('3', _('23~30')),
            ('4', _('31~40')),
            ('5', _('超過40歲')),

        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(age__gte=0,
                                    age__lte=19)
        if self.value() == '2':
            return queryset.filter(age__gte=20,
                                    age__lte=22)
        if self.value() == '3':
            return queryset.filter(age__gte=23,
                                    age__lte=30)
        if self.value() == '4':
            return queryset.filter(age__gte=31,
                                    age__lte=40)
        if self.value() == '5':
            return queryset.filter(age__gte=41)

class GenderListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Gender')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'gender'

    def lookups(self, request, model_admin):

        return (
            ('1', _('Male')),
            ('2', _('Female')),
            ('3', _('Others')),
        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(gender__exact = 'male')
        if self.value() == '2':
            return queryset.filter(gender__exact = 'female')
        if self.value() == '3':
            return queryset.filter(gender__exact = 'others')

class StartdateListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Start Date')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'start_date'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
        	('2009',_('Before 2010')),
            ('2010', _('2010')),
            ('2011', _('2011')),
            ('2012', _('2012')),
            ('2013', _('2013')),
            ('2014', _('2014')),
            ('2015', _('2015')),
            ('2016', _('2016')),
            ('2017', _('Start after 2017')),

        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '2009':
            return queryset.filter(start_date__lte=date(2009, 12, 31))
        if self.value() == '2010':
            return queryset.filter(start_date__gte=date(2010 ,1, 1),
                                    start_date__lte=date(2010, 12, 31))
        if self.value() == '2011':
            return queryset.filter(start_date__gte=date(2011, 1, 1),
                                    start_date__lte=date(2011, 12, 31))
        if self.value() == '2012':
            return queryset.filter(start_date__gte=date(2012, 1, 1),
                                    start_date__lte=date(2012, 12, 31))
        if self.value() == '2013':
            return queryset.filter(start_date__gte=date(2013, 1, 1),
                                    start_date__lte=date(2013, 12, 31))
        if self.value() == '2014':
            return queryset.filter(start_date__gte=date(2014, 1, 1),
                                    start_date__lte=date(2014, 12, 31))
        if self.value() == '2015':
            return queryset.filter(start_date__gte=date(2015, 1, 1),
                                    start_date__lte=date(2015, 12, 31))
        if self.value() == '2016':
            return queryset.filter(start_date__gte=date(2016, 1, 1),
                                    start_date__lte=date(2016, 12, 31))
        if self.value() == '2017':
            return queryset.filter(start_date__gte=date(2017, 1, 1))

class JobtypeListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Job')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'job_type'

    def lookups(self, request, model_admin):

        return (
            ('1', _('Manager')),
            ('2', _('Receptionist')),
            ('3', _('Technician')),
            ('4', _('Photographer')),
            ('5', _('Assistence')),
        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(job_type__exact = 'Manager')
        if self.value() == '2':
            return queryset.filter(job_type__exact = 'Receptionist')
        if self.value() == '3':
            return queryset.filter(job_type__exact = 'Technician')
        if self.value() == '4':
            return queryset.filter(job_type__exact = 'Photographer')
        if self.value() == '5':
            return queryset.filter(job_type__exact = 'Assistence')

class JobTypeForListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Job')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'job_type__job_type'

    def lookups(self, request, model_admin):

        return (
            ('1', _('Manager')),
            ('2', _('Receptionist')),
            ('3', _('Technician')),
            ('4', _('Photographer')),
            ('5', _('Assistence')),
        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(job_type__job_type__exact = 'Manager')
        if self.value() == '2':
            return queryset.filter(job_type__job_type__exact = 'Receptionist')
        if self.value() == '3':
            return queryset.filter(job_type__job_typee__exact = 'Technician')
        if self.value() == '4':
            return queryset.filter(job_type__job_type__exact = 'Photographer')
        if self.value() == '5':
            return queryset.filter(job_type__job_type__exact = 'Assistence')

class JobListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Job')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'job__job_type'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Manager')),
            ('2', _('Receptionist')),
            ('3', _('Technician')),
            ('4', _('Photographer')),
            ('5', _('Assistence')),
        )
    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(job__job_type__exact = 'Manager')
        if self.value() == '2':
            return queryset.filter(job__job_type__exact = 'Receptionist')
        if self.value() == '3':
            return queryset.filter(job__job_type__exact = 'Technician')
        if self.value() == '4':
            return queryset.filter(job__job_type__exact = 'Photographer')
        if self.value() == '5':
            return queryset.filter(job__job_type__exact = 'Assistence')

class SalaryListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Salary Per hour')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'salary_per_hour'
    def lookups(self, request, model_admin):
        return (
            ('1', _('130元以下')),
            ('2', _('131~140')),
            ('3', _('141~150')),
            ('4', _('151~160')),
            ('5', _('超過160元')),

        )
    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(salary_per_hour__gte=0,
                                    salary_per_hour__lte=130)
        if self.value() == '2':
            return queryset.filter(salary_per_hour__gte=131,
                                    salary_per_hour__lte=140)
        if self.value() == '3':
            return queryset.filter(salary_per_hour__gte=141,
                                    salary_per_hour__lte=150)
        if self.value() == '4':
            return queryset.filter(salary_per_hour__gte=151,
                                    salary_per_hour__lte=160)
        if self.value() == '5':
            return queryset.filter(salary_per_hour__gte=161)

class BuyingdateListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Buy Date')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'buying_date'

    def lookups(self, request, model_admin):
        return (
        	('1',_('Before 2014')),
            ('2', _('2014.06')),
            ('3', _('2014.12')),
            ('4', _('2015.06')),
            ('5', _('2015.12')),
            ('6', _('2016.06')),
            ('7', _('2016.12')),
            ('8', _('After 2017.01')),

        )

    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(buying_date__lte=date(2013, 12, 31))
        if self.value() == '2':
            return queryset.filter(buying_date__gte=date(2014, 1, 1),
                                    buying_date__lte=date(2014, 6, 30))
        if self.value() == '3':
            return queryset.filter(buying_date__gte=date(2014, 7, 1),
                                    buying_date__lte=date(2014, 12, 31))
        if self.value() == '4':
            return queryset.filter(buying_date__gte=date(2015, 1, 1),
                                    buying_date__lte=date(2015, 6, 30))        
        if self.value() == '5':
            return queryset.filter(buying_date__gte=date(2015, 7, 1),
                                    buying_date__lte=date(2015, 12, 31))
        if self.value() == '6':
            return queryset.filter(buying_date__gte=date(2016, 1, 1),
                                    buying_date__lte=date(2016, 6, 30))
        if self.value() == '7':
            return queryset.filter(buying_date__gte=date(2016, 7, 1),
                                    buying_date__lte=date(2016, 12, 31))
        if self.value() == '8':
            return queryset.filter(buying_date__gte=date(2017, 1, 1))

class PriceListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Price')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'price'
    def lookups(self, request, model_admin):
        return (
            ('1', _('200元以下')),
            ('2', _('201~300元')),
            ('3', _('301~400元')),
            ('4', _('401~500元')),
            ('5', _('超過501元')),

        )

    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(price__gte=0,
                                    price__lte=200)
        if self.value() == '2':
            return queryset.filter(price__gte=201,
                                    price__lte=300)
        if self.value() == '3':
            return queryset.filter(price__gte=301,
                                    price__lte=400)
        if self.value() == '4':
            return queryset.filter(price__gte=401,
                                    price__lte=500)
        if self.value() == '5':
            return queryset.filter(price__gte=501)

class TicketListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Ticket Type')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'ticket_type'

    def lookups(self, request, model_admin):

        return (
            ('1', _('Normal')),
            ('2', _('Student')),
            ('3', _('Discount')),
        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(ticket_type__exact = 'Normal')
        if self.value() == '2':
            return queryset.filter(ticket_type__exact = 'Student')
        if self.value() == '3':
            return queryset.filter(ticket_type__exact = 'Discount')

class AmountListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Amount')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'amount'

    def lookups(self, request, model_admin):

        return (
            ('1', _('50張以下')),
            ('2', _('51~70張')),
            ('3', _('71~90張')),
            ('4', _('91~100張')),
            ('5', _('超過100張')),

        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(amount__gte=0,
                                    amount__lte=50)
        if self.value() == '2':
            return queryset.filter(amount__gte=51,
                                    amount__lte=70)
        if self.value() == '3':
            return queryset.filter(amount__gte=71,
                                    amount__lte=90)
        if self.value() == '4':
            return queryset.filter(amount__gte=91,
                                    amount__lte=100)
        if self.value() == '5':
            return queryset.filter(amount__gte=101)

class SalarymonthListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Monthly Pay')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'salary_per_month'

    def lookups(self, request, model_admin):

        return (
            ('1', _('20000元以下')),
            ('2', _('20001~25000')),
            ('3', _('25001~30000')),
            ('4', _('30001~35000')),
            ('5', _('超過35000元')),

        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(salary_per_month__gte=0,
                                    salary_per_month__lte=20000)
        if self.value() == '2':
            return queryset.filter(salary_per_month__gte=20001,
                                    salary_per_month__lte=25000)
        if self.value() == '3':
            return queryset.filter(salary_per_month__gte=25001,
                                    salary_per_month__lte=30000)
        if self.value() == '4':
            return queryset.filter(salary_per_month__gte=30001,
                                    salary_per_month__lte=35000)
        if self.value() == '5':
            return queryset.filter(salary_per_month__gte=35001)

class DateListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Date')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return (
        	('1',_('Before 2015')),
            ('2', _('In 2015')),
            ('3', _('2016.3前')),
            ('4', _('2016.6前')),
            ('5', _('2016.9前')),
            ('6', _('2016年末')),
            ('7', _('2017'))
        )

    def queryset(self, request, queryset):
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(date__lte=date(2014, 12, 31))
        if self.value() == '2':
            return queryset.filter(date__gte=date(2015 ,1, 1),
                                    date__lte=date(2015, 12, 31))
        if self.value() == '3':
            return queryset.filter(date__gte=date(2016, 1, 1),
                                    date__lte=date(2016, 3, 31))
        if self.value() == '4':
            return queryset.filter(date__gte=date(2016, 4, 1),
                                    date__lte=date(2016, 6, 30))
        if self.value() == '5':
            return queryset.filter(date__gte=date(2016, 7, 1),
                                    date__lte=date(2016, 9, 30))
        if self.value() == '6':
            return queryset.filter(date__gte=date(2016, 10, 1),
                                    date__lte=date(2016, 12, 31))
        if self.value() == '7':
            return queryset.filter(date__gte=date(2017, 1, 1))
        
class DurationListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Duration')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'duration'

    def lookups(self, request, model_admin):

        return (
            ('1', _('Less than 1 Hour')),
            ('2', _('Less than 2 Hour')),
            ('3', _('Less than 3 Hour')),
            ('4', _('Less than 4 Hour')),
            ('5', _('Above 4 Hour')),

        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(duration__lte =timedelta(hours = 1))
        if self.value() == '2':
            return queryset.filter(duration__lt =timedelta(hours = 2))
        if self.value() == '3':
            return queryset.filter(duration__lt =timedelta(hours = 3))
        if self.value() == '4':
            return queryset.filter(duration__lt =timedelta(hours = 4))
        if self.value() == '5':
            return queryset.filter(duration__gte =timedelta(hours = 4))

class WorkhourListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Working hour')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'working_hours'

    def lookups(self, request, model_admin):

        return (
            ('1', _('Less than 5 Hour')),
            ('2', _('5 Hour to 8 Hour')),
            ('3', _('9 Hour to 12 Hour')),
            ('4', _('13 Hour to 16 Hour')),
            ('5', _('Above 16 Hour')),

        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(working_hours__lte =timedelta(hours = 4))
        if self.value() == '2':
            return queryset.filter(working_hours__gte =timedelta(hours = 5),
                                    working_hours__lte =timedelta(hours = 8))
        if self.value() == '3':
            return queryset.filter(working_hours__gte =timedelta(hours = 9),
                                    working_hours__lte =timedelta(hours = 12))
        if self.value() == '4':
            return queryset.filter(working_hours__gte =timedelta(hours = 13),
                                    working_hours__lte =timedelta(hours = 16))
        if self.value() == '5':
            return queryset.filter(working_hours__gte =timedelta(hours = 17))            

class RatingListFilter(admin.SimpleListFilter):
   # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Rating')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'rating'

    def lookups(self, request, model_admin):

        return (
            ('1', _('1')),
            ('2', _('2')),
            ('3', _('3')),
            ('4', _('4')),
            ('5', _('5')),
        )

    def queryset(self, request, queryset):

        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(rating__exact = 'One')
        if self.value() == '2':
            return queryset.filter(rating__exact = 'Two')
        if self.value() == '3':
            return queryset.filter(rating__exact = 'Three')
        if self.value() == '4':
            return queryset.filter(rating__exact = 'Four')
        if self.value() == '5':
            return queryset.filter(rating__exact = 'Five')


class ProgramAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'program_type', 'cost', 'audience_number')
	search_fields = ('title',)
	list_filter = (ProgramtypeListFilter,CostListFilter,AudienceListFilter,)
#no foreign key

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'age', 'gender', 'start_date')
	search_fields = ('name',)
	list_filter = (AgeListFilter,GenderListFilter,StartdateListFilter,)
#no foreign key

class JobAdmin(admin.ModelAdmin):
	list_display = ('job_type', 'work', 'salary_per_hour')
	search_fields = ('work',)
	list_filter = (JobtypeListFilter,SalaryListFilter,)
#no foreign key

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('id','equipment_type', 'model', 'buying_date', 'condition')
	search_fields = ('equipment_type', 'model', 'condition',)
	list_filter = (BuyingdateListFilter,)
#no foreign key

class TicketAdmin(admin.ModelAdmin):
	list_display = ('id', 'program', 'ticket_type', 'price', 'amount')
	search_fields = ('program__title',)
	list_filter = (TicketListFilter,PriceListFilter,AmountListFilter,)

class ManagerAdmin(admin.ModelAdmin):
	list_display = ('id','employee', 'program_type', 'salary_per_month')
	search_fields = ('employee__name',)
	list_filter = (ProgramtypeListFilter,SalarymonthListFilter,)
	
class PerformerAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'email', 'phone_number')
	search_fields = ('name', 'email', 'phone_number',)
#no foreign key

class TimeofprogramAdmin(admin.ModelAdmin):
	list_display = ('id','program', 'date', 'start_time', 'duration')
	search_fields = ('program__title',)
	list_filter = (DateListFilter,'start_time',DurationListFilter,)

class WorksonAdmin(admin.ModelAdmin):
	list_display = ('id','employee', 'program', 'job_type','working_hours')
	search_fields = ('employee__name', 'program__title',)
	list_filter = (WorkhourListFilter,JobtypeListFilter,)

class UseAdmin(admin.ModelAdmin):
	list_display = ('id','program', 'equipment')
	search_fields = ('program__title', 'equipment__equipment_type',)
	
class PerformAdmin(admin.ModelAdmin):
	list_display = ('id','performer', 'program')
	search_fields = ('performer__name', 'program__title',)
    

class QuestionnaireAdmin(admin.ModelAdmin):
	list_display = ('id','program', 'audience_name', 'audience_email', 'comment', 'rating')
	search_fields = ('program__title', 'audience_name', 'audience_email', 'comment',)
	list_filter = ('rating',)

class DoAdmin(admin.ModelAdmin):
	list_display = ('id','employee', 'job')
	search_fields = ('employee__name',)
	list_filter = (JobListFilter,)
	



admin.site.register(models.Program, ProgramAdmin)
admin.site.register(models.Time_of_program,TimeofprogramAdmin)
admin.site.register(models.Employee,EmployeeAdmin)
admin.site.register(models.Job,JobAdmin)
admin.site.register(models.Works_on,WorksonAdmin)
admin.site.register(models.Equipment,EquipmentAdmin)
admin.site.register(models.Ticket,TicketAdmin)
admin.site.register(models.Use,UseAdmin)
admin.site.register(models.Performer,PerformerAdmin)
admin.site.register(models.Perform,PerformAdmin)
admin.site.register(models.Questionnaire,QuestionnaireAdmin)
admin.site.register(models.Manager,ManagerAdmin)
admin.site.register(models.Do,DoAdmin)

# Register your models here.
