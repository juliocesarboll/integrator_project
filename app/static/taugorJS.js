function run() {
 
    // Creating Our XMLHttpRequest object 
    let xhr = new XMLHttpRequest();
 
    // Making our connection  
    let url = '/search-caixa?' + document.getElementById('searchBox').value;
    xhr.open("GET", url, true);
 
    // function execute after request is successful 
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    }
    // Sending our request 
    xhr.send();
}