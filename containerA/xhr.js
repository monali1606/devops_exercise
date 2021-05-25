let xhr = new XMLHttpRequest();
xhr.open('get', 'http://localhost:5000');
xhr.send();

xhr.onload = function() {
    console.log(xhr.response);
    
};