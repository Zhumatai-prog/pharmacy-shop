from django.contrib import admin
from django.urls import path

from . import views
app_name = 'delivery'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # PRODUCTS
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    # PERSONNEL
    path('personnel_list/', views.PersonnelListView.as_view(), name='personnel_list'),
    path('personnel/create/', views.PersonnelCreateView.as_view(), name='personnel_create'),
    path('personnel/detail/<int:pk>/', views.PersonnelDetailView.as_view(), name='personnel_detail'),
    path('personnel/update/<int:pk>/', views.PersonnelUpdateView.as_view(), name='personnel_update'),
    path('personnel/delete/<int:pk>/', views.PersonnelDeleteView.as_view(), name='personnel_delete'),

    # SUPPLIER
    path('supplier/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/update/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier_delete'),

    # ORDER_PRODUCT
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),

    # PRODUCT_SUPPLY
    path('product_supply/list/', views.ProductSupplyListView.as_view(), name='product_supply'),
    path('product_supply/create/', views.ProductSupplyCreateView.as_view(), name='product_supply_create'),

    # PRODUCT_SALE
    path('product_sale/', views.ProductSaleListView.as_view(), name='product_sale'),
    path('product_sale/create/', views.ProductSaleCreateView.as_view(), name='product_sale_create'),

    # SALARY
    path('salary/list/', views.SalaryListView.as_view(), name='salary_list'),
    path('salary/create/', views.SalaryCreateView.as_view(), name='salary_create'),

    # CUSTOMER
    path('customer/list/', views.CustomerListView.as_view(), name='customers'),
    path('customer/detail/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customer/update/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # INCOMES
    path('incomes/', views.IncomeListView.as_view(), name='incomes'),
    path('income/create/', views.IncomeCreateView.as_view(), name='income_create'),

    # EXPENSES
    path('expenses/', views.ExpenseListView.as_view(), name='expenses'),
    path('expense/create/', views.ExpenseCreateView.as_view(), name='expense_create'),

    # ACCOUNTINGS
    path('accounting/', views.AccountingListView.as_view(), name='accounting'),
    path('accounting/create/', views.AccountingCreateView.as_view(), name='accounting_create'),

    path('login/', views.ProjectLoginView.as_view(), name='login_page'),
    path('register/', views.RegisterUserView.as_view(), name='register_page'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout_page'),

]
