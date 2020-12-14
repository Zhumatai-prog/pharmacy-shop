from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login


from .forms import *
from .models import *
from .views import *


def home_page(request):
    return render(request, 'delivery/home.html')

# PRODUCT CRUD VIEW

class ProductListView(ListView):

    model = Product
    template_name = 'delivery/products/product_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        object_list = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(object_list, self.paginate_by)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        context['object_list'] = object_list
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'delivery/products/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'delivery/products/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'delivery/products/product_update.html'
    context_object_name = 'product'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('delivery:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delivery/products/product_delete.html'
    success_url = reverse_lazy('delivery:product_list')



# PERSONNEL CRUD VIEW

class PersonnelListView(ListView):

    model = Personnel
    template_name = 'delivery/personnel/personnel_list.html'
    context_object_name = 'personnels'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PersonnelListView, self).get_context_data(**kwargs)
        personnels = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(personnels, self.paginate_by)
        try:
            personnels = paginator.page(page)
        except PageNotAnInteger:
            personnels = paginator.page(1)
        except EmptyPage:
            personnels = paginator.page(paginator.num_pages)
        context['personnels'] = personnels
        return context

class PersonnelCreateView(CreateView):
    model = Personnel
    template_name = 'delivery/personnel/personnel_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:personnel_list')


class PersonnelDetailView(DetailView):
    model = Personnel
    template_name = 'delivery/personnel/personnel_detail.html'


class PersonnelUpdateView(UpdateView):
    model = Personnel
    template_name = 'delivery/personnel/personnel_update.html'
    context_object_name = 'personnel'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('delivery:personnel_detail', kwargs={'pk': self.object.id})


class PersonnelDeleteView(DeleteView):
    model = Personnel
    template_name = 'delivery/personnel/personnel_delete.html'
    success_url = reverse_lazy('delivery:personnel_list')



# SUPPLIER CRUD VIEW

class SupplierListView(ListView):

    model = Supplier
    template_name = 'delivery/suppliers/supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SupplierListView, self).get_context_data(**kwargs)
        suppliers = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(suppliers, self.paginate_by)
        try:
            suppliers = paginator.page(page)
        except PageNotAnInteger:
            suppliers = paginator.page(1)
        except EmptyPage:
            suppliers = paginator.page(paginator.num_pages)
        context['suppliers'] = suppliers
        return context


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'delivery/suppliers/supplier_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:supplier_list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'delivery/suppliers/supplier_update.html'
    context_object_name = 'supplier'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('delivery:supplier_list')


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'delivery/suppliers/supplier_delete.html'
    success_url = reverse_lazy('delivery:supplier_list')



# ORDER_PRODUCT CRUD VIEW

class OrderListView(ListView):
    model = Order_product
    template_name = 'delivery/order_product/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        orders = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(orders, self.paginate_by)
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)
        context['orders'] = orders
        return context


class OrderCreateView(CreateView):
    model = Order_product
    template_name = 'delivery/order_product/order_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:order_list')



# PRODUCT_SUPPLY CRUD VIEW

class ProductSupplyListView(ListView):
    model = Product_supply
    template_name = 'delivery/product_supply/product_supply.html'
    context_object_name = 'supplies'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProductSupplyListView, self).get_context_data(**kwargs)
        supplies = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(supplies, self.paginate_by)
        try:
            supplies = paginator.page(page)
        except PageNotAnInteger:
            supplies = paginator.page(1)
        except EmptyPage:
            supplies = paginator.page(paginator.num_pages)
        context['supplies'] = supplies
        return context



class ProductSupplyCreateView(CreateView):
    model = Product_supply
    template_name = 'delivery/product_supply/product_supply_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:product_supply')



# PRODUCT_SALE CRUD VIEW

class ProductSaleListView(ListView):
    model = Product_sale
    template_name = 'delivery/product_sale/product_sale.html'
    context_object_name = 'sales'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProductSaleListView, self).get_context_data(**kwargs)
        sales = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(sales, self.paginate_by)
        try:
            sales = paginator.page(page)
        except PageNotAnInteger:
            sales = paginator.page(1)
        except EmptyPage:
            sales = paginator.page(paginator.num_pages)
        context['sales'] = sales
        return context


