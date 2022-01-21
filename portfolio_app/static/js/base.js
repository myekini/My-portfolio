var element  = document.getElementById('light-theme')
element.addEventListener("click", function(){
    alert('hello world'); 
});


function ChangeTheme() {
    var x  = document.getElementById('style-link')
    x.href = "{% static '/css/black.css'%}"  
}
