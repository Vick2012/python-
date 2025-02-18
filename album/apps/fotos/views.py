from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'fotos/index.html')
def home(request):
    items = [
        {"title": "What is HTML", "description": "HTML es el lenguaje estándar para la web.", "link": "https://www.w3schools.com/html/", "icon": "fa-brands fa-html5", "language": "Lenguaje 01"},
        {"title": "What is CSS", "description": "CSS define la presentación de HTML.", "link": "https://www.w3schools.com/css/", "icon": "fa-brands fa-css3-alt", "language": "Lenguaje 02"},
        {"title": "What is JavaScript", "description": "JavaScript agrega interactividad.", "link": "https://www.w3schools.com/js/", "icon": "fa-brands fa-js", "language": "Lenguaje 03"},
        {"title": "What is Framework", "description": "Un framework agiliza el desarrollo.", "link": "https://unirfp.unir.net/revista/ingenieria-y-tecnologia/framework/", "icon": "fa-brands fa-phoenix-framework", "language": "Lenguaje 04"},
        {"title": "What is PHP", "description": "PHP es un lenguaje de servidor.", "link": "https://www.php.net/", "icon": "fa-brands fa-php", "language": "Lenguaje 05"},
        {"title": "What is SQL", "description": "SQL gestiona bases de datos.", "link": "https://www.w3schools.com/sql/", "icon": "fa-solid fa-database", "language": "Lenguaje 06"},
        {"title": "What is Python", "description": "Python es un lenguaje versátil.", "link": "https://www.python.org/", "icon": "fa-brands fa-python", "language": "Lenguaje 07"},
        {"title": "What is Java", "description": "Java es orientado a objetos.", "link": "https://www.java.com/", "icon": "fa-brands fa-java", "language": "Lenguaje 08"},
        {"title": "What is C++", "description": "C++ es de alto rendimiento.", "link": "https://www.cplusplus.com/", "icon": "fa-solid fa-c", "language": "Lenguaje 09"},
    ]
    return render(request, 'mi_app/index.html', {'items': items})
