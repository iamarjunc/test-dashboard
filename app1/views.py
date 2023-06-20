from django.http import JsonResponse
from django.shortcuts import redirect, render
import pyodbc #pip install pyodbc ,pip install django-pyodbc-azure
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt  # Import the csrf_exempt decorator


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        p1="123"
        hashed_password = make_password(p1)

        print(hashed_password)  
        if username == 'admin' and password == '123':
            # Successful login, redirect to a success page
            return redirect('http://127.0.0.1:8000/template2/')
        else:
            # Invalid credentials, render login template with error message
            error = "Invalid username or password."
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')

@csrf_exempt  # Apply the csrf_exempt decorator to bypass CSRF protection
def process_branch(request):
    if request.method == 'POST':
        branch_code = request.POST.get('branchCode')
        print('Clicked value : '+branch_code)
        conn = pyodbc.connect(
            "DRIVER={SQL Server Native Client 11.0};SERVER="
            + settings.DATABASES['default']['HOST'] +
            ";DATABASE=" + settings.DATABASES['default']['NAME'] +
            ";UID=" + settings.DATABASES['default']['USER'] +
            ";PWD=" + settings.DATABASES['default']['PASSWORD'] + ";"
        )
        cursor = conn.cursor()

        cursor.execute("SET NOCOUNT ON; EXEC usp_Rpt_Dash1 2, ?", [branch_code])
        result1 = cursor.fetchall()
        
        cursor.execute("SET NOCOUNT ON; EXEC usp_Rpt_Dash1 3, ?", [branch_code])
        result2 = cursor.fetchall()

        cursor.execute("SET NOCOUNT ON; EXEC usp_Rpt_Dash1 4, ?", [branch_code])
        result3 = cursor.fetchall()

        cursor.execute("SET NOCOUNT ON; EXEC usp_Rpt_Dash1 5, ?", [branch_code])
        result4 = cursor.fetchall()

        cursor.execute("SET NOCOUNT ON; EXEC usp_Rpt_Dash1 6, ?", [branch_code])
        result5 = cursor.fetchall()
        
        
   

        chartTitle1=[]
        chartlabel1=[]
        chartdata1=[]

        chartTitle2=[]
        chartlabel2=[]
        chartdata2=[]

        chartTitle3=[]
        chartlabel3=[]
        chartdata3=[]

        narration=[]
        saleamount=[]
        percentsale=[]
        titletable=[]


        Title =[]
        SaleAmt =[]
        Persale =[]
        Sortid =[]
        for row in result1:
            Title.append(row[0])
            SaleAmt.append(row[1])
            Persale.append(row[2])
            Sortid.append(row[3])
        spdata1 = {'Title' : Title, 'SaleAmt' : SaleAmt, 'Persale':Persale,'Sortid' : Sortid}

        
        for row in result2:
            chartTitle1.append(row[0])
            chartlabel1.append(row[1])
            chartdata1.append(row[2])
        chartval1 = {'Title' : chartTitle1, 'label' : chartlabel1, 'data':chartdata1}

        for row in result3:
            chartTitle2.append(row[0])
            chartlabel2.append(row[1])
            chartdata2.append(row[2])
        chartval2 = {'Title' : chartTitle2, 'label' : chartlabel2, 'data':chartdata2}

        for row in result4:
            chartTitle3.append(row[0])
            chartlabel3.append(row[1])
            chartdata3.append(row[2])
        chartval3 = {'Title' : chartTitle3, 'label' : chartlabel3, 'data':chartdata3}

        for row in result5:
            narration.append(row[0])
            saleamount.append(row[1])
            percentsale.append(row[2])
            titletable.append(row[3])
        chartval4 = {'narration' : narration, 'saleamount' : saleamount, 'percentsale':percentsale, 'titletable':titletable}

        
        conn.commit()

        cursor.close()
        conn.close()

        return JsonResponse({'data': spdata1,'Chartdata1':chartval1,'Chartdata2':chartval2,'Chartdata3':chartval3,'Chartdata4':chartval4})
    else:
        return JsonResponse({'status': 'error'})


def json2(request):
    
    spdata1 = {'BranchCode': ['TP01', 'TP02', 'TP03', 'TP04', 'TP07'], 'BranchName': ['ULLOOR', 'VAZHUTHAKKADU', 'KARAMANA', 'VANCHIYOOR', 'MARUTHOOR'], 'SaleAmt': ['222.43 K', '74.08 K', '57.51 K', '91.46 K', '81.06 K'], 'Persale': ['125%', '200%', '46%', '117%', '80%']}
    
    chartval1 = {'Title': ['Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution', 'Company wise Sales Distribution'], 'label': ['PIDILITE', 'OTHERS', 'LION', 'JK', 'INDIGO', 'ESDEE', 'CAPTAIN', 'BIRLA', 'BERGER', 'ASIAN', 'AKZONOBEL'], 'data': [17.15, 22.14, 4.94, 10.74, 8.5, 6.91, 3.33, 3.17, 99.81, 91.76, 3.83]}
    
    chartval2 = {'Title': ['Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales', 'Asian Groupwise Sales'], 'label': ['WOOD COAT', 'WATERPROOFING', 'THINNER', 'SPECIAL EFFECTS', 'PUTTY', 'OTHERS', 'METAL PRIMER', 'METAL COAT', 'ENAMEL', 'EMULSION', 'CEMENT PRIMER'], 'data': [6.07, 4.84, 1.67, 4.76, 0.84, 0.37, 1.08, 0.29, 18.3, 41.38, 12.15]}
    
    chartval3 = {'Title': ['Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales', 'Berger Groupwise Sales'], 'label': ['WOOD PRIMER', 'WOOD COAT', 'WATERPROOFING', 'PUTTY', 'METAL PRIMER', 'ENAMEL', 'EMULSION', 'CEMENT PRIMER', 'BASECOAT', 'ABRASIVES'], 'data': [0.1, 0.58, 8.17, 2.16, 1.92, 49.91, 30.98, 5.11, 0.4, 0.47]}
    tableval = {'narration': ['Cash Sale Yesterday', 'Credit Sale Yesterday', 'Collections Yesterday', 'Payments Yesterday'], 'saleamount': ['173.86 K', '53.81 K', '392.38 K', '5.99 K'], 'percentsale': ['99%', '221%', '59%', '45%'], 'titletable': ['Ulloor Sales', 'Ulloor Sales', 'Ulloor Sales', 'Ulloor Sales']}

    # Pass the results to the template
    return JsonResponse({'data':spdata1,'chart1':chartval1,'chart2':chartval2,'chart3':chartval3,'tableval':tableval})


def index1(request):
    return render(request,'template1.html')



def index2(request):
    return render(request,'template2.html')



