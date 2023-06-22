function login (){
    var user, password;
    user = document.getElementById("usuario").value;
    password = document.getElementById("contrasena").value;
    if( user == "admin" && password == "1234"){
        window.location = "Inicio.html";
    } else {
        alert("Datos incorrectos")
    }
}