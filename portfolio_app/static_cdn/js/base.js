var x  = document.querySelector('dot')
x.addEventListener("mouseover", function(){
    ChangeTheme(); 
});

var x  = document.getElementById('light-theme')
x.addEventListener("mouseout", function(){
    var y = document.body.style.backgroundColor = 'yellow'; 
});



function ChangeTheme() {
    var x  = document.body
    x.style.backgroundColor = "red"    
}
