
let element = document.getElementsByClassName('dot')
for(var i=0; element.length > i; i++) {
    element[i].addEventListener('click', function() {
        let mode = this.dataset.mode
        console.log('optioned clicked', mode)
        ChangeTheme(mode)
    })
}

function ChangeTheme(mode) {
    if(mode == 'light') {
        document.getElementById('style-link').href = 'static/css/white.css';
    } else if (mode == 'grey'){
        document.getElementById('style-link').href = 'static/css/grey.css';
    } else if (mode == 'dark'){
        document.getElementById('style-link').href = 'static/css.black.css';
    }
}