class ProductSaleCreateView(CreateView):
    model = Product_sale
    template_name = 'delivery/product_sale/product_sale_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:product_sale')

# SALARY CRUD VIEW

class SalaryListView(ListView):
    model = Salary
    template_name = 'delivery/salary/salary_list.html'
    context_object_name = 'salaries'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SalaryListView, self).get_context_data(**kwargs)
        salaries = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(salaries, self.paginate_by)
        try:
            salaries = paginator.page(page)
        except PageNotAnInteger:
            salaries = paginator.page(1)
        except EmptyPage:
            salaries = paginator.page(paginator.num_pages)
        context['salaries'] = salaries
        return context


class SalaryCreateView(CreateView):
    model = Salary
    template_name = 'delivery/salary/salary_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:salary_list')



# CUSTOMER CRUD VIEW

class CustomerListView(ListView):
    model = Customer
    template_name = 'delivery/customers/customers.html'
    context_object_name = 'customers'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        customers = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(customers, self.paginate_by)
        try:
            customers = paginator.page(page)
        except PageNotAnInteger:
            customers = paginator.page(1)
        except EmptyPage:
            customers = paginator.page(paginator.num_pages)
        context['customers'] = customers
        return context


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'delivery/customers/customer_detail.html'


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'delivery/customers/customer_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:customers')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'delivery/customers/customer_update.html'
    context_object_name = 'customer'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('delivery:customers')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'delivery/customers/customer_delete.html'
    success_url = reverse_lazy('delivery:customers')



# INCOMES CRUD VIEW

class IncomeListView(ListView):
    model = Pharmacy_income
    template_name = 'delivery/incomes/incomes.html'
    context_object_name = 'incomes'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        incomes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(incomes, self.paginate_by)
        try:
            incomes = paginator.page(page)
        except PageNotAnInteger:
            incomes = paginator.page(1)
        except EmptyPage:
            incomes = paginator.page(paginator.num_pages)
        context['incomes'] = incomes
        return context


class IncomeCreateView(CreateView):
    model = Pharmacy_income
    template_name = 'delivery/incomes/income_create.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery:incomes')



# EXPENSE CRUD VIEW

class ExpenseListView(ListView):
    model = Pharmacy_expense
    template_name = 'delivery/expenses/expenses.html'
    context_object_name = 'expenses'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        expenses = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(expenses, self.paginate_by)
        try:
            expenses = paginator.page(page)
        except PageNotAnInteger:
            expenses = paginator.page(1)
        except EmptyPage:
            expenses = paginator.page(paginator.num_pages)
        context['expenses'] = expenses
        return context


class ExpenseCreateView(CreateView):
    model = Pharmacy_expense
    template_name = 'delivery/expenses/expense_create.html'
    fields = ('month', 'year', 'rent', 'utilities', 'advertising', 'inner_expenses', )
    success_url = reverse_lazy('delivery:expenses')





class AccountingListView(ListView):
    model = Accounting
    template_name = 'delivery/accountings/accounting_list.html'
    context_object_name = 'accountings'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(AccountingListView, self).get_context_data(**kwargs)
        accountings = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(accountings, self.paginate_by)
        try:
            accountings = paginator.page(page)
        except PageNotAnInteger:
            accountings = paginator.page(1)
        except EmptyPage:
            accountings = paginator.page(paginator.num_pages)
        context['accountings'] = accountings

        return context


class AccountingCreateView(CreateView):
    model = Accounting
    template_name = 'delivery/accountings/accounting_create.html'
    fields = ('month_i', 'month_e', )
    success_url = reverse_lazy('delivery:accounting')





class ProjectLoginView(LoginView):
    template_name = 'delivery/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('delivery:home_page')

    def get_success_url(self):
        return self.success_url



class RegisterUserView(CreateView):
     model = User
     template_name = 'delivery/register_page.html'
     form_class = RegisterUserForm
     success_url = reverse_lazy('delivery:home_page')
     success_msg = 'User created successfully!'

     def get_success_url(self):
         return self.success_url

     def form_valid(self, form):
         form_valid = super().form_valid(form)
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         aut_user = authenticate(username=username, password=password)
         login(self.request, aut_user)
         return form_valid



class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('delivery:home_page')
