from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from core.models import Category, Product, Transaction, Contato
from .forms import ProductForm
from .formsCategory import CategoryForm
from .formsContato import ContatoForm
from django.contrib import messages
import pymysql
import mysql.connector
from random import randint


"""
PRODUCTS
"""
def productsList(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def productView(request, id):
    product = get_object_or_404(Product.objects.all(), id=id)
    category = Category.objects.filter(product__id = id).values()
    return render(request, 'products/product.html', {'product': product, 'category': category})

def productCreate(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
       
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Produto cadastrado com sucesso.')
            return redirect('/products/')
        
    form = ProductForm()
    return render(request, 'products/product-create.html', {'form': form})

def productEdit(request, id):
    product = get_object_or_404(Product.objects.all(), id=id)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
       form = ProductForm(request.POST, instance=product)
       
       if form.is_valid():
           product = form.save()
           messages.info(request, 'Produto atualizado com sucesso.')
           return redirect('/products/')
    
    return render(request, 'products/product-edit.html', {'form': form, 'product': product})

def productDelete(request, id):
    product = get_object_or_404(Product.objects.all(), id=id)
    product.delete()
    messages.info(request, 'Produto deletado com sucesso.')
    return redirect('/products/')



"""
CATEGORIES
"""
def categoriesList(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

def categoryView(request, id):
    category = get_object_or_404(Category.objects.all(), id=id)
    return render(request, 'categories/category.html', {'category': category})

def categoryCreate(request):
    if request.method == 'POST':
       form = CategoryForm(request.POST)
       
       if form.is_valid():
           category = form.save()
           messages.info(request, 'Categoria cadastrada com sucesso.')
           return redirect('/categories/')
        
    form = CategoryForm()
    return render(request, 'categories/category-create.html', {'form': form})

def categoryEdit(request, id):
    category = get_object_or_404(Category.objects.all(), id=id)
    form = CategoryForm(instance=category)
    
    if request.method == 'POST':
       form = CategoryForm(request.POST, instance=category)
       
       if form.is_valid():
           category = form.save()
           messages.info(request, 'Categoria atualizada com sucesso.')
           return redirect('/categories/')
    
    return render(request, 'categories/category-edit.html', {'form': form, 'category': category})

def categoryDelete(request, id):
    category = get_object_or_404(Category.objects.all(), id=id)
    category.delete()
    messages.info(request, 'Categoria deletado com sucesso.')
    return redirect('/categories/')


"""
TRANSACTION
"""
def transactionsList(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions.html', {'transactions': transactions})

def transactionCreate(request, id):
    product = get_object_or_404(Product.objects.all(), id=id)
    
    try:
        transaction = Transaction.objects.create(
                    code = randint(0,999),
                    status = "pending",
                    value = product.value,
                )
        
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yveltal#147",
            database="teste_pratico_django"
        )
        
        cursor = conexao.cursor()
        sql_insert = "INSERT INTO core_transaction_product (transaction_id, product_id) VALUES (%s, %s)"
        val = (transaction.id, product.id)
        cursor.execute(sql_insert, val, True)
        conexao.commit()
    
    except:
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()
            
    
    return redirect('/transactions/')

def transactionUpdate(request, id):
    transaction = get_object_or_404(Transaction.objects.all(), id=id)
    
    print(transaction.status)
    
    if transaction.status == "pending":
        transaction.status = "paid"
    else:
        transaction.status = "pending"
        
    transaction.save()
    
    messages.info(request, 'Transação atualizada com sucesso. STATUS = ' + transaction.status)
    return redirect('/transactions/')

"""
CONTATO
"""
def faleConosco(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')        
        message = "nome: " + name + "\n email: " + email + "\n telefone: " + phone + "\n mensagem: " + message

        recipients = ['romulo.xavier@catskillet.com']
        
        send_mail(subject, message, email, recipients)
    
        messages.info(request, 'Formulário enviado com sucesso.')
       
        return redirect('/contato/')
       
    form = ContatoForm()
    return render(request, 'contato/contato.html', {'form': form})

